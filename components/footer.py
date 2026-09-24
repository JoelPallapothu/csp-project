"""
CAVI - Cyber Aware Village Initiative
Professional Public Welfare Desktop-First Footer Component with Helpline Links and CSP Attribution.
Bilingual: Telugu (Default) and English.
"""

import streamlit as st
from data.translations import get_text
from utils.helpers import get_current_lang, navigate_to
from utils.styling import render_html

def render_footer():
    lang = get_current_lang()

    em_heading = "🚨 అత్యవసర సహాయం (Emergency)" if lang == "te" else "🚨 24x7 Emergency Helplines"
    nat_helpline = "జాతీయ సైబర్ క్రైమ్ హెల్ప్‌లైన్:" if lang == "te" else "National Cyber Crime Helpline:"
    off_site = "అధికారిక వెబ్‌సైట్:" if lang == "te" else "Official Government Portal:"
    principles_head = "🛡️ ముఖ్య సూత్రాలు (Core Principles)" if lang == "te" else "🛡️ Core Principles"
    csp_title = "కమ్యూనిటీ సర్వీస్ ప్రాజెక్ట్ (Community Service Project - CSP)" if lang == "te" else "Community Service Project (CSP) Educational Outreach"
    foot_tag = "ఆంధ్రప్రదేశ్ గ్రామీణ వర్గాల డిజిటల్ రక్షణకై రూపొందించబడింది • 2026" if lang == "te" else "Empowering Rural Citizens with Digital Security • Andhra Pradesh 2026"

    render_html(f"""
    <div class="cavi-footer">
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 32px; margin-bottom: 28px;">
            <div>
                <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 12px;">
                    <span style="font-size: 2.0rem;">🛡️</span>
                    <span style="font-size: 1.55rem; font-weight: 950; color: #ffffff;">CAVI</span>
                </div>
                <div style="font-size: 1.15rem; font-weight: 850; color: #38bdf8; margin-bottom: 8px;">
                    {get_text('app_full_name', lang)}
                </div>
                <p style="font-size: 1.02rem; color: #e2e8f0; line-height: 1.6; margin-bottom: 12px;">
                    "{get_text('tagline', lang)}"
                </p>
                <div style="font-size: 0.95rem; color: #cbd5e1; font-weight: 700;">
                    {csp_title}
                </div>
            </div>

            <div>
                <div style="font-size: 1.25rem; font-weight: 950; color: #ffffff; margin-bottom: 16px;">
                    {em_heading}
                </div>
                <div style="margin-bottom: 12px;">
                    <div style="font-size: 0.92rem; color: #e2e8f0; margin-bottom: 2px;">{nat_helpline}</div>
                    <a href="tel:1930" style="color: #fca5a5; font-weight: 950; font-size: 1.65rem; text-decoration: none; display: inline-flex; align-items: center; gap: 6px;">
                        <span>📞</span> <span>1930 (24x7)</span>
                    </a>
                </div>
                <div style="margin-bottom: 12px;">
                    <div style="font-size: 0.92rem; color: #e2e8f0; margin-bottom: 2px;">{off_site}</div>
                    <a href="https://cybercrime.gov.in" target="_blank" style="color: #38bdf8; font-weight: 850; text-decoration: none; font-size: 1.05rem;">
                        🌐 cybercrime.gov.in ↗
                    </a>
                </div>
                <div style="font-size: 0.95rem; color: #e2e8f0;">
                    పోలీస్ ఎమర్జెన్సీ / Police Emergency: <b style="color: #ffffff;">112 / 100</b>
                </div>
            </div>

            <div>
                <div style="font-size: 1.25rem; font-weight: 950; color: #ffffff; margin-bottom: 16px;">
                    {principles_head}
                </div>
                <div style="font-size: 1.02rem; color: #e2e8f0; line-height: 2.1;">
                    <div>🛡️ <b style="color: #ffffff;">జాగ్రత్తగా ఉండండి</b> (Stay Alert)</div>
                    <div>📱 <b style="color: #ffffff;">భద్రంగా ఉండండి</b> (Stay Safe)</div>
                    <div>🚨 <b style="color: #fca5a5;">1930 కి కాల్ చేయండి</b> (Report Fraud Early)</div>
                    <div>🤝 <b style="color: #ffffff;">గ్రామస్తులకు వివరించండి</b> (Spread Awareness)</div>
                </div>
            </div>
        </div>

        <hr style="border: none; border-top: 1px solid rgba(255,255,255,0.22); margin: 24px 0 18px 0;">

        <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 14px; font-size: 0.95rem; color: #e2e8f0;">
            <div style="color: #cbd5e1;">
                {get_text('footer_text', lang)}
            </div>
            <div style="font-weight: 800; color: #ffffff;">
                {foot_tag}
            </div>
        </div>
    </div>
    """)
