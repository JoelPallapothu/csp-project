"""
CAVI - Cyber Aware Village Initiative
Bilingual Knowledge Base, Curated Q&A, and Guardrail Data for CAVI Cyber Safety Assistant.
Language support: Telugu (Default/Primary) & English. Strict zero Hindi.
"""

# 10 Standard Quick Questions required by prompt
QUICK_QUESTIONS = {
    "en": [
        "What is OTP fraud?",
        "Is this UPI request safe?",
        "What is KYC fraud?",
        "I received a prize message",
        "Someone wants screen access",
        "I lost money",
        "How do I report fraud?",
        "Is this link suspicious?",
        "Someone is asking for my PIN",
        "How can I stay safe online?"
    ],
    "te": [
        "OTP మోసం అంటే ఏమిటి?",
        "ఈ UPI రిక్వెస్ట్ సురక్షితమేనా?",
        "KYC మోసం అంటే ఏమిటి?",
        "నాకు బహుమతి వచ్చినట్లు మెసేజ్ వచ్చింది",
        "ఎవరో నా ఫోన్ స్క్రీన్ యాక్సెస్ అడుగుతున్నారు",
        "నేను డబ్బు కోల్పోయాను",
        "మోసాన్ని ఎలా రిపోర్ట్ చేయాలి?",
        "ఈ లింక్ అనుమానాస్పదంగా ఉందా?",
        "ఎవరో నా PIN అడుగుతున్నారు",
        "ఆన్లైన్లో ఎలా సురక్షితంగా ఉండాలి?"
    ]
}

# Standard Out-of-Scope Responses
OUT_OF_SCOPE_RESPONSES = {
    "en": (
        "I'm mainly designed to help with cyber-fraud awareness and online safety. "
        "I can help you with OTP, UPI, KYC, phishing, screen-sharing scams, "
        "suspicious links, and reporting fraud."
    ),
    "te": (
        "నేను ప్రధానంగా సైబర్ మోసాలు మరియు ఆన్లైన్ భద్రత గురించి సహాయం చేయడానికి రూపొందించబడ్డాను. "
        "OTP, UPI, KYC, ఫిషింగ్, స్క్రీన్ షేరింగ్ మోసాలు, అనుమానాస్పద లింకులు మరియు "
        "మోసాల రిపోర్టింగ్ గురించి నేను సహాయం చేయగలను."
    )
}

# Sensitive Information Warning
SENSITIVE_WARNING = {
    "en": (
        "⚠️ Please do not share OTP, PIN, password, CVV, bank details or other sensitive information here.\n\n"
        "For your safety, remove that information from the chat."
    ),
    "te": (
        "⚠️ దయచేసి OTP, PIN, పాస్‌వర్డ్, CVV, బ్యాంక్ వివరాలు లేదా ఇతర సున్నితమైన సమాచారాన్ని ఇక్కడ పంచుకోవద్దు.\n\n"
        "మీ భద్రత కోసం, ఆ వివరాలను వెంటనే తొలగించండి."
    )
}

# Emergency Lost Money Responses (PART 12)
EMERGENCY_RESPONSES = {
    "en": (
        "🚨 CYBER FRAUD EMERGENCY\n\n"
        "📞 1930\n"
        "🌐 cybercrime.gov.in\n\n"
        "Call 1930 immediately if you have experienced cyber financial fraud.\n\n"
        "Immediate Action Steps:\n"
        "1. Do NOT panic — act fast during the 'Golden Hour' (first 2-3 hours).\n"
        "2. Call 1930 right away to freeze the fraud transaction.\n"
        "3. Lodge an official complaint online at cybercrime.gov.in.\n"
        "4. Contact your bank immediately and block your ATM card, UPI, and net banking.\n"
        "5. Do NOT send any more money to anyone claiming they will recover your funds.\n"
        "6. Do NOT share OTP, PIN, or passwords with anyone.\n"
        "7. Save all evidence: screenshots of messages, transaction IDs, bank statements, and phone numbers."
    ),
    "te": (
        "🚨 అత్యవసర సైబర్ మోసం హెచ్చరిక (CYBER FRAUD EMERGENCY)\n\n"
        "📞 1930\n"
        "🌐 cybercrime.gov.in\n\n"
        "మీరు సైబర్ మోసంలో డబ్బు కోల్పోతే వెంటనే 1930 కు కాల్ చేయండి.\n\n"
        "తక్షణమే చేయవలసిన పనులు:\n"
        "1. భయపడకండి — గోల్డెన్ అవర్ (మొదటి 2-3 గంటలు) లో వెంటనే స్పందించండి.\n"
        "2. వెంటనే 1930 హెల్ప్‌లైన్‌కు కాల్ చేసి మోసపూరిత లావాదేవీని నిలిపివేయించండి.\n"
        "3. అధికారిక వెబ్‌సైట్ cybercrime.gov.in లో కూడా ఫిర్యాదు నమోదు చేయండి.\n"
        "4. మీ బ్యాంకుకు ఫోన్ చేసి ఏటీఎం కార్డు, యూపీఐ (UPI) లావాదేవీలను వెంటనే బ్లాక్ చేయించండి.\n"
        "5. డబ్బులు తిరిగి ఇప్పిస్తామని చెప్పే గుర్తుతెలియని వ్యక్తులకు ఎలాంటి అదనపు డబ్బు పంపకండి.\n"
        "6. ఎవరికీ మీ OTP, UPI PIN, పాస్‌వర్డ్‌లు చెప్పకండి.\n"
        "7. మెసేజ్‌ల స్క్రీన్‌షాట్లు, బ్యాంక్ మెసేజ్‌లు, ట్రాన్సాక్షన్ ఐడీలను సాక్ష్యాలుగా భద్రపరుచుకోండి."
    )
}

# Curated Knowledge Base for all 16 CAVI Topics
KNOWLEDGE_BASE = {
    "otp_fraud": {
        "en": (
            "🛡️ What is OTP Fraud?\n\n"
            "An OTP (One-Time Password) is like a digital key to your bank account. "
            "Scammers call pretending to be bank managers, electricity officers, or delivery agents, "
            "asking you to read out the 4 or 6-digit code sent to your phone.\n\n"
            "Key Safety Rules:\n"
            "• Bank officials, police, or genuine companies NEVER ask for OTP.\n"
            "• Entering or sharing an OTP is strictly for DEBITING (withdrawing) money from your account.\n"
            "• Never read out or forward an OTP to anyone.\n"
            "• If you suspect fraud, call 📞 1930 immediately."
        ),
        "te": (
            "🛡️ OTP మోసం అంటే ఏమిటి?\n\n"
            "ఓటీపీ (One-Time Password) అనేది మీ బ్యాంకు ఖాతాకు ఒక తాళం చెవి లాంటిది. "
            "స్కామర్లు బ్యాంకు మేనేజర్లుగా, కరెంట్ బిల్లు ఆఫీసర్లుగా లేదా కొరియర్ డెలివరీ బాయ్‌లుగా నటించి, "
            "మీ ఫోన్‌కు వచ్చిన 4 లేదా 6 అంకెల నంబర్‌ను చెప్పమని అడుగుతారు.\n\n"
            "ముఖ్యమైన రక్షణ సూత్రాలు:\n"
            "• బ్యాంక్ అధికారులు, పోలీసులు ఎప్పుడూ మీ OTP అడగరు.\n"
            "• OTP ఎంటర్ చేస్తే మీ ఖాతా నుండి డబ్బులు కట్ అవుతాయి తప్ప, మీకు డబ్బులు రావు.\n"
            "• ఎవరికీ మీ OTP ని ఫోన్‌లో చెప్పకండి లేదా మెసేజ్ చేయకండి.\n"
            "• ఏదైనా అనుమానం ఉంటే వెంటనే 📞 1930 కు కాల్ చేయండి."
        )
    },
    "upi_safety": {
        "en": (
            "🛡️ UPI & PIN Safety Guide:\n\n"
            "• UPI PIN is ONLY entered to SEND money, never to RECEIVE money.\n"
            "• Scanning a QR code or entering your PIN will IMMEDIATELY debit money from your bank.\n"
            "• If someone says: 'Enter PIN to accept Rs. 10,000 lottery/scholarship', it is 100% a SCAM!\n"
            "• Never approve 'Collect' or 'Payment Requests' from unknown persons on PhonePe, Google Pay, or Paytm.\n"
            "• If scammed, call 📞 1930 immediately to freeze the payment."
        ),
        "te": (
            "🛡️ యూపీఐ (UPI) & పిన్ రక్షణ సూత్రాలు:\n\n"
            "• గుర్తుంచుకోండి: మీ ఖాతా నుండి డబ్బులు ఇతరులకు పంపేటప్పుడు మాత్రమే UPI PIN ఎంటర్ చేయాలి.\n"
            "• మీకు ఎవరైనా డబ్బులు పంపుతుంటే, మీరు ఎలాంటి PIN ఎంటర్ చేయనవసరం లేదు.\n"
            "• QR కోడ్ స్కాన్ చేసినా లేదా PIN ఎంటర్ చేసినా మీ ఖాతా ఖాళీ అవుతుంది.\n"
            "• ఫోన్‌పే, గూగుల్‌పే లో గుర్తుతెలియని వ్యక్తులు పంపే 'Collect Request' లను ఎప్పుడూ ఆమోదించకండి.\n"
            "• మోసం జరిగితే ఆలస్యం చేయకుండా 📞 1930 కు కాల్ చేయండి."
        )
    },
    "kyc_fraud": {
        "en": (
            "🛡️ Fake KYC / Bank Verification Scams:\n\n"
            "Scammers send SMS messages claiming: 'Your Bank Account / SIM card will be blocked within 24 hours. Update KYC immediately by clicking this link.'\n\n"
            "How to stay safe:\n"
            "• Banks NEVER block accounts via random SMS or WhatsApp links.\n"
            "• Never click on links in SMS to update KYC or Aadhaar.\n"
            "• Always visit your local bank branch directly in your village or town for KYC updates.\n"
            "• Never download any app sent by someone claiming to be customer care."
        ),
        "te": (
            "🛡️ నకిలీ కేవైసీ (KYC) మోసాలు:\n\n"
            "స్కామర్లు 'మీ బ్యాంక్ ఖాతా లేదా సిమ్ కార్డు 24 గంటల్లో బ్లాక్ చేయబడుతుంది. వెంటనే ఈ లింక్ క్లిక్ చేసి KYC అప్‌డేట్ చేయండి' అని భయపెట్టే మెసేజ్‌లు పంపుతారు.\n\n"
            "రక్షణ సూత్రాలు:\n"
            "• బ్యాంకులు ఎప్పుడూ వాట్సాప్ లేదా ఎస్ఎంఎస్ లింకుల ద్వారా ఖాతాలను బ్లాక్ చేయవు.\n"
            "• ఎస్ఎంఎస్‌లోని అనుమానాస్పద లింకులను అస్సలు క్లిక్ చేయకండి.\n"
            "• KYC అప్‌డేట్ కోసం ఎల్లప్పుడూ మీ ఊరిలోని లేదా దగ్గర్లోని బ్యాంకు బ్రాంచ్‌కు స్వయంగా వెళ్లండి.\n"
            "• కస్టమర్ కేర్ పేరుతో వచ్చే గుర్తుతెలియని యాప్‌లను ఎప్పుడూ ఇన్‌స్టాల్ చేయకండి."
        )
    },
    "prize_scam": {
        "en": (
            "🛡️ Lottery, Prize & Subsidy Scams:\n\n"
            "If you receive a message saying: 'Congratulations! You won Rs. 25 Lakhs / a new Car / Government subsidy. Pay Rs. 2,000 registration fee to claim', it is a FRAUD!\n\n"
            "Remember:\n"
            "• You cannot win a lottery or prize for a contest you never entered.\n"
            "• Genuine winners NEVER have to pay 'processing fees', 'tax', or 'registration fees' in advance.\n"
            "• Never send money or share bank details for prize claims."
        ),
        "te": (
            "🛡️ బహుమతి & లాటరీ మోసాలు:\n\n"
            "'అభినందనలు! మీకు రూ. 25 లక్షల లాటరీ / కొత్త కారు / ప్రభుత్వ సబ్సిడీ వచ్చింది. బహుమతి అందుకోవడానికి రూ. 2,000 ప్రాసెసింగ్ ఫీజు చెల్లించండి' అని వచ్చే మెసేజ్‌లు 100% నకిలీవి!\n\n"
            "ముఖ్య సూత్రాలు:\n"
            "• మీరు పాల్గొనని పోటీలో లేదా కొనని లాటరీలో మీకు బహుమతి రాదు.\n"
            "• నిజమైన బహుమతులకు ముందస్తుగా 'రిజిస్ట్రేషన్ ఫీజు' లేదా 'పన్ను' కట్టమని ఎవరూ అడగరు.\n"
            "• బహుమతి ఆశతో ఎవరికీ డబ్బులు పంపకండి."
        )
    },
    "screen_sharing": {
        "en": (
            "🛡️ Screen-Sharing App Scams (AnyDesk, TeamViewer, RustDesk):\n\n"
            "Scammers ask you to install apps like AnyDesk, TeamViewer, QuickSupport, or RustDesk under the pretext of fixing your phone or helping you with banking.\n\n"
            "Danger:\n"
            "• These apps allow the scammer to see your phone screen in real time from anywhere.\n"
            "• They can see your OTPs, passwords, and banking apps while you type.\n"
            "• NEVER install screen-sharing apps on the advice of an unknown caller.\n"
            "• If already installed, immediately turn off mobile data/Wi-Fi and uninstall the app!"
        ),
        "te": (
            "🛡️ స్క్రీన్ షేరింగ్ యాప్ మోసాలు (AnyDesk, TeamViewer):\n\n"
            "కరెంట్ బిల్లు సమస్య లేదా బ్యాంక్ సమస్యను పరిష్కరిస్తామని చెప్పి AnyDesk, TeamViewer, QuickSupport వంటి యాప్‌లను ఇన్‌స్టాల్ చేయమని మోసగాళ్లు చెబుతారు.\n\n"
            "ప్రమాదం ఏమిటి?\n"
            "• ఈ యాప్‌లు మీ ఫోన్ స్క్రీన్‌ను మోసగాళ్లకు పూర్తిగా చూపించేస్తాయి.\n"
            "• మీ ఫోన్‌కు వచ్చే OTPలు, మీ బ్యాంక్ పిన్ నంబర్లను వారు లైవ్‌గా చూసి మీ ఖాతాలోని డబ్బులు దొంగిలిస్తారు.\n"
            "• ఎవరి మాటా విని ఇలాంటి స్క్రీన్ షేరింగ్ యాప్‌లను మీ మొబైల్‌లో ఎక్కించకండి.\n"
            "• పొరపాటున ఇన్‌స్టాల్ చేస్తే వెంటనే ఇంటర్నెట్ ఆపివేసి ఆ యాప్‌ను డిలీట్ చేయండి."
        )
    },
    "suspicious_link": {
        "en": (
            "🛡️ Suspicious Link & Phishing Analysis:\n\n"
            "Common warning signs of a scam message:\n"
            "1. Urgency: 'Do this immediately within 1 hour or account suspended.'\n"
            "2. Unrealistic offers: Free recharges, lottery winnings, easy work-from-home money.\n"
            "3. Strange web addresses: Fake links often look like 'sbi-update-kyc.top' instead of official domains like 'sbi.co.in'.\n"
            "4. APK downloads: Links ending in '.apk' install dangerous spyware.\n\n"
            "Rule: When in doubt, DELETE the message and DO NOT click the link."
        ),
        "te": (
            "🛡️ అనుమానాస్పద లింకుల గుర్తింపు సూత్రాలు:\n\n"
            "మోసపూరిత మెసేజ్‌లను ఇలా గుర్తించండి:\n"
            "1. తొందరపెట్టడం: 'వెంటనే 1 గంటలో చేయకపోతే మీ అకౌంట్ బంద్ అవుతుంది' అని భయపెట్టడం.\n"
            "2. ఆశ చూపించడం: ఉచిత రీఛార్జ్, ప్రభుత్వం ఉచితంగా డబ్బులు పంచుతోందనే ప్రచారం.\n"
            "3. వింతైన వెబ్‌సైట్ పేర్లు: బ్యాంక్ పేరుతో మొదలయ్యే నకిలీ లింకులు.\n"
            "4. .apk ఫైల్స్: యాప్‌లను డౌన్‌లోడ్ చేయమనే లింకులు ప్రమాదకరమైన వైరస్‌లను ఇన్‌స్టాల్ చేస్తాయి.\n\n"
            "సూత్రం: అనుమానం ఉంటే ఆ మెసేజ్‌ను వెంటనే డిలీట్ చేయండి. లింక్‌ను ఎప్పుడూ తెరవకండి."
        )
    },
    "general_safety": {
        "en": (
            "🛡️ CAVI 5 Golden Rules for Online Safety:\n\n"
            "1. NEVER share OTP, UPI PIN, or passwords with anyone.\n"
            "2. UPI PIN is only for sending money, NEVER for receiving money.\n"
            "3. Do not click random links in SMS, WhatsApp, or Facebook.\n"
            "4. Never install screen-sharing apps (AnyDesk, QuickSupport) on callers' instructions.\n"
            "5. If scammed, dial 📞 1930 immediately within the Golden Hour (2-3 hours)!"
        ),
        "te": (
            "🛡️ CAVI 5 సువర్ణ భద్రతా సూత్రాలు:\n\n"
            "1. మీ OTP, UPI PIN, పాస్‌వర్డ్‌లను ఎవరితోనూ పంచుకోవద్దు.\n"
            "2. UPI PIN కేవలం డబ్బు పంపడానికే, డబ్బు అందుకోవడానికి PIN అవసరం లేదు.\n"
            "3. వాట్సాప్ లేదా ఎస్ఎంఎస్ లలో వచ్చే గుర్తుతెలియని లింకులను క్లిక్ చేయకండి.\n"
            "4. ఇతరుల మాటలు నమ్మి AnyDesk లాంటి స్క్రీన్ షేరింగ్ యాప్‌లను డౌన్‌లోడ్ చేయకండి.\n"
            "5. మోసం జరిగితే మొదటి 2-3 గంటల్లోనే 📞 1930 కు కాల్ చేయండి!"
        )
    }
}
