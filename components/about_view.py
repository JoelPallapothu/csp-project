"""
CAVI - Cyber Aware Village Initiative
About Project Component: Project Objectives, Rural Andhra Pradesh Methodology,
How CAVI Works & Poster Showcase
"""

import streamlit as st
from components.poster_showcase import render_poster_showcase
from data.translations import get_text
from utils.helpers import get_current_lang
from utils.styling import render_html

def render_about_page():
    lang = get_current_lang()

    # Project Overview Banner
    render_html(f"""
    <div class="cavi-card" style="border-left: 6px solid #091b36; margin-bottom: 26px;">
        <span class="badge-pill badge-info" style="font-size: 0.9rem; margin-bottom: 8px;">
            🎓 కమ్యూనిటీ సర్వీస్ ప్రాజెక్ట్ (Community Service Project - CSP)
        </span>
        <h1 style="color: #091b36; font-size: 2.3rem; margin: 8px 0 10px 0; font-weight: 900;">
            Cyber Aware Village Initiative (CAVI)
        </h1>
        <h3 style="color: #0284c7; font-weight: 800; margin-top: 0; font-size: 1.35rem;">
            "Raising Awareness to Prevent Cyber Fraud Among Illiterate and Semi-Literate Villagers"
        </h3>
        <p style="font-size: 1.15rem; color: #1e293b; line-height: 1.65; margin-bottom: 0;">
            ఆంధ్రప్రదేశ్ గ్రామీణ ప్రాంతాల్లో తొలిసారి స్మార్ట్‌ఫోన్ మరియు డిజిటల్ చెల్లింపులు (UPI/PhonePe/GPay) వాడుతున్న నిరక్షరాస్యులు, రైతులు, మహిళలు, చిరువ్యాపారులు మరియు వృద్ధులను సైబర్ నేరగాళ్ల దోపిడీ నుండి రక్షించడానికి రూపొందించిన సమగ్ర ప్రజా అవగాహన వేదిక.
        </p>
    </div>
    """)

    # Target Audience & Location Cards
    t_col1, t_col2 = st.columns(2)
    with t_col1:
        render_html("""
        <div class="cavi-card" style="border-top: 4px solid #16a34a; height: 100%;">
            <h3 style="color: #15803d; margin-top: 0; font-size: 1.3rem;">🎯 లక్ష్య వర్గాలు (Target Audience):</h3>
            <ul style="font-size: 1.05rem; color: #1e293b; line-height: 1.7; padding-left: 20px; margin-bottom: 0;">
                <li>నిరక్షరాస్యులు మరియు పాక్షిక అక్షరాస్యులైన గ్రామస్తులు</li>
                <li>డ్వాక్రా మహిళలు మరియు స్వయం సహాయక సంఘాలు (SHGs)</li>
                <li>రైతులు మరియు వ్యవసాయ కూలీలు</li>
                <li>చిన్న కిరాణా మరియు గ్రామీణ వ్యాపారులు</li>
                <li>వృద్ధులు మరియు మొదటిసారి స్మార్ట్‌ఫోన్ వాడుతున్న వినియోగదారులు</li>
            </ul>
        </div>
        """)

    with t_col2:
        render_html("""
        <div class="cavi-card" style="border-top: 4px solid #0284c7; height: 100%;">
            <h3 style="color: #0369a1; margin-top: 0; font-size: 1.3rem;">📍 భౌగోళిక నేపథ్యం (Location & Context):</h3>
            <p style="font-size: 1.05rem; color: #1e293b; line-height: 1.65;">
                ఈ ప్రాజెక్ట్ ఆంధ్రప్రదేశ్‌లోని గ్రామీణ సచివాలయాలు (Grama Sachivalayam), రైతు భరోసా కేంద్రాలు (RBKs), మరియు పంచాయతీల కేంద్రంగా క్షేత్రస్థాయి పరిశీలనలు జరిపి రూపొందించబడింది.
            </p>
            <div style="background: #f0f9ff; border: 1px solid #bae6fd; border-radius: 12px; padding: 12px 16px; font-weight: 700; color: #0369a1; font-size: 0.95rem;">
                🏛️ గ్రామీణ ప్రజలకు సులభమైన తెలుగులో సైబర్ రక్షణ కవచం
            </div>
        </div>
        """)

    render_html("<div style='margin-bottom: 26px;'></div>")

    # Core Objectives
    render_html("### 🎯 ప్రాజెక్ట్ ప్రధాన లక్ష్యాలు (Core Objectives)")
    
    obj_cols1, obj_cols2 = st.columns(2)
    with obj_cols1:
        render_html("""
        <div class="cavi-card">
            <h4 style="color: #091b36; margin-top: 0; font-size: 1.15rem;">1. 💡 డిజిటల్ అక్షరాస్యతను పెంచడం</h4>
            <p style="color: #475569; font-size: 1.0rem; line-height: 1.5;">
                స్మార్ట్‌ఫోన్లు వాడుతున్న గ్రామీణులకు ఓటీపీ, పిన్ మరియు రహస్య సంఖ్యల భద్రతను వివరించడం.
            </p>
            <h4 style="color: #091b36; font-size: 1.15rem;">2. 🛡️ సైబర్ నేరాల బారిన పడకుండా నిరోధించడం</h4>
            <p style="color: #475569; font-size: 1.0rem; line-height: 1.5;">
                నకిలీ లాటరీలు, డిజిటల్ అరెస్ట్ మరియు లోన్ యాప్స్ ముఠాల ఉచ్చులో పడకుండా ముందే అప్రమత్తం చేయడం.
            </p>
            <h4 style="color: #091b36; font-size: 1.15rem;">3. 💳 సురక్షిత డిజిటల్ చెల్లింపుల శిక్షణ</h4>
            <p style="color: #475569; font-size: 1.0rem; line-height: 1.5;">
                డబ్బులు రావడానికి పిన్ అవసరం లేదనే సూత్రాన్ని ప్రతి ఒక్కరి మనసులో నాటుకుపోయేలా చేయడం.
            </p>
        </div>
        """)

    with obj_cols2:
        render_html("""
        <div class="cavi-card">
            <h4 style="color: #091b36; margin-top: 0; font-size: 1.15rem;">4. 🔍 మోసపూరిత ఎత్తుగడలను గుర్తించడం</h4>
            <p style="color: #475569; font-size: 1.0rem; line-height: 1.5;">
                నకిలీ కరెంట్ బిల్లు లింకులు, బహుమతి మెసేజ్‌లు, అనుమానాస్పద కాల్స్‌ను తిరస్కరించడం నేర్పడం.
            </p>
            <h4 style="color: #091b36; font-size: 1.15rem;">5. 🚨 గోల్డెన్ అవర్‌లో 1930 కు ఫిర్యాదు</h4>
            <p style="color: #475569; font-size: 1.0rem; line-height: 1.5;">
                మోసం జరిగిన 2-3 గంటల్లోపు ఫిర్యాదు చేసి నిధులు ఫ్రీజ్ చేయించడంపై స్పష్టమైన మార్గదర్శనం ఇవ్వడం.
            </p>
            <h4 style="color: #091b36; font-size: 1.15rem;">6. 🤝 గ్రామీణ సాధికారత & సమాజ రక్షణ</h4>
            <p style="color: #475569; font-size: 1.0rem; line-height: 1.5;">
                గ్రామాల్లో ఒకరికొకరు సహాయం చేసుకుంటూ సైబర్ మోసాల రహిత గ్రామాలుగా తీర్చిదిద్దడం.
            </p>
        </div>
        """)

    render_html("<div style='margin-bottom: 26px;'></div>")

    # How CAVI Works
    render_html("### ⚙️ CAVI 6-దశల కార్యాచరణ విధానం (How CAVI Works)")
    
    work_steps = [
        {"num": "1", "icon": "📢", "title": "అవగాహన (Awareness)", "desc": "గ్రామీణ భాషలో సులభమైన పోస్టర్లు, చిహ్నాలు మరియు బొమ్మల ద్వారా మోసాల వివరణ."},
        {"num": "2", "icon": "🎭", "title": "ప్రత్యక్ష డెమో (Demonstration)", "desc": "స్పాట్ ది స్కామ్ మరియు యూపీఐ సిమ్యులేటర్ల ద్వారా ఆచరణాత్మక అనుభవం."},
        {"num": "3", "icon": "🎥", "title": "వీడియో లెర్నింగ్ (Videos)", "desc": "కేంద్ర ప్రభుత్వం మరియు ఆర్బీఐ అధికారిక అవగాహన వీడియోల ప్రదర్శన."},
        {"num": "4", "icon": "🧠", "title": "క్విజ్ పరీక్ష (Quiz)", "desc": "గ్రామీణ ప్రశ్నల ద్వారా నేర్చుకున్న విషయాల పునశ్చరణ మరియు సర్టిఫికేషన్."},
        {"num": "5", "icon": "🚨", "title": "ఫిర్యాదు శిక్షణ (Reporting)", "desc": "1930 హెల్ప్‌లైన్ మరియు సైబర్ పోర్టల్ ద్వారా తక్షణ సహాయం పొందే విధానం."},
        {"num": "6", "icon": "🌾", "title": "సమాజ భాగస్వామ్యం (Outreach)", "desc": "గ్రామ సచివాలయాలు, కాలేజీ విద్యార్థులు మరియు వాలంటీర్లతో విస్తృత ప్రచారం."}
    ]

    h_cols = st.columns(3)
    for idx, step in enumerate(work_steps):
        with h_cols[idx % 3]:
            render_html(f"""
            <div class="cavi-card" style="border-top: 4px solid #0284c7; min-height: 165px; margin-bottom: 16px;">
                <div style="font-size: 2.0rem; margin-bottom: 6px;">{step['icon']}</div>
                <div style="font-size: 1.15rem; font-weight: 800; color: #091b36; margin-bottom: 4px;">
                    {step['num']}. {step['title']}
                </div>
                <div style="font-size: 0.98rem; color: #475569; line-height: 1.5;">
                    {step['desc']}
                </div>
            </div>
            """)

    render_html("<div style='margin-bottom: 30px;'></div>")

    # Render Original Community Awareness Poster Showcase
    render_poster_showcase()
