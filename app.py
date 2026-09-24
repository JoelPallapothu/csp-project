"""
==============================================================================
CAVI - Cyber Aware Village Initiative
"Raising Awareness to Prevent Cyber Fraud Among Illiterate and Semi-Literate Villagers"
A Production-Quality Desktop-First Streamlit Web Application for Community Service Project (CSP)
Bilingual: Telugu (Default) and English.
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
    # Full-Width Premium Hero Section
    render_html(f"""
    <div class="hero-banner">
        <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 32px;">
            <div style="flex: 1 1 640px;">
                <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 14px; flex-wrap: wrap;">
                    <span class="badge-pill" style="background: rgba(56, 189, 248, 0.25); color: #7dd3fc; border: 1.5px solid #38bdf8; font-size: 0.92rem; padding: 6px 14px;">
                        🛡️ {get_text('csp_badge', lang)}
                    </span>
                    <span class="badge-pill" style="background: rgba(255, 255, 255, 0.16); color: #ffffff; border: 1.5px solid rgba(255,255,255,0.3); font-size: 0.92rem; padding: 6px 14px;">
                        📍 {get_text('ap_focus', lang)}
                    </span>
                </div>
                <h1 style="color: white; margin: 10px 0 16px 0; font-size: 2.6rem; font-weight: 950; line-height: 1.25;">
                    {get_text('app_title', lang)}
                </h1>
                <p style="margin-bottom: 20px; font-weight: 500; font-size: 1.2rem; line-height: 1.65; color: #e0f2fe; max-width: 720px;">
                    {get_text('hero_desc', lang)}
                </p>
                <div style="font-size: 1.3rem; font-weight: 900; color: #fef08a; letter-spacing: 0.3px; display: flex; align-items: center; gap: 8px;">
                    <span>✨</span> <span>{get_text('tagline', lang)}</span>
                </div>
            </div>
            
            <!-- Realistic Visual Composition Right Panel -->
            <div style="flex: 0 0 340px; text-align: center; background: rgba(255,255,255,0.1); border-radius: 28px; padding: 28px 24px; border: 2px solid rgba(255,255,255,0.25); box-shadow: 0 16px 36px rgba(0,0,0,0.25); backdrop-filter: blur(10px);">
                <div style="font-size: 3.8rem; margin-bottom: 10px; line-height: 1.1; letter-spacing: 4px;">
                    🌾📱🛡️🔐
                </div>
                <div style="font-weight: 950; font-size: 1.35rem; color: #ffffff; margin-bottom: 6px;">
                    గ్రామీణ సైబర్ రక్షణ కవచం
                </div>
                <div style="font-size: 0.98rem; color: #bae6fd; font-weight: 700; margin-bottom: 12px;">
                    Village Digital Security Network
                </div>
                <div style="display: flex; justify-content: center; gap: 8px; flex-wrap: wrap; margin-top: 10px;">
                    <span style="background: rgba(22,132,71,0.3); color: #86efac; border: 1px solid #86efac; border-radius: 9999px; padding: 4px 12px; font-size: 0.8rem; font-weight: 800;">👨‍👩‍👧‍👦 కుటుంబ భద్రత</span>
                    <span style="background: rgba(244,180,0,0.25); color: #fef08a; border: 1px solid #fef08a; border-radius: 9999px; padding: 4px 12px; font-size: 0.8rem; font-weight: 800;">100% ఉచిత ప్రజా సేవ</span>
                </div>
            </div>
        </div>
    </div>
    """)

    # 5 Large Vibrant Desktop Action Tiles
    col_h1, col_h2, col_h3, col_h4, col_h5 = st.columns(5)
    with col_h1:
        if st.button("🛡️ " + get_text('hero_btn_learn', lang), key="hero_learn", type="primary", use_container_width=True):
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

    render_html("<div style='margin-bottom: 24px;'></div>")

    # Compact Home Emergency Card
    render_html(f"""
    <div style="background: linear-gradient(90deg, #7f1d1d 0%, #b91c1c 45%, #991b1b 100%); border-radius: 20px; padding: 20px 28px; color: #ffffff; margin-bottom: 28px; box-shadow: 0 8px 24px rgba(185,28,28,0.25); display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 16px; border: 2px solid #fca5a5;">
        <div style="flex: 1 1 540px;">
            <div style="font-size: 1.3rem; font-weight: 950; color: #ffffff; margin-bottom: 4px; display: flex; align-items: center; gap: 10px;">
                <span style="font-size: 1.6rem;">🚨</span> <span>{get_text('home_emergency_title', lang)}</span>
            </div>
            <div style="font-size: 1.02rem; color: #fecaca; line-height: 1.5;">
                {get_text('home_emergency_desc', lang)}
            </div>
        </div>
        <div style="display: flex; gap: 12px; align-items: center; flex-wrap: wrap;">
            <a href="tel:1930" style="background: #ffffff; color: #b91c1c; font-weight: 950; padding: 12px 26px; border-radius: 9999px; text-decoration: none; font-size: 1.15rem; box-shadow: 0 4px 14px rgba(0,0,0,0.18); display: inline-flex; align-items: center; gap: 8px;">
                <span>📞</span> <span>1930</span>
            </a>
            <a href="https://cybercrime.gov.in" target="_blank" style="background: rgba(0,0,0,0.4); color: #ffffff; font-weight: 800; padding: 12px 22px; border-radius: 9999px; text-decoration: none; font-size: 1.0rem; border: 1.5px solid rgba(255,255,255,0.4); display: inline-flex; align-items: center; gap: 6px;">
                <span>{get_text('home_emergency_portal_btn', lang)}</span> <span>↗</span>
            </a>
        </div>
    </div>
    """)

    # 4 Key Statistics Cards
    stat_cols = st.columns(4)
    stats = [
        {"icon": "🛡️", "title": get_text('stat_tips_title', lang), "val": get_text('stat_tips_val', lang), "color": "#168447"},
        {"icon": "⚠️", "title": get_text('stat_frauds_title', lang), "val": get_text('stat_frauds_val', lang), "color": "#d62828"},
        {"icon": "🎭", "title": get_text('stat_sims_title', lang), "val": get_text('stat_sims_val', lang), "color": "#0b63ce"},
        {"icon": "🌐", "title": get_text('stat_langs_title', lang), "val": get_text('stat_langs_val', lang), "color": "#063970"}
    ]
    for idx, stat in enumerate(stats):
        with stat_cols[idx]:
            render_html(f"""
            <div class="cavi-card" style="border-bottom: 5px solid {stat['color']}; text-align: center; padding: 22px 18px; margin-bottom: 0;">
                <div style="font-size: 2.4rem; margin-bottom: 6px;">{stat['icon']}</div>
                <div style="font-size: 2.0rem; font-weight: 950; color: {stat['color']}; margin-bottom: 3px;">
                    {stat['val']}
                </div>
                <div style="font-size: 1.05rem; font-weight: 800; color: #475569;">
                    {stat['title']}
                </div>
            </div>
            """)

    render_html("<div style='margin-bottom: 28px;'></div>")

    # Interactive "Cyber Rakshak" Progress Level Bar
    safety_score = calculate_safety_score()
    if safety_score < 40:
        level_label = "🌱 ఆరంభ స్థాయి (Beginner Explorer) - పాఠాలు చూడండి!" if lang == "te" else "🌱 Beginner Explorer - Start learning lessons!"
        level_color = "#0b63ce"
    elif safety_score < 75:
        level_label = "⚡ అప్రమత్త గ్రామస్తుడు (Alert Villager) - మంచి పురోగతి!" if lang == "te" else "⚡ Alert Citizen - Good progress!"
        level_color = "#f4b400"
    else:
        level_label = "🏆 గ్రామ సైబర్ రక్షకుడు (Village Cyber Guardian) - అద్భుతం!" if lang == "te" else "🏆 Village Cyber Guardian - Outstanding!"
        level_color = "#168447"

    render_html(f"""
    <div class="cavi-card" style="background: linear-gradient(90deg, #f0f9ff 0%, #ffffff 100%); border-left: 6px solid {level_color};">
        <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 12px; margin-bottom: 8px;">
            <div>
                <div style="font-size: 1.25rem; font-weight: 900; color: #063970;">
                    📊 {get_text('progress_title', lang)}
                </div>
                <div style="font-size: 1.02rem; font-weight: 800; color: {level_color}; margin-top: 3px;">
                    {level_label}
                </div>
            </div>
            <div style="font-size: 2.2rem; font-weight: 950; color: {level_color};">
                {safety_score}%
            </div>
        </div>
    </div>
    """)
    st.progress(safety_score / 100)

    render_html("<div style='margin-bottom: 32px;'></div>")

    # Original Community Awareness Poster Showcase on Home
    render_poster_showcase()

    render_html("<div style='margin-bottom: 36px;'></div>")

    # Section 01 Header: Common Frauds
    render_html(f"""
    <div class="section-header-box">
        <span class="section-number">01</span>
        <div>
            <h2 style="color: #063970; margin: 0; font-size: 1.9rem; font-weight: 900;">
                ⚠️ {get_text('common_frauds_heading', lang)}
            </h2>
            <p style="font-size: 1.15rem; color: #475569; margin: 4px 0 0 0;">
                {get_text('common_frauds_sub', lang)}
            </p>
        </div>
    </div>
    """)

    # 12 Common Fraud Cards Grid
    render_frauds_grid()

# ==============================================================================
# 2. KNOW THE FRAUD ROUTE (01)
# ==============================================================================
elif current_page == "frauds":
    selected_fraud = st.session_state.get("selected_fraud_id", None)
    if selected_fraud:
        render_fraud_detail(selected_fraud)
    else:
        render_html(f"""
        <div class="section-header-box">
            <span class="section-number">01</span>
            <div>
                <h2 style="color: #063970; margin: 0; font-size: 1.9rem; font-weight: 900;">
                    ⚠️ {get_text('sec_01_frauds', lang)}
                </h2>
                <p style="font-size: 1.15rem; color: #475569; margin: 4px 0 0 0;">
                    {get_text('common_frauds_sub', lang)}
                </p>
            </div>
        </div>
        """)
        render_frauds_grid()

# ==============================================================================
# 3. AWARENESS VIDEOS ROUTE (02)
# ==============================================================================
elif current_page == "videos":
    render_html(f"""
    <div class="section-header-box">
        <span class="section-number">02</span>
        <div>
            <h2 style="color: #063970; margin: 0; font-size: 1.9rem; font-weight: 900;">
                🎥 {get_text('sec_02_videos', lang)}
            </h2>
        </div>
    </div>
    """)
    render_video_center()

# ==============================================================================
# 4. SAFETY GUIDE ROUTE (03)
# ==============================================================================
elif current_page == "rules":
    render_html(f"""
    <div class="section-header-box">
        <span class="section-number">03</span>
        <div>
            <h2 style="color: #063970; margin: 0; font-size: 1.9rem; font-weight: 900;">
                🛡️ {get_text('sec_03_rules', lang)}
            </h2>
        </div>
    </div>
    """)
    render_safety_guide()

# ==============================================================================
# 5. CYBER SAFETY QUIZ ROUTE (04)
# ==============================================================================
elif current_page == "quiz":
    render_html(f"""
    <div class="section-header-box">
        <span class="section-number">04</span>
        <div>
            <h2 style="color: #063970; margin: 0; font-size: 1.9rem; font-weight: 900;">
                🧠 {get_text('sec_04_quiz', lang)}
            </h2>
        </div>
    </div>
    """)
    render_quiz()

# ==============================================================================
# 6. SPOT THE SCAM & UPI SIMULATION ROUTE (05)
# ==============================================================================
elif current_page == "simulations":
    render_html(f"""
    <div class="section-header-box">
        <span class="section-number">05</span>
        <div>
            <h2 style="color: #063970; margin: 0; font-size: 1.9rem; font-weight: 900;">
                🎭 {get_text('sec_05_sims', lang)}
            </h2>
        </div>
    </div>
    """)
    render_simulations_page()

# ==============================================================================
# 7. REPORT FRAUD ROUTE (06 - 1930)
# ==============================================================================
elif current_page == "report":
    render_html(f"""
    <div class="section-header-box">
        <span class="section-number">06</span>
        <div>
            <h2 style="color: #063970; margin: 0; font-size: 1.9rem; font-weight: 900;">
                🚨 {get_text('sec_06_report', lang)}
            </h2>
        </div>
    </div>
    """)
    render_emergency_page()

# ==============================================================================
# 8. ABOUT CAVI ROUTE (07)
# ==============================================================================
elif current_page == "about":
    render_html(f"""
    <div class="section-header-box">
        <span class="section-number">07</span>
        <div>
            <h2 style="color: #063970; margin: 0; font-size: 1.9rem; font-weight: 900;">
                ℹ️ {get_text('nav_about', lang)}
            </h2>
        </div>
    </div>
    """)
    render_about_page()

# Always render footer at bottom
render_footer()
