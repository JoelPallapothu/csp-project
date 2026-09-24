"""
CAVI - Cyber Aware Village Initiative
Secure AI Engine with Guardrails, Streamlit Secrets Management, Emergency Protocols,
Sensitive Data Filtering, and Seamless Fallback to Curated Knowledge.
"""

import os
import re
import json
import streamlit as st
from typing import Tuple, Dict, Any, Optional

from data.chatbot_data import (
    QUICK_QUESTIONS,
    OUT_OF_SCOPE_RESPONSES,
    SENSITIVE_WARNING,
    EMERGENCY_RESPONSES,
    KNOWLEDGE_BASE
)

# System prompt for LLM generation
SYSTEM_PROMPT = """You are the 'CAVI Cyber Safety Assistant' (CAVI సైబర్ భద్రత సహాయకుడు), a compassionate, patient, and highly accessible cybersecurity awareness guide for rural citizens, elderly people, farmers, women, and first-time smartphone users in Andhra Pradesh, India.

CRITICAL GUIDELINES:
1. FOCUS ONLY ON CYBER SAFETY: OTP fraud, UPI safety, QR code scams, KYC verification scams, lottery/prize scams, fake customer care, phishing links, screen-sharing apps (AnyDesk, TeamViewer), job scams, and reporting fraud.
2. LANGUAGE: Respond strictly in the user's selected language (English or Telugu). Never use Hindi.
3. TONE: Friendly, patient, respectful, non-technical, simple words. NEVER blame the victim (e.g. say "Don't worry. Take these steps immediately to protect yourself." instead of "You made a mistake.").
4. EMERGENCY RULE: Whenever financial loss, scammed money, or fraud is mentioned, ALWAYS prominently advise calling helpline 1930 immediately within the Golden Hour (2-3 hours) and reporting at cybercrime.gov.in. Keep "1930" and "cybercrime.gov.in" clearly visible.
5. SENSITIVE DATA: NEVER ask the user for OTP, PIN, password, CVV, bank account, or Aadhaar.
6. SUSPICIOUS MESSAGES: When analyzing pasted messages, use cautious wording ("This message shows signs of a possible scam because...").
7. OUT OF SCOPE: If asked about non-cyber safety topics (weather, movies, coding), politely state that you are specialized in cyber safety and guide them back.
"""

def get_configured_api_key() -> Tuple[Optional[str], str]:
    """
    Retrieves the LLM API key securely from Streamlit Secrets or environment variables.
    Returns (api_key, provider_type) where provider_type is 'gemini' or 'openai'.
    NEVER hardcodes keys or exposes secrets.
    """
    # 1. Check Streamlit secrets standard structure [api] key = "..."
    try:
        if hasattr(st, "secrets"):
            if "api" in st.secrets and "key" in st.secrets["api"]:
                k = st.secrets["api"]["key"]
                if k and k != "YOUR_API_KEY" and len(k) > 10:
                    return k, "gemini" if k.startswith("AIza") else "openai"
            
            if "GEMINI_API_KEY" in st.secrets:
                k = st.secrets["GEMINI_API_KEY"]
                if k and k != "YOUR_API_KEY" and len(k) > 10:
                    return k, "gemini"
                    
            if "OPENAI_API_KEY" in st.secrets:
                k = st.secrets["OPENAI_API_KEY"]
                if k and k != "YOUR_API_KEY" and len(k) > 10:
                    return k, "openai"
                    
            if "api_key" in st.secrets:
                k = st.secrets["api_key"]
                if k and k != "YOUR_API_KEY" and len(k) > 10:
                    return k, "gemini" if k.startswith("AIza") else "openai"
    except Exception:
        pass

    # 2. Check environment variables
    env_gemini = os.environ.get("GEMINI_API_KEY")
    if env_gemini and env_gemini != "YOUR_API_KEY" and len(env_gemini) > 10:
        return env_gemini, "gemini"
        
    env_openai = os.environ.get("OPENAI_API_KEY")
    if env_openai and env_openai != "YOUR_API_KEY" and len(env_openai) > 10:
        return env_openai, "openai"

    return None, ""

def detect_sensitive_data(text: str) -> bool:
    """
    Detects if user accidentally typed OTP, PIN, password, CVV, or card/Aadhaar numbers.
    """
    lower = text.lower()
    patterns = [
        r'\b(?:otp|one time password|code)\s*(?:is|:|=)?\s*([0-9]{4,8})\b',
        r'\b(?:upi pin|mpin|atm pin|pin)\s*(?:is|:|=)?\s*([0-9]{4,6})\b',
        r'\b(?:cvv|cvc)\s*(?:is|:|=)?\s*([0-9]{3,4})\b',
        r'\b(?:password|pwd)\s*(?:is|:|=)?\s*([^\s]{4,})\b',
        r'\b[0-9]{4}[\s-]?[0-9]{4}[\s-]?[0-9]{4}[\s-]?[0-9]{4}\b', # 16-digit card
        r'\b[0-9]{4}[\s-]?[0-9]{4}[\s-]?[0-9]{4}\b' # 12-digit aadhaar
    ]
    for p in patterns:
        if re.search(p, lower):
            return True
            
    # Explicit keywords
    if any(k in lower for k in ["my otp is", "my pin is", "my password is", "నా otp", "నా pin", "నా పాస్‌వర్డ్"]):
        return True
        
    return False

def detect_emergency(text: str) -> bool:
    """
    Detects if user is experiencing active financial loss or cyber fraud.
    """
    lower = text.lower()
    em_en = [
        "lost money", "was scammed", "money was stolen", "money stolen",
        "got cheated", "fraud happened", "account debited", "money deducted",
        "scammed me", "cheated me", "lost rs", "debited without", "stole my money"
    ]
    em_te = [
        "డబ్బు పోయింది", "డబ్బులు పోయాయి", "మోసం చేశారు", "మోసపోయాను",
        "ఖాతాలో డబ్బు కట్", "డబ్బులు కట్ అయ్యాయి", "ఖాతా ఖాళీ", "నన్ను మోసం",
        "డబ్బులు పోయినాయి", "మోసం జరిగింది"
    ]
    return any(k in lower for k in em_en) or any(k in text for k in em_te)

def detect_out_of_scope(text: str) -> bool:
    """
    Detects queries completely unrelated to cyber safety, smartphones, payments, or fraud.
    """
    lower = text.lower()
    irrelevant_keywords = [
        "weather", "cricket score", "movie", "recipe", "cook", "poem", "joke",
        "write a python script", "solve this math", "president", "capital of",
        "cinema", "hero", "heroine", "వాతావరణం", "సినిమా", "వంట"
    ]
    return any(k in lower for k in irrelevant_keywords)

def get_curated_answer(query: str, lang: str = "te") -> Optional[str]:
    """
    Matches query against curated CAVI safety knowledge base.
    """
    lower = query.lower()
    
    # 1. OTP
    if "otp" in lower or "ఓటీపీ" in query:
        return KNOWLEDGE_BASE["otp_fraud"].get(lang, KNOWLEDGE_BASE["otp_fraud"]["en"])
        
    # 2. UPI / PIN / QR
    if any(k in lower for k in ["upi", "pin", "qr", "collect request"]) or any(k in query for k in ["యూపీఐ", "పిన్", "క్యూఆర్"]):
        return KNOWLEDGE_BASE["upi_safety"].get(lang, KNOWLEDGE_BASE["upi_safety"]["en"])
        
    # 3. KYC
    if "kyc" in lower or "కేవైసీ" in query or "aadhaar link" in lower:
        return KNOWLEDGE_BASE["kyc_fraud"].get(lang, KNOWLEDGE_BASE["kyc_fraud"]["en"])
        
    # 4. Prize / Lottery
    if any(k in lower for k in ["prize", "lottery", "won", "gift", "car"]) or any(k in query for k in ["బహుమతి", "లాటరీ", "సబ్సిడీ"]):
        return KNOWLEDGE_BASE["prize_scam"].get(lang, KNOWLEDGE_BASE["prize_scam"]["en"])
        
    # 5. Screen Sharing
    if any(k in lower for k in ["screen", "anydesk", "teamviewer", "rustdesk", "quicksupport"]) or any(k in query for k in ["స్క్రీన్", "యాక్సెస్"]):
        return KNOWLEDGE_BASE["screen_sharing"].get(lang, KNOWLEDGE_BASE["screen_sharing"]["en"])
        
    # 6. Suspicious link / APK
    if any(k in lower for k in ["link", "sms", "message", "apk", "suspicious", "url"]) or any(k in query for k in ["లింక్", "మెసేజ్"]):
        return KNOWLEDGE_BASE["suspicious_link"].get(lang, KNOWLEDGE_BASE["suspicious_link"]["en"])
        
    # 7. General Safety / How to stay safe
    if any(k in lower for k in ["safe", "guideline", "rules", "protect", "hygiene"]) or any(k in query for k in ["సురక్షితం", "రక్షణ", "సూత్రాలు"]):
        return KNOWLEDGE_BASE["general_safety"].get(lang, KNOWLEDGE_BASE["general_safety"]["en"])

    return None

def call_gemini_api(api_key: str, user_query: str, lang: str = "te") -> Tuple[bool, str]:
    """
    Calls Google Gemini REST API using requests.
    Zero external heavy dependencies. Timeout 10s.
    """
    import requests
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={api_key}"
    
    lang_instruction = "Respond in simple, clear Telugu." if lang == "te" else "Respond in simple, clear English."
    full_prompt = f"{SYSTEM_PROMPT}\n\n{lang_instruction}\n\nUser Question: {user_query}"
    
    payload = {
        "contents": [
            {
                "parts": [{"text": full_prompt}]
            }
        ],
        "generationConfig": {
            "temperature": 0.3,
            "maxOutputTokens": 600
        }
    }
    
    headers = {"Content-Type": "application/json"}
    
    try:
        resp = requests.post(url, json=payload, headers=headers, timeout=10)
        if resp.status_code == 200:
            data = resp.json()
            candidates = data.get("candidates", [])
            if candidates:
                content = candidates[0].get("content", {})
                parts = content.get("parts", [])
                if parts:
                    return True, parts[0].get("text", "").strip()
        return False, ""
    except Exception:
        return False, ""

def call_openai_api(api_key: str, user_query: str, lang: str = "te") -> Tuple[bool, str]:
    """
    Calls OpenAI REST API using requests.
    Timeout 10s.
    """
    import requests
    url = "https://api.openai.com/v1/chat/completions"
    lang_instruction = "Respond in simple, clear Telugu." if lang == "te" else "Respond in simple, clear English."
    
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": "gpt-4o-mini",
        "messages": [
            {"role": "system", "content": f"{SYSTEM_PROMPT}\n{lang_instruction}"},
            {"role": "user", "content": user_query}
        ],
        "temperature": 0.3,
        "max_tokens": 600
    }
    try:
        resp = requests.post(url, json=payload, headers=headers, timeout=10)
        if resp.status_code == 200:
            data = resp.json()
            choices = data.get("choices", [])
            if choices:
                return True, choices[0].get("message", {}).get("content", "").strip()
        return False, ""
    except Exception:
        return False, ""

def generate_chatbot_response(user_query: str, lang: str = "te") -> str:
    """
    Main response generation pipeline:
    1. Guardrail: Sensitive Information check (PART 13)
    2. Guardrail: Emergency financial fraud detection (PART 12)
    3. Guardrail: Out of scope check (PART 16)
    4. Curated match lookup
    5. Live LLM API invocation if secret key configured (PART 7, 8)
    6. Graceful fallback on missing key or network error (PART 11, 21)
    """
    clean_query = user_query.strip()
    if not clean_query:
        return ""
        
    # 1. Guardrail: Sensitive information
    if detect_sensitive_data(clean_query):
        return SENSITIVE_WARNING.get(lang, SENSITIVE_WARNING["en"])
        
    # 2. Guardrail: Emergency loss
    if detect_emergency(clean_query):
        return EMERGENCY_RESPONSES.get(lang, EMERGENCY_RESPONSES["en"])
        
    # 3. Guardrail: Out of scope
    if detect_out_of_scope(clean_query):
        return OUT_OF_SCOPE_RESPONSES.get(lang, OUT_OF_SCOPE_RESPONSES["en"])

    # 4. Check for Curated Answer
    curated = get_curated_answer(clean_query, lang=lang)
    
    # 5. Check API key
    api_key, provider = get_configured_api_key()
    
    if api_key:
        success = False
        api_response = ""
        if provider == "gemini":
            success, api_response = call_gemini_api(api_key, clean_query, lang=lang)
        elif provider == "openai":
            success, api_response = call_openai_api(api_key, clean_query, lang=lang)
            
        if success and api_response:
            return api_response
        else:
            # API failure: Show courteous failure notification + curated answer
            error_notice = (
                "క్షమించండి, ప్రస్తుతం మీ ప్రశ్నకు సమాధానం ఇవ్వలేకపోతున్నాను. దయచేసి మళ్లీ ప్రయత్నించండి లేదా CAVI Safety Guide ను చూడండి."
                if lang == "te" else
                "Sorry, I couldn't process that right now. Please try again or use the CAVI Safety Guide."
            )
            if curated:
                return f"{error_notice}\n\n---\n\n{curated}"
            return error_notice

    # 6. Missing API key: Provide friendly notice as specified in PART 11 + Curated answer
    missing_notice = (
        "AI చాట్బాట్ కాన్ఫిగరేషన్ ఇంకా అందుబాటులో లేదు. మీరు CAVI Safety Guide మరియు అత్యవసర రిపోర్టింగ్ సమాచారాన్ని ఉపయోగించవచ్చు."
        if lang == "te" else
        "AI chatbot configuration is not available yet. You can still use the CAVI Safety Guide and emergency reporting information."
    )
    if curated:
        return f"{curated}\n\n---\nℹ️ *{missing_notice}*"
    else:
        # Fallback to general safety
        gen_ans = KNOWLEDGE_BASE["general_safety"].get(lang, KNOWLEDGE_BASE["general_safety"]["en"])
        return f"{gen_ans}\n\n---\nℹ️ *{missing_notice}*"
