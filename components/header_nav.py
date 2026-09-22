"""
CAVI - Cyber Aware Village Initiative
Header, Top Navigation, Segmented Language Switcher, Accessibility Controls & Emergency Alert Bar
"""

import streamlit as st
from data.translations import get_text
from utils.helpers import get_current_lang, set_current_lang, get_current_page, navigate_to

from utils.styling import render_html

def render_header_nav():
    lang = get_current_lang()
    current_page = get_current_page()
    current_font = st.session_state.get("font_size_mode", "normal")
    
    # ------------------ TOP UTILITY BAR (Brand + Accessibility + Language) ------------------
    col_brand, col_controls = st.columns([5, 6])
    
    with col_brand:
        render_html(f"""
        <div style="display: flex; align-items: center; gap: 14px; padding: 4px 0;">
            <div style="background: linear-gradient(135deg, #091b36 0%, #1d4ed8 100%); 
                        color: white; border-radius: 16px; padding: 10px 16px; font-weight: 900; 
                        font-size: 1.35rem; letter-spacing: 1px; box-shadow: 0 4px 14px rgba(15,43,92,0.25);
                        border: 1px solid rgba(255,255,255,0.2); display: flex; align-items: center; gap: 8px;">
                <span>🛡️</span> <span>CAVI</span>
            </div>
            <div>
                <div style="font-size: 1.15rem; font-weight: 800; color: #091b36; line-height: 1.25;">
                    {get_text('app_full_name', lang)}
                </div>
                <div style="font-size: 0.85rem; font-weight: 700; color: #0284c7; margin-top: 2px;">
                    {get_text('tagline', lang)}
                </div>
            </div>
        </div>
        """)

    with col_controls:
        # Side-by-side controls: Text Size + Language Switcher
        c_size_wrap, c_lang_wrap = st.columns([4, 6])
        
        with c_size_wrap:
            render_html(f"<div style='font-size: 0.8rem; font-weight: 800; color: #475569; margin-bottom: 4px;'>{get_text('font_size_label', lang)}</div>")
            s1, s2, s3 = st.columns(3)
            with s1:
                btn_type_sm = "primary" if current_font == "normal" else "secondary"
                if st.button("A−", key="btn_font_normal", type=btn_type_sm, help=get_text('font_normal', lang), use_container_width=True):
                    st.session_state.font_size_mode = "normal"
                    st.rerun()
            with s2:
                btn_type_md = "primary" if current_font == "large" else "secondary"
                if st.button("A", key="btn_font_large", type=btn_type_md, help=get_text('font_large', lang), use_container_width=True):
                    st.session_state.font_size_mode = "large"
                    st.rerun()
            with s3:
                btn_type_lg = "primary" if current_font == "xlarge" else "secondary"
                if st.button("A+", key="btn_font_xlarge", type=btn_type_lg, help=get_text('font_xlarge', lang), use_container_width=True):
                    st.session_state.font_size_mode = "xlarge"
                    st.rerun()

        with c_lang_wrap:
            render_html("<div style='font-size: 0.8rem; font-weight: 800; color: #475569; margin-bottom: 4px;'>🌐 భాష / Language:</div>")
            l1, l2, l3 = st.columns(3)
            with l1:
                is_te = (lang == "te")
                if st.button("తెలుగు" + (" ✓" if is_te else ""), key="btn_lang_te", type="primary" if is_te else "secondary", use_container_width=True):
                    set_current_lang("te")
                    st.rerun()
            with l2:
                is_en = (lang == "en")
                if st.button("English" + (" ✓" if is_en else ""), key="btn_lang_en", type="primary" if is_en else "secondary", use_container_width=True):
                    set_current_lang("en")
                    st.rerun()
            with l3:
                is_hi = (lang == "hi")
                if st.button("हिंदी" + (" ✓" if is_hi else ""), key="btn_lang_hi", type="primary" if is_hi else "secondary", use_container_width=True):
                    set_current_lang("hi")
                    st.rerun()

    render_html("<hr style='margin: 12px 0 16px 0; border: none; border-top: 1px solid #e2e8f0;'>")

    # ------------------ EMERGENCY TOP NOTIFICATION STRIP ------------------
    render_html(f"""
    <div class="emergency-strip">
        <div style="display: flex; align-items: center; gap: 12px; font-weight: 800; font-size: 1.1rem;">
            <span style="font-size: 1.6rem;">🚨</span>
            <span>{get_text('emergency_alert_title', lang)}</span>
        </div>
        <div style="display: flex; align-items: center; gap: 10px; flex-wrap: wrap;">
            <a href="tel:1930" style="background: #ffffff; color: #b91c1c; padding: 8px 20px; border-radius: 9999px; 
                                     font-weight: 900; text-decoration: none; font-size: 1.05rem; box-shadow: 0 4px 10px rgba(0,0,0,0.2); display: inline-flex; align-items: center; gap: 6px;">
                <span>📞</span> <span>1930 కాల్ చేయండి</span>
            </a>
            <a href="https://cybercrime.gov.in" target="_blank" style="background: #091b36; color: #ffffff; padding: 8px 18px; border-radius: 9999px; 
                                     font-weight: 800; text-decoration: none; font-size: 0.95rem; border: 1px solid rgba(255,255,255,0.3); display: inline-flex; align-items: center; gap: 6px;">
                <span>🌐</span> <span>cybercrime.gov.in ↗</span>
            </a>
        </div>
    </div>
    """)

    # ------------------ NAVIGATION BUTTONS ROW ------------------
    nav_items = [
        {"id": "home", "icon": "🏠", "label": get_text('nav_home', lang)},
        {"id": "frauds", "icon": "🔐", "label": get_text('nav_frauds', lang)},
        {"id": "simulations", "icon": "🎭", "label": get_text('nav_simulations', lang)},
        {"id": "videos", "icon": "🎥", "label": get_text('nav_videos', lang)},
        {"id": "rules", "icon": "🛡️", "label": get_text('nav_rules', lang)},
        {"id": "quiz", "icon": "🧠", "label": get_text('nav_quiz', lang)},
        {"id": "report", "icon": "🚨", "label": get_text('nav_report', lang)},
        {"id": "about", "icon": "ℹ️", "label": get_text('nav_about', lang)}
    ]

    cols = st.columns(len(nav_items))
    for i, item in enumerate(nav_items):
        with cols[i]:
            is_active = (current_page == item["id"])
            btn_type = "primary" if is_active else "secondary"
            btn_title = f"{item['icon']} {item['label']}"
            if st.button(btn_title, key=f"nav_btn_{item['id']}", type=btn_type, use_container_width=True):
                navigate_to(item["id"])

    render_html("<div style='margin-bottom: 22px;'></div>")
