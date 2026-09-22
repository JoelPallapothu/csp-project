"""
CAVI - Cyber Aware Village Initiative
Interactive Simulation Data: "Spot the Scam" scenarios and UPI Simulator configuration
"""

SPOT_THE_SCAM_SCENARIOS = [
    {
        "id": "scenario_lottery",
        "type": "WhatsApp Message",
        "sender": "+92 301 8492011",
        "sender_label": "Unknown International Number",
        "time": "10:45 AM",
        "message_mock": {
            "title": "🎉 KBC & ALL INDIA LOTTERY WINNER 🎉",
            "body": "Congratulations! Your mobile number has won ₹25,00,000 cash prize in our lucky festival draw. To claim your lottery amount directly into your bank account, click this link now: http://kbc-lottery-winner2026.xyz/claim and pay ₹1,500 file charges.",
            "footer": "Issued by Mumbai Headquarters. Strictly confidential."
        },
        "is_scam": True,
        "correct_answer": "scam",
        "explanation": {
            "te": "🚨 ఇది పక్కా మోసం! మీరు టికెట్ కొనకుండా లాటరీ రాదు. విదేశీ కోడ్ (+92) నుండి మెసేజ్ వచ్చింది. బహుమతి ఇవ్వడానికి ముందు డబ్బులు కట్టమంటున్నారంటే అది మోసగాళ్ల పనే.",
            "en": "🚨 This is 100% a SCAM! You cannot win a lottery you never bought tickets for. Notice the foreign country code (+92), suspicious website link, and upfront fee demand.",
            "hi": "🚨 यह पूरी तरह से एक धोखा (SCAM) है! बिना टिकट खरीदे कोई लॉटरी नहीं लगती। विदेशी नंबर (+92), फर्जी लिंक और पहले पैसे मांगने से साफ पता चलता है कि यह ठगों का काम है।"
        },
        "red_flag_points": {
            "te": ["విదేశీ దేశ కోడ్ (+92)", "ముందుగా ₹1,500 ఫీజు డిమాండ్", "నకిలీ వెబ్‌సైట్ లింక్ (.xyz)"],
            "en": ["Foreign country code (+92)", "Demanding ₹1,500 upfront fees", "Suspicious link (.xyz)"],
            "hi": ["विदेशी कोड (+92)", "पहले ₹1,500 की मांग", "फर्जी वेबसाइट लिंक"]
        }
    },
    {
        "id": "scenario_electricity",
        "type": "SMS Alert",
        "sender": "VM-9848123456",
        "sender_label": "10-Digit Private Mobile",
        "time": "Yesterday, 8:15 PM",
        "message_mock": {
            "title": "URGENT ELECTRICITY ALERT ⚡",
            "body": "Dear Consumer, your electricity power will be disconnected tonight at 9:30 PM because previous month bill was not updated. Please call our power officer at 9848123456 immediately or pay ₹11 pending charges via link: bit.ly/apcpdcl-pay",
            "footer": "Electricity Distribution Office"
        },
        "is_scam": True,
        "correct_answer": "scam",
        "explanation": {
            "te": "🚨 ఇది మోసం! విద్యుత్ శాఖ సాధారణ మొబైల్ నంబర్ల నుండి రాత్రిపూట కరెంట్ కట్ చేస్తామని మెసేజ్ పంపదు. బిల్లుల కోసం ఎల్లప్పుడూ అధికారిక సచివాలయం లేదా బిల్లు కలెక్టర్‌ను మాత్రమే సంప్రదించండి.",
            "en": "🚨 This is a SCAM! Government electricity boards do not send cutoff threats from personal 10-digit mobile numbers with shortened bit.ly links.",
            "hi": "🚨 यह धोखा (SCAM) है! बिजली विभाग किसी निजी मोबाइल नंबर से रात में बिजली काटने की धमकी और bit.ly लिंक नहीं भेजता।"
        },
        "red_flag_points": {
            "te": ["వ్యక్తిగత 10 అంకెల మొబైల్ నంబర్", "రాత్రికి కరెంట్ కట్ అవుతుందనే భయం", "షార్ట్ లింక్ (bit.ly)"],
            "en": ["Personal 10-digit mobile sender", "Artificial urgency & threats", "Shortened suspicious link"],
            "hi": ["निजी मोबाइल नंबर से मैसेज", "रात को बिजली काटने का डर", "संदिग्ध शॉर्ट लिंक"]
        }
    },
    {
        "id": "scenario_bank_legit",
        "type": "Official Bank SMS",
        "sender": "VK-SBIINB",
        "sender_label": "Official Bank Sender ID",
        "time": "Today, 11:30 AM",
        "message_mock": {
            "title": "BANK TRANSACTION ALERT 🏦",
            "body": "Your a/c no. XX4129 is credited with Rs 2,000.00 on 22-09-2026 by PM-KISAN installment. Available Bal: Rs 4,850.00. Never share your OTP, PIN or CVV with anyone. - SBI",
            "footer": "Official Automated Banking Alert"
        },
        "is_scam": False,
        "correct_answer": "safe",
        "explanation": {
            "te": "✅ ఇది సురక్షితమైన అధికారిక బ్యాంక్ మెసేజ్! ఇందులో ఎలాంటి అనుమానాస్పద లింకులు లేవు, ఓటీపీ లేదా పిన్ అడగలేదు. పంపిన ఐడీ (VK-SBIINB) అధికారిక బ్యాంక్ హ్యాండల్.",
            "en": "✅ This is a SAFE, legitimate bank SMS! Notice the official bank header (VK-SBIINB), no suspicious hyperlinks, no demands for OTP or PIN, and it warns you to stay safe.",
            "hi": "✅ यह पूरी तरह से सुरक्षित (SAFE) बैंक मैसेज है! इसमें कोई लिंक नहीं है, न ही कोई पिन या ओटीपी मांगा गया है। प्रेषक आईडी (VK-SBIINB) बैंक की अधिकृत आईडी है।"
        },
        "red_flag_points": {
            "te": ["అధికారిక బ్యాంక్ సెండర్ ఐడీ", "ఎలాంటి లింకులు లేదా ఫోన్ నంబర్లు లేవు", "కేవలం బ్యాలెన్స్ సమాచారం మాత్రమే ఇచ్చింది"],
            "en": ["Official verified bank sender ID", "Zero links or request for personal details", "Informational balance alert only"],
            "hi": ["बैंक की अधिकृत प्रेषक आईडी", "कोई भी लिंक या फोन नंबर नहीं", "केवल खाते की जानकारी दी गई है"]
        }
    },
    {
        "id": "scenario_fake_relative",
        "type": "WhatsApp Message",
        "sender": "+91 91234 56789",
        "sender_label": "Unsaved Number with Relative's Photo",
        "time": "Today, 2:10 PM",
        "message_mock": {
            "title": "URGENT FAMILY HOSPITAL EMERGENCY 🏥",
            "body": "Mama, this is Suresh (your nephew). My phone fell into water so using friend's phone. I had a small bike accident near Vijayawada. Hospital doctor needs ₹8,000 immediately for injection. Please send to this GPay number 9123456789 right now. Don't tell auntie, she will worry.",
            "footer": "Please send urgently Mama!"
        },
        "is_scam": True,
        "correct_answer": "scam",
        "explanation": {
            "te": "🚨 ఇది మోసం (నకిలీ బంధువుల ఎమోషనల్ మోసం)! మోసగాళ్లు సోషల్ మీడియా నుండి బంధువుల ఫోటోలు తీసుకుని ప్రమాదం జరిగిందని అబద్ధాలు చెబుతారు. వెంటనే మీ బంధువు పాత నంబర్‌కు లేదా వారి ఇంట్లోని వేరే వారికి ఫోన్ చేసి నిజమో కాదో నిర్ధారించుకోవాలి.",
            "en": "🚨 This is a SCAM (Imposter Relative Scam)! Fraudsters steal profile pictures from social media and fabricate accident emergencies. Always call your relative's known telephone number to verify before sending a single rupee.",
            "hi": "🚨 यह एक गंभीर धोखा (SCAM) है! धोखेबाज रिश्तेदारों की फोटो लगाकर अस्पताल का झूठा बहाना बनाते हैं। पैसे भेजने से पहले हमेशा रिश्तेदार के पुराने नंबर पर कॉल करके सच्चाई जान लें।"
        },
        "red_flag_points": {
            "te": ["కొత్త నంబర్ నుండి మెసేజ్", "హాస్పిటల్ ఎమర్జెన్సీ పేరిట భయం మరియు భావోద్వేగం", "ఇంట్లో ఎవరికీ చెప్పవద్దని చెప్పడం"],
            "en": ["New unknown mobile number", "High emotional panic & hospital emergency", "Instruction not to inform family members"],
            "hi": ["अज्ञात नए नंबर से मैसेज", "अस्पताल के नाम पर भावनात्मक दबाव", "घर में किसी को न बताने की बात कहना"]
        }
    },
    {
        "id": "scenario_screen_share",
        "type": "Incoming Phone Call / SMS",
        "sender": "+91 88990 11223",
        "sender_label": "Caller claiming to be Courier Agent",
        "time": "Just now",
        "message_mock": {
            "title": "PARCEL DELIVERY HOLD NOTIFICATION 📦",
            "body": "Sir, your government gift parcel address is incomplete. To update address and release parcel, please install 'QuickSupport' app from Play Store and tell me the 9-digit partner ID on the call.",
            "footer": "Express Parcel Logistics"
        },
        "is_scam": True,
        "correct_answer": "scam",
        "explanation": {
            "te": "🚨 ఇది స్క్రీన్ షేరింగ్ మోసం! డెలివరీ ఏజెంట్లు ఎప్పుడూ మీ ఫోన్‌లో QuickSupport లేదా AnyDesk వంటి యాప్‌లను వేయమని అడగరు. ఆ 9 అంకెల కోడ్ చెబితే మీ ఫోన్ స్క్రీన్ వారికి కనిపిస్తుంది.",
            "en": "🚨 This is a SCREEN SHARING SCAM! Real courier agents never ask customers to install remote control apps like QuickSupport. Revealing that 9-digit code exposes your entire phone screen.",
            "hi": "🚨 यह स्क्रीन शेयरिंग धोखाधड़ी (SCAM) है! कोई भी कूरियर वाला QuickSupport या AnyDesk ऐप इंस्टॉल करने को नहीं कहता। कोड बताते ही आपका पूरा फोन हैक हो जाता है।"
        },
        "red_flag_points": {
            "te": ["రిమోట్ కంట్రోల్ యాప్ (QuickSupport) ఇన్‌స్టాల్ చేయమని కోరడం", "స్క్రీన్ కోడ్ అడగడం", "తెలియని పార్శిల్ గురించి చెప్పడం"],
            "en": ["Asking to install remote assistance app", "Demanding 9-digit screen sharing code", "Vague parcel delivery excuse"],
            "hi": ["स्क्रीन शेयरिंग ऐप इंस्टॉल करने को कहना", "9 अंकों का सीक्रेट कोड मांगना", "अज्ञात पार्सल का बहाना बनाना"]
        }
    }
]

UPI_SIMULATOR_STEPS = {
    "scammer_request_amount": 5000,
    "buyer_name": "Ramesh Seeds & Fertilizers (Fake Buyer)",
    "scenario_intro": {
        "te": "ఒక గుర్తుతెలియని వ్యక్తి మీ వద్ద ధాన్యం కొంటానని చెప్పి, ₹5,000 మీకు పంపిస్తున్నానని నమ్మిస్తాడు. మీ ఫోన్‌పే లేదా గూగుల్ పే లో క్రింది విధంగా నోటిఫికేషన్ కనిపిస్తుంది.",
        "en": "A stranger pretends to purchase farm grain from you and claims he is transferring ₹5,000. Your payment app shows the simulated screen below.",
        "hi": "एक अनजान व्यक्ति आपसे फसल खरीदने का नाटक करता है और कहता है कि वह आपको ₹5,000 भेज रहा है। आपके फोनपे या गूगलपे पर नीचे दी गई स्क्रीन खुलती है।"
    }
}
