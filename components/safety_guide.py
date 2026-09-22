"""
CAVI - Cyber Aware Village Initiative
Safety Guide Component: 10 Golden Rules with Voice Audio & High-Contrast DO vs DON'T Matrix
"""

import streamlit as st
from data.rules import GOLDEN_RULES, DOS_AND_DONTS
from data.translations import get_text
from utils.helpers import get_current_lang, render_speech_audio_button
from utils.styling import render_html

def render_safety_guide():
    lang = get_current_lang()
    st.session_state.progress["rules_read"] = True

    render_html("""
    <div style="margin-bottom: 26px;">
        <h2 style="color: #091b36; margin-bottom: 6px;">🛡️ సైబర్ రక్షణ 10 సువర్ణ సూత్రాలు (10 Golden Rules)</h2>
        <p style="font-size: 1.15rem; color: #475569;">
            "ఈ పది నియమాలను పాటిస్తే మీ స్మార్ట్‌ఫోన్ మరియు బ్యాంక్ ఖాతా ఎల్లప్పుడూ సురక్షితంగా ఉంటాయి."
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
                
                render_html(f"""
                <div class="cavi-card" style="border-left: 6px solid #16a34a; min-height: 220px; display: flex; flex-direction: column; justify-content: space-between;">
                    <div>
                        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px;">
                            <span style="font-size: 2.2rem; line-height: 1;">{rule['icon']}</span>
                            <span class="badge-pill badge-safe" style="font-size: 0.8rem;">
                                నియమం {rule['number']} / Rule {rule['number']}
                            </span>
                        </div>
                        <div style="font-size: 1.25rem; font-weight: 800; color: #091b36; margin-bottom: 8px; line-height: 1.3;">
                            {r_title}
                        </div>
                        <div style="font-size: 1.02rem; color: #334155; line-height: 1.55; margin-bottom: 12px;">
                            {r_desc}
                        </div>
                    </div>
                </div>
                """)
                
                # Audio playback for illiterate users
                render_speech_audio_button(r_desc, lang=lang, key_id=f"rule_audio_{rule['number']}")
        render_html("<div style='margin-bottom: 14px;'></div>")

    render_html("<div style='margin-bottom: 30px;'></div>")

    # DO VS DON'T COMPARISON MATRIX
    render_html("""
    <div style="margin-bottom: 22px;">
        <h3 style="color: #091b36; font-size: 1.55rem; margin-bottom: 6px;">
            ⚖️ ఏమి చేయాలి? ఏమి చేయకూడదు? (DO vs DON'T Matrix)
        </h3>
        <p style="font-size: 1.08rem; color: #475569;">
            ఆకుపచ్చ రంగు (DO) లో ఉన్నవి సురక్షిత అలవాట్లు. ఎరుపు రంగు (DON'T) లో ఉన్నవి ఎట్టి పరిస్థితుల్లోనూ చేయకూడని ప్రమాదకరమైన పనులు.
        </p>
    </div>
    """)

    col_do, col_dont = st.columns(2)

    with col_do:
        dos_html_items = "".join([
            f'<div style="background: white; border-radius: 14px; padding: 14px 18px; margin-bottom: 12px; border: 1.5px solid #bbf7d0; font-size: 1.05rem; color: #14532d; font-weight: 700; line-height: 1.5; box-shadow: 0 2px 6px rgba(0,0,0,0.02);">{item["icon"]} {item.get(lang, item["te"])}</div>'
            for item in DOS_AND_DONTS["dos"]
        ])
        render_html(f"""
        <div class="do-box">
            <h3 style="color: #15803d; margin-top: 0; display: flex; align-items: center; gap: 10px; font-size: 1.4rem;">
                <span style="font-size: 1.6rem;">✅</span> చేయవలసినవి (DO - SAFE ACTIONS)
            </h3>
            {dos_html_items}
        </div>
        """)

    with col_dont:
        donts_html_items = "".join([
            f'<div style="background: white; border-radius: 14px; padding: 14px 18px; margin-bottom: 12px; border: 1.5px solid #fecaca; font-size: 1.05rem; color: #7f1d1d; font-weight: 700; line-height: 1.5; box-shadow: 0 2px 6px rgba(0,0,0,0.02);">{item["icon"]} {item.get(lang, item["te"])}</div>'
            for item in DOS_AND_DONTS["donts"]
        ])
        render_html(f"""
        <div class="dont-box">
            <h3 style="color: #b91c1c; margin-top: 0; display: flex; align-items: center; gap: 10px; font-size: 1.4rem;">
                <span style="font-size: 1.6rem;">❌</span> చేయకూడనివి (DON'T - DANGER ACTIONS)
            </h3>
            {donts_html_items}
        </div>
        """)
