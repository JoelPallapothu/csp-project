"""
CAVI - Cyber Aware Village Initiative
Fraud Cards Grid & Detailed Interactive Learning Drilldown View with
Enhanced Visual Process Flowcharts, Dialogue Simulators, and In-Page Knowledge Check
"""

import streamlit as st
from data.frauds import get_all_frauds, get_fraud_by_id
from data.translations import get_text
from utils.helpers import get_current_lang, navigate_to, record_fraud_view, render_speech_audio_button
from utils.styling import render_html

def render_frauds_grid(limit: int = None):
    """Renders visual cards for fraud types in an elevated responsive grid."""
    lang = get_current_lang()
    frauds = get_all_frauds()
    if limit:
        frauds = frauds[:limit]

    cols_per_row = 3
    for i in range(0, len(frauds), cols_per_row):
        row_frauds = frauds[i:i + cols_per_row]
        cols = st.columns(len(row_frauds))
        for j, fraud in enumerate(row_frauds):
            with cols[j]:
                f_title = fraud["title"].get(lang, fraud["title"]["te"])
                f_short = fraud["short_desc"].get(lang, fraud["short_desc"]["te"])
                
                render_html(f"""
                <div class="fraud-grid-card" style="border-top: 5px solid {fraud['color']};">
                    <div>
                        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 14px;">
                            <div style="font-size: 2.5rem; line-height: 1;">{fraud['icon']}</div>
                            <span class="badge-pill badge-danger" style="font-size: 0.8rem;">{fraud['badge']}</span>
                        </div>
                        <div style="font-size: 1.28rem; font-weight: 800; color: #091b36; margin-bottom: 8px; line-height: 1.3;">
                            {f_title}
                        </div>
                        <div style="font-size: 0.98rem; color: #475569; line-height: 1.5; margin-bottom: 16px;">
                            {f_short}
                        </div>
                    </div>
                </div>
                """)
                
                if st.button(f"{get_text('btn_learn_more', lang)}", key=f"btn_learn_{fraud['id']}", use_container_width=True):
                    record_fraud_view(fraud["id"])
                    navigate_to("frauds", fraud["id"])
        render_html("<div style='margin-bottom: 16px;'></div>")

def render_fraud_detail(fraud_id: str):
    """Renders the comprehensive interactive learning view for a specific fraud."""
    lang = get_current_lang()
    fraud = get_fraud_by_id(fraud_id)
    if not fraud:
        st.error("Fraud details not found.")
        if st.button("⬅️ Back to Frauds"):
            navigate_to("frauds")
        return

    record_fraud_view(fraud["id"])

    f_title = fraud["title"].get(lang, fraud["title"]["te"])
    f_what = fraud["what_happens"].get(lang, fraud["what_happens"]["te"])
    f_audio = fraud["audio_text"].get(lang, fraud["audio_text"]["te"])
    red_flags = fraud["red_flags"].get(lang, fraud["red_flags"]["te"])
    actions = fraud["what_to_do"].get(lang, fraud["what_to_do"]["te"])

    # Back Navigation Bar
    col_back, col_title = st.columns([3, 9])
    with col_back:
        if st.button("⬅️ అన్ని మోసాల జాబితా (Back)", key="btn_back_to_frauds", use_container_width=True):
            navigate_to("frauds")
    with col_title:
        render_html(f"""
        <div style="display: flex; align-items: center; gap: 12px;">
            <span style="font-size: 2.2rem;">{fraud['icon']}</span>
            <div>
                <h2 style='color: #091b36; margin: 0; font-size: 1.75rem;'>{f_title}</h2>
                <span class="badge-pill badge-danger" style="margin-top: 4px;">{fraud['badge']}</span>
            </div>
        </div>
        """)

    render_html("<hr style='margin: 16px 0 22px 0;'>")

    # Audio Read-Aloud Bar for Low-Literacy / Illiterate Users
    render_html(f"""
    <div style="background: #f0f9ff; border: 1px solid #bae6fd; border-radius: 14px; padding: 14px 18px; margin-bottom: 22px; display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 12px;">
        <div style="display: flex; align-items: center; gap: 10px;">
            <span style="font-size: 1.5rem;">🔊</span>
            <div>
                <div style="font-weight: 800; color: #0369a1; font-size: 1.05rem;">వినండి – ఆడియో వివరణ (Audio Read-Aloud)</div>
                <div style="font-size: 0.88rem; color: #475569;">చదవడానికి ఇబ్బందిగా ఉంటే బటన్ నొక్కి వివరాలను వినవచ్చు</div>
            </div>
        </div>
    </div>
    """)
    render_speech_audio_button(f_audio, lang=lang, key_id=f"audio_{fraud['id']}")

    # 1. WHAT HAPPENS SECTION
    render_html(f"""
    <div class="cavi-card" style="border-left: 6px solid {fraud['color']};">
        <h3 style="color: #091b36; margin-top: 0; font-size: 1.45rem; display: flex; align-items: center; gap: 8px;">
            <span>📌</span> ఈ మోసం ఎలా జరుగుతుంది? (What Happens?)
        </h3>
        <p style="font-size: 1.18rem; color: #1e293b; line-height: 1.65; margin-bottom: 0;">
            {f_what}
        </p>
    </div>
    """)

    # 2. VISUAL WORKFLOW WITH DIRECTIONAL ARROWS
    render_html("""
    <h3 style="color: #091b36; margin: 26px 0 14px 0; font-size: 1.45rem;">
        🔄 మోసం జరిగే 4 దశలు (Visual Step-by-Step Flowchart)
    </h3>
    """)

    flow_cols = st.columns(len(fraud["workflow"]))
    for idx, step in enumerate(fraud["workflow"]):
        with flow_cols[idx]:
            step_text = step.get(lang, step["te"])
            is_last = (idx == len(fraud["workflow"]) - 1)
            border_color = "#dc2626" if is_last else "#0284c7"
            
            render_html(f"""
            <div class="workflow-step-box" style="border-top: 4px solid {border_color}; min-height: 165px; display: flex; flex-direction: column; justify-content: space-between;">
                <div>
                    <div style="font-size: 2.2rem; margin-bottom: 6px;">{step['icon']}</div>
                    <div style="font-weight: 900; color: #091b36; font-size: 0.95rem;">
                        దశ {step['step']}
                    </div>
                    <div style="font-size: 1.02rem; font-weight: 700; color: #1e293b; margin-top: 6px; line-height: 1.4;">
                        {step_text}
                    </div>
                </div>
                <div style="font-size: 0.8rem; font-weight: 800; color: {'#dc2626' if is_last else '#0284c7'}; margin-top: 6px;">
                    {'⚠️ ప్రమాదం!' if is_last else '➔ తదుపరి దశ'}
                </div>
            </div>
            """)

    render_html("<div style='margin-bottom: 24px;'></div>")

    # 3. RED FLAGS & WHAT TO DO (DO VS DON'T)
    c_danger, c_safe = st.columns(2)
    with c_danger:
        render_html(f"""
        <div class="dont-box">
            <h3 style="color: #991b1b; margin-top: 0; display: flex; align-items: center; gap: 10px; font-size: 1.35rem;">
                <span style="font-size: 1.6rem;">❌</span> మోసాన్ని గుర్తించడం ఎలా? (Red Flags)
            </h3>
            <ul style="font-size: 1.1rem; color: #7f1d1d; line-height: 1.65; padding-left: 20px; margin-bottom: 0;">
                {''.join([f'<li style="margin-bottom: 10px; font-weight: 600;">{rf}</li>' for rf in red_flags])}
            </ul>
        </div>
        """)

    with c_safe:
        render_html(f"""
        <div class="do-box">
            <h3 style="color: #166534; margin-top: 0; display: flex; align-items: center; gap: 10px; font-size: 1.35rem;">
                <span style="font-size: 1.6rem;">✅</span> మీరు ఏమి చేయాలి? (What to Do)
            </h3>
            <ul style="font-size: 1.1rem; color: #14532d; line-height: 1.65; padding-left: 20px; margin-bottom: 0;">
                {''.join([f'<li style="margin-bottom: 10px; font-weight: 600;">{act}</li>' for act in actions])}
            </ul>
        </div>
        """)

    render_html("<div style='margin-bottom: 28px;'></div>")

    # 4. REAL-LIFE CONVERSATION (Scammer vs Villager)
    render_html("""
    <h3 style="color: #091b36; margin-bottom: 14px; font-size: 1.45rem;">
        🎭 నిజ జీవిత సంభాషణ – ఎలా తిరస్కరించాలి? (Real-Life Dialogue)
    </h3>
    """)
    
    dialogue = fraud["dialogue"]
    scammer_line = dialogue.get(f"scammer_{lang}", dialogue.get("scammer_te", ""))
    villager_line = dialogue.get(f"villager_{lang}", dialogue.get("villager_te", ""))
    outcome_line = dialogue.get(f"outcome_{lang}", dialogue.get("outcome_te", ""))

    render_html(f"""
    <div style="background: #ffffff; border-radius: 22px; padding: 26px; border: 1px solid #e2e8f0; box-shadow: 0 6px 20px rgba(15,43,92,0.06); margin-bottom: 24px;">
        <div style="margin-bottom: 16px;">
            <div style="display: flex; align-items: center; gap: 8px; font-weight: 800; color: #dc2626; font-size: 1.05rem; margin-bottom: 6px;">
                <span>🎭</span> <span>మోసగాడి మాట (Scammer):</span>
            </div>
            <div class="chat-bubble-scammer">
                "{scammer_line}"
            </div>
        </div>
        <div style="margin-bottom: 16px;">
            <div style="display: flex; align-items: center; justify-content: flex-end; gap: 8px; font-weight: 800; color: #15803d; font-size: 1.05rem; margin-bottom: 6px;">
                <span>🧑‍🌾</span> <span>అప్రమత్త గ్రామస్తుడి సమాధానం (Aware Villager):</span>
            </div>
            <div class="chat-bubble-villager">
                "{villager_line}"
            </div>
        </div>
        <div style="background: #f0fdf4; border: 2px solid #86efac; border-radius: 14px; padding: 14px 20px; font-weight: 800; color: #166534; font-size: 1.12rem; text-align: center;">
            {outcome_line}
        </div>
    </div>
    """)

    # 5. IN-PAGE MINI CHECK (Active Recall)
    render_html("""
    <div class="cavi-card" style="background: #f8fafc; border: 2px dashed #94a3b8; margin-bottom: 24px;">
        <h4 style="color: #091b36; margin-top: 0; font-size: 1.25rem;">
            🧠 తక్షణ పరీక్ష (Quick Check): ఈ మోసంలో ప్రధాన నియమం ఏమిటి?
        </h4>
    </div>
    """)

    chk_col1, chk_col2 = st.columns(2)
    with chk_col1:
        if st.button("❌ ఎవరైనా అడగ్గానే వెంటనే నంబర్లు చెప్పేయాలి", key=f"chk_wrong_{fraud['id']}", use_container_width=True):
            st.error("⚠️ తప్పు! ఎవరికీ రహస్య నంబర్లు చెప్పకూడదు.")
    with chk_col2:
        if st.button("✅ ఎట్టి పరిస్థితుల్లోనూ ఓటీపీ/పిన్ చెప్పకూడదు", key=f"chk_right_{fraud['id']}", type="primary", use_container_width=True):
            st.success("🎉 కరెక్ట్! మీరు సరైన భద్రతా సూత్రాన్ని నేర్చుకున్నారు!")

    # 6. ACTION BUTTONS ROW
    st.markdown("---")
    act_col1, act_col2, act_col3 = st.columns(3)
    with act_col1:
        if st.button("🎥 అవగాహన వీడియోలు చూడండి", key=f"btn_vid_{fraud['id']}", use_container_width=True):
            navigate_to("videos")
    with act_col2:
        if st.button("🧠 పూర్తి సైబర్ క్విజ్ రాయండి", key=f"btn_quiz_{fraud['id']}", use_container_width=True):
            navigate_to("quiz")
    with act_col3:
        if st.button("🚨 మోసం జరిగితే రిపోర్ట్ చేయండి (1930)", key=f"btn_rep_{fraud['id']}", type="primary", use_container_width=True):
            navigate_to("report")
