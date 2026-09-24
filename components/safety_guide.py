"""
CAVI - Cyber Aware Village Initiative
Safety Guide Component: 10 Golden Rules with Web Speech Audio & High-Contrast DO vs DON'T Matrix.
Bilingual: Telugu (Default) and English.
"""

import streamlit as st
from data.rules import GOLDEN_RULES, DOS_AND_DONTS
from data.translations import get_text
from utils.helpers import get_current_lang, render_speech_audio_button
from utils.styling import render_html

def render_safety_guide():
    lang = get_current_lang()
    st.session_state.progress["rules_read"] = True

    sub_title = (
        '"ఈ పది నియమాలను పాటిస్తే మీ స్మార్ట్‌ఫోన్ మరియు బ్యాంక్ ఖాతా ఎల్లప్పుడూ సురక్షితంగా ఉంటాయి."'
        if lang == "te" else
        '"Following these 10 golden rules ensures your smartphone and bank account stay 100% secure."'
    )
    render_html(f"""
    <div style="margin-bottom: 26px;">
        <p style="font-size: 1.2rem; color: #475569; margin: 0; font-weight: 500;">
            {sub_title}
        </p>
    </div>
    """)

    # 10 Golden Rules Cards with Audio Playback
    cols_per_row = 2
    for i in range(0, len(GOLDEN_RULES), cols_per_row):
        row_rules = GOLDEN_RULES[i:i + cols_per_row]
        cols = st.columns(len(row_rules))
        for j, rule in enumerate(row_rules):
            with cols[j]:
                r_title = rule["title"].get(lang, rule["title"]["te"])
                r_desc = rule["desc"].get(lang, rule["desc"]["te"])
                rule_badge = f"నియమం {rule['number']}" if lang == "te" else f"Rule {rule['number']}"
                
                render_html(f"""
                <div class="cavi-card" style="border-left: 6px solid #168447; min-height: 220px; display: flex; flex-direction: column; justify-content: space-between;">
                    <div>
                        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px;">
                            <span style="font-size: 2.3rem; line-height: 1;">{rule['icon']}</span>
                            <span class="badge-pill badge-safe" style="font-size: 0.85rem;">
                                {rule_badge}
                            </span>
                        </div>
                        <div style="font-size: 1.28rem; font-weight: 900; color: #063970; margin-bottom: 8px; line-height: 1.35;">
                            {r_title}
                        </div>
                        <div style="font-size: 1.05rem; color: #334155; line-height: 1.6; margin-bottom: 12px;">
                            {r_desc}
                        </div>
                    </div>
                </div>
                """)
                
                # Audio playback control for illiterate & semi-literate users
                render_speech_audio_button(r_desc, lang=lang, key_id=f"rule_audio_{rule['number']}")
        render_html("<div style='margin-bottom: 16px;'></div>")

    render_html("<div style='margin-bottom: 34px;'></div>")

    # DO VS DON'T COMPARISON MATRIX
    matrix_heading = "⚖️ ఏమి చేయాలి? ఏమి చేయకూడదు? (DO vs DON'T Matrix)" if lang == "te" else "⚖️ DO vs DON'T — Clear Safety Matrix"
    matrix_sub = (
        "ఆకుపచ్చ రంగు (DO) లో ఉన్నవి సురక్షిత అలవాట్లు. ఎరుపు రంగు (DON'T) లో ఉన్నవి ఎట్టి పరిస్థితుల్లోనూ చేయకూడని ప్రమాదకరమైన పనులు."
        if lang == "te" else
        "Green represents Safe Habits (DO). Red represents Dangerous Actions (DON'T) that must be avoided at all costs."
    )
    render_html(f"""
    <div style="margin-bottom: 24px;">
        <h3 style="color: #063970; font-size: 1.65rem; font-weight: 900; margin-bottom: 6px;">
            {matrix_heading}
        </h3>
        <p style="font-size: 1.12rem; color: #475569; margin: 0;">
            {matrix_sub}
        </p>
    </div>
    """)

    col_do, col_dont = st.columns(2)

    do_header = "✅ చేయవలసినవి (DO - SAFE HABITS)" if lang == "te" else "✅ DO (Safe Habits)"
    dont_header = "❌ చేయకూడనివి (DON'T - DANGER ACTIONS)" if lang == "te" else "❌ DON'T (Danger Actions)"

    with col_do:
        dos_html_items = "".join([
            f'<div style="background: white; border-radius: 14px; padding: 14px 18px; margin-bottom: 12px; border: 1.5px solid #bbf7d0; font-size: 1.05rem; color: #14532d; font-weight: 700; line-height: 1.55; box-shadow: 0 2px 6px rgba(0,0,0,0.02);">{item["icon"]} {item.get(lang, item["te"])}</div>'
            for item in DOS_AND_DONTS["dos"]
        ])
        render_html(f"""
        <div class="do-box">
            <h3 style="color: #166534; margin-top: 0; display: flex; align-items: center; gap: 10px; font-size: 1.45rem; font-weight: 900;">
                <span style="font-size: 1.6rem;">✅</span> {do_header}
            </h3>
            {dos_html_items}
        </div>
        """)

    with col_dont:
        donts_html_items = "".join([
            f'<div style="background: white; border-radius: 14px; padding: 14px 18px; margin-bottom: 12px; border: 1.5px solid #fecaca; font-size: 1.05rem; color: #7f1d1d; font-weight: 700; line-height: 1.55; box-shadow: 0 2px 6px rgba(0,0,0,0.02);">{item["icon"]} {item.get(lang, item["te"])}</div>'
            for item in DOS_AND_DONTS["donts"]
        ])
        render_html(f"""
        <div class="dont-box">
            <h3 style="color: #991b1b; margin-top: 0; display: flex; align-items: center; gap: 10px; font-size: 1.45rem; font-weight: 900;">
                <span style="font-size: 1.6rem;">❌</span> {dont_header}
            </h3>
            {donts_html_items}
        </div>
        """)
