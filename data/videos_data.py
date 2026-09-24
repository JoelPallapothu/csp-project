"""
CAVI - Cyber Aware Village Initiative
Awareness Videos Data Registry with Fraud-Type and Language Filtering,
Official Government Sources (I4C, RBI Kehta Hai, CyberDost),
and "3 Things to Remember" + "Safety Tip" Educational Summaries.
Bilingual: Telugu (Default) and English.
"""

OFFICIAL_GOV_VIDEO_PORTAL = "https://cybercrime.gov.in/Webform/CyberAware.aspx"
RBI_KEHTA_HAI_PORTAL = "https://rbikehtahai.rbi.org.in/"

VIDEO_CATEGORIES = [
    "All",
    "OTP",
    "UPI",
    "KYC",
    "Digital Arrest",
    "Investment Scam",
    "Fake Refund",
    "Vishing",
    "E-Wallet",
    "AEPS",
    "Malware",
    "Online Job",
    "Loan Fraud",
    "Screen Sharing",
    "Fake Customer Care"
]

VIDEOS_REGISTRY = [
    {
        "id": "vid_otp_01",
        "category": "OTP",
        "title": {
            "te": "ఓటీపీ ఎవరితోనూ పంచుకోవద్దు - సురక్షిత బ్యాంకింగ్",
            "en": "Never Share OTP - RBI Kehta Hai Official Awareness"
        },
        "description": {
            "te": "బ్యాంకు పేరుతో మోసపూరిత కాల్స్ వస్తే ఓటీపీని ఎందుకు ఎవరికీ చెప్పకూడదో వివరించే అధికారిక అవగాహన వీడియో.",
            "en": "Official public awareness video highlighting why no financial institution ever requests OTP over telephone."
        },
        "source": "RBI Kehta Hai / I4C Official",
        "language": "తెలుగు / English",
        "duration": "1:30 Min",
        "embed_url": "https://www.youtube.com/embed/Z1BCZXw41mU",
        "has_embed": True,
        "official_source_url": "https://rbikehtahai.rbi.org.in/",
        "safety_tip": {
            "te": "🛡️ భద్రతా సూత్రం: బ్యాంక్ మేనేజర్ లేదా పోలీస్ అధికారి అయినా సరే ఫోన్‌లో ఓటీపీ అడిగితే కాల్ వెంటనే కట్ చేయండి.",
            "en": "🛡️ Safety Tip: Hang up immediately if anyone, even claiming to be police or bank manager, asks for your OTP."
        },
        "three_things_to_remember": {
            "te": [
                "1. ఎట్టి పరిస్థితుల్లోనూ ఓటీపీ లేదా పిన్ ఎవరితోనూ పంచుకోవద్దు.",
                "2. చెల్లింపులు లేదా వివరాలు ఇచ్చేముందు ఎల్లప్పుడూ నేరుగా ధృవీకరించుకోండి.",
                "3. అనుమానాస్పద కార్యకలాపాలు జరిగితే వెంటనే 1930 కు రిపోర్ట్ చేయండి."
            ],
            "en": [
                "1. Never share OTP or PIN with anyone under any circumstance.",
                "2. Always verify credentials before transferring any money or details.",
                "3. Report suspicious activity immediately to Helpline 1930."
            ]
        }
    },
    {
        "id": "vid_upi_02",
        "category": "UPI",
        "title": {
            "te": "డబ్బులు రావడానికి యూపీఐ పిన్ అవసరం లేదు!",
            "en": "UPI PIN is Only for Sending Money - CyberDost / NPCI"
        },
        "description": {
            "te": "క్యూఆర్ కోడ్ స్కాన్ చేసి లేదా పిన్ కొట్టి డబ్బులు రిసీవ్ చేసుకోవాలనే మోసాల నుండి ఎలా కాపాడుకోవాలో తెలిపే వీడియో.",
            "en": "Demonstration on how fraudsters trick citizens into scanning QR codes and entering PINs to 'receive' money."
        },
        "source": "NPCI / CyberDost Official",
        "language": "తెలుగు / English",
        "duration": "2:00 Min",
        "embed_url": "https://www.youtube.com/embed/n423hX-wKz4",
        "has_embed": True,
        "official_source_url": "https://cybercrime.gov.in/Webform/CyberAware.aspx",
        "safety_tip": {
            "te": "🛡️ భద్రతా సూత్రం: మీ ఖాతాలోకి డబ్బులు రావడానికి (Receive) పిన్ అస్సలు కొట్టకూడదు. పిన్ కొడితే మీ డబ్బులే ఎదుటివారికి వెళ్తాయి.",
            "en": "🛡️ Safety Tip: Never enter UPI PIN to receive money. UPI PIN is solely required to send or deduct money."
        },
        "three_things_to_remember": {
            "te": [
                "1. యూపీఐ పిన్ కేవలం డబ్బులు పంపడానికి (Send) మాత్రమే.",
                "2. డబ్బులు ఖాతాలోకి రావడానికి క్యూఆర్ కోడ్ స్కాన్ చేయకూడదు.",
                "3. గుర్తుతెలియని వ్యక్తుల చెల్లింపు అభ్యర్థనలను (Collect Requests) తిరస్కరించండి."
            ],
            "en": [
                "1. UPI PIN is used strictly to send money out.",
                "2. You never need to scan a QR code to receive payments.",
                "3. Decline unknown collect requests immediately."
            ]
        }
    },
    {
        "id": "vid_kyc_03",
        "category": "KYC",
        "title": {
            "te": "నకిలీ కేవైసీ మెసేజ్ లతో జాగ్రత్త - బ్యాంక్ అలర్ట్",
            "en": "Beware of Fake KYC Expiry Links - Bank Safety Alert"
        },
        "description": {
            "te": "బ్యాంక్ ఖాతా ఆగిపోతుందని ఎస్ఎంఎస్ పంపి నకిలీ లింకుల ద్వారా మోసం చేసే విధానంపై అవగాహన.",
            "en": "How cybercriminals use fake bank suspension SMS alerts to phish netbanking credentials."
        },
        "source": "Indian Cyber Crime Coordination Centre (I4C)",
        "language": "తెలుగు / English",
        "duration": "1:45 Min",
        "embed_url": "",
        "has_embed": False,
        "placeholder_note": "అధికారిక వీడియో పోర్టల్ ద్వారా అందుబాటులో ఉంటుంది / Available via Official Portal",
        "official_source_url": "https://cybercrime.gov.in/Webform/CyberAware.aspx",
        "safety_tip": {
            "te": "🛡️ భద్రతా సూత్రం: కేవైసీ అప్‌డేట్ కోసం ఎస్ఎంఎస్ లింకులను నొక్కకండి. మీ సొంత బ్యాంక్ బ్రాంచ్‌ను మాత్రమే సంప్రదించండి.",
            "en": "🛡️ Safety Tip: Never click on KYC update links in text messages. Visit your local bank branch directly."
        },
        "three_things_to_remember": {
            "te": [
                "1. ఎస్ఎంఎస్‌లోని కేవైసీ లింకులను ఎప్పుడూ నొక్కకండి.",
                "2. కేవైసీ కోసం మీ స్వంత బ్యాంక్ బ్రాంచ్‌ను మాత్రమే సంప్రదించండి.",
                "3. మీ ఆధార్, పాన్ కార్డు వివరాలను అపరిచిత వెబ్‌సైట్లలో ఎంటర్ చేయవద్దు."
            ],
            "en": [
                "1. Never click on KYC update links received in text messages.",
                "2. Visit your physical bank branch for all document updates.",
                "3. Never enter banking credentials on unverified websites."
            ]
        }
    },
    {
        "id": "vid_digital_arrest_04",
        "category": "Digital Arrest",
        "title": {
            "te": "డిజిటల్ అరెస్ట్ మోసం - కేంద్ర హోం మంత్రిత్వ శాఖ హెచ్చరిక",
            "en": "Digital Arrest Scam Warning - Ministry of Home Affairs / I4C"
        },
        "description": {
            "te": "పోలీసులు లేదా సీబీఐ అధికారులమని వీడియో కాల్స్ చేసి బెదిరించే నకిలీ ముఠాల నుండి ఎలా అప్రమత్తంగా ఉండాలో తెలిపే వీడియో.",
            "en": "Detailed warning against fraudsters posing as police or customs officials extorting citizens over video calls."
        },
        "source": "Ministry of Home Affairs (MHA / I4C)",
        "language": "తెలుగు / English",
        "duration": "2:30 Min",
        "embed_url": "",
        "has_embed": False,
        "placeholder_note": "కేంద్ర సైబర్ భద్రతా విభాగం అధికారిక వీడియో / Official MHA Awareness Resource",
        "official_source_url": "https://cybercrime.gov.in/Webform/CyberAware.aspx",
        "safety_tip": {
            "te": "🛡️ భద్రతా సూత్రం: భారతీయ చట్టంలో 'డిజిటల్ అరెస్ట్' అనేదే లేదు. పోలీసులు వీడియో కాల్‌లో బెదిరిస్తే వెంటనే కాల్ కట్ చేసి 1930 కి ఫోన్ చేయండి.",
            "en": "🛡️ Safety Tip: Indian law has NO provision for 'Digital Arrest'. Real police never demand money transfers over video calls."
        },
        "three_things_to_remember": {
            "te": [
                "1. చట్టంలో డిజిటల్ అరెస్ట్ అనే నిబంధనే లేదు.",
                "2. పోలీసులు ఎప్పుడూ వీడియో కాల్‌లో డబ్బులు అడగరు.",
                "3. భయపడకుండా వెంటనే కాల్ కట్ చేసి 1930 కి ఫోన్ చేయండి."
            ],
            "en": [
                "1. There is no concept of 'Digital Arrest' in Indian law.",
                "2. Law enforcement never demands money transfers on video calls.",
                "3. Do not panic; hang up immediately and dial 1930."
            ]
        }
    },
    {
        "id": "vid_screenshare_05",
        "category": "Screen Sharing",
        "title": {
            "te": "స్క్రీన్ షేరింగ్ యాప్స్ ప్రమాదం - మొబైల్ భద్రత",
            "en": "Dangers of Remote Screen Sharing Apps - AnyDesk & QuickSupport"
        },
        "description": {
            "te": "అపరిచితుల మాట విని AnyDesk వంటి యాప్‌లు ఇన్‌స్టాల్ చేస్తే ఫోన్ ఎలా హ్యాక్ అవుతుందో వివరించే పాఠం.",
            "en": "How remote access applications compromise smartphone security and expose bank balances to callers."
        },
        "source": "CyberDost / State Police Cyber Cell",
        "language": "తెలుగు / English",
        "duration": "1:50 Min",
        "embed_url": "",
        "has_embed": False,
        "placeholder_note": "సైబర్ దోస్త్ అధికారిక మార్గదర్శకాలు / CyberDost Guidelines",
        "official_source_url": "https://cybercrime.gov.in/Webform/CyberAware.aspx",
        "safety_tip": {
            "te": "🛡️ భద్రతా సూత్రం: ఎవరి ఆదేశాల మేరకూ AnyDesk లేదా QuickSupport యాప్‌లను ఫోన్‌లో వేయవద్దు, స్క్రీన్ కోడ్ చెప్పవద్దు.",
            "en": "🛡️ Safety Tip: Never install remote desktop applications on an unverified caller's instructions."
        },
        "three_things_to_remember": {
            "te": [
                "1. అపరిచితులు చెప్పే ఏ యాప్‌నూ ఫోన్‌లో ఎక్కించవద్దు.",
                "2. స్క్రీన్ పై వచ్చే 9 అంకెల కోడ్‌ను ఎవరికీ చెప్పవద్దు.",
                "3. ఫోన్ లో ఉండే రహస్య పాస్‌వర్డ్‌లను ఎవరికీ చూపించవద్దు."
            ],
            "en": [
                "1. Never install unknown apps on telephone caller requests.",
                "2. Never disclose screen connection codes generated by remote apps.",
                "3. Keep banking passwords and credentials private."
            ]
        }
    },
    {
        "id": "vid_loan_06",
        "category": "Loan Fraud",
        "title": {
            "te": "నకిలీ లోన్ యాప్‌ల బ్లాక్‌మెయిలింగ్ నుండి రక్షణ",
            "en": "Protection Against Illegal Loan Apps & Extortion"
        },
        "description": {
            "te": "క్షణాల్లో లోన్ ఇస్తామని చెప్పి ఫోటోలు మార్చి వేధించే నకిలీ చట్టవిరుద్ధ యాప్‌ల మోసాలను ఎలా ఎదుర్కోవాలో మార్గదర్శనం.",
            "en": "Legal guidance on tackling aggressive extortion from unregulated instant mobile loan applications."
        },
        "source": "Reserve Bank of India (RBI) / I4C",
        "language": "తెలుగు / English",
        "duration": "2:15 Min",
        "embed_url": "",
        "has_embed": False,
        "placeholder_note": "ఆర్బీఐ అవగాహన వీడియో / RBI Awareness Portal",
        "official_source_url": "https://cybercrime.gov.in/Webform/CyberAware.aspx",
        "safety_tip": {
            "te": "🛡️ భద్రతా సూత్రం: రిజిస్టర్ కాని లోన్ యాప్‌లను ఫోన్‌లో ఎక్కించకండి. బ్లాక్‌మెయిల్ చేస్తే భయపడకుండా 1930 కి ఫిర్యాదు చేయండి.",
            "en": "🛡️ Safety Tip: Never download unregulated loan apps. Report extortion immediately to 1930 without paying any blackmail money."
        },
        "three_things_to_remember": {
            "te": [
                "1. అనధికారిక లోన్ యాప్స్ మీ ఫోన్ ఫోటోలు, కాంటాక్ట్‌లను దొంగిలిస్తాయి.",
                "2. బ్లాక్‌మెయిల్ చేస్తే భయపడి డబ్బులు కట్టకండి.",
                "3. వెంటనే 1930 కు లేదా స్థానిక పోలీసులకు ఫిర్యాదు చేయండి."
            ],
            "en": [
                "1. Illegal loan apps harvest personal photos and contact lists.",
                "2. Never pay extortion money out of fear or shame.",
                "3. Report immediately to 1930 and state cyber cell."
            ]
        }
    },
    {
        "id": "vid_invest_07",
        "category": "Investment Scam",
        "title": {
            "te": "నకిలీ పెట్టుబడి మోసాలు - అధిక లాభాల ఉచ్చు",
            "en": "Fake Investment & High Return Schemes - SEBI / CyberDost Alert"
        },
        "description": {
            "te": "వారం రోజుల్లో రెట్టింపు డబ్బులు లేదా రోజువారీ లాభాలు ఇస్తామని వాట్సాప్ మరియు టెలిగ్రామ్‌లలో జరిగే భారీ పెట్టుబడి మోసాలపై అవగాహన.",
            "en": "Awareness on fraudulent WhatsApp/Telegram stock tips and high-return guarantee schemes."
        },
        "source": "SEBI / CyberDost Official",
        "language": "తెలుగు / English",
        "duration": "2:05 Min",
        "embed_url": "",
        "has_embed": False,
        "placeholder_note": "సెబీ మరియు సైబర్ దోస్త్ అధికారిక హెచ్చరిక / SEBI Cyber Alert",
        "official_source_url": "https://cybercrime.gov.in/Webform/CyberAware.aspx",
        "safety_tip": {
            "te": "🛡️ భద్రతా సూత్రం: ఎలాంటి నష్టం లేకుండా రెట్టింపు లాభాలు ఇచ్చే పథకాలు ఉండవు. గుర్తుతెలియని వ్యక్తుల అకౌంట్లకు డబ్బులు డిపాజిట్ చేయకండి.",
            "en": "🛡️ Safety Tip: Guaranteed high returns with zero risk is the hallmark of a scam. Never transfer funds to personal UPI handles for 'investments'."
        },
        "three_things_to_remember": {
            "te": [
                "1. రెట్టింపు లాభాల ఆశ చూపే స్కీమ్‌లను నమ్మవద్దు.",
                "2. వాట్సాప్ లేదా టెలిగ్రామ్ గ్రూపులలో పెట్టుబడులు పెట్టవద్దు.",
                "3. సెబీ గుర్తింపు పొందిన సంస్థల ద్వారా మాత్రమే పెట్టుబడి పెట్టండి."
            ],
            "en": [
                "1. Never trust schemes promising guaranteed double returns.",
                "2. Do not invest through WhatsApp or Telegram channels.",
                "3. Verify SEBI registration before investing any money."
            ]
        }
    },
    {
        "id": "vid_job_08",
        "category": "Online Job",
        "title": {
            "te": "నకిలీ పార్ట్‌టైమ్ ఉద్యోగాల మోసం (Like & Subscribe Fraud)",
            "en": "Work-From-Home & YouTube Like Scam Warning"
        },
        "description": {
            "te": "యూట్యూబ్ వీడియోలు లైక్ చేస్తే రోజుకు ₹3,000 వస్తాయని నమ్మించి లక్షల రూపాయలు కాజేసే ముఠాలపై అవగాహన.",
            "en": "How cybercriminals use fake work-from-home tasks to trap unemployed youth and homemakers."
        },
        "source": "I4C National Cyber Cell",
        "language": "తెలుగు / English",
        "duration": "1:55 Min",
        "embed_url": "",
        "has_embed": False,
        "placeholder_note": "కేంద్ర సైబర్ క్రైమ్ విభాగం అవగాహన / I4C Alert",
        "official_source_url": "https://cybercrime.gov.in/Webform/CyberAware.aspx",
        "safety_tip": {
            "te": "🛡️ భద్రతా సూత్రం: ఉద్యోగం ఇవ్వడానికి ముందుగా రిజిస్ట్రేషన్ ఫీజు లేదా టాస్క్ అమౌంట్ అడిగే వారంతా మోసగాళ్లే.",
            "en": "🛡️ Safety Tip: Any job offer demanding an advance fee or security deposit is guaranteed fraud."
        },
        "three_things_to_remember": {
            "te": [
                "1. ఉద్యోగం ఇవ్వడానికి నిజమైన కంపెనీలు ఫీజు అడగవు.",
                "2. ఆన్‌లైన్ టాస్క్‌ల పేరుతో డబ్బులు డిపాజిట్ చేయవద్దు.",
                "3. మొదటి చిన్న లాభాల ఎరతో పెద్ద మొత్తం కాజేస్తారు, జాగ్రత్త."
            ],
            "en": [
                "1. Genuine companies never charge advance fees for jobs.",
                "2. Never deposit money to unlock high-paying tasks.",
                "3. Small initial payouts are bait to steal larger sums."
            ]
        }
    },
    {
        "id": "vid_cust_09",
        "category": "Fake Customer Care",
        "title": {
            "te": "గూగుల్ సెర్చ్ లో నకిలీ కస్టమర్ కేర్ నంబర్ల మోసం",
            "en": "Google Search Helpline Scam - Cyber Safety"
        },
        "description": {
            "te": "గూగుల్‌లో కనిపించే నకిలీ బ్యాంక్ మరియు కొరియర్ హెల్ప్‌లైన్ నంబర్లకు ఫోన్ చేసి మోసపోకుండా ఉండే విధానం.",
            "en": "How scammers replace official helpline numbers on Google maps and search results."
        },
        "source": "State Cyber Police Awareness",
        "language": "తెలుగు / English",
        "duration": "1:40 Min",
        "embed_url": "",
        "has_embed": False,
        "placeholder_note": "అధికారిక హెచ్చరిక / Official Police Alert",
        "official_source_url": "https://cybercrime.gov.in/Webform/CyberAware.aspx",
        "safety_tip": {
            "te": "🛡️ భద్రతా సూత్రం: బ్యాంక్ పాస్‌బుక్ లేదా ఏటీఎం కార్డు వెనుక ఉన్న నంబర్ మాత్రమే నిజమైన హెల్ప్‌లైన్.",
            "en": "🛡️ Safety Tip: Use only helpline numbers printed on your bank passbook or credit/debit card."
        },
        "three_things_to_remember": {
            "te": [
                "1. గూగుల్ సెర్చ్ లోని నంబర్లు నకిలీవి అయ్యే ప్రమాదం ఉంది.",
                "2. కస్టమర్ కేర్ వాళ్లు ఎప్పుడూ ఓటీపీ లేదా పిన్ అడగరు.",
                "3. రిఫండ్ కోసం ఎలాంటి స్క్రీన్ షేరింగ్ యాప్ వేయవద్దు."
            ],
            "en": [
                "1. Unverified numbers on Google search are frequently manipulated.",
                "2. Real customer care representatives never request OTP or passwords.",
                "3. Never install remote access apps to process a refund."
            ]
        }
    }
]

def get_all_videos():
    return VIDEOS_REGISTRY

def filter_videos(category: str = "All", lang: str = "te"):
    videos = VIDEOS_REGISTRY
    if category and category != "All":
        videos = [v for v in videos if v["category"] == category]
    return videos
