"""
CAVI - Cyber Aware Village Initiative
Awareness Videos Data Registry with Fraud-Type and Language Filtering,
Official Government Sources (I4C, RBI Kehta Hai, CyberDost),
and "3 Things to Remember" Educational Summaries.
"""

OFFICIAL_GOV_VIDEO_PORTAL = "https://cybercrime.gov.in/Webform/CyberAware.aspx"
RBI_KEHTA_HAI_PORTAL = "https://rbikehtahai.rbi.org.in/"

VIDEO_CATEGORIES = [
    "All",
    "OTP Fraud",
    "UPI Fraud",
    "KYC Fraud",
    "Digital Arrest",
    "Investment Scam",
    "Fake Refund",
    "Vishing",
    "E-Wallet Fraud",
    "AEPS Fraud",
    "Malware",
    "Online Job Fraud",
    "Loan Fraud",
    "Screen Sharing",
    "Fake Customer Care"
]

VIDEOS_REGISTRY = [
    {
        "id": "vid_otp_01",
        "category": "OTP Fraud",
        "title": {
            "te": "ఓటీపీ ఎవరితోనూ పంచుకోవద్దు - సురక్షిత బ్యాంకింగ్",
            "en": "Never Share OTP - RBI Kehta Hai Official Awareness",
            "hi": "ओटीपी किसी के साथ साझा न करें - आरबीआई कहता है"
        },
        "description": {
            "te": "బ్యాంకు పేరుతో మోసపూరిత కాల్స్ వస్తే ఓటీపీని ఎందుకు ఎవరికీ చెప్పకూడదో వివరించే అధికారిక అవగాహన వీడియో.",
            "en": "Official public awareness video highlighting why no financial institution ever requests OTP over telephone.",
            "hi": "आरबीआई की आधिकारिक जागरूकता: बैंक कभी भी फोन पर आपसे ओटीपी नहीं मांगते। सतर्क रहें।"
        },
        "source": "RBI Kehta Hai / I4C Official",
        "language": "తెలుగు / English / हिंदी",
        "duration": "1:30 Min",
        "embed_url": "https://www.youtube.com/embed/Z1BCZXw41mU", # RBI official awareness video on cyber safety
        "has_embed": True,
        "official_source_url": "https://rbikehtahai.rbi.org.in/",
        "three_things_to_remember": {
            "te": [
                "బ్యాంక్ అధికారులు ఎప్పుడూ మీ ఓటీపీ అడగరు.",
                "ఓటీపీని ఎవరితోనూ ఫోన్‌లో లేదా మెసేజ్‌లో పంచుకోవద్దు.",
                "సందేహం వస్తే వెంటనే మీ బ్యాంకుకు లేదా 1930 కి ఫోన్ చేయండి."
            ],
            "en": [
                "Bank officials NEVER ask for your confidential OTP.",
                "Do not share OTP over phone, WhatsApp, or email.",
                "Report suspicious calls immediately to your bank and 1930."
            ],
            "hi": [
                "बैंक अधिकारी कभी आपका गोपनीय OTP नहीं मांगते।",
                "फोन या मैसेज पर किसी को भी OTP न बताएं।",
                "शक होने पर तुरंत बैंक और 1930 पर सूचना दें।"
            ]
        }
    },
    {
        "id": "vid_upi_02",
        "category": "UPI Fraud",
        "title": {
            "te": "డబ్బులు రావడానికి యూపీఐ పిన్ అవసరం లేదు!",
            "en": "UPI PIN is Only for Sending Money - CyberDost / NPCI",
            "hi": "पैसे पाने के लिए UPI PIN की जरूरत नहीं - साइबर दोस्त"
        },
        "description": {
            "te": "క్యూఆర్ కోడ్ స్కాన్ చేసి లేదా పిన్ కొట్టి డబ్బులు రిసీవ్ చేసుకోవాలనే మోసాల నుండి ఎలా కాపాడుకోవాలో తెలిపే వీడియో.",
            "en": "Demonstration on how fraudsters trick citizens into scanning QR codes and entering PINs to 'receive' money.",
            "hi": "पैसे पाने के लिए क्यूआर कोड स्कैन करने या यूपीआई पिन डालने के झांसे से बचने की मार्गदर्शिका।"
        },
        "source": "NPCI / CyberDost Official",
        "language": "తెలుగు / English / हिंदी",
        "duration": "2:00 Min",
        "embed_url": "https://www.youtube.com/embed/n423hX-wKz4", # Official NPCI UPI Safety video
        "has_embed": True,
        "official_source_url": "https://cybercrime.gov.in/Webform/CyberAware.aspx",
        "three_things_to_remember": {
            "te": [
                "యూపీఐ పిన్ కేవలం డబ్బులు పంపడానికి (Send) మాత్రమే.",
                "డబ్బులు మీ ఖాతాలోకి రావడానికి (Receive) పిన్ అవసరం లేదు.",
                "క్యూఆర్ కోడ్ స్కాన్ చేసి ఎప్పుడూ పిన్ కొట్టవద్దు."
            ],
            "en": [
                "UPI PIN is used STRICTLY to send money out.",
                "You NEVER enter a PIN to receive or claim money.",
                "Never scan a stranger's QR code to accept payment."
            ],
            "hi": [
                "UPI PIN का प्रयोग सिर्फ पैसे भेजने के लिए होता है।",
                "पैसे खाते में आने के लिए कभी भी पिन नहीं डाला जाता।",
                "पैसे लेने के लिए किसी का QR कोड स्कैन न करें।"
            ]
        }
    },
    {
        "id": "vid_kyc_03",
        "category": "KYC Fraud",
        "title": {
            "te": "నకిలీ కేవైసీ మెసేజ్ లతో జాగ్రత్త - బ్యాంక్ అలర్ట్",
            "en": "Beware of Fake KYC Expiry Links - Bank Safety Alert",
            "hi": "फर्जी केवाईसी अपडेट मैसेज से रहें सावधान"
        },
        "description": {
            "te": "బ్యాంక్ ఖాతా ఆగిపోతుందని ఎస్ఎంఎస్ పంపి నకిలీ లింకుల ద్వారా మోసం చేసే విధానంపై అవగాహన.",
            "en": "How cybercriminals use fake bank suspension SMS alerts to phish netbanking credentials.",
            "hi": "बैंक खाता बंद होने का डर दिखाकर फर्जी लिंक से ठगी करने के तरीके पर जागरूकता।"
        },
        "source": "Indian Cyber Crime Coordination Centre (I4C)",
        "language": "తెలుగు / English",
        "duration": "1:45 Min",
        "embed_url": "", # Placeholder configured cleanly
        "has_embed": False,
        "placeholder_note": "అధికారిక వీడియో పోర్టల్ ద్వారా అందుబాటులో ఉంటుంది / Available via Official Portal",
        "official_source_url": "https://cybercrime.gov.in/Webform/CyberAware.aspx",
        "three_things_to_remember": {
            "te": [
                "ఎస్ఎంఎస్‌లోని కేవైసీ లింకులను ఎప్పుడూ నొక్కకండి.",
                "కేవైసీ అప్‌డేట్ కోసం మీ స్వంత బ్యాంక్ బ్రాంచ్‌ను మాత్రమే సంప్రదించండి.",
                "మీ ఆధార్, పాన్ కార్డు వివరాలను అపరిచిత వెబ్‌సైట్లలో ఎంటర్ చేయవద్దు."
            ],
            "en": [
                "Never click on KYC update links received in text messages.",
                "Visit your physical bank branch for all document updates.",
                "Never enter banking credentials on unverified websites."
            ],
            "hi": [
                "SMS में आए किसी भी KYC लिंक पर कभी क्लिक न करें।",
                "केवाईसी अपडेट हमेशा अपनी बैंक शाखा में जाकर ही करवाएं।",
                "अज्ञात वेबसाइटों पर अपने दस्तावेज या बैंक विवरण न भरें।"
            ]
        }
    },
    {
        "id": "vid_digital_arrest_04",
        "category": "Digital Arrest",
        "title": {
            "te": "డిజిటల్ అరెస్ట్ మోసం - కేంద్ర హోం మంత్రిత్వ శాఖ హెచ్చరిక",
            "en": "Digital Arrest Scam Warning - Ministry of Home Affairs / I4C",
            "hi": "डिजिटल अरेस्ट धोखाधड़ी - गृह मंत्रालय की चेतावनी"
        },
        "description": {
            "te": "పోలీసులు లేదా సీబీఐ అధికారులమని వీడియో కాల్స్ చేసి బెదిరించే నకిలీ ముఠాల నుండి ఎలా అప్రమత్తంగా ఉండాలో తెలిపే వీడియో.",
            "en": "Detailed warning against fraudsters posing as police or customs officials extorting citizens over video calls.",
            "hi": "पुलिस या सीबीआई अधिकारी बनकर वीडियो कॉल पर डराने वाले गिरोह से सावधान रहने हेतु विशेष वीडियो।"
        },
        "source": "Ministry of Home Affairs (MHA / I4C)",
        "language": "తెలుగు / English / हिंदी",
        "duration": "2:30 Min",
        "embed_url": "",
        "has_embed": False,
        "placeholder_note": "కేంద్ర సైబర్ భద్రతా విభాగం అధికారిక వీడియో / Official MHA Awareness Resource",
        "official_source_url": "https://cybercrime.gov.in/Webform/CyberAware.aspx",
        "three_things_to_remember": {
            "te": [
                "చట్టంలో డిజిటల్ అరెస్ట్ అనే నిబంధనే లేదు.",
                "పోలీసులు ఎప్పుడూ వీడియో కాల్‌లో డబ్బులు అడగరు.",
                "భయపడకుండా వెంటనే కాల్ కట్ చేసి 1930 కి ఫోన్ చేయండి."
            ],
            "en": [
                "There is no concept of 'Digital Arrest' in Indian law.",
                "Law enforcement never demands money transfers on video calls.",
                "Do not panic; hang up immediately and dial 1930."
            ],
            "hi": [
                "भारतीय कानून में डिजिटल अरेस्ट का कोई प्रावधान नहीं है।",
                "पुलिस कभी वीडियो कॉल पर पैसे की मांग नहीं करती।",
                "घबराएं नहीं, तुरंत कॉल काटें और 1930 पर संपर्क करें।"
            ]
        }
    },
    {
        "id": "vid_screenshare_05",
        "category": "Screen Sharing",
        "title": {
            "te": "స్క్రీన్ షేరింగ్ యాప్స్ ప్రమాదం - మొబైల్ భద్రత",
            "en": "Dangers of Remote Screen Sharing Apps - AnyDesk & QuickSupport",
            "hi": "स्क्रीन शेयरिंग ऐप का खतरा - मोबाइल सुरक्षा"
        },
        "description": {
            "te": "అపరిచితుల మాట విని AnyDesk వంటి యాప్‌లు ఇన్‌స్టాల్ చేస్తే ఫోన్ ఎలా హ్యాక్ అవుతుందో వివరించే పాఠం.",
            "en": "How remote access applications compromise smartphone security and expose bank balances to callers.",
            "hi": "अजनबियों के कहने पर AnyDesk या QuickSupport ऐप इंस्टॉल करने से फोन कैसे हैक होता है।"
        },
        "source": "CyberDost / State Police Cyber Cell",
        "language": "తెలుగు / English",
        "duration": "1:50 Min",
        "embed_url": "",
        "has_embed": False,
        "placeholder_note": "సైబర్ దోస్త్ అధికారిక మార్గదర్శకాలు / CyberDost Guidelines",
        "official_source_url": "https://cybercrime.gov.in/Webform/CyberAware.aspx",
        "three_things_to_remember": {
            "te": [
                "అపరిచితులు చెప్పే ఏ యాప్‌నూ ఫోన్‌లో ఎక్కించవద్దు.",
                "స్క్రీన్ పై వచ్చే 9 అంకెల కోడ్‌ను ఎవరికీ చెప్పవద్దు.",
                "ఫోన్ లో ఉండే రహస్య పాస్‌వర్డ్‌లను ఎవరికీ చూపించవద్దు."
            ],
            "en": [
                "Never install unknown apps on telephone caller requests.",
                "Never disclose screen connection codes generated by remote apps.",
                "Keep banking passwords and credentials private."
            ],
            "hi": [
                "कॉलर के कहने पर कभी कोई ऐप फोन में इंस्टॉल न करें।",
                "स्क्रीन पर आने वाला 9 अंकों का कोड किसी को न बताएं।",
                "अपने फोन का पासवर्ड किसी के सामने न खोलें।"
            ]
        }
    },
    {
        "id": "vid_loan_06",
        "category": "Loan Fraud",
        "title": {
            "te": "నకిలీ లోన్ యాప్‌ల బ్లాక్‌మెయిలింగ్ నుండి రక్షణ",
            "en": "Protection Against Illegal Loan Apps & Extortion",
            "hi": "फर्जी लोन ऐप्स और ब्लैकमेलिंग से बचाव"
        },
        "description": {
            "te": "క్షణాల్లో లోన్ ఇస్తామని చెప్పి ఫోటోలు మార్చి వేధించే నకిలీ చట్టవిరుద్ధ యాప్‌ల మోసాలను ఎలా ఎదుర్కోవాలో మార్గదర్శనం.",
            "en": "Legal guidance on tackling aggressive extortion from unregulated instant mobile loan applications.",
            "hi": "आसान लोन देने वाले अवैध ऐप्स द्वारा फोटो से छेड़छाड़ और ब्लैकमेलिंग से बचने के उपाय।"
        },
        "source": "Reserve Bank of India (RBI) / I4C",
        "language": "తెలుగు / English / हिंदी",
        "duration": "2:15 Min",
        "embed_url": "",
        "has_embed": False,
        "placeholder_note": "ఆర్బీఐ అవగాహన వీడియో / RBI Awareness Portal",
        "official_source_url": "https://cybercrime.gov.in/Webform/CyberAware.aspx",
        "three_things_to_remember": {
            "te": [
                "అనధికారిక లోన్ యాప్స్ మీ ఫోన్ ఫోటోలు, కాంటాక్ట్‌లను దొంగిలిస్తాయి.",
                "బ్లాక్‌మెయిల్ చేస్తే భయపడి డబ్బులు కట్టకండి.",
                "వెంటనే 1930 కు లేదా స్థానిక పోలీసులకు ఫిర్యాదు చేయండి."
            ],
            "en": [
                "Illegal loan apps harvest personal photos and contact lists.",
                "Never pay extortion money out of fear or shame.",
                "Report immediately to 1930 and state cyber cell."
            ],
            "hi": [
                "अवैध लोन ऐप्स आपकी फोटो और कॉन्टैक्ट्स चुरा लेते हैं।",
                "डरकर किसी को भी जबरन वसूली के पैसे न दें।",
                "तुरंत 1930 या नजदीकी पुलिस थाने में शिकायत दर्ज कराएं।"
            ]
        }
    }
]

def get_all_videos():
    return VIDEOS_REGISTRY

def filter_videos(category: str = "All"):
    if category == "All" or not category:
        return VIDEOS_REGISTRY
    return [v for v in VIDEOS_REGISTRY if v["category"] == category]
