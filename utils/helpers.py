"""
CAVI - Cyber Aware Village Initiative
Session State Managers, Web Speech API Audio Narration Component, and Progress Tracker
"""

import streamlit as st
import streamlit.components.v1 as components
import json

def init_session_state():
    """Initializes all necessary session state variables with defaults."""
    if "language" not in st.session_state:
        st.session_state.language = "te"  # Telugu is default as required
    
    if "current_page" not in st.session_state:
        st.session_state.current_page = "home"
        
    if "selected_fraud_id" not in st.session_state:
        st.session_state.selected_fraud_id = None
        
    if "font_size_mode" not in st.session_state:
        st.session_state.font_size_mode = "normal"  # normal, large, xlarge
        
    # Progress Tracking (Local session-based, no personal data)
    if "progress" not in st.session_state:
        st.session_state.progress = {
            "frauds_viewed": set(),
            "scenarios_completed": {},
            "upi_sim_done": False,
            "videos_watched": set(),
            "rules_read": False,
            "quiz_completed": False,
            "quiz_score": 0,
            "quiz_total": 10
        }

def get_current_lang():
    return st.session_state.get("language", "te")

def set_current_lang(lang_code: str):
    st.session_state.language = lang_code

def get_current_page():
    return st.session_state.get("current_page", "home")

def navigate_to(page_name: str, fraud_id: str = None):
    st.session_state.current_page = page_name
    if fraud_id:
        st.session_state.selected_fraud_id = fraud_id
    else:
        st.session_state.selected_fraud_id = None
    st.rerun()

def record_fraud_view(fraud_id: str):
    if "progress" in st.session_state:
        st.session_state.progress["frauds_viewed"].add(fraud_id)

def record_video_view(video_id: str):
    if "progress" in st.session_state:
        st.session_state.progress["videos_watched"].add(video_id)

def record_scam_scenario(scenario_id: str, is_correct: bool):
    if "progress" in st.session_state:
        st.session_state.progress["scenarios_completed"][scenario_id] = is_correct

def calculate_safety_score() -> int:
    """
    Computes overall cyber awareness score from 0 to 100 based on session interactions.
    """
    prog = st.session_state.get("progress", {})
    score = 0
    
    # Frauds viewed (up to 30 points)
    frauds_count = len(prog.get("frauds_viewed", []))
    score += min(frauds_count * 5, 30)
    
    # Scenarios answered correctly (up to 20 points)
    correct_scenarios = sum(1 for v in prog.get("scenarios_completed", {}).values() if v)
    score += min(correct_scenarios * 4, 20)
    
    # UPI Sim done (15 points)
    if prog.get("upi_sim_done", False):
        score += 15
        
    # Rules read (15 points)
    if prog.get("rules_read", False):
        score += 15
        
    # Quiz score (up to 20 points)
    if prog.get("quiz_completed", False):
        q_score = prog.get("quiz_score", 0)
        q_total = prog.get("quiz_total", 10)
        score += int((q_score / max(q_total, 1)) * 20)
        
    return min(max(score, 5), 100)

def render_speech_audio_button(text_to_speak: str, lang: str = "te", btn_label: str = None, key_id: str = "tts"):
    """
    Renders an accessible client-side Web Speech API audio button that speaks aloud
    the text in Telugu ('te-IN'), English ('en-IN'), or Hindi ('hi-IN').
    Works offline in modern browsers without needing external cloud API keys.
    """
    voice_lang_map = {
        "te": "te-IN",
        "en": "en-IN",
        "hi": "hi-IN"
    }
    target_locale = voice_lang_map.get(lang, "te-IN")
    
    if not btn_label:
        if lang == "te":
            btn_label = "వినండి 🔊"
        elif lang == "hi":
            btn_label = "सुनिए 🔊"
        else:
            btn_label = "Listen 🔊"

    escaped_text = json.dumps(text_to_speak)
    button_html = f"""
    <div style="margin: 8px 0;">
        <button id="btn_{key_id}" onclick="speakText_{key_id}()" 
            style="background: linear-gradient(135deg, #0284c7 0%, #0369a1 100%);
                   color: #ffffff; border: none; padding: 7px 16px; border-radius: 20px;
                   font-size: 15px; font-weight: 700; cursor: pointer;
                   box-shadow: 0 2px 8px rgba(2, 132, 199, 0.35); display: inline-flex;
                   align-items: center; gap: 6px; transition: transform 0.15s ease;">
            <span>🔊</span> <span id="label_{key_id}">{btn_label}</span>
        </button>
        <span id="status_{key_id}" style="margin-left: 10px; font-size: 13px; color: #0284c7; font-weight: 600;"></span>
    </div>

    <script>
        function speakText_{key_id}() {{
            if (!('speechSynthesis' in window)) {{
                document.getElementById('status_{key_id}').innerText = 'Audio not supported in this browser';
                return;
            }}
            window.speechSynthesis.cancel();
            var text = {escaped_text};
            var utterance = new SpeechSynthesisUtterance(text);
            utterance.lang = '{target_locale}';
            utterance.rate = 0.9; // Slightly slower for low-literacy clarity
            utterance.pitch = 1.0;

            var btn = document.getElementById('btn_{key_id}');
            var status = document.getElementById('status_{key_id}');

            utterance.onstart = function() {{
                btn.style.background = '#15803d';
                status.innerText = '▶️ వినబడుతోంది...';
            }};

            utterance.onend = function() {{
                btn.style.background = 'linear-gradient(135deg, #0284c7 0%, #0369a1 100%)';
                status.innerText = '';
            }};

            utterance.onerror = function() {{
                btn.style.background = 'linear-gradient(135deg, #0284c7 0%, #0369a1 100%)';
                status.innerText = '';
            }};

            window.speechSynthesis.speak(utterance);
        }}
    </script>
    """
    components.html(button_html, height=52)
