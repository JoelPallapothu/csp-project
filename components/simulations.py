"""
CAVI - Cyber Aware Village Initiative
Interactive Practical Simulators:
1. "Spot the Scam" (Realistic Smartphone Mockup & WhatsApp Interface)
2. Interactive UPI PIN Safety Simulator (PhonePe/GPay Mock with Interactive Touch Keypad)
"""

import streamlit as st
from data.simulations_data import SPOT_THE_SCAM_SCENARIOS, UPI_SIMULATOR_STEPS
from data.translations import get_text
from utils.helpers import get_current_lang, record_scam_scenario
from utils.styling import render_html

def render_simulations_page():
    lang = get_current_lang()

    # Safety Disclaimer Header
    render_html(f"""
    <div style="background: #fffbeb; border-left: 6px solid #f59e0b; padding: 16px 22px; border-radius: 14px; margin-bottom: 24px; box-shadow: 0 4px 14px rgba(245, 158, 11, 0.1);">
        <div style="font-weight: 800; color: #b45309; font-size: 1.05rem;">
            🛡️ విద్యాసంబంధిత డెమో (EDUCATIONAL SIMULATION ONLY):
        </div>
        <div style="color: #78350f; font-size: 0.95rem; margin-top: 4px;">
            {get_text('safety_disclaimer', lang)}
        </div>
    </div>
    """)

    sim_tab1, sim_tab2 = st.tabs([
        "🎭 'Spot the Scam' (మోసాన్ని గుర్తించండి)",
        "💳 UPI PIN Safety Simulator (యూపీఐ సిమ్యులేటర్)"
    ])

    with sim_tab1:
        render_spot_the_scam(lang)

    with sim_tab2:
        render_upi_simulator(lang)

def render_spot_the_scam(lang: str):
    render_html("""
    <div style="margin-bottom: 18px;">
        <h2 style="color: #091b36; margin-bottom: 6px;">🎭 నిజమైనదా లేక మోసమా? (Spot the Scam)</h2>
        <p style="font-size: 1.15rem; color: #475569;">
            మీ మొబైల్‌కు వచ్చే సందేశాలు లేదా ఫోన్ కాల్స్‌ను జాగ్రత్తగా గమనించండి. అది <b>సురక్షితమైనదా (SAFE)</b> లేక <b>మోసమా (SCAM)</b> చెప్పండి.
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
    scenario = SPOT_THE_SCAM_SCENARIOS[idx]
    total_scenarios = len(SPOT_THE_SCAM_SCENARIOS)

    st.markdown(f"**సందర్భం {idx + 1} / {total_scenarios} (Scenario {idx + 1} of {total_scenarios}):**")

    # Realistic Smartphone Screen Mockup
    msg = scenario["message_mock"]
    render_html(f"""
    <div style="max-width: 520px; margin: 0 auto 26px auto; background: #0b1320; border-radius: 40px; padding: 14px; box-shadow: 0 20px 48px rgba(0,0,0,0.35); border: 4px solid #334155;">
        <!-- Top Status Bar -->
        <div style="display: flex; justify-content: space-between; align-items: center; padding: 4px 18px 10px 18px; color: #cbd5e1; font-size: 0.8rem; font-weight: 700;">
            <span>10:45 AM</span>
            <!-- Camera notch -->
            <div style="width: 70px; height: 5px; background: #475569; border-radius: 9999px;"></div>
            <span>📶 4G • 🔋 88%</span>
        </div>
        
        <!-- Screen Canvas -->
        <div style="background: #efeae2; border-radius: 28px; overflow: hidden; min-height: 360px; display: flex; flex-direction: column; justify-content: space-between;">
            <!-- WhatsApp / App Top Header -->
            <div style="background: #075e54; color: white; padding: 12px 16px; display: flex; align-items: center; gap: 12px;">
                <div style="background: #128c7e; width: 42px; height: 42px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 1.4rem;">
                    👤
                </div>
                <div style="flex: 1;">
                    <div style="font-weight: 800; font-size: 1.05rem; line-height: 1.2;">
                        {scenario['sender_label']}
                    </div>
                    <div style="font-size: 0.78rem; opacity: 0.85;">
                        {scenario['sender']}
                    </div>
                </div>
                <span class="badge-pill" style="background: rgba(255,255,255,0.2); color: white; font-size: 0.75rem;">
                    {scenario['type']}
                </span>
            </div>

            <!-- Message Bubble -->
            <div style="padding: 20px 16px; flex: 1;">
                <div style="background: #ffffff; border-radius: 16px 16px 16px 4px; padding: 16px; box-shadow: 0 2px 6px rgba(0,0,0,0.08); max-width: 95%;">
                    <div style="font-weight: 800; color: #dc2626; font-size: 1.1rem; margin-bottom: 8px;">
                        {msg['title']}
                    </div>
                    <div style="font-size: 1.0rem; color: #1e293b; line-height: 1.5; margin-bottom: 10px;">
                        {msg['body']}
                    </div>
                    <div style="display: flex; justify-content: space-between; align-items: center; font-size: 0.75rem; color: #64748b; font-style: italic;">
                        <span>{msg['footer']}</span>
                        <span style="color: #0284c7; font-weight: 700;">{scenario['time']} ✓✓</span>
                    </div>
                </div>
            </div>

            <!-- Bottom App Footer Mock -->
            <div style="background: #f0f2f5; padding: 10px 16px; display: flex; align-items: center; justify-content: space-between; border-top: 1px solid #d1d7db; color: #64748b; font-size: 0.85rem;">
                <span>💬 Message</span>
                <span>📎 📷 🎤</span>
            </div>
        </div>
    </div>
    """)

    # Interactive Large Touch Buttons
    if not st.session_state.scenario_answered:
        render_html("<h3 style='text-align: center; color: #091b36; margin-bottom: 16px;'>ఈ సందేశం సురక్షితమైనదా లేక మోసమా? (Safe or Scam?)</h3>")
        col_safe, col_scam = st.columns(2)
        with col_safe:
            if st.button("🟢 సురక్షితం (SAFE)", key=f"btn_safe_{idx}", use_container_width=True):
                st.session_state.user_scenario_choice = "safe"
                st.session_state.scenario_answered = True
                record_scam_scenario(scenario["id"], scenario["correct_answer"] == "safe")
                st.rerun()

        with col_scam:
            if st.button("🔴 మోసం (SCAM)", key=f"btn_scam_{idx}", type="primary", use_container_width=True):
                st.session_state.user_scenario_choice = "scam"
                st.session_state.scenario_answered = True
                record_scam_scenario(scenario["id"], scenario["correct_answer"] == "scam")
                st.rerun()
    else:
        user_choice = st.session_state.user_scenario_choice
        is_correct = (user_choice == scenario["correct_answer"])

        if is_correct:
            st.success("🎉 అద్భుతం! మీరు సరిగ్గా గుర్తించారు! (Correct Answer!)")
        else:
            st.error("⚠️ జాగ్రత్త! ఇది మోసం (Incorrect choice - Be cautious!)")

        # Explanation Card
        explanation_text = scenario["explanation"].get(lang, scenario["explanation"]["te"])
        render_html(f"""
        <div class="cavi-card" style="border-left: 6px solid {'#16a34a' if is_correct else '#dc2626'};">
            <h4 style="margin-top: 0; color: #091b36; font-size: 1.25rem;">పరిష్కారం & వివరణ (Explanation):</h4>
            <p style="font-size: 1.15rem; line-height: 1.6; color: #1e293b; margin-bottom: 0;">{explanation_text}</p>
        </div>
        """)

        # Red Flags list
        red_flags_list = scenario["red_flag_points"].get(lang, scenario["red_flag_points"]["te"])
        st.markdown("##### 🚩 గుర్తించవలసిన ముఖ్య ఆధారాలు (Key Red Flags):")
        rf_cols = st.columns(len(red_flags_list))
        for r_idx, rf_item in enumerate(red_flags_list):
            with rf_cols[r_idx]:
                render_html(f"""
                <div style="background: #ffffff; border: 1px solid #cbd5e1; border-radius: 12px; padding: 12px; text-align: center; font-weight: 700; color: #091b36; box-shadow: 0 2px 6px rgba(0,0,0,0.04);">
                    📌 {rf_item}
                </div>
                """)

        render_html("<div style='margin-bottom: 20px;'></div>")
        
        # Navigation
        if idx < total_scenarios - 1:
            if st.button("తదుపరి సందర్భం (Next Scenario) ➔", key="btn_next_scenario", type="primary"):
                st.session_state.current_scenario_idx += 1
                st.session_state.scenario_answered = False
                st.session_state.user_scenario_choice = None
                st.rerun()
        else:
            st.info("👏 అభినందనలు! మీరు అన్ని సందర్భాలను పూర్తి చేశారు!")
            if st.button("మళ్ళీ మొదటి నుండి ప్రయత్నించండి (Restart Scenarios) 🔄", key="btn_restart_scenarios"):
                st.session_state.current_scenario_idx = 0
                st.session_state.scenario_answered = False
                st.session_state.user_scenario_choice = None
                st.rerun()

def render_upi_simulator(lang: str):
    render_html("""
    <div style="margin-bottom: 18px;">
        <h2 style="color: #091b36; margin-bottom: 6px;">💳 యూపీఐ భద్రతా సిమ్యులేటర్ (UPI PIN Safety Simulator)</h2>
        <p style="font-size: 1.15rem; color: #475569;">
            భారతదేశంలో ఎక్కువ మంది రైతులు, చిరువ్యాపారులు మోసపోయే సందర్భం: <b>"మీ ఖాతాకు ₹5,000 పంపాను, రిసీవ్ చేసుకోవడానికి యూపీఐ పిన్ కొట్టండి"</b>. క్రింది లైవ్ డెమో ద్వారా నిజమైన నియమాన్ని నేర్చుకోండి!
        </p>
    </div>
    """)

    if "upi_step" not in st.session_state:
        st.session_state.upi_step = "request_received"

    # Screen 1: Payment Request Screen
    if st.session_state.upi_step == "request_received":
        render_html(f"""
        <div style="max-width: 480px; margin: 0 auto 24px auto; background: #ffffff; border-radius: 28px; padding: 24px; border: 2px solid #e2e8f0; box-shadow: 0 16px 36px rgba(15,43,92,0.1);">
            <div style="display: flex; align-items: center; justify-content: space-between; border-bottom: 2px solid #f1f5f9; padding-bottom: 14px; margin-bottom: 18px;">
                <span style="font-weight: 900; color: #5b21b6; font-size: 1.35rem; display: flex; align-items: center; gap: 6px;">
                    <span>📱</span> PhonePe / Google Pay
                </span>
                <span class="badge-pill badge-danger" style="font-size: 0.82rem;">చెల్లింపు అభ్యర్థన</span>
            </div>
            
            <div style="text-align: center; padding: 12px 0;">
                <div style="font-size: 1.0rem; color: #64748b; font-weight: 600;">డబ్బులు అడుగుతున్న వ్యక్తి (Requester):</div>
                <div style="font-size: 1.3rem; font-weight: 900; color: #091b36; margin: 6px 0;">
                    {UPI_SIMULATOR_STEPS['buyer_name']}
                </div>
                <div style="font-size: 3.0rem; font-weight: 950; color: #dc2626; margin: 14px 0; letter-spacing: -1px;">
                    ₹5,000.00
                </div>
                <div style="background: #fef2f2; border: 1.5px solid #fecaca; border-radius: 14px; padding: 12px 16px; font-size: 0.98rem; color: #991b1b; font-weight: 700; line-height: 1.45;">
                    📞 మోసగాడి మాట: "అన్నా, ధాన్యం డబ్బులు ₹5,000 పంపాను. మీ ఫోన్‌లో PAY నొక్కి 4 అంకెల యూపీఐ పిన్ కొట్టండి!"
                </div>
            </div>
        </div>
        """)

        render_html("<h3 style='text-align: center; color: #091b36; margin-bottom: 16px;'>మీరు ఇప్పుడు ఏమి చేస్తారు?</h3>")

        col1, col2 = st.columns(2)
        with col1:
            if st.button("🛑 DECLINE (తిరస్కరించండి)", key="btn_upi_decline", type="primary", use_container_width=True):
                st.session_state.upi_step = "safe_declined"
                st.session_state.progress["upi_sim_done"] = True
                st.rerun()
        with col2:
            if st.button("👉 PAY / ENTER PIN (పిన్ కొట్టడానికి వెళ్లండి)", key="btn_upi_pay", use_container_width=True):
                st.session_state.upi_step = "keypad_screen"
                st.rerun()

    # Screen 2: Interactive Keypad Screen (Simulated Pin entry)
    elif st.session_state.upi_step == "keypad_screen":
        render_html("""
        <div style="max-width: 440px; margin: 0 auto 20px auto; background: #0f172a; border-radius: 28px; padding: 24px; color: white; text-align: center; box-shadow: 0 16px 36px rgba(0,0,0,0.3);">
            <div style="font-size: 1.1rem; color: #94a3b8; margin-bottom: 8px;">Enter 4-Digit UPI PIN to Pay ₹5,000</div>
            <!-- Pin Dots -->
            <div style="display: flex; justify-content: center; gap: 16px; margin: 18px 0;">
                <div style="width: 18px; height: 18px; border-radius: 50%; border: 2px solid #38bdf8; background: #38bdf8;"></div>
                <div style="width: 18px; height: 18px; border-radius: 50%; border: 2px solid #64748b;"></div>
                <div style="width: 18px; height: 18px; border-radius: 50%; border: 2px solid #64748b;"></div>
                <div style="width: 18px; height: 18px; border-radius: 50%; border: 2px solid #64748b;"></div>
            </div>
            <div style="font-size: 0.85rem; color: #f87171; font-weight: 700;">
                ⚠️ కీప్యాడ్‌పై ఏదైనా నంబర్ నొక్కండి (Tap any key below)
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
        render_html("""
        <div style="max-width: 580px; margin: 0 auto; background: #fef2f2; border: 3.5px solid #dc2626; border-radius: 26px; padding: 32px 26px; text-align: center; box-shadow: 0 16px 36px rgba(220,38,38,0.25);">
            <div style="font-size: 4rem; margin-bottom: 8px;">🛑 DANGER! 🛑</div>
            <h2 style="color: #991b1b; margin-top: 0; font-size: 2.0rem; font-weight: 950; line-height: 1.25;">
                ఆగండి! మీరు మీ అకౌంట్ నుండి ₹5,000 పోగొట్టుకునేవారు!
            </h2>
            <div style="background: #ffffff; border-radius: 18px; padding: 22px; border: 2px solid #ef4444; margin: 20px 0; text-align: left;">
                <h3 style="color: #991b1b; margin-top: 0; font-size: 1.35rem;">⚠️ అత్యంత ముఖ్యమైన సూత్రం (GOLDEN RULE):</h3>
                <p style="font-size: 1.2rem; color: #091b36; line-height: 1.65; font-weight: 800; margin-bottom: 0;">
                    యూపీఐ పిన్ (UPI PIN) అనేది మీ బ్యాంక్ ఖాతా నుండి డబ్బులు <u>పంపించడానికి (SEND)</u> మాత్రమే ఉపయోగించాలి.
                    మీ ఖాతాలోకి డబ్బులు <u>రావడానికి (RECEIVE)</u> పిన్ అస్సలు కొట్టకూడదు!
                </p>
            </div>
            <p style="font-size: 1.1rem; color: #7f1d1d; font-weight: 700;">
                డబ్బులు పంపామని చెప్పి పిన్ కొట్టమంటే అది 100% మోసగాడే!
            </p>
        </div>
        """)

        render_html("<div style='margin-bottom: 22px;'></div>")
        if st.button("🔄 డెమోను మళ్ళీ ప్రయత్నించండి (Try Again)", key="btn_retry_upi", type="primary"):
            st.session_state.upi_step = "request_received"
            st.rerun()

    # Screen 3B: User clicked decline
    elif st.session_state.upi_step == "safe_declined":
        render_html("""
        <div style="max-width: 580px; margin: 0 auto; background: #f0fdf4; border: 3.5px solid #16a34a; border-radius: 26px; padding: 32px 26px; text-align: center; box-shadow: 0 16px 36px rgba(220,163,74,0.25);">
            <div style="font-size: 4rem; margin-bottom: 8px;">🎉 శభాష్! 🎉</div>
            <h2 style="color: #166534; margin-top: 0; font-size: 2.0rem; font-weight: 950; line-height: 1.25;">
                మీరు మీ ₹5,000 ను కాపాడుకున్నారు!
            </h2>
            <div style="background: #ffffff; border-radius: 18px; padding: 22px; border: 2px solid #86efac; margin: 20px 0; text-align: left;">
                <h3 style="color: #166534; margin-top: 0; font-size: 1.35rem;">✅ సరైన నిర్ణయం:</h3>
                <p style="font-size: 1.2rem; color: #091b36; line-height: 1.65; font-weight: 800; margin-bottom: 0;">
                    మోసపూరిత చెల్లింపు అభ్యర్థనను మీరు తిరస్కరించారు. డబ్బులు జమ అయ్యాయో లేదో తెలుసుకోవడానికి మీ బ్యాంక్ అధికారిక ఎస్ఎంఎస్ లేదా బ్యాలెన్స్ మాత్రమే తనిఖీ చేయాలి.
                </p>
            </div>
            <p style="font-size: 1.1rem; color: #14532d; font-weight: 700;">
                ఈ ముఖ్యమైన విషయాన్ని మీ తోటి రైతులకు, గ్రామస్తులకు తప్పక చెప్పండి!
            </p>
        </div>
        """)

        render_html("<div style='margin-bottom: 22px;'></div>")
        if st.button("🔄 డెమోను మళ్ళీ చేయండి (Restart Demo)", key="btn_restart_upi"):
            st.session_state.upi_step = "request_received"
            st.rerun()
