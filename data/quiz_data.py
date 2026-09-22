"""
CAVI - Cyber Aware Village Initiative
10 Village-Oriented Interactive Cyber Safety Quiz Questions with Instant Explanations
"""

QUIZ_QUESTIONS = [
    {
        "id": 1,
        "category": "OTP Safety",
        "question": {
            "te": "బ్యాంక్ మేనేజర్‌ని అని ఫోన్ చేసి మీ మొబైల్‌కు వచ్చిన ఓటీపీ (OTP) అడిగితే మీరు ఏం చేస్తారు?",
            "en": "Someone calls pretending to be a bank manager and asks for your OTP. What should you do?",
            "hi": "कोई व्यक्ति बैंक मैनेजर बनकर कॉल करे और आपके फोन पर आया OTP मांगे, तो आप क्या करेंगे?"
        },
        "options": {
            "te": [
                "ఓటీపీ వెంటనే చెప్పేస్తాను",
                "ఎట్టి పరిస్థితుల్లోనూ ఓటీపీ చెప్పను, కాల్ కట్ చేస్తాను",
                "వాట్సాప్‌లో మెసేజ్ చేస్తాను"
            ],
            "en": [
                "Tell the OTP immediately",
                "Never share OTP under any circumstance, hang up immediately",
                "Send it through WhatsApp"
            ],
            "hi": [
                "तुरंत OTP बता दूंगा",
                "किसी भी हालत में OTP नहीं बताऊंगा और तुरंत कॉल काट दूंगा",
                "व्हाट्सएप पर भेज दूंगा"
            ]
        },
        "correct_index": 1,
        "explanation": {
            "te": "🎉 సరైన సమాధానం! బ్యాంక్ మేనేజర్ అయినా, పోలీస్ అధికారి అయినా ఫోన్‌లో ఎప్పుడూ ఓటీపీ అడగరు. ఓటీపీ ఎవరికీ చెప్పకూడదు.",
            "en": "🎉 Correct! Real bank managers and police officers NEVER ask for your OTP over phone. Keep your OTP secret.",
            "hi": "🎉 सही उत्तर! असली बैंक मैनेजर या पुलिस कभी फोन पर OTP नहीं मांगते। अपना OTP किसी को न दें।"
        }
    },
    {
        "id": 2,
        "category": "UPI Payments",
        "question": {
            "te": "ఒక వ్యక్తి మీకు ₹5,000 పంపిస్తున్నానని చెప్పి, మీ యూపీఐ పిన్ (UPI PIN) కొట్టమంటే ఏం జరుగుతుంది?",
            "en": "Someone says: 'I am sending you ₹5,000, please enter your UPI PIN to receive it.' What happens if you enter your PIN?",
            "hi": "कोई कहे: 'मैं आपको ₹5,000 भेज रहा हूँ, पैसे पाने के लिए अपना UPI PIN डालें।' यदि आप पिन डालते हैं तो क्या होगा?"
        },
        "options": {
            "te": [
                "నా అకౌంట్‌లోకి ₹5,000 వస్తాయి",
                "నా అకౌంట్ నుండి ₹5,000 ఎదుటివారికి వెళ్ళిపోతాయి",
                "ఏమీ జరగదు"
            ],
            "en": [
                "₹5,000 will be credited into my account",
                "₹5,000 will be STOLEN from my account and sent to the scammer",
                "Nothing will happen"
            ],
            "hi": [
                "मेरे खाते में ₹5,000 आ जाएंगे",
                "मेरे खाते से ₹5,000 कटकर धोखेबाज के पास चले जाएंगे",
                "कुछ नहीं होगा"
            ]
        },
        "correct_index": 1,
        "explanation": {
            "te": "🎉 సరైన సమాధానం! డబ్బులు రావడానికి ఎప్పుడూ పిన్ కొట్టవలసిన అవసరం లేదు. పిన్ కొడితే మీ డబ్బులే పోతాయి.",
            "en": "🎉 Correct! UPI PIN is ONLY entered to SEND money. You never enter a PIN to receive money.",
            "hi": "🎉 सही उत्तर! पैसे प्राप्त करने के लिए कभी भी पिन नहीं डाला जाता। पिन डालने से आपके ही पैसे कटते हैं।"
        }
    },
    {
        "id": 3,
        "category": "Lottery Fraud",
        "question": {
            "te": "వాట్సాప్‌లో 'మీకు ₹25 లక్షల లాటరీ తగిలింది, ముందుగా ₹2,000 టాక్స్ కట్టండి' అని వస్తే మీరు ఏం చేయాలి?",
            "en": "You receive a message saying: 'You won a ₹25 Lakh lottery! Pay ₹2,000 tax first to claim it.' What should you do?",
            "hi": "व्हाट्सएप पर मैसेज आए: 'आपने 25 लाख की लॉटरी जीती है, पहले ₹2,000 टैक्स जमा करें।' आपको क्या करना चाहिए?"
        },
        "options": {
            "te": [
                "వెంటనే ₹2,000 పంపిస్తాను",
                "ఇది మోసమని గుర్తించి మెసేజ్ డిలీట్ చేసి నంబర్ బ్లాక్ చేస్తాను",
                "స్నేహితులకు ఫార్వర్డ్ చేస్తాను"
            ],
            "en": [
                "Send ₹2,000 immediately to get the lottery",
                "Recognize it as a scam, delete the message, and block the sender",
                "Forward it to friends and relatives"
            ],
            "hi": [
                "लॉटरी पाने के लिए तुरंत ₹2,000 भेज दूंगा",
                "धोखाधड़ी समझकर मैसेज डिलीट करूंगा और नंबर ब्लॉक करूंगा",
                "दोस्तों और रिश्तेदारों को फॉरवर्ड करूंगा"
            ]
        },
        "correct_index": 1,
        "explanation": {
            "te": "🎉 సరైన సమాధానం! టికెట్ కొనకుండా లాటరీ రాదు. బహుమతి ఇవ్వడానికి ముందు డబ్బులు అడిగేవాళ్లంతా మోసగాళ్లే.",
            "en": "🎉 Correct! Real lotteries never demand advance processing fees or tax deposits.",
            "hi": "🎉 सही उत्तर! बिना टिकट खरीदे लॉटरी नहीं लगती। पहले पैसे मांगने वाले सभी धोखेबाज होते हैं।"
        }
    },
    {
        "id": 4,
        "category": "Screen Sharing",
        "question": {
            "te": "అపరిచితుడు ఫోన్ చేసి 'AnyDesk' లేదా 'QuickSupport' యాప్ ఎక్కించమంటే ఎందుకు ఎక్కించకూడదు?",
            "en": "Why should you NEVER install apps like 'AnyDesk' or 'QuickSupport' on an unknown caller's instruction?",
            "hi": "अजनबी के कहने पर 'AnyDesk' या 'QuickSupport' ऐप क्यों नहीं डाउनलोड करना चाहिए?"
        },
        "options": {
            "te": [
                "ఫోన్ బ్యాటరీ అయిపోతుంది కాబట్టి",
                "ఆ యాప్ వల్ల మోసగాడు మీ ఫోన్ స్క్రీన్, పాస్‌వర్డ్‌లను చూసి డబ్బులు దొంగిలిస్తాడు కాబట్టి",
                "ఫోన్ బరువు పెరుగుతుంది కాబట్టి"
            ],
            "en": [
                "Because phone battery drains quickly",
                "Because it allows the scammer to see your screen live, view passwords, and steal money",
                "Because phone gets heavy"
            ],
            "hi": [
                "क्योंकि फोन की बैटरी खत्म हो जाएगी",
                "क्योंकि धोखेबाज आपकी स्क्रीन और गुप्त पासवर्ड देखकर पैसे चुरा लेगा",
                "क्योंकि फोन भारी हो जाता है"
            ]
        },
        "correct_index": 1,
        "explanation": {
            "te": "🎉 సరైన సమాధానం! స్క్రీన్ షేరింగ్ యాప్స్ ద్వారా మీ ఫోన్ కంట్రోల్ మోసగాళ్ల చేతుల్లోకి వెళ్తుంది.",
            "en": "🎉 Correct! Screen sharing apps transmit your private screen and PINs live to the scammer.",
            "hi": "🎉 सही उत्तर! स्क्रीन शेयरिंग ऐप्स से आपके फोन का पूरा कंट्रोल धोखेबाजों के हाथ में चला जाता है।"
        }
    },
    {
        "id": 5,
        "category": "Digital Arrest",
        "question": {
            "te": "పోలీస్ డ్రెస్‌లో వీడియో కాల్ చేసి 'మీపై కేసు ఉంది, డిజిటల్ అరెస్ట్ చేశాం, డబ్బులు పంపండి' అని బెదిరిస్తే ఏమిటి నిజం?",
            "en": "Someone in police uniform video-calls claiming you are under 'Digital Arrest' and demands money. What is the truth?",
            "hi": "पुलिस की वर्दी में वीडियो कॉल कर कोई कहे कि आप 'डिजिटल अरेस्ट' हैं और पैसे मांगें, तो सच्चाई क्या है?"
        },
        "options": {
            "te": [
                "భారతదేశ చట్టంలో 'డిజిటల్ అరెస్ట్' అనేదే లేదు, ఇది నకిలీ మోసం!",
                "నిజమే, వెంటనే వారు చెప్పిన ఖాతాకు డబ్బులు కట్టాలి",
                "గదిలోనే బంధీగా ఉండిపోవాలి"
            ],
            "en": [
                "There is NO such thing as 'Digital Arrest' in Indian law; it is completely a scam!",
                "It is real, pay the money immediately",
                "Stay locked inside your room"
            ],
            "hi": [
                "भारतीय कानून में 'डिजिटल अरेस्ट' नाम की कोई चीज़ नहीं होती, यह 100% फर्जी धोखाधड़ी है!",
                "यह सच है, तुरंत पैसे भेज देने चाहिए",
                "कमरे में बंद रहना चाहिए"
            ]
        },
        "correct_index": 0,
        "explanation": {
            "te": "🎉 సరైన సమాధానం! చట్టబద్ధమైన పోలీసులు ఎప్పుడూ వీడియో కాల్‌లో అరెస్ట్ చేయరు లేదా డబ్బులు అడగరు.",
            "en": "🎉 Correct! Real law enforcement officers never conduct arrests or demand money transfers over video calls.",
            "hi": "🎉 सही उत्तर! कानून में वीडियो कॉल पर अरेस्ट या पैसे मांगने का कोई प्रावधान नहीं है।"
        }
    },
    {
        "id": 6,
        "category": "Emergency Reporting",
        "question": {
            "te": "సైబర్ మోసం జరిగి మీ బ్యాంకు ఖాతా నుండి డబ్బులు పోతే వెంటనే ఏ నంబర్‌కు ఫోన్ చేయాలి?",
            "en": "If cyber fraud occurs and money is stolen from your bank account, which emergency helpline should you dial immediately?",
            "hi": "यदि साइबर धोखाधड़ी से बैंक खाते से पैसे कट जाएं, तो तुरंत किस राष्ट्रीय हेल्पलाइन नंबर पर कॉल करना चाहिए?"
        },
        "options": {
            "te": [
                "100",
                "1930 (జాతీయ సైబర్ హెల్ప్‌లైన్)",
                "108"
            ],
            "en": [
                "100",
                "1930 (National Cyber Crime Helpline)",
                "108"
            ],
            "hi": [
                "100",
                "1930 (राष्ट्रीय साइबर हेल्पलाइन)",
                "108"
            ]
        },
        "correct_index": 1,
        "explanation": {
            "te": "🎉 సరైన సమాధానం! 1930 అనేది కేంద్ర ప్రభుత్వ అధికారిక సైబర్ క్రైమ్ హెల్ప్‌లైన్ నంబర్. మొదటి 2-3 గంటల్లో ఫిర్యాదు చేయడం చాలా ముఖ్యం.",
            "en": "🎉 Correct! 1930 is the official National Cyber Crime Helpline. Call immediately within the first 2-3 hours.",
            "hi": "🎉 सही उत्तर! 1930 भारत सरकार की आधिकारिक साइबर अपराध हेल्पलाइन है। तुरंत कॉल करने से पैसे रोके जा सकते हैं।"
        }
    },
    {
        "id": 7,
        "category": "Phishing Links",
        "question": {
            "te": "మీ మొబైల్‌కు 'ఈ రాత్రికి కరెంట్ కట్ అవుతుంది, బిల్ చెల్లించడానికి లింక్ నొక్కండి' అని ఎస్ఎంఎస్ వస్తే ఏం చేయాలి?",
            "en": "You receive an SMS: 'Electricity power will be cut tonight. Click link to update bill.' What should you do?",
            "hi": "मैसेज आए: 'आज रात बिजली कट जाएगी, बिल भरने के लिए लिंक पर क्लिक करें।' क्या करना चाहिए?"
        },
        "options": {
            "te": [
                "లింక్ నొక్కి కార్డు వివరాలు ఇస్తాను",
                "లింక్ క్లిక్ చేయకుండా, ఊరిలోని విద్యుత్ సచివాలయం సిబ్బందిని లేదా అధికారిక కార్యాలయాన్ని సంప్రదిస్తాను",
                "ఆ లింక్‌ను అందరికీ పంపుతాను"
            ],
            "en": [
                "Click the link and enter debit card details",
                "Do NOT click the link; check directly at the local electricity office or Grama Sachivalayam",
                "Share the link with everyone"
            ],
            "hi": [
                "लिंक खोलकर कार्ड की जानकारी भर दूंगा",
                "लिंक पर क्लिक नहीं करूंगा; सीधे बिजली विभाग या ग्राम पंचायत से संपर्क करूंगा",
                "लिंक सबको भेज दूंगा"
            ]
        },
        "correct_index": 1,
        "explanation": {
            "te": "🎉 సరైన సమాధానం! గుర్తుతెలియని నంబర్ల నుండి వచ్చే లింకులను ఎప్పుడూ నొక్కకూడదు.",
            "en": "🎉 Correct! Official electricity departments do not issue cutoff threats via personal SMS links.",
            "hi": "🎉 सही उत्तर! अनजान नंबरों से आए बिजली बिल या अन्य लिंक पर कभी क्लिक नहीं करना चाहिए।"
        }
    },
    {
        "id": 8,
        "category": "Customer Care",
        "question": {
            "te": "బ్యాంక్ కస్టమర్ కేర్ నంబర్ కోసం ఎక్కడ వెతకడం సురక్షితం?",
            "en": "Where is it SAFE to find your official Bank Customer Care phone number?",
            "hi": "बैंक कस्टमर केयर का असली नंबर कहाँ देखना सुरक्षित है?"
        },
        "options": {
            "te": [
                "గూగుల్ సెర్చ్‌లో కనిపించే నంబర్",
                "బ్యాంక్ పాస్‌బుక్ లేదా ఏటీఎం కార్డు వెనుక ముద్రించిన అధికారిక నంబర్",
                "ఫేస్‌బుక్‌లో ఎవరో రాసిన కామెంట్ లోని నంబర్"
            ],
            "en": [
                "Random number found on Google search",
                "Official number printed on your Bank Passbook or back of your ATM card",
                "A number found in Facebook comments"
            ],
            "hi": [
                "गूगल पर मिला कोई भी नंबर",
                "बैंक पासबुक या एटीएम कार्ड के पीछे छपा अधिकृत नंबर",
                "फेसबुक कमेंट में लिखा नंबर"
            ]
        },
        "correct_index": 1,
        "explanation": {
            "te": "🎉 సరైన సమాధానం! గూగుల్ సెర్చ్‌లో మోసగాళ్లు నకిలీ నంబర్లు పెడతారు. పాస్‌బుక్ లేదా ఏటీఎం కార్డు పై ఉన్న నంబర్ మాత్రమే నిజమైనది.",
            "en": "🎉 Correct! Google search often displays fraudulent helpline numbers. Always use passbook or card numbers.",
            "hi": "🎉 सही उत्तर! गूगल सर्च पर अक्सर ठगों के नंबर होते हैं। हमेशा पासबुक या कार्ड पर छपे नंबर का ही उपयोग करें।"
        }
    },
    {
        "id": 9,
        "category": "Loan Apps",
        "question": {
            "te": "ఎలాంటి పత్రాలు లేకుండా 5 నిమిషాల్లో లోన్ ఇస్తామనే గుర్తుతెలియని యాప్స్‌ను ఫోన్‌లో ఎక్కించవచ్చా?",
            "en": "Should you install unverified instant loan apps promising cash without documents?",
            "hi": "क्या बिना दस्तावेज 5 मिनट में लोन देने वाले अनजान ऐप्स को फोन में डाउनलोड करना चाहिए?"
        },
        "options": {
            "te": [
                "అస్సలు ఎక్కించకూడదు! అవి మీ ఫోటోలు, కాంటాక్ట్‌లు దొంగిలించి బ్లాక్‌మెయిల్ చేస్తాయి",
                "ఎక్కించుకోవచ్చు, ఉచితంగా డబ్బులు వస్తాయి",
                "స్నేహితులకు కూడా చెప్పి అందరూ ఎక్కించుకోవాలి"
            ],
            "en": [
                "NEVER install them! They harvest your photos and contacts to blackmail you and your family",
                "Yes, free cash without effort",
                "Recommend to all friends"
            ],
            "hi": [
                "बिल्कुल नहीं! वे आपकी फोटो और कॉन्टैक्ट्स चुराकर ब्लैकमेल करते हैं",
                "हाँ, आसानी से पैसे मिल जाएंगे",
                "दोस्तों को भी इंस्टॉल करवाएंगे"
            ]
        },
        "correct_index": 0,
        "explanation": {
            "te": "🎉 సరైన సమాధానం! చట్టవిరుద్ధ లోన్ యాప్స్ ప్రజలను తీవ్రంగా బ్లాక్‌మెయిల్ చేస్తాయి. రుణం కోసం ప్రభుత్వ గుర్తింపు పొందిన బ్యాంకులకే వెళ్ళాలి.",
            "en": "🎉 Correct! Predatory instant loan apps extort families using stolen private photos. Always rely on regulated banks.",
            "hi": "🎉 सही उत्तर! फर्जी लोन ऐप्स फोटो चुराकर ब्लैकमेल करते हैं। कर्ज केवल बैंक से ही लें।"
        }
    },
    {
        "id": 10,
        "category": "ATM PIN Privacy",
        "question": {
            "te": "మీ ఏటీఎం కార్డు పిన్ నంబర్‌ను ఎవరెవరికి చెప్పవచ్చు?",
            "en": "With whom are you allowed to share your 4-digit ATM PIN?",
            "hi": "अपना 4 अंकों का एटीएम पिन आपको किसके साथ साझा करना चाहिए?"
        },
        "options": {
            "te": [
                "ఏటీఎం వద్ద సహాయం చేసే అపరిచిత వ్యక్తికి",
                "ఫోన్ చేసిన బ్యాంక్ ఏజెంట్‌కి",
                "ఎవరికీ చెప్పకూడదు! పిన్ పూర్తిగా రహస్యంగా ఉంచాలి"
            ],
            "en": [
                "A stranger standing near the ATM offering to help",
                "A caller saying they are bank verification agents",
                "NO ONE! ATM PIN must remain strictly confidential and known only to you"
            ],
            "hi": [
                "एटीएम के बाहर खड़े किसी अजनबी मददगार को",
                "फोन पर बात कर रहे बैंक कर्मचारी को",
                "किसी को भी नहीं! एटीएम पिन पूरी तरह से आपका व्यक्तिगत रहस्य है"
            ]
        },
        "correct_index": 2,
        "explanation": {
            "te": "🎉 సరైన సమాధానం! మీ ఏటీఎం పిన్ మీ ఒక్కరికే తెలియాలి. ఏటీఎం కార్డుపై పిన్ రాయడం లేదా ఇతరులకు చెప్పడం చేయకూడదు.",
            "en": "🎉 Correct! Your ATM PIN is strictly for you. Never write it on your card or share it with anyone.",
            "hi": "🎉 सही उत्तर! एटीएम पिन केवल आपको पता होना चाहिए। इसे कभी किसी को न बताएं।"
        }
    }
]

def get_all_questions():
    return QUIZ_QUESTIONS
