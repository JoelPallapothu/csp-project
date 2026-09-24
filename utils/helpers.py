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

import re

def render_speech_audio_button(text_to_speak: str, lang: str = "te", btn_label: str = None, key_id: str = "tts"):
    """
    Renders an accessible client-side Web Speech API audio control that speaks aloud
    the text in Telugu ('te-IN') or English ('en-IN').
    Includes Read Aloud ▶ and Stop ⏸ controls, HTML tag stripping, and voice availability checks.
    """
    # Clean text to guarantee no HTML tags or code gets read aloud
    clean_text = re.sub(r'<[^>]+>', ' ', text_to_speak)
    clean_text = re.sub(r'\s+', ' ', clean_text).strip()

    target_locale = "te-IN" if lang == "te" else "en-IN"
    
    play_label = "చదవండి 🔊" if lang == "te" else "Read Aloud 🔊"
    stop_label = "ఆపండి ⏹️" if lang == "te" else "Stop ⏹️"
    active_label = "వినిపిస్తోంది... 🔊" if lang == "te" else "Speaking... 🔊"
    no_te_voice_msg = (
        "Telugu voice is not available on this device/browser. Please select a Telugu voice in your device settings."
        if lang == "te" else "English voice is not available on this device/browser."
    )

    escaped_text = json.dumps(clean_text)
    button_html = f"""
    <div style="display: flex; align-items: center; gap: 8px; flex-wrap: wrap; margin: 10px 0;">
        <button id="btn_play_{key_id}" onclick="speakText_{key_id}()" 
            style="background: linear-gradient(135deg, #0b63ce 0%, #063970 100%);
                   color: #ffffff; border: none; padding: 7px 16px; border-radius: 9999px;
                   font-size: 14px; font-weight: 700; cursor: pointer;
                   box-shadow: 0 2px 8px rgba(11, 99, 206, 0.3); display: inline-flex;
                   align-items: center; gap: 6px; transition: all 0.2s ease;">
            <span>▶</span> <span id="label_play_{key_id}">{play_label}</span>
        </button>
        <button id="btn_stop_{key_id}" onclick="stopText_{key_id}()" 
            style="background: #f1f5f9; color: #475569; border: 1px solid #cbd5e1;
                   padding: 7px 14px; border-radius: 9999px; font-size: 14px;
                   font-weight: 700; cursor: pointer; display: inline-flex;
                   align-items: center; gap: 4px; transition: all 0.2s ease;">
            <span>⏹</span> <span>{stop_label}</span>
        </button>
        <span id="status_{key_id}" style="font-size: 13px; color: #0b63ce; font-weight: 600; margin-left: 6px;"></span>
    </div>

    <script>
        function stopText_{key_id}() {{
            if ('speechSynthesis' in window) {{
                window.speechSynthesis.cancel();
            }}
            var btnPlay = document.getElementById('btn_play_{key_id}');
            var status = document.getElementById('status_{key_id}');
            if (btnPlay) btnPlay.style.background = 'linear-gradient(135deg, #0b63ce 0%, #063970 100%)';
            if (status) status.innerText = '';
        }}

        function speakText_{key_id}() {{
            if (!('speechSynthesis' in window)) {{
                document.getElementById('status_{key_id}').innerText = 'Audio not supported in this browser';
                return;
            }}
            window.speechSynthesis.cancel();
            
            var text = {escaped_text};
            var utterance = new SpeechSynthesisUtterance(text);
            utterance.lang = '{target_locale}';
            utterance.rate = 0.92; // Clear rate for rural accessibility
            utterance.pitch = 1.0;

            var voices = window.speechSynthesis.getVoices();
            var isTelugu = ('{target_locale}' === 'te-IN');
            var matchedVoice = null;

            if (voices && voices.length > 0) {{
                if (isTelugu) {{
                    matchedVoice = voices.find(function(v) {{
                        return v.lang.indexOf('te') === 0 || (v.name && v.name.toLowerCase().indexOf('telugu') !== -1);
                    }});
                }} else {{
                    matchedVoice = voices.find(function(v) {{
                        return v.lang === 'en-IN' || v.lang.indexOf('en') === 0;
                    }});
                }}
            }}

            var status = document.getElementById('status_{key_id}');
            var btnPlay = document.getElementById('btn_play_{key_id}');

            if (isTelugu && !matchedVoice && voices && voices.length > 0) {{
                if (status) {{
                    status.style.color = '#d62828';
                    status.innerText = '{no_te_voice_msg}';
                }}
                // Still allow utterance to proceed with default locale fallback so no crash occurs
            }}

            if (matchedVoice) {{
                utterance.voice = matchedVoice;
            }}

            utterance.onstart = function() {{
                if (btnPlay) btnPlay.style.background = '#168447';
                if (status && (!isTelugu || matchedVoice)) {{
                    status.style.color = '#168447';
                    status.innerText = '{active_label}';
                }}
            }};

            utterance.onend = function() {{
                stopText_{key_id}();
            }};

            utterance.onerror = function() {{
                stopText_{key_id}();
            }};

            window.speechSynthesis.speak(utterance);
        }}
    </script>
    """
    components.html(button_html, height=54)
