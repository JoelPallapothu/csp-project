"""
CAVI - Cyber Aware Village Initiative
Bilingual AI Cyber Safety Assistant Component.
Desktop-First, Accessible, High-Contrast UI with Quick Questions, In-Chatbot Language Switching,
Audio TTS Read Aloud, Emergency Detection, and Navigation Shortcuts.
"""

import streamlit as st
from utils.helpers import get_current_lang, set_current_lang, navigate_to, render_speech_audio_button
from utils.styling import render_html
from utils.ai_engine import generate_chatbot_response
from data.chatbot_data import QUICK_QUESTIONS

def render_chatbot():
    """
    Renders the CAVI Cyber Safety Assistant interface.
    """
    # Sync with main app language or allow in-chatbot toggle
    if "chatbot_lang" not in st.session_state:
        st.session_state.chatbot_lang = get_current_lang()
        
    c_lang = st.session_state.chatbot_lang

    # Ensure chat history exists
    if "chat_history" not in st.session_state or not isinstance(st.session_state.chat_history, list):
        welcome_msg = (
            "నమస్కారం! నేను CAVI సైబర్ భద్రత సహాయకుడిని 🤖.\n\n"
            "OTP మోసాలు, యూపీఐ (UPI) భద్రత, నకిలీ లింకులు, బహుమతి స్కామ్‌ల గురించి ఏదైనా అడగండి. "
            "మీరు ఒకవేళ సైబర్ మోసంలో డబ్బు పోగొట్టుకుంటే ఆలస్యం చేయకుండా వెంటనే **📞 1930** కు కాల్ చేయండి."
            if c_lang == "te" else
            "Hello! I am your CAVI Cyber Safety Assistant 🤖.\n\n"
            "Ask me anything about OTP fraud, UPI safety, fake links, prize scams, or reporting fraud. "
            "If you have experienced financial fraud, dial **📞 1930** immediately."
        )
        st.session_state.chat_history = [
            {"role": "assistant", "content": welcome_msg}
        ]

    # 1. Header Banner Box
    title_text = "CAVI సైబర్ భద్రత సహాయకుడు" if c_lang == "te" else "CAVI Cyber Safety Assistant"
    sub_text = "సైబర్ భద్రత కోసం మీ నమ్మకమైన మార్గదర్శి" if c_lang == "te" else "Your trusted guide for cyber safety"
    
    render_html(f"""
    <div style="background: linear-gradient(135deg, #063970 0%, #0b63ce 100%); 
                border-radius: 20px; padding: 24px 28px; color: #ffffff; margin-bottom: 22px; 
                box-shadow: 0 6px 20px rgba(11, 99, 206, 0.2); border: 1.5px solid #38bdf8;">
        <div style="display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 14px;">
            <div style="display: flex; align-items: center; gap: 14px;">
                <div style="font-size: 2.4rem; background: rgba(255,255,255,0.15); border-radius: 16px; padding: 8px 14px;">
                    🤖
                </div>
                <div>
                    <h2 style="color: #ffffff; margin: 0; font-size: 1.85rem; font-weight: 950; letter-spacing: -0.5px;">
                        {title_text}
                    </h2>
                    <p style="color: #bae6fd; font-size: 1.05rem; margin: 4px 0 0 0; font-weight: 600;">
                        {sub_text}
                    </p>
                </div>
            </div>
            <div style="display: flex; align-items: center; gap: 8px; background: rgba(255,255,255,0.12); padding: 6px 14px; border-radius: 9999px; border: 1px solid rgba(255,255,255,0.25);">
                <span style="font-size: 0.95rem; font-weight: 800; color: #ffffff;">🚨 24x7 Helpline:</span>
                <a href="tel:1930" style="color: #fef08a; font-weight: 950; font-size: 1.15rem; text-decoration: none;">
                    📞 1930
                </a>
            </div>
        </div>
    </div>
    """)

    # 2. Controls Row: Language Selector & Quick Action Shortcuts
    col_lang, col_clear = st.columns([3, 1])
    with col_lang:
        render_html("<div style='font-size: 0.88rem; font-weight: 850; color: #475569; margin-bottom: 4px;'>🌐 భాష / Language:</div>")
        l1, l2 = st.columns(2)
        with l1:
            is_te = (c_lang == "te")
            if st.button("🇮🇳 తెలుగు" + (" ✓" if is_te else ""), key="chat_lang_te", type="primary" if is_te else "secondary", use_container_width=True):
                st.session_state.chatbot_lang = "te"
                set_current_lang("te")
                st.rerun()
        with l2:
            is_en = (c_lang == "en")
            if st.button("🇬🇧 English" + (" ✓" if is_en else ""), key="chat_lang_en", type="primary" if is_en else "secondary", use_container_width=True):
                st.session_state.chatbot_lang = "en"
                set_current_lang("en")
                st.rerun()
                
    with col_clear:
        render_html("<div style='font-size: 0.88rem; font-weight: 850; color: #475569; margin-bottom: 4px;'>&nbsp;</div>")
        clear_label = "చాట్ క్లియర్ 🗑️" if c_lang == "te" else "Clear Chat 🗑️"
        if st.button(clear_label, key="chat_clear_btn", use_container_width=True):
            st.session_state.chat_history = []
            st.rerun()

    # 3. Quick Navigation Buttons to Existing Sections (PART 17)
    nav_box_title = "ముఖ్యాంశాలకు వెళ్లండి:" if c_lang == "te" else "Quick Links to Guides:"
    render_html(f"<div style='font-size: 0.88rem; font-weight: 850; color: #64748b; margin: 14px 0 6px 0;'>🧭 {nav_box_title}</div>")
    n1, n2, n3, n4 = st.columns(4)
    with n1:
        btn_f_txt = "🛡️ మోసాలు తెలుసుకోండి" if c_lang == "te" else "🛡️ Learn About Fraud"
        if st.button(btn_f_txt, key="cnav_frauds", use_container_width=True):
            navigate_to("frauds")
    with n2:
        btn_r_txt = "📜 రక్షణ సూత్రాలు" if c_lang == "te" else "📜 Safety Guide"
        if st.button(btn_r_txt, key="cnav_rules", use_container_width=True):
            navigate_to("rules")
    with n3:
        btn_u_txt = "📱 యూపీఐ భద్రత" if c_lang == "te" else "📱 Learn UPI Safety"
        if st.button(btn_u_txt, key="cnav_sims", use_container_width=True):
            navigate_to("simulations")
    with n4:
        btn_e_txt = "🚨 మోసాన్ని నివేదించండి" if c_lang == "te" else "🚨 Report Cyber Fraud"
        if st.button(btn_e_txt, key="cnav_rep", use_container_width=True):
            navigate_to("report")

    render_html("<hr style='border: none; border-top: 1.5px solid #e2e8f0; margin: 18px 0 14px 0;'>")

    # 4. Quick Questions Accordion / Buttons (PART 6)
    quick_title = "💡 త్వరిత ప్రశ్నలు (Quick Questions) — క్లిక్ చేయండి:" if c_lang == "te" else "💡 Quick Questions — Click to ask instantly:"
    render_html(f"<div style='font-size: 0.95rem; font-weight: 850; color: #063970; margin-bottom: 10px;'>{quick_title}</div>")
    
    questions = QUICK_QUESTIONS.get(c_lang, QUICK_QUESTIONS["en"])
    
    # Render quick questions in 2 columns of 5 buttons each
    q_col1, q_col2 = st.columns(2)
    for idx, q_text in enumerate(questions):
        target_col = q_col1 if idx % 2 == 0 else q_col2
        with target_col:
            if st.button(f"💬 {q_text}", key=f"quick_q_{c_lang}_{idx}", use_container_width=True):
                # Add to history
                st.session_state.chat_history.append({"role": "user", "content": q_text})
                # Generate response
                bot_ans = generate_chatbot_response(q_text, lang=c_lang)
                st.session_state.chat_history.append({"role": "assistant", "content": bot_ans})
                st.rerun()

    render_html("<div style='margin-bottom: 20px;'></div>")

    # 5. Chat Conversation Area
    render_html("""
    <div style="font-size: 1.15rem; font-weight: 900; color: #063970; margin-bottom: 12px; display: flex; align-items: center; gap: 8px;">
        <span>💬</span> <span>సంభాషణ / Conversation</span>
    </div>
    """)

    for idx, msg in enumerate(st.session_state.chat_history):
        role = msg["role"]
        content = msg["content"]
        
        if role == "user":
            with st.chat_message("user", avatar="👤"):
                st.markdown(f"**{content}**")
        else:
            with st.chat_message("assistant", avatar="🛡️"):
                st.markdown(content)
                # Accessible Audio TTS Read Aloud Button (PART 18)
                render_speech_audio_button(
                    text_to_speak=content,
                    lang=c_lang,
                    key_id=f"chat_tts_{idx}"
                )

    # 6. Chat Input Bar
    placeholder = "మీ ప్రశ్నను ఇక్కడ అడగండి (ఉదా: లింక్ సురక్షితమేనా?)..." if c_lang == "te" else "Type your question or paste a suspicious message here..."
    user_input = st.chat_input(placeholder=placeholder, key="cavi_chat_input")
    
    if user_input and user_input.strip():
        # Append user query
        st.session_state.chat_history.append({"role": "user", "content": user_input.strip()})
        # Generate bot response
        bot_ans = generate_chatbot_response(user_input.strip(), lang=c_lang)
        st.session_state.chat_history.append({"role": "assistant", "content": bot_ans})
        st.rerun()
