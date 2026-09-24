"""
CAVI - Cyber Aware Village Initiative
Original Community Awareness Poster Interactive Showcase, Hotspot Breakdown & Download Facility.
Bilingual: Telugu (Default) and English.
"""

import streamlit as st
import os
from data.translations import get_text
from utils.helpers import get_current_lang
from utils.styling import render_html

def render_poster_showcase():
    lang = get_current_lang()
    poster_svg_path = os.path.join(os.path.dirname(__file__), "..", "assets", "poster", "cavi_awareness_poster.svg")
    
    svg_content = ""
    if os.path.exists(poster_svg_path):
        with open(poster_svg_path, "r", encoding="utf-8") as f:
            svg_content = f.read()

    csp_poster_badge = "🎓 కమ్యూనిటీ సర్వీస్ ప్రాజెక్ట్ (CSP) అధికారిక పోస్టర్" if lang == "te" else "🎓 Official Community Service Project Awareness Poster"
    render_html(f"""
    <div class="cavi-card" style="border-top: 6px solid #063970; margin-bottom: 28px;">
        <div style="display: flex; justify-content: space-between; align-items: flex-start; flex-wrap: wrap; gap: 14px; margin-bottom: 12px;">
            <div>
                <span class="badge-pill badge-info" style="font-size: 0.88rem;">
                    {csp_poster_badge}
                </span>
                <h2 style="color: #063970; margin: 10px 0 6px 0; font-size: 1.85rem; font-weight: 900;">
                    {get_text('poster_heading', lang)}
                </h2>
                <p style="color: #475569; font-size: 1.12rem; margin-bottom: 0;">
                    {get_text('poster_sub', lang)}
                </p>
            </div>
        </div>
    </div>
    """)

    col_poster_view, col_poster_info = st.columns([6, 5])

    with col_poster_view:
        if svg_content:
            st.image(svg_content, use_container_width=True)
            st.download_button(
                label=f"📥 {get_text('poster_download', lang)} (High-Resolution SVG Poster)",
                data=svg_content,
                file_name="cavi_village_awareness_poster.svg",
                mime="image/svg+xml",
                type="primary",
                use_container_width=True
            )
        else:
            st.warning("Poster graphic loading...")

    with col_poster_info:
        card_heading = "📌 పోస్టర్ లోని 5 ప్రధాన హెచ్చరికలు:" if lang == "te" else "📌 5 Golden Alerts Highlighted in the Poster:"
        
        if lang == "te":
            p1_title = "1. 🔐 ఓటీపీ రక్షణ (Never Share OTP):"
            p1_desc = "బ్యాంక్ అధికారులు ఎప్పుడూ ఓటీపీ అడగరు. ఎవరికీ మీ నంబర్లు చెప్పకండి."
            p2_title = "2. 💳 యూపీఐ సువర్ణ నియమం (UPI Golden Rule):"
            p2_desc = "డబ్బులు మీ ఖాతాలోకి రావడానికి పిన్ అవసరం లేదు. పిన్ కేవలం పంపడానికి మాత్రమే."
            p3_title = "3. 🏦 నకిలీ కేవైసీ లింకులు (Fake KYC Links):"
            p3_desc = "ఖాతా ఆగిపోతుందని వచ్చే ఎస్ఎంఎస్ లింకులను నొక్కవద్దు. బ్రాంచ్‌ను నేరుగా కలవండి."
            p4_title = "4. 🎁 బహుమతి / లాటరీ మోసం (Lottery Scam):"
            p4_desc = "టికెట్ కొనకుండా లాటరీ రాదు. బహుమతి కోసం ముందుగా డబ్బులు అడిగితే మోసమే."
            p5_title = "5. 📱 స్క్రీన్ షేరింగ్ ప్రమాదం (AnyDesk Danger):"
            p5_desc = "AnyDesk వంటి యాప్‌లు ఎక్కిస్తే మీ ఫోన్ పాస్‌వర్డ్‌లను మోసగాళ్లు చూస్తారు."
            emer_label = "🚨 అత్యవసర హెల్ప్‌లైన్: 1930"
            portal_label = "పోర్టల్: cybercrime.gov.in"
        else:
            p1_title = "1. 🔐 Never Share Your OTP:"
            p1_desc = "Bank managers and government officials never ask for OTP. Keep it secret."
            p2_title = "2. 💳 UPI Golden Rule:"
            p2_desc = "You NEVER enter a UPI PIN to receive money. PIN is strictly for debiting funds."
            p3_title = "3. 🏦 Fake KYC Update SMS:"
            p3_desc = "Never tap SMS links threatening account suspension. Visit your branch directly."
            p4_title = "4. 🎁 Lottery & Prize Traps:"
            p4_desc = "You cannot win a lottery you never entered. Demanding upfront fees = 100% scam."
            p5_title = "5. 📱 Screen Sharing Dangers:"
            p5_desc = "Never install AnyDesk or QuickSupport on caller requests; it exposes passwords."
            emer_label = "🚨 Emergency Helpline: 1930"
            portal_label = "Official Portal: cybercrime.gov.in"

        render_html(f"""
        <div style="background: #ffffff; border: 1px solid #e2e8f0; border-radius: 22px; padding: 26px; box-shadow: 0 6px 20px rgba(15,43,92,0.06);">
            <h3 style="color: #063970; margin-top: 0; font-size: 1.35rem; font-weight: 900; display: flex; align-items: center; gap: 8px;">
                {card_heading}
            </h3>
            
            <div style="background: #f8fafc; border-left: 4px solid #d62828; border-radius: 10px; padding: 12px 16px; margin-bottom: 12px;">
                <div style="font-weight: 800; color: #d62828; font-size: 1.05rem;">{p1_title}</div>
                <div style="font-size: 0.98rem; color: #334155; margin-top: 2px;">{p1_desc}</div>
            </div>

            <div style="background: #f8fafc; border-left: 4px solid #f4b400; border-radius: 10px; padding: 12px 16px; margin-bottom: 12px;">
                <div style="font-weight: 800; color: #b45309; font-size: 1.05rem;">{p2_title}</div>
                <div style="font-size: 0.98rem; color: #334155; margin-top: 2px;">{p2_desc}</div>
            </div>

            <div style="background: #f8fafc; border-left: 4px solid #0b63ce; border-radius: 10px; padding: 12px 16px; margin-bottom: 12px;">
                <div style="font-weight: 800; color: #0b63ce; font-size: 1.05rem;">{p3_title}</div>
                <div style="font-size: 0.98rem; color: #334155; margin-top: 2px;">{p3_desc}</div>
            </div>

            <div style="background: #f8fafc; border-left: 4px solid #7c3aed; border-radius: 10px; padding: 12px 16px; margin-bottom: 12px;">
                <div style="font-weight: 800; color: #7c3aed; font-size: 1.05rem;">{p4_title}</div>
                <div style="font-size: 0.98rem; color: #334155; margin-top: 2px;">{p4_desc}</div>
            </div>

            <div style="background: #f8fafc; border-left: 4px solid #063970; border-radius: 10px; padding: 12px 16px; margin-bottom: 16px;">
                <div style="font-weight: 800; color: #063970; font-size: 1.05rem;">{p5_title}</div>
                <div style="font-size: 0.98rem; color: #334155; margin-top: 2px;">{p5_desc}</div>
            </div>

            <div style="background: #fef2f2; border: 2px solid #fecaca; border-radius: 14px; padding: 14px; text-align: center;">
                <div style="font-size: 1.2rem; font-weight: 950; color: #d62828;">{emer_label}</div>
                <div style="font-size: 0.95rem; font-weight: 700; color: #063970; margin-top: 3px;">{portal_label}</div>
            </div>
        </div>
        """)
