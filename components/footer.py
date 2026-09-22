"""
CAVI - Cyber Aware Village Initiative
Professional Public Welfare Footer Component with Helpline Links and CSP Attribution
"""

import streamlit as st
from data.translations import get_text
from utils.helpers import get_current_lang
from utils.styling import render_html

def render_footer():
    lang = get_current_lang()

    render_html(f"""
    <div class="cavi-footer">
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 28px; margin-bottom: 24px;">
            <div>
                <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 12px;">
                    <span style="font-size: 1.8rem;">🛡️</span>
                    <span style="font-size: 1.4rem; font-weight: 900; color: #ffffff;">CAVI</span>
                </div>
                <div style="font-size: 1.05rem; font-weight: 700; color: #38bdf8; margin-bottom: 8px;">
                    {get_text('app_full_name', lang)}
                </div>
                <p style="font-size: 0.95rem; color: #94a3b8; line-height: 1.5;">
                    "Raising Awareness to Prevent Cyber Fraud Among Illiterate and Semi-Literate Villagers"
                </p>
                <div style="font-size: 0.88rem; color: #cbd5e1; font-weight: 600;">
                    కమ్యూనిటీ సర్వీస్ ప్రాజెక్ట్ (Community Service Project - CSP)
                </div>
            </div>

            <div>
                <div style="font-size: 1.15rem; font-weight: 800; color: #ffffff; margin-bottom: 14px;">
                    🚨 అత్యవసర సహాయం (Emergency Contacts)
                </div>
                <div style="margin-bottom: 10px;">
                    <div style="font-size: 0.85rem; color: #94a3b8;">జాతీయ సైబర్ క్రైమ్ హెల్ప్‌లైన్:</div>
                    <a href="tel:1930" style="color: #f87171; font-weight: 900; font-size: 1.4rem; text-decoration: none;">
                        📞 1930 (24x7 టోల్ ఫ్రీ)
                    </a>
                </div>
                <div style="margin-bottom: 10px;">
                    <div style="font-size: 0.85rem; color: #94a3b8;">అధికారిక వెబ్‌సైట్:</div>
                    <a href="https://cybercrime.gov.in" target="_blank" style="color: #38bdf8; font-weight: 700; text-decoration: none; font-size: 1.0rem;">
                        🌐 cybercrime.gov.in ↗
                    </a>
                </div>
                <div style="font-size: 0.88rem; color: #94a3b8;">
                    పోలీస్ ఎమర్జెన్సీ: <b>112 / 100</b>
                </div>
            </div>

            <div>
                <div style="font-size: 1.15rem; font-weight: 800; color: #ffffff; margin-bottom: 14px;">
                    🛡️ ముఖ్య సూత్రాలు (Core Principles)
                </div>
                <div style="font-size: 0.95rem; color: #cbd5e1; line-height: 1.8;">
                    <div>🛡️ <b>జాగ్రత్తగా ఉండండి</b> (Stay Alert)</div>
                    <div>📱 <b>భద్రంగా ఉండండి</b> (Stay Safe)</div>
                    <div>🚨 <b>వెంటనే రిపోర్ట్ చేయండి</b> (Report Fraud Early)</div>
                    <div>🤝 <b>గ్రామస్తులకు వివరించండి</b> (Spread Awareness)</div>
                </div>
            </div>
        </div>

        <hr style="border: none; border-top: 1px solid rgba(255,255,255,0.1); margin: 20px 0;">

        <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 12px; font-size: 0.88rem; color: #94a3b8;">
            <div>
                {get_text('footer_text', lang)}
            </div>
            <div style="font-weight: 600; color: #cbd5e1;">
                ఆంధ్రప్రదేశ్ గ్రామీణ వర్గాల డిజిటల్ రక్షణకై రూపొందించబడింది • 2026
            </div>
        </div>
    </div>
    """)
