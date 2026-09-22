"""
CAVI - Cyber Aware Village Initiative
Original Community Awareness Poster Interactive Showcase, Hotspot Breakdown & Download Facility
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

    render_html(f"""
    <div class="cavi-card" style="border-top: 6px solid #091b36; margin-bottom: 28px;">
        <div style="display: flex; justify-content: space-between; align-items: flex-start; flex-wrap: wrap; gap: 14px; margin-bottom: 12px;">
            <div>
                <span class="badge-pill badge-info" style="font-size: 0.85rem;">
                    🎓 కమ్యూనిటీ సర్వీస్ ప్రాజెక్ట్ (CSP) అధికారిక పోస్టర్
                </span>
                <h2 style="color: #091b36; margin: 10px 0 6px 0; font-size: 1.75rem;">
                    {get_text('poster_heading', lang)}
                </h2>
                <p style="color: #475569; font-size: 1.08rem; margin-bottom: 0;">
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
        render_html("""
        <div style="background: #ffffff; border: 1px solid #e2e8f0; border-radius: 22px; padding: 26px; box-shadow: 0 6px 20px rgba(15,43,92,0.06);">
            <h3 style="color: #091b36; margin-top: 0; font-size: 1.35rem; display: flex; align-items: center; gap: 8px;">
                <span>📌</span> పోస్టర్ లోని 5 ప్రధాన హెచ్చరికలు:
            </h3>
            
            <div style="background: #f8fafc; border-left: 4px solid #dc2626; border-radius: 10px; padding: 12px 14px; margin-bottom: 12px;">
                <div style="font-weight: 800; color: #dc2626; font-size: 1.05rem;">1. 🔐 ఓటీపీ రక్షణ (Never Share OTP):</div>
                <div style="font-size: 0.95rem; color: #334155; margin-top: 2px;">బ్యాంక్ అధికారులు ఎప్పుడూ ఓటీపీ అడగరు. ఎవరికీ మీ నంబర్లు చెప్పకండి.</div>
            </div>

            <div style="background: #f8fafc; border-left: 4px solid #ea580c; border-radius: 10px; padding: 12px 14px; margin-bottom: 12px;">
                <div style="font-weight: 800; color: #ea580c; font-size: 1.05rem;">2. 💳 యూపీఐ సువర్ణ నియమం (UPI Golden Rule):</div>
                <div style="font-size: 0.95rem; color: #334155; margin-top: 2px;">డబ్బులు మీ ఖాతాలోకి రావడానికి పిన్ అవసరం లేదు. పిన్ కేవలం పంపడానికి మాత్రమే.</div>
            </div>

            <div style="background: #f8fafc; border-left: 4px solid #b91c1c; border-radius: 10px; padding: 12px 14px; margin-bottom: 12px;">
                <div style="font-weight: 800; color: #b91c1c; font-size: 1.05rem;">3. 🏦 నకిలీ కేవైసీ లింకులు (Fake KYC Links):</div>
                <div style="font-size: 0.95rem; color: #334155; margin-top: 2px;">ఖాతా ఆగిపోతుందని వచ్చే ఎస్ఎంఎస్ లింకులను నొక్కవద్దు. బ్రాంచ్‌ను నేరుగా కలవండి.</div>
            </div>

            <div style="background: #f8fafc; border-left: 4px solid #d97706; border-radius: 10px; padding: 12px 14px; margin-bottom: 12px;">
                <div style="font-weight: 800; color: #d97706; font-size: 1.05rem;">4. 🎁 బహుమతి / లాటరీ మోసం (Lottery Scam):</div>
                <div style="font-size: 0.95rem; color: #334155; margin-top: 2px;">టికెట్ కొనకుండా లాటరీ రాదు. బహుమతి కోసం ముందుగా డబ్బులు అడిగితే మోసమే.</div>
            </div>

            <div style="background: #f8fafc; border-left: 4px solid #7c3aed; border-radius: 10px; padding: 12px 14px; margin-bottom: 14px;">
                <div style="font-weight: 800; color: #7c3aed; font-size: 1.05rem;">5. 📱 స్క్రీన్ షేరింగ్ ప్రమాదం (AnyDesk Danger):</div>
                <div style="font-size: 0.95rem; color: #334155; margin-top: 2px;">AnyDesk వంటి యాప్‌లు ఎక్కిస్తే మీ ఫోన్ పాస్‌వర్డ్‌లను మోసగాళ్లు చూస్తారు.</div>
            </div>

            <div style="background: #fef2f2; border: 2px solid #fecaca; border-radius: 12px; padding: 14px; text-align: center;">
                <div style="font-size: 1.15rem; font-weight: 950; color: #dc2626;">🚨 అత్యవసర హెల్ప్‌లైన్: 1930</div>
                <div style="font-size: 0.92rem; font-weight: 700; color: #091b36; margin-top: 2px;">పోర్టల్: cybercrime.gov.in</div>
            </div>
        </div>
        """)
