"""
==============================================================================
CAVI - Cyber Aware Village Initiative
"Raising Awareness to Prevent Cyber Fraud Among Illiterate and Semi-Literate Villagers"
A Production-Quality Streamlit Web Application for Community Service Project (CSP)
==============================================================================
"""

import streamlit as st
import os

# Page config must be first Streamlit command
st.set_page_config(
    page_title="CAVI - Cyber Aware Village Initiative",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

from utils.helpers import (
    init_session_state, get_current_lang, get_current_page, navigate_to, calculate_safety_score
)
from utils.styling import get_custom_css, render_html
from data.translations import get_text
from components.header_nav import render_header_nav
from components.fraud_card import render_frauds_grid, render_fraud_detail
from components.simulations import render_simulations_page
from components.video_center import render_video_center
from components.safety_guide import render_safety_guide
from components.quiz import render_quiz
from components.emergency_view import render_emergency_page
from components.about_view import render_about_page
from components.poster_showcase import render_poster_showcase
from components.footer import render_footer

# Initialize session state variables
init_session_state()

# Inject modern responsive CSS with dynamic font size accessibility mode
font_mode = st.session_state.get("font_size_mode", "normal")
render_html(get_custom_css(font_mode))

# Render persistent header, accessibility toolbar, emergency strip & navigation
render_header_nav()

# Retrieve current route & language
current_page = get_current_page()
lang = get_current_lang()

# ==============================================================================
# 1. HOME PAGE ROUTE
# ==============================================================================
if current_page == "home":
    # Illustrative Rural Hero Section
    render_html(f"""
    <div class="hero-banner">
        <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 24px;">
            <div style="flex: 1 1 580px;">
                <div style="display: flex; align-items: center; gap: 8px; margin-bottom: 12px; flex-wrap: wrap;">
                    <span class="badge-pill" style="background: rgba(56, 189, 248, 0.22); color: #7dd3fc; border: 1px solid #38bdf8; font-size: 0.88rem;">
                        🛡️ {get_text('csp_badge', lang)}
                    </span>
                    <span class="badge-pill" style="background: rgba(255, 255, 255, 0.15); color: #ffffff; border: 1px solid rgba(255,255,255,0.25); font-size: 0.88rem;">
                        📍 {get_text('ap_focus', lang)}
                    </span>
                </div>
                <h1 style="color: white; margin: 8px 0 14px 0;">
                    {get_text('app_title', lang)}
                </h1>
                <p style="margin-bottom: 16px; font-weight: 500; font-size: 1.15rem; line-height: 1.6;">
                    {get_text('hero_desc', lang)}
                </p>
                <div style="font-size: 1.25rem; font-weight: 900; color: #fef08a; letter-spacing: 0.3px;">
                    {get_text('tagline', lang)}
                </div>
            </div>
            <div style="flex: 0 0 260px; text-align: center; background: rgba(255,255,255,0.09); border-radius: 24px; padding: 24px; border: 1.5px solid rgba(255,255,255,0.2); box-shadow: 0 8px 24px rgba(0,0,0,0.2);">
                <div style="font-size: 4.2rem; margin-bottom: 6px; line-height: 1;">🌾📱🛡️</div>
                <div style="font-weight: 900; font-size: 1.25rem; color: #ffffff; margin-bottom: 4px;">గ్రామీణ సైబర్ రక్షణ</div>
                <div style="font-size: 0.9rem; color: #bae6fd; font-weight: 600;">CAVI Village Learning Hub</div>
                <div style="font-size: 0.78rem; color: #fef08a; margin-top: 6px; font-weight: 700;">100% ఉచిత ప్రజా సేవ</div>
            </div>
        </div>
    </div>
    """)

    # 5 Large Vibrant Action Tiles
    col_h1, col_h2, col_h3, col_h4, col_h5 = st.columns(5)
    with col_h1:
        if st.button("🔐 " + get_text('hero_btn_learn', lang), key="hero_learn", type="primary", use_container_width=True):
            navigate_to("frauds")
    with col_h2:
        if st.button("🎥 " + get_text('hero_btn_videos', lang), key="hero_vids", use_container_width=True):
            navigate_to("videos")
    with col_h3:
        if st.button("🧠 " + get_text('hero_btn_quiz', lang), key="hero_quiz", use_container_width=True):
            navigate_to("quiz")
    with col_h4:
        if st.button("🎭 " + get_text('hero_btn_spot_scam', lang), key="hero_sims", use_container_width=True):
            navigate_to("simulations")
    with col_h5:
        if st.button("🚨 " + get_text('hero_btn_report', lang), key="hero_rep", use_container_width=True):
            navigate_to("report")

    render_html("<div style='margin-bottom: 22px;'></div>")

    # Compact Home Emergency Card
    render_html(f"""
    <div style="background: linear-gradient(90deg, #7f1d1d 0%, #b91c1c 45%, #991b1b 100%); border-radius: 18px; padding: 18px 24px; color: #ffffff; margin-bottom: 26px; box-shadow: 0 8px 24px rgba(185,28,28,0.25); display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 16px; border: 1.5px solid #fca5a5;">
        <div style="flex: 1 1 500px;">
            <div style="font-size: 1.22rem; font-weight: 900; color: #ffffff; margin-bottom: 4px; display: flex; align-items: center; gap: 8px;">
                <span>🚨</span> <span>{get_text('home_emergency_title', lang)}</span>
            </div>
            <div style="font-size: 0.95rem; color: #fecaca; line-height: 1.45;">
                {get_text('home_emergency_desc', lang)}
            </div>
        </div>
        <div style="display: flex; gap: 10px; align-items: center; flex-wrap: wrap;">
            <a href="tel:1930" style="background: #ffffff; color: #b91c1c; font-weight: 900; padding: 10px 22px; border-radius: 9999px; text-decoration: none; font-size: 1.05rem; box-shadow: 0 4px 12px rgba(0,0,0,0.15); display: inline-flex; align-items: center; gap: 6px;">
                <span>📞</span> <span>1930</span>
            </a>
            <a href="https://cybercrime.gov.in" target="_blank" style="background: rgba(0,0,0,0.35); color: #ffffff; font-weight: 800; padding: 10px 20px; border-radius: 9999px; text-decoration: none; font-size: 0.95rem; border: 1px solid rgba(255,255,255,0.4); display: inline-flex; align-items: center; gap: 6px;">
                <span>{get_text('home_emergency_portal_btn', lang)}</span> <span>↗</span>
            </a>
        </div>
    </div>
    """)

    # 4 Key Statistics Cards
    stat_cols = st.columns(4)
    stats = [
        {"icon": "🛡️", "title": get_text('stat_tips_title', lang), "val": get_text('stat_tips_val', lang), "color": "#16a34a"},
        {"icon": "⚠️", "title": get_text('stat_frauds_title', lang), "val": get_text('stat_frauds_val', lang), "color": "#dc2626"},
        {"icon": "🎭", "title": get_text('stat_sims_title', lang), "val": get_text('stat_sims_val', lang), "color": "#0284c7"},
        {"icon": "🌐", "title": get_text('stat_langs_title', lang), "val": get_text('stat_langs_val', lang), "color": "#7c3aed"}
    ]
    for idx, stat in enumerate(stats):
        with stat_cols[idx]:
            render_html(f"""
            <div class="cavi-card" style="border-bottom: 5px solid {stat['color']}; text-align: center; padding: 20px 16px; margin-bottom: 0;">
                <div style="font-size: 2.2rem; margin-bottom: 4px;">{stat['icon']}</div>
                <div style="font-size: 1.85rem; font-weight: 950; color: {stat['color']}; margin-bottom: 2px;">
                    {stat['val']}
                </div>
                <div style="font-size: 0.98rem; font-weight: 700; color: #475569;">
                    {stat['title']}
                </div>
            </div>
            """)

    render_html("<div style='margin-bottom: 26px;'></div>")

    # Interactive "Cyber Rakshak" Progress Level Bar
    safety_score = calculate_safety_score()
    if safety_score < 40:
        level_label = "🌱 ఆరంభ స్థాయి (Beginner Explorer) - పాఠాలు చూడండి!"
        level_color = "#0284c7"
    elif safety_score < 75:
        level_label = "⚡ అప్రమత్త గ్రామస్తుడు (Alert Villager) - మంచి పురోగతి!"
        level_color = "#d97706"
    else:
        level_label = "🏆 గ్రామ సైబర్ రక్షకుడు (Village Cyber Guardian) - అద్భుతం!"
        level_color = "#16a34a"

    render_html(f"""
    <div class="cavi-card" style="background: linear-gradient(90deg, #f0f9ff 0%, #ffffff 100%); border-left: 6px solid {level_color};">
        <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 12px; margin-bottom: 8px;">
            <div>
                <div style="font-size: 1.2rem; font-weight: 900; color: #091b36;">
                    📊 {get_text('progress_title', lang)}
                </div>
                <div style="font-size: 0.95rem; font-weight: 700; color: {level_color}; margin-top: 2px;">
                    {level_label}
                </div>
            </div>
            <div style="font-size: 2.0rem; font-weight: 950; color: {level_color};">
                {safety_score}%
            </div>
        </div>
    </div>
    """)
    st.progress(safety_score / 100)

    render_html("<div style='margin-bottom: 32px;'></div>")

    # Original Community Awareness Poster Showcase on Home
    render_poster_showcase()

    render_html("<div style='margin-bottom: 32px;'></div>")

    # Common Frauds Section Header
    render_html(f"""
    <div style="margin-bottom: 20px;">
        <h2 style="color: #091b36; margin-bottom: 6px; font-size: 1.75rem;">
            ⚠️ {get_text('common_frauds_heading', lang)}
        </h2>
        <p style="font-size: 1.15rem; color: #475569;">
            {get_text('common_frauds_sub', lang)}
        </p>
    </div>
    """)

    # 12 Common Fraud Cards Grid
    render_frauds_grid()

# ==============================================================================
# 2. KNOW THE FRAUD ROUTE
# ==============================================================================
elif current_page == "frauds":
    selected_fraud = st.session_state.get("selected_fraud_id", None)
    if selected_fraud:
        render_fraud_detail(selected_fraud)
    else:
        render_html("""
        <div style="margin-bottom: 24px;">
            <h2 style="color: #091b36; margin-bottom: 6px; font-size: 1.75rem;">
                🔐 మీరు ఏ మోసం గురించి తెలుసుకోవాలనుకుంటున్నారు?
            </h2>
            <p style="font-size: 1.15rem; color: #475569;">
                గ్రామీణ ప్రాంతాల్లో జరుగుతున్న 12 ప్రధాన సైబర్ మోసాల వివరాలను క్రింది కార్డులపై నొక్కి సులభంగా తెలుసుకోండి.
            </p>
        </div>
        """)
        render_frauds_grid()

# ==============================================================================
# 3. REAL-LIFE SIMULATIONS ROUTE
# ==============================================================================
elif current_page == "simulations":
    render_simulations_page()

# ==============================================================================
# 4. AWARENESS VIDEOS ROUTE
# ==============================================================================
elif current_page == "videos":
    render_video_center()

# ==============================================================================
# 5. SAFETY GUIDE ROUTE
# ==============================================================================
elif current_page == "rules":
    render_safety_guide()

# ==============================================================================
# 6. CYBER SAFETY QUIZ ROUTE
# ==============================================================================
elif current_page == "quiz":
    render_quiz()

# ==============================================================================
# 7. REPORT FRAUD ROUTE (1930)
# ==============================================================================
elif current_page == "report":
    render_emergency_page()

# ==============================================================================
# 8. ABOUT CAVI ROUTE
# ==============================================================================
elif current_page == "about":
    render_about_page()

# Always render footer at bottom
render_footer()
