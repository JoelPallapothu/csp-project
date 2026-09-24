"""
CAVI - Cyber Aware Village Initiative
About Project Component: Project Objectives, Rural Andhra Pradesh Methodology,
How CAVI Works & Poster Showcase.
Bilingual: Telugu (Default) and English.
"""

import streamlit as st
from components.poster_showcase import render_poster_showcase
from data.translations import get_text
from utils.helpers import get_current_lang
from utils.styling import render_html

def render_about_page():
    lang = get_current_lang()

    # Project Overview Banner
    about_desc = (
        "ఆంధ్రప్రదేశ్ గ్రామీణ ప్రాంతాల్లో తొలిసారి స్మార్ట్‌ఫోన్ మరియు డిజిటల్ చెల్లింపులు (UPI/PhonePe/GPay) వాడుతున్న నిరక్షరాస్యులు, రైతులు, మహిళలు, చిరువ్యాపారులు మరియు వృద్ధులను సైబర్ నేరగాళ్ల దోపిడీ నుండి రక్షించడానికి రూపొందించిన సమగ్ర ప్రజా అవగాహన వేదిక."
        if lang == "te" else
        "A grassroots cyber-safety initiative designed to educate and protect illiterate and semi-literate villagers, farmers, women, small shopkeepers, and first-time smartphone users across rural Andhra Pradesh from digital financial fraud."
    )
    render_html(f"""
    <div class="cavi-card" style="border-left: 6px solid #063970; margin-bottom: 26px;">
        <span class="badge-pill badge-info" style="font-size: 0.92rem; margin-bottom: 8px;">
            🎓 {get_text('csp_badge', lang)}
        </span>
        <h1 style="color: #063970; font-size: 2.4rem; margin: 8px 0 10px 0; font-weight: 950;">
            Cyber Aware Village Initiative (CAVI)
        </h1>
        <h3 style="color: #0b63ce; font-weight: 800; margin-top: 0; font-size: 1.4rem;">
            "Raising Awareness to Prevent Cyber Fraud Among Illiterate and Semi-Literate Villagers"
        </h3>
        <p style="font-size: 1.18rem; color: #1e293b; line-height: 1.7; margin-bottom: 0;">
            {about_desc}
        </p>
    </div>
    """)

    # Target Audience & Location Cards
    t_col1, t_col2 = st.columns(2)
    aud_title = "🎯 లక్ష్య వర్గాలు (Target Community):" if lang == "te" else "🎯 Target Community:"
    loc_title = "📍 భౌగోళిక నేపథ్యం (Location & Context):" if lang == "te" else "📍 Location & Rural Context:"

    with t_col1:
        if lang == "te":
            aud_items = """
            <li>నిరక్షరాస్యులు మరియు పాక్షిక అక్షరాస్యులైన గ్రామస్తులు</li>
            <li>డ్వాక్రా మహిళలు మరియు స్వయం సహాయక సంఘాలు (SHGs)</li>
            <li>రైతులు మరియు వ్యవసాయ కూలీలు</li>
            <li>చిన్న కిరాణా మరియు గ్రామీణ వ్యాపారులు</li>
            <li>వృద్ధులు మరియు మొదటిసారి స్మార్ట్‌ఫోన్ వాడుతున్న వినియోగదారులు</li>
            """
        else:
            aud_items = """
            <li>Illiterate and semi-literate rural villagers</li>
            <li>Women self-help groups (SHGs / DWCRA)</li>
            <li>Farmers, smallholders, and agricultural laborers</li>
            <li>Local kirana store owners and small rural businesses</li>
            <li>Senior citizens and first-time digital payment adopters</li>
            """
        render_html(f"""
        <div class="cavi-card" style="border-top: 4px solid #168447; height: 100%;">
            <h3 style="color: #166534; margin-top: 0; font-size: 1.35rem; font-weight: 900;">{aud_title}</h3>
            <ul style="font-size: 1.08rem; color: #1e293b; line-height: 1.75; padding-left: 20px; margin-bottom: 0;">
                {aud_items}
            </ul>
        </div>
        """)

    with t_col2:
        loc_desc = (
            "ఈ ప్రాజెక్ట్ ఆంధ్రప్రదేశ్‌లోని గ్రామీణ సచివాలయాలు (Grama Sachivalayam), రైతు భరోసా కేంద్రాలు (RBKs), మరియు పంచాయతీల కేంద్రంగా క్షేత్రస్థాయి పరిశీలనలు జరిపి రూపొందించబడింది."
            if lang == "te" else
            "Developed with field observations centered around Village Secretariats (Grama Sachivalayams), Rythu Bharosa Kendras (RBKs), and Panchayats across rural Andhra Pradesh."
        )
        shield_txt = "🏛️ గ్రామీణ ప్రజలకు సులభమైన తెలుగులో సైబర్ రక్షణ కవచం" if lang == "te" else "🏛️ Accessible Grassroots Cyber Defense for Andhra Pradesh"
        render_html(f"""
        <div class="cavi-card" style="border-top: 4px solid #0b63ce; height: 100%;">
            <h3 style="color: #063970; margin-top: 0; font-size: 1.35rem; font-weight: 900;">{loc_title}</h3>
            <p style="font-size: 1.08rem; color: #1e293b; line-height: 1.7;">
                {loc_desc}
            </p>
            <div style="background: #f0f9ff; border: 1.5px solid #bae6fd; border-radius: 14px; padding: 14px 18px; font-weight: 800; color: #063970; font-size: 0.98rem;">
                {shield_txt}
            </div>
        </div>
        """)

    render_html("<div style='margin-bottom: 28px;'></div>")

    # Core Objectives
    obj_heading = "🎯 ప్రాజెక్ట్ ప్రధాన లక్ష్యాలు (Core Objectives)" if lang == "te" else "🎯 Core Project Objectives"
    render_html(f"<h3 style='color: #063970; font-size: 1.55rem; font-weight: 900; margin-bottom: 18px;'>{obj_heading}</h3>")
    
    obj_cols1, obj_cols2 = st.columns(2)
    with obj_cols1:
        if lang == "te":
            obj_l1 = """
            <h4 style="color: #063970; margin-top: 0; font-size: 1.2rem; font-weight: 900;">1. 💡 డిజిటల్ అక్షరాస్యతను పెంచడం</h4>
            <p style="color: #475569; font-size: 1.05rem; line-height: 1.6;">
                స్మార్ట్‌ఫోన్లు వాడుతున్న గ్రామీణులకు ఓటీపీ, పిన్ మరియు రహస్య సంఖ్యల భద్రతను వివరించడం.
            </p>
            <h4 style="color: #063970; font-size: 1.2rem; font-weight: 900;">2. 🛡️ సైబర్ నేరాల బారిన పడకుండా నిరోధించడం</h4>
            <p style="color: #475569; font-size: 1.05rem; line-height: 1.6;">
                నకిలీ లాటరీలు, డిజిటల్ అరెస్ట్ మరియు లోన్ యాప్స్ ముఠాల ఉచ్చులో పడకుండా ముందే అప్రమత్తం చేయడం.
            </p>
            <h4 style="color: #063970; font-size: 1.2rem; font-weight: 900;">3. 💳 సురక్షిత డిజిటల్ చెల్లింపుల శిక్షణ</h4>
            <p style="color: #475569; font-size: 1.05rem; line-height: 1.6;">
                డబ్బులు రావడానికి పిన్ అవసరం లేదనే సూత్రాన్ని ప్రతి ఒక్కరి మనసులో నాటుకుపోయేలా చేయడం.
            </p>
            """
        else:
            obj_l1 = """
            <h4 style="color: #063970; margin-top: 0; font-size: 1.2rem; font-weight: 900;">1. 💡 Bolster Digital Literacy</h4>
            <p style="color: #475569; font-size: 1.05rem; line-height: 1.6;">
                Demystify PIN, OTP, and passwords for rural smartphone owners through plain speech and visual storytelling.
            </p>
            <h4 style="color: #063970; font-size: 1.2rem; font-weight: 900;">2. 🛡️ Prevent Rural Financial Exploitation</h4>
            <p style="color: #475569; font-size: 1.05rem; line-height: 1.6;">
                Safeguard villagers from extortion rackets like Digital Arrest, fake lotteries, and predatory instant loan apps.
            </p>
            <h4 style="color: #063970; font-size: 1.2rem; font-weight: 900;">3. 💳 Secure Everyday UPI Transactions</h4>
            <p style="color: #475569; font-size: 1.05rem; line-height: 1.6;">
                Instill the universal rule: UPI PIN is strictly for sending money, never for receiving funds.
            </p>
            """
        render_html(f"""
        <div class="cavi-card">
            {obj_l1}
        </div>
        """)

    with obj_cols2:
        if lang == "te":
            obj_l2 = """
            <h4 style="color: #063970; margin-top: 0; font-size: 1.2rem; font-weight: 900;">4. 🔍 మోసపూరిత ఎత్తుగడలను గుర్తించడం</h4>
            <p style="color: #475569; font-size: 1.05rem; line-height: 1.6;">
                నకిలీ కరెంట్ బిల్లు లింకులు, బహుమతి మెసేజ్‌లు, అనుమానాస్పద కాల్స్‌ను తిరస్కరించడం నేర్పడం.
            </p>
            <h4 style="color: #063970; font-size: 1.2rem; font-weight: 900;">5. 🚨 గోల్డెన్ అవర్‌లో 1930 కు ఫిర్యాదు</h4>
            <p style="color: #475569; font-size: 1.05rem; line-height: 1.6;">
                మోసం జరిగిన 2-3 గంటల్లోపు ఫిర్యాదు చేసి నిధులు ఫ్రీజ్ చేయించడంపై స్పష్టమైన మార్గదర్శనం ఇవ్వడం.
            </p>
            <h4 style="color: #063970; font-size: 1.2rem; font-weight: 900;">6. 🤝 గ్రామీణ సాధికారత & సమాజ రక్షణ</h4>
            <p style="color: #475569; font-size: 1.05rem; line-height: 1.6;">
                గ్రామాల్లో ఒకరికొకరు సహాయం చేసుకుంటూ సైబర్ మోసాల రహిత గ్రామాలుగా తీర్చిదిద్దడం.
            </p>
            """
        else:
            obj_l2 = """
            <h4 style="color: #063970; margin-top: 0; font-size: 1.2rem; font-weight: 900;">4. 🔍 Spot Social Engineering Traps</h4>
            <p style="color: #475569; font-size: 1.05rem; line-height: 1.6;">
                Train citizens to recognize urgency, panic triggers, fake electricity cutoff threats, and malware APKs.
            </p>
            <h4 style="color: #063970; font-size: 1.2rem; font-weight: 900;">5. 🚨 Rapid Golden Hour Emergency Reporting</h4>
            <p style="color: #475569; font-size: 1.05rem; line-height: 1.6;">
                Promote immediate dialing of 1930 within the critical first 2-3 hours to freeze scam accounts.
            </p>
            <h4 style="color: #063970; font-size: 1.2rem; font-weight: 900;">6. 🤝 Grassroots Community Resilience</h4>
            <p style="color: #475569; font-size: 1.05rem; line-height: 1.6;">
                Empower village youth, volunteers, and panchayat leaders to spread digital security best practices.
            </p>
            """
        render_html(f"""
        <div class="cavi-card">
            {obj_l2}
        </div>
        """)

    render_html("<div style='margin-bottom: 28px;'></div>")

    # How CAVI Works
    work_heading = "⚙️ CAVI 6-దశల కార్యాచరణ విధానం (How CAVI Works)" if lang == "te" else "⚙️ How CAVI Works (6-Stage Methodology)"
    render_html(f"<h3 style='color: #063970; font-size: 1.55rem; font-weight: 900; margin-bottom: 18px;'>{work_heading}</h3>")
    
    if lang == "te":
        work_steps = [
            {"num": "1", "icon": "📢", "title": "అవగాహన (Awareness)", "desc": "గ్రామీణ భాషలో సులభమైన పోస్టర్లు, చిహ్నాలు మరియు బొమ్మల ద్వారా మోసాల వివరణ."},
            {"num": "2", "icon": "🎭", "title": "ప్రత్యక్ష డెమో (Demonstration)", "desc": "స్పాట్ ది స్కామ్ మరియు యూపీఐ సిమ్యులేటర్ల ద్వారా ఆచరణాత్మక అనుభవం."},
            {"num": "3", "icon": "🎥", "title": "వీడియో లెర్నింగ్ (Videos)", "desc": "కేంద్ర ప్రభుత్వం మరియు ఆర్బీఐ అధికారిక అవగాహన వీడియోల ప్రదర్శన."},
            {"num": "4", "icon": "🧠", "title": "క్విజ్ పరీక్ష (Quiz)", "desc": "గ్రామీణ ప్రశ్నల ద్వారా నేర్చుకున్న విషయాల పునశ్చరణ మరియు సర్టిఫికేషన్."},
            {"num": "5", "icon": "🚨", "title": "ఫిర్యాదు శిక్షణ (Reporting)", "desc": "1930 హెల్ప్‌లైన్ మరియు సైబర్ పోర్టల్ ద్వారా తక్షణ సహాయం పొందే విధానం."},
            {"num": "6", "icon": "🌾", "title": "సమాజ భాగస్వామ్యం (Outreach)", "desc": "గ్రామ సచివాలయాలు, కాలేజీ విద్యార్థులు మరియు వాలంటీర్లతో విస్తృత ప్రచారం."}
        ]
    else:
        work_steps = [
            {"num": "1", "icon": "📢", "title": "Awareness", "desc": "Visual storytelling and grassroots poster exhibitions in rural Telugu & English."},
            {"num": "2", "icon": "🎭", "title": "Demonstration", "desc": "Hands-on simulators for Spot-the-Scam messages and PhonePe/GPay UPI PIN keypad."},
            {"num": "3", "icon": "🎥", "title": "Video Learning", "desc": "Curated bilingual educational tutorials from RBI Kehta Hai and I4C (MHA)."},
            {"num": "4", "icon": "🧠", "title": "Interactive Quiz", "desc": "10-question evaluation awarding the Digital Village Cyber Guardian Certificate."},
            {"num": "5", "icon": "🚨", "title": "Reporting Guidance", "desc": "Actionable guidelines to report cybercrime via Helpline 1930 and cybercrime.gov.in."},
            {"num": "6", "icon": "🌾", "title": "Grassroots Outreach", "desc": "Community Service Project deployment in Grama Sachivalayams and Panchayats."}
        ]

    h_cols = st.columns(3)
    for idx, step in enumerate(work_steps):
        with h_cols[idx % 3]:
            render_html(f"""
            <div class="cavi-card" style="border-top: 4px solid #0b63ce; min-height: 165px; margin-bottom: 16px;">
                <div style="font-size: 2.2rem; margin-bottom: 6px;">{step['icon']}</div>
                <div style="font-size: 1.18rem; font-weight: 900; color: #063970; margin-bottom: 4px;">
                    {step['num']}. {step['title']}
                </div>
                <div style="font-size: 1.0rem; color: #475569; line-height: 1.55;">
                    {step['desc']}
                </div>
            </div>
            """)

    render_html("<div style='margin-bottom: 32px;'></div>")

    # Render Original Community Awareness Poster Showcase
    render_poster_showcase()
