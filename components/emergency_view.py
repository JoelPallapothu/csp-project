"""
CAVI - Cyber Aware Village Initiative
Emergency Response Center: 1930 Helpline, Golden Hour Infographic,
Evidence Checklist & 5-Step Action Flow.
Bilingual: Telugu (Default) and English.
"""

import streamlit as st
from data.translations import get_text
from utils.helpers import get_current_lang
from utils.styling import render_html

def render_emergency_page():
    lang = get_current_lang()

    # Giant Emergency Hero with Pulsing Border
    hero_title = (
        "సైబర్ మోసం జరిగిందా? భయపడకండి. వెంటనే స్పందించండి!"
        if lang == "te" else
        "CYBER FRAUD HAPPENED? DON'T PANIC. ACT QUICKLY!"
    )
    hero_sub = "DON'T PANIC • REPORT IN THE GOLDEN HOUR • DIAL 1930" if lang == "en" else "భయపడకండి • మొదటి 2-3 గంటల్లోనే ఫిర్యాదు చేయండి • 1930 కి కాల్ చేయండి"
    helpline_label = "జాతీయ సైబర్ క్రైమ్ హెల్ప్‌లైన్ (24x7 టోల్ ఫ్రీ)" if lang == "te" else "National Cyber Crime Helpline (24x7 Toll Free)"
    dial_now_btn = "వెంటనే 1930 కి కాల్ చేయండి (Dial 1930 Now)" if lang == "te" else "Dial 1930 Immediately"

    render_html(f"""
    <div style="background: linear-gradient(135deg, #7f1d1d 0%, #d62828 50%, #991b1b 100%); border-radius: 28px; padding: 42px 34px; color: white; text-align: center; box-shadow: 0 16px 40px rgba(214,40,40,0.35); margin-bottom: 30px; border: 3px solid #fca5a5;">
        <div style="font-size: 4.2rem; margin-bottom: 8px;">🚨</div>
        <h1 style="color: #ffffff; font-size: 2.5rem; font-weight: 950; margin: 0 0 10px 0; line-height: 1.25;">
            {hero_title}
        </h1>
        <p style="font-size: 1.35rem; color: #fef08a; font-weight: 800; margin-bottom: 26px;">
            {hero_sub}
        </p>
        
        <div style="background: #ffffff; border-radius: 24px; padding: 26px 38px; display: inline-block; box-shadow: 0 10px 30px rgba(0,0,0,0.3); max-width: 620px; margin-bottom: 20px;">
            <div style="font-size: 1.1rem; font-weight: 800; color: #64748b; margin-bottom: 6px;">
                {helpline_label}
            </div>
            <div style="font-size: 4.8rem; font-weight: 950; color: #d62828; line-height: 1; margin: 6px 0 18px 0; letter-spacing: 2px;">
                📞 1930
            </div>
            <a href="tel:1930" style="background: linear-gradient(135deg, #d62828 0%, #991b1b 100%); color: white; padding: 14px 36px; border-radius: 9999px; text-decoration: none; font-size: 1.25rem; font-weight: 900; display: inline-block; box-shadow: 0 6px 18px rgba(214,40,40,0.4);">
                {dial_now_btn}
            </a>
        </div>
    </div>
    """)

    # Golden Hour Infographic
    gh_title = "గోల్డెన్ అవర్ (Golden Hour) అంటే ఏమిటి? ఎందుకు అంత ముఖ్యం?" if lang == "te" else "What is the 'Golden Hour'? Why is it Critical?"
    gh_desc = (
        "మీ ఖాతా నుండి డబ్బులు కట్ అయిన <b>మొదటి 2 నుండి 3 గంటల సమయాన్ని 'గోల్డెన్ అవర్'</b> అంటారు. "
        "ఈ సమయంలో 1930 కు ఫోన్ చేస్తే, సైబర్ పోలీసులు నేరుగా బ్యాంక్ నోడల్ అధికారులతో మాట్లాడి మోసగాడి ఖాతాను వెంటనే ఫ్రీజ్ (Freeze) చేయిస్తారు. దీనివల్ల మీ డబ్బులు మోసగాడు ఏటీఎం నుండి డ్రా చేయకముందే సురక్షితంగా నిలిచిపోతాయి!"
        if lang == "te" else
        "The first <b>2 to 3 hours</b> following fraudulent money deduction is known as the <b>'Golden Hour'</b>. "
        "Reporting to 1930 immediately triggers real-time bank nodal intervention to freeze stolen funds before the fraudster withdraws them from an ATM or transfers them to secondary accounts!"
    )
    render_html(f"""
    <div class="cavi-card" style="border-left: 6px solid #f4b400; background: linear-gradient(90deg, #fffbeb 0%, #ffffff 100%); margin-bottom: 28px;">
        <div style="display: flex; align-items: center; gap: 18px; flex-wrap: wrap;">
            <div style="font-size: 3.5rem;">⏳</div>
            <div style="flex: 1 1 520px;">
                <h3 style="color: #92400e; margin: 0 0 8px 0; font-size: 1.45rem; font-weight: 900;">
                    {gh_title}
                </h3>
                <p style="font-size: 1.15rem; color: #1e293b; line-height: 1.65; margin: 0;">
                    {gh_desc}
                </p>
            </div>
        </div>
    </div>
    """)

    # Official Gov Portal Gateway
    col_portal1, col_portal2 = st.columns([7, 3])
    portal_title = "🌐 కేంద్ర ప్రభుత్వ అధికారిక నేషనల్ సైబర్ క్రైమ్ పోర్టల్" if lang == "te" else "🌐 Official National Cyber Crime Reporting Portal"
    portal_sub = (
        "కేంద్ర హోం మంత్రిత్వ శాఖ ఆధ్వర్యంలోని అధికారిక వెబ్‌సైట్ ద్వారా ఆన్‌లైన్‌లో ఎఫ్ఐఆర్ లేదా ఆర్థిక మోసం ఫిర్యాదును నమోదు చేయవచ్చు."
        if lang == "te" else
        "Ministry of Home Affairs official portal to register e-FIRs, financial cyber complaints, and track investigation progress."
    )
    portal_btn_txt = "పోర్టల్ లో రిపోర్ట్ చేయండి ↗" if lang == "te" else "Report on Official Portal ↗"

    with col_portal1:
        render_html(f"""
        <div class="cavi-card" style="border-left: 5px solid #0b63ce; margin-bottom: 0;">
            <h3 style="color: #063970; margin-top: 0; font-size: 1.35rem; font-weight: 900;">{portal_title}</h3>
            <p style="font-size: 1.08rem; color: #334155; margin-bottom: 0; line-height: 1.55;">
                {portal_sub}
            </p>
        </div>
        """)
    with col_portal2:
        render_html(f"""
        <div style="height: 100%; display: flex; align-items: center; justify-content: center; padding-top: 8px;">
            <a href="https://cybercrime.gov.in" target="_blank" 
               style="background: #063970; color: white; padding: 16px 24px; border-radius: 14px; text-decoration: none; font-weight: 800; font-size: 1.1rem; text-align: center; display: block; width: 100%; box-shadow: 0 4px 16px rgba(6,57,112,0.3);">
                {portal_btn_txt}
            </a>
        </div>
        """)

    render_html("<div style='margin-bottom: 32px;'></div>")

    # 5-Step Action Flow
    steps_heading = "🏃‍♂️ మోసం జరిగిన వెంటనే మీరు చేయవలసిన 5 పనులు (5-Step Action Plan)" if lang == "te" else "🏃‍♂️ 5 Immediate Action Steps When Cyber Fraud Happens"
    render_html(f"""
    <h3 style="color: #063970; margin-bottom: 16px; font-size: 1.5rem; font-weight: 900;">
        {steps_heading}
    </h3>
    """)

    steps = [
        {
            "num": "1️⃣",
            "title_te": "ఫోన్ కాల్ లేదా సందేశాన్ని వెంటనే నిలిపివేయండి",
            "desc_te": "మోసగాడితో మాట్లాడటం ఆపండి. అనుమానాస్పద నంబర్‌ను వెంటనే బ్లాక్ చేయండి.",
            "title_en": "Stop Communicating with the Scammer Immediately",
            "desc_en": "Hang up the phone call, do not reply to messages, and block the caller on your smartphone."
        },
        {
            "num": "2️⃣",
            "title_te": "మీ బ్యాంకుకు ఫోన్ చేసి కార్డు లేదా ఖాతా తాత్కాలికంగా బ్లాక్ చేయించండి",
            "desc_te": "మీ బ్యాంక్ కస్టమర్ కేర్‌కు లేదా బ్రాంచ్‌కు సమాచారం ఇచ్చి కార్డు/నెట్ బ్యాంకింగ్ ఆపమని చెప్పండి.",
            "title_en": "Contact Your Bank to Freeze Debit Card & Net Banking",
            "desc_en": "Call your official bank branch or customer care to immediately freeze your ATM card and online banking."
        },
        {
            "num": "3️⃣",
            "title_te": "వెంటనే 1930 హెల్ప్‌లైన్‌కు కాల్ చేయండి",
            "desc_te": "జాతీయ సైబర్ క్రైమ్ హెల్ప్‌లైన్ 1930 కు కాల్ చేసి ఘటన వివరాలు మరియు ట్రాన్సాక్షన్ నంబర్ చెప్పండి.",
            "title_en": "Dial 1930 National Cyber Crime Helpline",
            "desc_en": "Call 1930 immediately with transaction reference numbers (UTR) to initiate inter-bank account freezing."
        },
        {
            "num": "4️⃣",
            "title_te": "cybercrime.gov.in లో అధికారిక ఆన్‌లైన్ ఫిర్యాదు నమోదు చేయండి",
            "desc_te": "గ్రామ సచివాలయం డిజిటల్ అసిస్టెంట్ లేదా కుటుంబ సభ్యుల సహాయంతో పోర్టల్‌లో ఫిర్యాదు నమోదు చేయండి.",
            "title_en": "Lodge an Official Complaint on cybercrime.gov.in",
            "desc_en": "Submit complete incident details on the national cybercrime portal with digital assistance if needed."
        },
        {
            "num": "5️⃣",
            "title_te": "ఆధారాలను ఎట్టి పరిస్థితుల్లోనూ డిలీట్ చేయకండి",
            "desc_te": "మోసగాడి మెసేజ్‌లు, ఫోన్ నంబర్లు, బ్యాంక్ రసీదుల స్క్రీన్‌షాట్లు మరియు పాస్‌బుక్ ఎంట్రీలను భద్రపరచండి.",
            "title_en": "Preserve All Digital Evidence (Screenshots, UTR, Numbers)",
            "desc_en": "Never delete chat logs, caller phone numbers, SMS alerts, UPI transaction IDs, or payment receipts."
        }
    ]

    for s in steps:
        s_title = s["title_te"] if lang == "te" else s["title_en"]
        s_desc = s["desc_te"] if lang == "te" else s["desc_en"]
        render_html(f"""
        <div class="cavi-card" style="display: flex; align-items: flex-start; gap: 20px; padding: 22px 26px; margin-bottom: 14px; border-left: 5px solid #d62828;">
            <div style="font-size: 2.5rem; line-height: 1;">{s['num']}</div>
            <div>
                <div style="font-size: 1.25rem; font-weight: 800; color: #063970; margin-bottom: 4px;">
                    {s_title}
                </div>
                <div style="font-size: 1.05rem; color: #475569; line-height: 1.6;">
                    {s_desc}
                </div>
            </div>
        </div>
        """)

    render_html("<div style='margin-bottom: 30px;'></div>")

    # Interactive Evidence Checklist
    chk_heading = "📋 ఫిర్యాదు చేసే ముందు సిద్ధంగా ఉంచుకోవలసిన ఆధారాలు (Evidence Checklist):" if lang == "te" else "📋 Evidence Checklist (Have These Ready Before Calling 1930):"
    chk_sub = (
        "1930 కు కాల్ చేసేటప్పుడు ఈ వివరాలు మీ చేతిలో ఉంటే పోలీసులు వెంటనే డబ్బులు ఫ్రీజ్ చేయగలరు:"
        if lang == "te" else
        "Having these critical details on hand enables law enforcement to freeze funds with maximum speed:"
    )
    render_html(f"""
    <div style="background: #ffffff; border: 2px solid #cbd5e1; border-radius: 22px; padding: 26px; box-shadow: 0 4px 16px rgba(0,0,0,0.04); margin-bottom: 18px;">
        <h3 style="color: #063970; margin-top: 0; display: flex; align-items: center; gap: 10px; font-size: 1.35rem; font-weight: 900;">
            {chk_heading}
        </h3>
        <p style="font-size: 1.08rem; color: #475569; margin-bottom: 0;">
            {chk_sub}
        </p>
    </div>
    """)

    ch1, ch2 = st.columns(2)
    with ch1:
        st.checkbox("💳 " + ("ట్రాన్సాక్షన్ ఐడీ / యుటీఆర్ (UTR / Transaction ID)" if lang == "te" else "Transaction ID / UTR Number"), value=True, key="chk_utr")
        st.checkbox("🏦 " + ("మీ బ్యాంక్ ఖాతా నంబర్ & బ్రాంచ్ పేరు" if lang == "te" else "Your Bank Account Number & Branch"), value=True, key="chk_bank")
        st.checkbox("📞 " + ("మోసగాడి మొబైల్ నంబర్ / ప్రొఫైల్ వివరాలు" if lang == "te" else "Scammer's Phone Number & Profile Details"), value=True, key="chk_num")
        st.checkbox("💬 " + ("ఎస్ఎంఎస్ లేదా వాట్సాప్ సందేశాలు (Messages)" if lang == "te" else "SMS or WhatsApp Chat Messages"), value=True, key="chk_msgs")
    with ch2:
        st.checkbox("📸 " + ("లావాదేవీల రసీదులు & స్క్రీన్‌షాట్లు" if lang == "te" else "Payment Receipts & Screenshots"), value=True, key="chk_shots")
        st.checkbox("🕒 " + ("మోసం జరిగిన ఖచ్చితమైన తేదీ & సమయం" if lang == "te" else "Exact Date & Time of Incident"), value=True, key="chk_time")
        st.checkbox("🔗 " + ("మోసగాడు పంపిన లింక్ లేదా యాప్ పేరు" if lang == "te" else "Fraudulent Link or App Name (APK)"), value=True, key="chk_app")
        st.checkbox("📧 " + ("ఈమెయిల్ లేదా వెబ్‌సైట్ వివరాలు (URLs)" if lang == "te" else "Emails, Websites & Payment Handles"), value=True, key="chk_emails")
