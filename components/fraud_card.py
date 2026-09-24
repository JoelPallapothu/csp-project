"""
CAVI - Cyber Aware Village Initiative
Fraud Cards Grid & Detailed Interactive Learning Drilldown View with
Visual Process Flowcharts, Dialogue Simulators, Web Speech Audio, and In-Page Knowledge Check.
Bilingual: Telugu (Default) and English.
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
                        <div style="font-size: 1.25rem; font-weight: 800; color: #063970; margin-bottom: 8px; line-height: 1.35;">
                            {f_title}
                        </div>
                        <div style="font-size: 0.98rem; color: #475569; line-height: 1.55; margin-bottom: 16px;">
                            {f_short}
                        </div>
                    </div>
                </div>
                """)
                
                btn_label = "పూర్తి వివరాలు చూడండి ➔" if lang == "te" else "Learn More ➔"
                if st.button(btn_label, key=f"btn_learn_{fraud['id']}", use_container_width=True):
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
        back_btn_label = "⬅️ అన్ని మోసాల జాబితా" if lang == "te" else "⬅️ Back to All Frauds"
        if st.button(back_btn_label, key="btn_back_to_frauds", use_container_width=True):
            navigate_to("frauds")
    with col_title:
        render_html(f"""
        <div style="display: flex; align-items: center; gap: 14px;">
            <span style="font-size: 2.3rem;">{fraud['icon']}</span>
            <div>
                <h2 style='color: #063970; margin: 0; font-size: 1.8rem; font-weight: 900;'>{f_title}</h2>
                <span class="badge-pill badge-danger" style="margin-top: 4px;">{fraud['badge']}</span>
            </div>
        </div>
        """)

    render_html("<hr style='margin: 16px 0 20px 0;'>")

    # Audio Read-Aloud Bar for Low-Literacy / Illiterate Users
    audio_bar_title = "వినండి – ఆడియో వివరణ (Audio Read-Aloud)" if lang == "te" else "Listen – Audio Narration (Read Aloud)"
    audio_bar_sub = "చదవడానికి ఇబ్బందిగా ఉంటే బటన్ నొక్కి వివరాలను వినవచ్చు" if lang == "te" else "Click the button below to listen to the explanation aloud"
    render_html(f"""
    <div style="background: #f0f9ff; border: 1.5px solid #bae6fd; border-radius: 16px; padding: 14px 20px; margin-bottom: 20px; display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 12px;">
        <div style="display: flex; align-items: center; gap: 10px;">
            <span style="font-size: 1.6rem;">🔊</span>
            <div>
                <div style="font-weight: 800; color: #063970; font-size: 1.05rem;">{audio_bar_title}</div>
                <div style="font-size: 0.9rem; color: #475569;">{audio_bar_sub}</div>
            </div>
        </div>
    </div>
    """)
    render_speech_audio_button(f_audio, lang=lang, key_id=f"audio_{fraud['id']}")

    # 1. WHAT HAPPENS SECTION
    what_title = "📌 ఈ మోసం ఎలా జరుగుతుంది? (What is it?)" if lang == "te" else "📌 What is this Fraud? (How does it work?)"
    render_html(f"""
    <div class="cavi-card" style="border-left: 6px solid {fraud['color']};">
        <h3 style="color: #063970; margin-top: 0; font-size: 1.45rem; font-weight: 900; display: flex; align-items: center; gap: 8px;">
            {what_title}
        </h3>
        <p style="font-size: 1.18rem; color: #1e293b; line-height: 1.7; margin-bottom: 0;">
            {f_what}
        </p>
    </div>
    """)

    # 2. VISUAL WORKFLOW WITH DIRECTIONAL ARROWS
    flow_title = "🔄 మోసం జరిగే 4 దశలు (Visual Step-by-Step Flowchart)" if lang == "te" else "🔄 4-Stage Fraud Workflow (Step-by-Step Flowchart)"
    render_html(f"""
    <h3 style="color: #063970; margin: 26px 0 14px 0; font-size: 1.45rem; font-weight: 900;">
        {flow_title}
    </h3>
    """)

    flow_cols = st.columns(len(fraud["workflow"]))
    for idx, step in enumerate(fraud["workflow"]):
        with flow_cols[idx]:
            step_text = step.get(lang, step["te"])
            is_last = (idx == len(fraud["workflow"]) - 1)
            border_color = "#d62828" if is_last else "#0b63ce"
            step_label = f"దశ {step['step']}" if lang == "te" else f"Stage {step['step']}"
            arrow_label = ("⚠️ ప్రమాదం!" if lang == "te" else "⚠️ Danger!") if is_last else ("➔ తదుపరి దశ" if lang == "te" else "➔ Next Stage")
            
            render_html(f"""
            <div class="workflow-step-box" style="border-top: 4px solid {border_color}; min-height: 165px; display: flex; flex-direction: column; justify-content: space-between;">
                <div>
                    <div style="font-size: 2.2rem; margin-bottom: 6px;">{step['icon']}</div>
                    <div style="font-weight: 900; color: #063970; font-size: 0.95rem;">
                        {step_label}
                    </div>
                    <div style="font-size: 1.02rem; font-weight: 700; color: #1e293b; margin-top: 6px; line-height: 1.4;">
                        {step_text}
                    </div>
                </div>
                <div style="font-size: 0.82rem; font-weight: 800; color: {'#d62828' if is_last else '#0b63ce'}; margin-top: 6px;">
                    {arrow_label}
                </div>
            </div>
            """)

    render_html("<div style='margin-bottom: 24px;'></div>")

    # 3. RED FLAGS & WHAT TO DO (DO VS DON'T)
    c_danger, c_safe = st.columns(2)
    rf_title = "❌ మోసాన్ని గుర్తించడం ఎలా? (Warning Signs)" if lang == "te" else "❌ Warning Signs (Red Flags)"
    action_title = "✅ మీరు ఏమి చేయాలి? (Stay Safe)" if lang == "te" else "✅ How to Stay Safe (Action Steps)"
    
    with c_danger:
        render_html(f"""
        <div class="dont-box">
            <h3 style="color: #991b1b; margin-top: 0; display: flex; align-items: center; gap: 10px; font-size: 1.35rem; font-weight: 900;">
                <span style="font-size: 1.6rem;">❌</span> {rf_title}
            </h3>
            <ul style="font-size: 1.08rem; color: #7f1d1d; line-height: 1.7; padding-left: 20px; margin-bottom: 0;">
                {''.join([f'<li style="margin-bottom: 10px; font-weight: 600;">{rf}</li>' for rf in red_flags])}
            </ul>
        </div>
        """)

    with c_safe:
        render_html(f"""
        <div class="do-box">
            <h3 style="color: #166534; margin-top: 0; display: flex; align-items: center; gap: 10px; font-size: 1.35rem; font-weight: 900;">
                <span style="font-size: 1.6rem;">✅</span> {action_title}
            </h3>
            <ul style="font-size: 1.08rem; color: #14532d; line-height: 1.7; padding-left: 20px; margin-bottom: 0;">
                {''.join([f'<li style="margin-bottom: 10px; font-weight: 600;">{act}</li>' for act in actions])}
            </ul>
        </div>
        """)

    render_html("<div style='margin-bottom: 28px;'></div>")

    # 4. REAL-LIFE CONVERSATION (Scammer vs Villager)
    dialogue_header = "🎭 నిజ జీవిత సంభాషణ – ఎలా తిరస్కరించాలి? (Real-Life Dialogue)" if lang == "te" else "🎭 Real-Life Simulated Dialogue – How to Reject the Scammer"
    scammer_heading = "మోసగాడి మాట (Scammer):" if lang == "te" else "Scammer's Call:"
    villager_heading = "అప్రమత్త గ్రామస్తుడి సమాధానం (Aware Citizen):" if lang == "te" else "Alert Citizen's Safe Response:"
    
    dialogue = fraud["dialogue"]
    scammer_line = dialogue.get(f"scammer_{lang}", dialogue.get("scammer_te", ""))
    villager_line = dialogue.get(f"villager_{lang}", dialogue.get("villager_te", ""))
    outcome_line = dialogue.get(f"outcome_{lang}", dialogue.get("outcome_te", ""))

    render_html(f"""
    <h3 style="color: #063970; margin-bottom: 14px; font-size: 1.45rem; font-weight: 900;">
        {dialogue_header}
    </h3>
    <div style="background: #ffffff; border-radius: 22px; padding: 26px; border: 1px solid #e2e8f0; box-shadow: 0 6px 20px rgba(15,43,92,0.06); margin-bottom: 24px;">
        <div style="margin-bottom: 16px;">
            <div style="display: flex; align-items: center; gap: 8px; font-weight: 800; color: #d62828; font-size: 1.05rem; margin-bottom: 6px;">
                <span>🎭</span> <span>{scammer_heading}</span>
            </div>
            <div class="chat-bubble-scammer">
                "{scammer_line}"
            </div>
        </div>
        <div style="margin-bottom: 16px;">
            <div style="display: flex; align-items: center; justify-content: flex-end; gap: 8px; font-weight: 800; color: #168447; font-size: 1.05rem; margin-bottom: 6px;">
                <span>🧑‍🌾</span> <span>{villager_heading}</span>
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
    check_header = "🧠 తక్షణ పరీక్ష (Quick Check): ఈ మోసంలో ప్రధాన నియమం ఏమిటి?" if lang == "te" else "🧠 Quick Check: What is the golden rule for this scenario?"
    render_html(f"""
    <div class="cavi-card" style="background: #f8fafc; border: 2px dashed #94a3b8; margin-bottom: 24px;">
        <h4 style="color: #063970; margin-top: 0; font-size: 1.25rem; font-weight: 800;">
            {check_header}
        </h4>
    </div>
    """)

    chk_col1, chk_col2 = st.columns(2)
    wrong_btn = "❌ ఎవరైనా అడగ్గానే వెంటనే నంబర్లు చెప్పేయాలి" if lang == "te" else "❌ Share secret numbers immediately on call"
    right_btn = "✅ ఎట్టి పరిస్థితుల్లోనూ ఓటీపీ/పిన్ చెప్పకూడదు" if lang == "te" else "✅ NEVER share OTP or PIN under any condition"
    wrong_msg = "⚠️ తప్పు! ఎవరికీ రహస్య నంబర్లు చెప్పకూడదు." if lang == "te" else "⚠️ Incorrect! Secret numbers must never be shared."
    right_msg = "🎉 కరెక్ట్! మీరు సరైన భద్రతా సూత్రాన్ని నేర్చుకున్నారు!" if lang == "te" else "🎉 Correct! You followed the golden security rule!"

    with chk_col1:
        if st.button(wrong_btn, key=f"chk_wrong_{fraud['id']}", use_container_width=True):
            st.error(wrong_msg)
    with chk_col2:
        if st.button(right_btn, key=f"chk_right_{fraud['id']}", type="primary", use_container_width=True):
            st.success(right_msg)

    # 6. ACTION BUTTONS ROW
    render_html("<hr style='margin: 24px 0;'>")
    act_col1, act_col2, act_col3 = st.columns(3)
    btn_vid_txt = "🎥 అవగాహన వీడియోలు చూడండి" if lang == "te" else "🎥 Watch Awareness Videos"
    btn_quiz_txt = "🧠 సైబర్ క్విజ్ రాయండి" if lang == "te" else "🧠 Take the Cyber Quiz"
    btn_rep_txt = "🚨 మోసాన్ని నివేదించండి (1930)" if lang == "te" else "🚨 Report Fraud (1930 Helpline)"

    with act_col1:
        if st.button(btn_vid_txt, key=f"btn_vid_{fraud['id']}", use_container_width=True):
            navigate_to("videos")
    with act_col2:
        if st.button(btn_quiz_txt, key=f"btn_quiz_{fraud['id']}", use_container_width=True):
            navigate_to("quiz")
    with act_col3:
        if st.button(btn_rep_txt, key=f"btn_rep_{fraud['id']}", type="primary", use_container_width=True):
            navigate_to("report")
