"""
CAVI - Cyber Aware Village Initiative
Interactive Cyber Safety Quiz with Large Touch-Friendly Cards, Instant Feedback & Digital Guardian Certificate
"""

import streamlit as st
from data.quiz_data import get_all_questions
from utils.helpers import get_current_lang
from utils.styling import render_html

def render_quiz():
    lang = get_current_lang()
    questions = get_all_questions()
    total_q = len(questions)

    render_html("""
    <div style="margin-bottom: 22px;">
        <h2 style="color: #091b36; margin-bottom: 6px;">🧠 గ్రామ సైబర్ భద్రతా క్విజ్ (Village Cyber Safety Quiz)</h2>
        <p style="font-size: 1.15rem; color: #475569;">
            మీరు సైబర్ మోసాల బారిన పడకుండా ఎంతవరకు అప్రమత్తంగా ఉన్నారో పరీక్షించుకోండి. ప్రతి ప్రశ్నకు సరైన సమాధానం ఎంచుకోండి.
        </p>
    </div>
    """)

    # Initialize quiz state
    if "quiz_answers" not in st.session_state:
        st.session_state.quiz_answers = {}
    if "quiz_submitted" not in st.session_state:
        st.session_state.quiz_submitted = False

    answered_count = len(st.session_state.quiz_answers)
    
    st.progress(answered_count / total_q)
    render_html(f"""
    <div style="display: flex; justify-content: space-between; align-items: center; font-size: 0.95rem; font-weight: 800; color: #0284c7; margin: 8px 0 24px 0;">
        <span>పూర్తి చేసిన ప్రశ్నలు (Completed): {answered_count} / {total_q}</span>
        <span>మొత్తం ప్రశ్నలు: {total_q}</span>
    </div>
    """)

    # Render each question
    for idx, q in enumerate(questions):
        q_id = q["id"]
        q_text = q["question"].get(lang, q["question"]["te"])
        options = q["options"].get(lang, q["options"]["te"])
        correct_idx = q["correct_index"]
        exp_text = q["explanation"].get(lang, q["explanation"]["te"])

        user_answer = st.session_state.quiz_answers.get(q_id, None)

        badge_status = '<span class="badge-pill badge-safe">సమాధానం ఇచ్చారు ✓</span>' if user_answer is not None else ''
        render_html(f"""
        <div class="cavi-card" style="border-left: 6px solid #091b36; margin-bottom: 20px;">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px;">
                <span class="badge-pill badge-info" style="font-size: 0.85rem;">
                    ప్రశ్న {idx + 1} / {total_q} • {q['category']}
                </span>
                {badge_status}
            </div>
            <div style="font-size: 1.3rem; font-weight: 800; color: #091b36; line-height: 1.45; margin-bottom: 16px;">
                {q_text}
            </div>
        </div>
        """)

        # Large Touch-friendly Options
        cols = st.columns(len(options))
        for opt_idx, opt_text in enumerate(options):
            with cols[opt_idx]:
                is_selected = (user_answer == opt_idx)
                btn_type = "primary" if is_selected else "secondary"
                label_text = f"{chr(65 + opt_idx)}) {opt_text}"
                
                if st.button(label_text, key=f"q_{q_id}_opt_{opt_idx}", type=btn_type, use_container_width=True):
                    st.session_state.quiz_answers[q_id] = opt_idx
                    st.rerun()

        # Immediate feedback banner
        if user_answer is not None:
            if user_answer == correct_idx:
                render_html(f"""
                <div style="background: #f0fdf4; border: 2px solid #86efac; border-radius: 14px; padding: 14px 20px; margin: 14px 0 28px 0; color: #166534; font-weight: 800; font-size: 1.1rem; box-shadow: 0 4px 12px rgba(22,163,74,0.08);">
                    {exp_text}
                </div>
                """)
            else:
                render_html(f"""
                <div style="background: #fef2f2; border: 2px solid #fecaca; border-radius: 14px; padding: 14px 20px; margin: 14px 0 28px 0; color: #991b1b; font-weight: 800; font-size: 1.1rem; box-shadow: 0 4px 12px rgba(220,38,38,0.08);">
                    ⚠️ జాగ్రత్త! సరైన సమాధానం: <b>{chr(65 + correct_idx)}) {options[correct_idx]}</b><br>
                    <span style="font-size: 1.0rem; font-weight: 600; margin-top: 6px; display: inline-block;">{exp_text}</span>
                </div>
                """)
        else:
            render_html("<div style='margin-bottom: 26px;'></div>")

    # Final Score & Digital Certificate
    if answered_count == total_q:
        correct_count = sum(1 for q in questions if st.session_state.quiz_answers.get(q["id"]) == q["correct_index"])
        st.session_state.progress["quiz_completed"] = True
        st.session_state.progress["quiz_score"] = correct_count
        st.session_state.progress["quiz_total"] = total_q

        is_expert = (correct_count >= 8)
        guardian_msg = (
            "అభినందనలు! మీరు సైబర్ మోసాల నివారణపై సంపూర్ణ అవగాహన సాధించారు. మీరు నిజమైన 'గ్రామ సైబర్ రక్షకుడు' (Village Cyber Guardian)!" 
            if is_expert else 
            "మంచి ప్రయత్నం! 10 ముఖ్యమైన సైబర్ నియమాలను మరోసారి తెలుసుకోండి. ఎవరికీ మీ ఓటీపీ లేదా పిన్ నంబర్లను ఎప్పుడూ చెప్పవద్దు."
        )

        render_html(f"""
        <div style="background: linear-gradient(135deg, #06152b 0%, #0f2b5c 50%, #1d4ed8 100%); border-radius: 28px; padding: 40px 32px; color: white; text-align: center; margin-top: 36px; box-shadow: 0 16px 40px rgba(15,43,92,0.35); border: 2px solid rgba(255,255,255,0.15);">
            <div style="font-size: 4rem; margin-bottom: 10px;">🏆</div>
            <span class="badge-pill" style="background: rgba(56, 189, 248, 0.2); color: #7dd3fc; border: 1px solid #38bdf8; font-size: 1.0rem; padding: 6px 18px; margin-bottom: 14px;">
                CAVI సైబర్ రక్షక్ సర్టిఫికేట్ (Digital Cyber Guardian Award)
            </span>
            <h1 style="color: #fef08a; margin: 12px 0 8px 0; font-size: 2.3rem; font-weight: 900;">
                మీ సైబర్ భద్రత స్కోర్ (CYBER SAFETY SCORE)
            </h1>
            <div style="font-size: 4.5rem; font-weight: 950; color: #38bdf8; margin: 10px 0; letter-spacing: -1px;">
                {correct_count} / {total_q}
            </div>
            <p style="font-size: 1.3rem; color: #e0f2fe; line-height: 1.6; max-width: 720px; margin: 0 auto 24px auto; font-weight: 600;">
                {guardian_msg}
            </p>
            <div style="background: rgba(255,255,255,0.08); border-radius: 16px; padding: 16px 28px; display: inline-block; font-weight: 700; color: #cbd5e1; border: 1px solid rgba(255,255,255,0.15);">
                🎓 Community Service Project • Cyber Aware Village Initiative (CAVI) Certified
            </div>
        </div>
        """)

        render_html("<div style='margin-bottom: 24px;'></div>")
        if st.button("🔄 క్విజ్ మళ్ళీ రాయండి (Retake Quiz)", key="btn_retake_quiz", type="primary"):
            st.session_state.quiz_answers = {}
            st.session_state.progress["quiz_completed"] = False
            st.rerun()
