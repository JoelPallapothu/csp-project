"""
CAVI - Cyber Aware Village Initiative
Interactive Practical Simulators:
1. "Spot the Scam" (Realistic Smartphone Mockup & Chat Interface)
2. Interactive UPI PIN Safety Simulator (PhonePe/GPay Mock with Interactive Touch Keypad)
Bilingual: Telugu (Default) and English.
"""

import streamlit as st
from data.simulations_data import SPOT_THE_SCAM_SCENARIOS, UPI_SIMULATOR_STEPS
from data.translations import get_text
from utils.helpers import get_current_lang, record_scam_scenario
from utils.styling import render_html

def render_simulations_page():
    lang = get_current_lang()

    # Safety Disclaimer Header
    disclaimer_title = "🛡️ విద్యాసంబంధిత డెమో (EDUCATIONAL SIMULATION ONLY):" if lang == "te" else "🛡️ EDUCATIONAL SIMULATION ONLY (No Financial Data Collected):"
    render_html(f"""
    <div style="background: #fffbeb; border-left: 6px solid #f4b400; padding: 18px 24px; border-radius: 16px; margin-bottom: 26px; box-shadow: 0 4px 14px rgba(244, 180, 0, 0.12);">
        <div style="font-weight: 900; color: #b45309; font-size: 1.1rem;">
            {disclaimer_title}
        </div>
        <div style="color: #78350f; font-size: 1.02rem; margin-top: 4px; line-height: 1.5;">
            {get_text('safety_disclaimer', lang)}
        </div>
    </div>
    """)

    tab1_label = "🎭 'Spot the Scam' (మోసాన్ని గుర్తించండి)" if lang == "te" else "🎭 'Spot the Scam' (Interactive Lab)"
    tab2_label = "💳 UPI PIN Safety Simulator (యూపీఐ సిమ్యులేటర్)" if lang == "te" else "💳 UPI PIN Safety Simulator (Interactive Keypad)"
    
    sim_tab1, sim_tab2 = st.tabs([tab1_label, tab2_label])

    with sim_tab1:
        render_spot_the_scam(lang)

    with sim_tab2:
        render_upi_simulator(lang)

def render_spot_the_scam(lang: str):
    header_title = "🎭 నిజమైనదా లేక మోసమా? (Spot the Scam)" if lang == "te" else "🎭 Safe or Scam? Spot the Trap"
    header_sub = (
        "మీ మొబైల్‌కు వచ్చే సందేశాలు లేదా ఫోన్ కాల్స్‌ను జాగ్రత్తగా గమనించండి. అది <b>సురక్షితమైనదా (SAFE)</b> లేక <b>మోసమా (SCAM)</b> చెప్పండి."
        if lang == "te" else
        "Examine the simulated smartphone alert below. Is it <b>SAFE</b> or a <b>SCAM</b>?"
    )
    render_html(f"""
    <div style="margin-bottom: 20px;">
        <h2 style="color: #063970; margin-bottom: 6px; font-size: 1.7rem; font-weight: 900;">{header_title}</h2>
        <p style="font-size: 1.15rem; color: #475569; margin: 0;">
            {header_sub}
        </p>
    </div>
    """)

    if "current_scenario_idx" not in st.session_state:
        st.session_state.current_scenario_idx = 0
    if "scenario_answered" not in st.session_state:
        st.session_state.scenario_answered = False
    if "user_scenario_choice" not in st.session_state:
        st.session_state.user_scenario_choice = None

    idx = st.session_state.current_scenario_idx
    total_scenarios = len(SPOT_THE_SCAM_SCENARIOS)
    if idx >= total_scenarios:
        idx = 0
        st.session_state.current_scenario_idx = 0
    scenario = SPOT_THE_SCAM_SCENARIOS[idx]

    step_text = f"సందర్భం {idx + 1} / {total_scenarios} (Scenario {idx + 1} of {total_scenarios})" if lang == "te" else f"Scenario {idx + 1} of {total_scenarios}"
    render_html(f"<div style='font-size: 1.05rem; font-weight: 800; color: #0b63ce; margin-bottom: 12px;'>📌 {step_text}</div>")

    # Realistic Smartphone Screen Mockup
    msg = scenario["message_mock"]
    render_html(f"""
    <div style="max-width: 540px; margin: 0 auto 28px auto; background: #06152b; border-radius: 40px; padding: 14px; box-shadow: 0 20px 48px rgba(0,0,0,0.35); border: 4px solid #334155;">
        <!-- Top Status Bar -->
        <div style="display: flex; justify-content: space-between; align-items: center; padding: 6px 20px 10px 20px; color: #cbd5e1; font-size: 0.82rem; font-weight: 700;">
            <span>10:45 AM</span>
            <!-- Camera notch -->
            <div style="width: 70px; height: 6px; background: #475569; border-radius: 9999px;"></div>
            <span>📶 4G • 🔋 88%</span>
        </div>
        
        <!-- Screen Canvas -->
        <div style="background: #efeae2; border-radius: 28px; overflow: hidden; min-height: 360px; display: flex; flex-direction: column; justify-content: space-between;">
            <!-- WhatsApp / App Top Header -->
            <div style="background: #075e54; color: white; padding: 12px 18px; display: flex; align-items: center; gap: 12px;">
                <div style="background: #128c7e; width: 44px; height: 44px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 1.4rem;">
                    👤
                </div>
                <div style="flex: 1;">
                    <div style="font-weight: 800; font-size: 1.08rem; line-height: 1.2;">
                        {scenario['sender_label']}
                    </div>
                    <div style="font-size: 0.8rem; opacity: 0.88;">
                        {scenario['sender']}
                    </div>
                </div>
                <span class="badge-pill" style="background: rgba(255,255,255,0.22); color: white; font-size: 0.78rem;">
                    {scenario['type']}
                </span>
            </div>

            <!-- Message Bubble -->
            <div style="padding: 22px 18px; flex: 1;">
                <div style="background: #ffffff; border-radius: 16px 16px 16px 4px; padding: 18px; box-shadow: 0 2px 8px rgba(0,0,0,0.08); max-width: 95%;">
                    <div style="font-weight: 900; color: #d62828; font-size: 1.15rem; margin-bottom: 8px;">
                        {msg['title']}
                    </div>
                    <div style="font-size: 1.05rem; color: #1e293b; line-height: 1.55; margin-bottom: 12px;">
                        {msg['body']}
                    </div>
                    <div style="display: flex; justify-content: space-between; align-items: center; font-size: 0.8rem; color: #64748b; font-style: italic;">
                        <span>{msg['footer']}</span>
                        <span style="color: #0b63ce; font-weight: 800;">{scenario['time']} ✓✓</span>
                    </div>
                </div>
            </div>

            <!-- Bottom App Footer Mock -->
            <div style="background: #f0f2f5; padding: 10px 18px; display: flex; align-items: center; justify-content: space-between; border-top: 1px solid #d1d7db; color: #64748b; font-size: 0.88rem;">
                <span>💬 Message</span>
                <span>📎 📷 🎤</span>
            </div>
        </div>
    </div>
    """)

    # Interactive Buttons
    if not st.session_state.scenario_answered:
        q_label = "ఈ సందేశం సురక్షితమైనదా లేక మోసమా? (Safe or Scam?)" if lang == "te" else "Is this message SAFE or a SCAM?"
        render_html(f"<h3 style='text-align: center; color: #063970; margin-bottom: 18px; font-weight: 900;'>{q_label}</h3>")
        
        btn_safe_text = "🟢 సురక్షితం (SAFE)" if lang == "te" else "🟢 SAFE"
        btn_scam_text = "🔴 మోసం (SCAM)" if lang == "te" else "🔴 SCAM"
        
        col_safe, col_scam = st.columns(2)
        with col_safe:
            if st.button(btn_safe_text, key=f"btn_safe_{idx}", use_container_width=True):
                st.session_state.user_scenario_choice = "safe"
                st.session_state.scenario_answered = True
                record_scam_scenario(scenario["id"], scenario["correct_answer"] == "safe")
                st.rerun()

        with col_scam:
            if st.button(btn_scam_text, key=f"btn_scam_{idx}", type="primary", use_container_width=True):
                st.session_state.user_scenario_choice = "scam"
                st.session_state.scenario_answered = True
                record_scam_scenario(scenario["id"], scenario["correct_answer"] == "scam")
                st.rerun()
    else:
        user_choice = st.session_state.user_scenario_choice
        is_correct = (user_choice == scenario["correct_answer"])

        if is_correct:
            st.success("🎉 అద్భుతం! మీరు సరిగ్గా గుర్తించారు! (Correct Answer!)" if lang == "te" else "🎉 Excellent! You correctly spotted the scenario!")
        else:
            st.error("⚠️ జాగ్రత్త! ఇది మోసం (Incorrect choice - Be cautious!)" if lang == "te" else "⚠️ Caution! This was a trap — be alert!")

        # Explanation Card
        explanation_text = scenario["explanation"].get(lang, scenario["explanation"]["te"])
        exp_header = "పరిష్కారం & వివరణ (Explanation):" if lang == "te" else "Explanation & Reasoning:"
        render_html(f"""
        <div class="cavi-card" style="border-left: 6px solid {'#168447' if is_correct else '#d62828'};">
            <h4 style="margin-top: 0; color: #063970; font-size: 1.3rem; font-weight: 900;">{exp_header}</h4>
            <p style="font-size: 1.18rem; line-height: 1.65; color: #1e293b; margin-bottom: 0;">{explanation_text}</p>
        </div>
        """)

        # Red Flags list
        red_flags_list = scenario["red_flag_points"].get(lang, scenario["red_flag_points"]["te"])
        rf_header = "🚩 గుర్తించవలసిన ముఖ్య ఆధారాలు (Key Red Flags):" if lang == "te" else "🚩 Key Red Flags to Spot:"
        st.markdown(f"##### {rf_header}")
        rf_cols = st.columns(len(red_flags_list))
        for r_idx, rf_item in enumerate(red_flags_list):
            with rf_cols[r_idx]:
                render_html(f"""
                <div style="background: #ffffff; border: 1.5px solid #cbd5e1; border-radius: 14px; padding: 14px; text-align: center; font-weight: 700; color: #063970; box-shadow: 0 2px 6px rgba(0,0,0,0.04); font-size: 1.0rem;">
                    📌 {rf_item}
                </div>
                """)

        render_html("<div style='margin-bottom: 22px;'></div>")
        
        # Navigation
        if idx < total_scenarios - 1:
            next_label = "తదుపరి సందర్భం (Next Scenario) ➔" if lang == "te" else "Next Scenario ➔"
            if st.button(next_label, key="btn_next_scenario", type="primary"):
                st.session_state.current_scenario_idx += 1
                st.session_state.scenario_answered = False
                st.session_state.user_scenario_choice = None
                st.rerun()
        else:
            congrats_msg = "👏 అభినందనలు! మీరు అన్ని సందర్భాలను పూర్తి చేశారు!" if lang == "te" else "👏 Congratulations! You completed all simulation scenarios!"
            restart_label = "మళ్ళీ మొదటి నుండి ప్రయత్నించండి (Restart Scenarios) 🔄" if lang == "te" else "Restart All Scenarios 🔄"
            st.info(congrats_msg)
            if st.button(restart_label, key="btn_restart_scenarios"):
                st.session_state.current_scenario_idx = 0
                st.session_state.scenario_answered = False
                st.session_state.user_scenario_choice = None
                st.rerun()

def render_upi_simulator(lang: str):
    header_title = "💳 యూపీఐ భద్రతా సిమ్యులేటర్ (UPI PIN Safety Simulator)" if lang == "te" else "💳 UPI PIN Safety Simulator (Interactive Keypad)"
    header_sub = (
        'భారతదేశంలో ఎక్కువ మంది రైతులు, చిరువ్యాపారులు మోసపోయే సందర్భం: <b>"మీ ఖాతాకు ₹5,000 పంపాను, రిసీవ్ చేసుకోవడానికి యూపీఐ పిన్ కొట్టండి"</b>. క్రింది లైవ్ డెమో ద్వారా నిజమైన నియమాన్ని నేర్చుకోండి!'
        if lang == "te" else
        'The #1 scam targeting rural citizens: <b>"I am transferring ₹5,000 to you, enter your UPI PIN to receive it."</b> Test this interactive simulator to master the golden rule!'
    )
    render_html(f"""
    <div style="margin-bottom: 20px;">
        <h2 style="color: #063970; margin-bottom: 6px; font-size: 1.7rem; font-weight: 900;">{header_title}</h2>
        <p style="font-size: 1.15rem; color: #475569; margin: 0;">
            {header_sub}
        </p>
    </div>
    """)

    if "upi_step" not in st.session_state:
        st.session_state.upi_step = "request_received"

    # Screen 1: Payment Request Screen
    if st.session_state.upi_step == "request_received":
        req_badge = "చెల్లింపు అభ్యర్థన" if lang == "te" else "COLLECT REQUEST"
        requester_label = "డబ్బులు అడుగుతున్న వ్యక్తి (Requester):" if lang == "te" else "Payment Requester:"
        scammer_call_text = (
            '📞 మోసగాడి మాట: "అన్నా, ధాన్యం డబ్బులు ₹5,000 పంపాను. మీ ఫోన్‌లో PAY నొక్కి 4 అంకెల యూపీఐ పిన్ కొట్టండి!"'
            if lang == "te" else
            '📞 Scammer\'s Voice on Call: "Sir, I sent ₹5,000 for your grain. Please tap PAY and enter your 4-digit UPI PIN to receive it!"'
        )
        what_next = "మీరు ఇప్పుడు ఏమి చేస్తారు?" if lang == "te" else "What action will you take now?"
        decline_btn = "🛑 DECLINE (తిరస్కరించండి)" if lang == "te" else "🛑 DECLINE (Reject Request)"
        pay_btn = "👉 PAY / ENTER PIN (పిన్ కొట్టడానికి వెళ్లండి)" if lang == "te" else "👉 PAY (Enter UPI PIN)"

        render_html(f"""
        <div style="max-width: 500px; margin: 0 auto 26px auto; background: #ffffff; border-radius: 28px; padding: 26px; border: 2px solid #e2e8f0; box-shadow: 0 16px 36px rgba(6,57,112,0.12);">
            <div style="display: flex; align-items: center; justify-content: space-between; border-bottom: 2px solid #f1f5f9; padding-bottom: 14px; margin-bottom: 18px;">
                <span style="font-weight: 950; color: #5b21b6; font-size: 1.4rem; display: flex; align-items: center; gap: 8px;">
                    <span>📱</span> PhonePe / Google Pay
                </span>
                <span class="badge-pill badge-danger" style="font-size: 0.85rem;">{req_badge}</span>
            </div>
            
            <div style="text-align: center; padding: 12px 0;">
                <div style="font-size: 1.0rem; color: #64748b; font-weight: 600;">{requester_label}</div>
                <div style="font-size: 1.35rem; font-weight: 900; color: #063970; margin: 6px 0;">
                    {UPI_SIMULATOR_STEPS['buyer_name']}
                </div>
                <div style="font-size: 3.2rem; font-weight: 950; color: #d62828; margin: 14px 0; letter-spacing: -1px;">
                    ₹5,000.00
                </div>
                <div style="background: #fef2f2; border: 1.5px solid #fecaca; border-radius: 14px; padding: 14px 18px; font-size: 1.02rem; color: #991b1b; font-weight: 700; line-height: 1.5;">
                    {scammer_call_text}
                </div>
            </div>
        </div>
        """)

        render_html(f"<h3 style='text-align: center; color: #063970; margin-bottom: 18px; font-weight: 900;'>{what_next}</h3>")

        col1, col2 = st.columns(2)
        with col1:
            if st.button(decline_btn, key="btn_upi_decline", type="primary", use_container_width=True):
                st.session_state.upi_step = "safe_declined"
                st.session_state.progress["upi_sim_done"] = True
                st.rerun()
        with col2:
            if st.button(pay_btn, key="btn_upi_pay", use_container_width=True):
                st.session_state.upi_step = "keypad_screen"
                st.rerun()

    # Screen 2: Interactive Keypad Screen (Simulated Pin entry)
    elif st.session_state.upi_step == "keypad_screen":
        pin_prompt = "Enter 4-Digit UPI PIN to Pay ₹5,000"
        keypad_hint = "⚠️ కీప్యాడ్‌పై ఏదైనా నంబర్ నొక్కండి (Tap any key below)" if lang == "te" else "⚠️ Tap any number on the keypad below"
        render_html(f"""
        <div style="max-width: 440px; margin: 0 auto 20px auto; background: #06152b; border-radius: 28px; padding: 24px; color: white; text-align: center; box-shadow: 0 16px 36px rgba(0,0,0,0.35);">
            <div style="font-size: 1.15rem; color: #94a3b8; margin-bottom: 8px; font-weight: 700;">{pin_prompt}</div>
            <!-- Pin Dots -->
            <div style="display: flex; justify-content: center; gap: 16px; margin: 18px 0;">
                <div style="width: 18px; height: 18px; border-radius: 50%; border: 2px solid #38bdf8; background: #38bdf8;"></div>
                <div style="width: 18px; height: 18px; border-radius: 50%; border: 2px solid #64748b;"></div>
                <div style="width: 18px; height: 18px; border-radius: 50%; border: 2px solid #64748b;"></div>
                <div style="width: 18px; height: 18px; border-radius: 50%; border: 2px solid #64748b;"></div>
            </div>
            <div style="font-size: 0.9rem; color: #f87171; font-weight: 800;">
                {keypad_hint}
            </div>
        </div>
        """)

        # Interactive Keypad Grid
        k_rows = [
            ["1", "2", "3"],
            ["4", "5", "6"],
            ["7", "8", "9"],
            ["✕ Cancel", "0", "✓ Submit"]
        ]
        
        for r_idx, row in enumerate(k_rows):
            k_cols = st.columns(3)
            for c_idx, key_val in enumerate(row):
                with k_cols[c_idx]:
                    if st.button(key_val, key=f"k_{r_idx}_{c_idx}", use_container_width=True):
                        if "Cancel" in key_val:
                            st.session_state.upi_step = "safe_declined"
                        else:
                            st.session_state.upi_step = "entered_pin_danger"
                        st.session_state.progress["upi_sim_done"] = True
                        st.rerun()

    # Screen 3A: User entered pin (Dangerous Trap Triggered)
    elif st.session_state.upi_step == "entered_pin_danger":
        danger_title = "ఆగండి! మీరు మీ అకౌంట్ నుండి ₹5,000 పోగొట్టుకునేవారు!" if lang == "te" else "STOP! ₹5,000 Would Have Been Stolen From Your Account!"
        rule_header = "⚠️ అత్యంత ముఖ్యమైన సూత్రం (GOLDEN RULE):" if lang == "te" else "⚠️ THE GOLDEN UPI RULE:"
        rule_body = (
            "యూపీఐ పిన్ (UPI PIN) అనేది మీ బ్యాంక్ ఖాతా నుండి డబ్బులు <u>పంపించడానికి (SEND)</u> మాత్రమే ఉపయోగించాలి. మీ ఖాతాలోకి డబ్బులు <u>రావడానికి (RECEIVE)</u> పిన్ అస్సలు కొట్టకూడదు!"
            if lang == "te" else
            "UPI PIN is used STRICTLY to <u>SEND/DEDUCT</u> money from your account. You NEVER need to enter a PIN to <u>RECEIVE</u> money!"
        )
        footer_alert = "డబ్బులు పంపామని చెప్పి పిన్ కొట్టమంటే అది 100% మోసగాడే!" if lang == "te" else "Anyone asking you to enter your PIN to receive money is 100% a fraudster!"
        retry_label = "🔄 డెమోను మళ్ళీ ప్రయత్నించండి (Try Again)" if lang == "te" else "Try Again 🔄"

        render_html(f"""
        <div style="max-width: 620px; margin: 0 auto; background: #fef2f2; border: 3.5px solid #d62828; border-radius: 28px; padding: 34px 28px; text-align: center; box-shadow: 0 16px 36px rgba(214,40,40,0.25);">
            <div style="font-size: 4rem; margin-bottom: 8px;">🛑 DANGER! 🛑</div>
            <h2 style="color: #991b1b; margin-top: 0; font-size: 2.1rem; font-weight: 950; line-height: 1.25;">
                {danger_title}
            </h2>
            <div style="background: #ffffff; border-radius: 20px; padding: 22px; border: 2px solid #ef4444; margin: 20px 0; text-align: left;">
                <h3 style="color: #991b1b; margin-top: 0; font-size: 1.35rem; font-weight: 900;">{rule_header}</h3>
                <p style="font-size: 1.22rem; color: #063970; line-height: 1.65; font-weight: 800; margin-bottom: 0;">
                    {rule_body}
                </p>
            </div>
            <p style="font-size: 1.15rem; color: #7f1d1d; font-weight: 800;">
                {footer_alert}
            </p>
        </div>
        """)

        render_html("<div style='margin-bottom: 24px;'></div>")
        if st.button(retry_label, key="btn_retry_upi", type="primary"):
            st.session_state.upi_step = "request_received"
            st.rerun()

    # Screen 3B: User clicked decline
    elif st.session_state.upi_step == "safe_declined":
        bravo_title = "మీరు మీ ₹5,000 ను కాపాడుకున్నారు!" if lang == "te" else "You Successfully Protected Your ₹5,000!"
        bravo_header = "✅ సరైన నిర్ణయం (Safe Choice):" if lang == "te" else "✅ Safe & Smart Action:"
        bravo_body = (
            "మోసపూరిత చెల్లింపు అభ్యర్థనను మీరు తిరస్కరించారు. డబ్బులు జమ అయ్యాయో లేదో తెలుసుకోవడానికి మీ బ్యాంక్ అధికారిక ఎస్ఎంఎస్ లేదా బ్యాలెన్స్ మాత్రమే తనిఖీ చేయాలి."
            if lang == "te" else
            "You declined the fraudulent collect request. To verify credits, always check your bank account balance or official bank SMS directly."
        )
        bravo_foot = "ఈ ముఖ్యమైన విషయాన్ని మీ తోటి గ్రామస్తులకు తప్పక చెప్పండి!" if lang == "te" else "Share this life-saving cyber tip with friends and neighbors!"
        restart_upi_label = "🔄 డెమోను మళ్ళీ చేయండి (Restart Demo)" if lang == "te" else "Restart Demo 🔄"

        render_html(f"""
        <div style="max-width: 620px; margin: 0 auto; background: #f0fdf4; border: 3.5px solid #168447; border-radius: 28px; padding: 34px 28px; text-align: center; box-shadow: 0 16px 36px rgba(22,132,71,0.25);">
            <div style="font-size: 4rem; margin-bottom: 8px;">🎉 శభాష్! 🎉</div>
            <h2 style="color: #166534; margin-top: 0; font-size: 2.1rem; font-weight: 950; line-height: 1.25;">
                {bravo_title}
            </h2>
            <div style="background: #ffffff; border-radius: 20px; padding: 22px; border: 2px solid #86efac; margin: 20px 0; text-align: left;">
                <h3 style="color: #166534; margin-top: 0; font-size: 1.35rem; font-weight: 900;">{bravo_header}</h3>
                <p style="font-size: 1.22rem; color: #063970; line-height: 1.65; font-weight: 800; margin-bottom: 0;">
                    {bravo_body}
                </p>
            </div>
            <p style="font-size: 1.15rem; color: #14532d; font-weight: 800;">
                {bravo_foot}
            </p>
        </div>
        """)

        render_html("<div style='margin-bottom: 24px;'></div>")
        if st.button(restart_upi_label, key="btn_restart_upi"):
            st.session_state.upi_step = "request_received"
            st.rerun()
