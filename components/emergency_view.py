"""
CAVI - Cyber Aware Village Initiative
Emergency Response Center: 1930 Helpline, Golden Hour Infographic, Evidence Checklist & 5-Step Action Flow
"""

import streamlit as st
from data.translations import get_text
from utils.helpers import get_current_lang
from utils.styling import render_html

def render_emergency_page():
    lang = get_current_lang()

    # Giant Emergency Hero with Pulsing Border
    render_html("""
    <div style="background: linear-gradient(135deg, #7f1d1d 0%, #dc2626 50%, #991b1b 100%); border-radius: 28px; padding: 40px 32px; color: white; text-align: center; box-shadow: 0 16px 40px rgba(220,38,38,0.35); margin-bottom: 30px; border: 3px solid #fca5a5;">
        <div style="font-size: 4rem; margin-bottom: 6px;">🚨</div>
        <h1 style="color: #ffffff; font-size: 2.4rem; font-weight: 950; margin: 0 0 10px 0; line-height: 1.25;">
            సైబర్ మోసం జరిగిందా? భయపడకండి. వెంటనే స్పందించండి!
        </h1>
        <p style="font-size: 1.35rem; color: #fef08a; font-weight: 800; margin-bottom: 26px;">
            CYBER FINANCIAL FRAUD? DON'T PANIC. ACT QUICKLY.
        </p>
        
        <div style="background: #ffffff; border-radius: 24px; padding: 26px 36px; display: inline-block; box-shadow: 0 10px 30px rgba(0,0,0,0.3); max-width: 620px; margin-bottom: 22px;">
            <div style="font-size: 1.1rem; font-weight: 800; color: #64748b; margin-bottom: 6px;">
                జాతీయ సైబర్ క్రైమ్ హెల్ప్‌లైన్ నంబర్ (24x7 టోల్ ఫ్రీ)
            </div>
            <div style="font-size: 4.5rem; font-weight: 950; color: #dc2626; line-height: 1; margin: 6px 0 16px 0; letter-spacing: 2px;">
                📞 1930
            </div>
            <a href="tel:1930" style="background: linear-gradient(135deg, #dc2626 0%, #991b1b 100%); color: white; padding: 14px 34px; border-radius: 9999px; text-decoration: none; font-size: 1.25rem; font-weight: 900; display: inline-block; box-shadow: 0 6px 18px rgba(220,38,38,0.4);">
                వెంటనే 1930 కి కాల్ చేయండి (Dial 1930 Now)
            </a>
        </div>
    </div>
    """)

    # Golden Hour Infographic
    render_html("""
    <div class="cavi-card" style="border-left: 6px solid #d97706; background: linear-gradient(90deg, #fffbeb 0%, #ffffff 100%); margin-bottom: 28px;">
        <div style="display: flex; align-items: center; gap: 16px; flex-wrap: wrap;">
            <div style="font-size: 3.2rem;">⏳</div>
            <div style="flex: 1 1 500px;">
                <h3 style="color: #92400e; margin: 0 0 6px 0; font-size: 1.45rem; font-weight: 900;">
                    గోల్డెన్ అవర్ (Golden Hour) అంటే ఏమిటి? ఎందుకు అంత ముఖ్యం?
                </h3>
                <p style="font-size: 1.15rem; color: #1e293b; line-height: 1.6; margin: 0;">
                    మీ ఖాతా నుండి డబ్బులు కట్ అయిన <b>మొదటి 2 నుండి 3 గంటల సమయాన్ని 'గోల్డెన్ అవర్'</b> అంటారు. 
                    ఈ సమయంలో 1930 కు ఫోన్ చేస్తే, సైబర్ పోలీసులు నేరుగా బ్యాంక్ నోడల్ అధికారులతో మాట్లాడి మోసగాడి ఖాతాను వెంటనే ఫ్రీజ్ (Freeze) చేయిస్తారు. దీనివల్ల మీ డబ్బులు మోసగాడు ఏటీఎం నుండి డ్రా చేయకముందే సురక్షితంగా నిలిచిపోతాయి!
                </p>
            </div>
        </div>
    </div>
    """)

    # Official Gov Portal Gateway
    col_portal1, col_portal2 = st.columns([7, 3])
    with col_portal1:
        render_html("""
        <div class="cavi-card" style="border-left: 5px solid #0284c7; margin-bottom: 0;">
            <h3 style="color: #091b36; margin-top: 0; font-size: 1.35rem;">🌐 కేంద్ర ప్రభుత్వ అధికారిక నేషనల్ సైబర్ క్రైమ్ పోర్టల్</h3>
            <p style="font-size: 1.05rem; color: #334155; margin-bottom: 0; line-height: 1.55;">
                కేంద్ర హోం మంత్రిత్వ శాఖ ఆధ్వర్యంలోని అధికారిక వెబ్‌సైట్ ద్వారా ఆన్‌లైన్‌లో ఎఫ్ఐఆర్ లేదా ఆర్థిక మోసం ఫిర్యాదును నమోదు చేయవచ్చు.
            </p>
        </div>
        """)
    with col_portal2:
        render_html("""
        <div style="height: 100%; display: flex; align-items: center; justify-content: center; padding-top: 10px;">
            <a href="https://cybercrime.gov.in" target="_blank" 
               style="background: #091b36; color: white; padding: 16px 24px; border-radius: 14px; text-decoration: none; font-weight: 800; font-size: 1.1rem; text-align: center; display: block; width: 100%; box-shadow: 0 4px 16px rgba(9,27,54,0.3);">
                పోర్టల్ లో రిపోర్ట్ చేయండి ↗
            </a>
        </div>
        """)

    render_html("<div style='margin-bottom: 32px;'></div>")

    # 5-Step Action Flow
    render_html("""
    <h3 style="color: #091b36; margin-bottom: 16px; font-size: 1.45rem;">
        🏃‍♂️ మోసం జరిగిన వెంటనే మీరు చేయవలసిన 5 పనులు (5-Step Action Plan)
    </h3>
    """)

    steps = [
        {
            "num": "1️⃣",
            "title": "ఫోన్ కాల్ లేదా సందేశాన్ని వెంటనే నిలిపివేయండి",
            "desc": "మోసగాడితో మాట్లాడటం ఆపండి. అనుమానాస్పద నంబర్‌ను వెంటనే బ్లాక్ చేయండి."
        },
        {
            "num": "2️⃣",
            "title": "మీ బ్యాంకుకు ఫోన్ చేసి కార్డు లేదా ఖాతా తాత్కాలికంగా బ్లాక్ చేయించండి",
            "desc": "మీ బ్యాంక్ కస్టమర్ కేర్‌కు లేదా బ్రాంచ్‌కు సమాచారం ఇచ్చి కార్డు/నెట్ బ్యాంకింగ్ ఆపమని చెప్పండి."
        },
        {
            "num": "3️⃣",
            "title": "వెంటనే 1930 హెల్ప్‌లైన్‌కు కాల్ చేయండి",
            "desc": "జాతీయ సైబర్ క్రైమ్ హెల్ప్‌లైన్ 1930 కు కాల్ చేసి ఘటన వివరాలు మరియు ట్రాన్సాక్షన్ నంబర్ చెప్పండి."
        },
        {
            "num": "4️⃣",
            "title": "cybercrime.gov.in లో ఆన్‌లైన్ ఫిర్యాదు నమోదు చేయండి",
            "desc": "సచివాలయం డిజిటల్ అసిస్టెంట్ లేదా మీ కుటుంబ సభ్యుల సహాయంతో ఆన్‌లైన్ ఫిర్యాదు ఫారమ్ పూర్తి చేయండి."
        },
        {
            "num": "5️⃣",
            "title": "ఆధారాలను ఎట్టి పరిస్థితుల్లోనూ డిలీట్ చేయకండి",
            "desc": "మోసగాడి మెసేజ్‌లు, ఫోన్ నంబర్లు, బ్యాంక్ రసీదుల స్క్రీన్‌షాట్లు మరియు పాస్‌బుక్ ఎంట్రీలను జాగ్రత్తగా ఉంచుకోండి."
        }
    ]

    for s in steps:
        render_html(f"""
        <div class="cavi-card" style="display: flex; align-items: flex-start; gap: 20px; padding: 20px 24px; margin-bottom: 14px; border-left: 5px solid #dc2626;">
            <div style="font-size: 2.4rem; line-height: 1;">{s['num']}</div>
            <div>
                <div style="font-size: 1.2rem; font-weight: 800; color: #091b36; margin-bottom: 4px;">
                    {s['title']}
                </div>
                <div style="font-size: 1.02rem; color: #475569; line-height: 1.55;">
                    {s['desc']}
                </div>
            </div>
        </div>
        """)

    render_html("<div style='margin-bottom: 28px;'></div>")

    # Interactive Evidence Checklist
    render_html("""
    <div style="background: #ffffff; border: 2px solid #cbd5e1; border-radius: 22px; padding: 26px; box-shadow: 0 4px 16px rgba(0,0,0,0.04); margin-bottom: 18px;">
        <h3 style="color: #091b36; margin-top: 0; display: flex; align-items: center; gap: 10px; font-size: 1.35rem;">
            <span>📋</span> ఫిర్యాదు చేసే ముందు ఈ వివరాలను సిద్ధంగా ఉంచుకోండి (Checklist):
        </h3>
        <p style="font-size: 1.05rem; color: #475569; margin-bottom: 0;">
            1930 కు కాల్ చేసేటప్పుడు ఈ వివరాలు మీ చేతిలో ఉంటే పోలీసులు వెంటనే డబ్బులు ఫ్రీజ్ చేయగలరు:
        </p>
    </div>
    """)

    ch1, ch2 = st.columns(2)
    with ch1:
        st.checkbox("💳 ట్రాన్సాక్షన్ ఐడీ / యుటీఆర్ (UTR Number)", value=True, key="chk_utr")
        st.checkbox("🏦 మీ బ్యాంక్ ఖాతా నంబర్ & బ్రాంచ్ పేరు", value=True, key="chk_bank")
        st.checkbox("📞 మోసగాడి మొబైల్ నంబర్ / వాట్సాప్ ప్రొఫైల్", value=True, key="chk_num")
    with ch2:
        st.checkbox("📸 ఎస్ఎంఎస్ లేదా చాట్ స్క్రీన్‌షాట్లు", value=True, key="chk_shots")
        st.checkbox("🕒 మోసం జరిగిన ఖచ్చితమైన తేదీ & సమయం", value=True, key="chk_time")
        st.checkbox("🔗 మోసగాడు పంపిన లింక్ లేదా యాప్ పేరు", value=True, key="chk_app")
