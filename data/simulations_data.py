"""
CAVI - Cyber Aware Village Initiative
Interactive Simulation Data: "Spot the Scam" Scenarios and UPI Simulator Configuration.
Bilingual: Telugu (Default) and English.
Includes: Fake Prize, KYC Message, UPI Collect Request, Fake Customer Care, and Online Job Scam.
"""

SPOT_THE_SCAM_SCENARIOS = [
    {
        "id": "scenario_prize",
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
            "en": "🚨 This is 100% a SCAM! You cannot win a lottery you never bought tickets for. Notice the foreign country code (+92), suspicious website link, and upfront fee demand."
        },
        "red_flag_points": {
            "te": ["విదేశీ దేశ కోడ్ (+92)", "ముందుగా ₹1,500 ఫీజు డిమాండ్", "నకిలీ వెబ్‌సైట్ లింక్ (.xyz)"],
            "en": ["Foreign country code (+92)", "Demanding ₹1,500 upfront fees", "Suspicious link (.xyz)"]
        }
    },
    {
        "id": "scenario_kyc",
        "type": "SMS Alert",
        "sender": "VM-9848123456",
        "sender_label": "10-Digit Private Mobile",
        "time": "Yesterday, 8:15 PM",
        "message_mock": {
            "title": "URGENT BANK KYC SUSPENSION ⚠️",
            "body": "Dear SBI Customer, your bank account will be BLOCKED today because KYC PAN update is pending. Please click link to verify Aadhaar now: bit.ly/sbi-kyc-verify or call 9848123456 immediately to prevent debit freeze.",
            "footer": "State Banking Compliance Cell"
        },
        "is_scam": True,
        "correct_answer": "scam",
        "explanation": {
            "te": "🚨 ఇది మోసం! బ్యాంకులు సాధారణ 10-అంకెల ప్రైవేట్ మొబైల్ నంబర్ల నుండి రాత్రిపూట ఖాతా బ్లాక్ చేస్తామని బిట్లీ (bit.ly) లింకులు పంపవు. కేవైసీ కోసం ఎల్లప్పుడూ మీ సొంత బ్యాంక్ బ్రాంచ్‌ను మాత్రమే సంప్రదించండి.",
            "en": "🚨 This is a SCAM! Banks never send account freeze threats from personal 10-digit mobile numbers with shortened bit.ly links. Always visit your branch for KYC."
        },
        "red_flag_points": {
            "te": ["వ్యక్తిగత 10 అంకెల మొబైల్ నంబర్", "ఖాతా బ్లాక్ అవుతుందనే భయం & ఒత్తిడి", "షార్ట్ లింక్ (bit.ly)"],
            "en": ["Personal 10-digit mobile sender", "Artificial urgency & panic threats", "Shortened suspicious link"]
        }
    },
    {
        "id": "scenario_upi_collect",
        "type": "PhonePe Notification",
        "sender": "+91 97001 23456",
        "sender_label": "Unknown Buyer (Ramesh Agri)",
        "time": "Today, 11:20 AM",
        "message_mock": {
            "title": "PAYMENT COLLECT REQUEST: ₹5,000 💸",
            "body": "Ramesh Agri has requested ₹5,000 from you. Message: 'Sending grain purchase amount, enter UPI PIN to receive money in your account'.",
            "footer": "Click to Pay or Decline"
        },
        "is_scam": True,
        "correct_answer": "scam",
        "explanation": {
            "te": "🚨 ఇది యూపీఐ కలెక్ట్ మోసం! డబ్బులు పంపిస్తున్నామని చెప్పి కలెక్ట్ రిక్వెస్ట్ పంపారు. ఇందులో పిన్ కొడితే మీ ఖాతా నుండి ₹5,000 మోసగాడికి వెళ్తాయి. డబ్బులు రావడానికి ఎప్పుడూ పిన్ కొట్టవలసిన అవసరం లేదు!",
            "en": "🚨 This is a UPI COLLECT SCAM! The fraudster claims to send money but actually sends a collect request. If you enter your UPI PIN, ₹5,000 will be STOLEN from your account. You never enter a PIN to receive money!"
        },
        "red_flag_points": {
            "te": ["డబ్బులు రావడానికి పిన్ కొట్టమని చెప్పడం", "చెల్లింపు అభ్యర్థన (Collect Request)", "మోసపూరిత ఎర"],
            "en": ["Demanding PIN to 'receive' money", "Collect request instead of credit", "Deceptive financial trap"]
        }
    },
    {
        "id": "scenario_cust_care",
        "type": "Incoming Phone Call / SMS",
        "sender": "+91 88990 11223",
        "sender_label": "Claiming to be Courier / Bank Support",
        "time": "Just now",
        "message_mock": {
            "title": "PARCEL REFUND HELPLINE 📦",
            "body": "Sir, your government subsidy parcel failed delivery. For immediate refund of ₹1,200 to your bank account, install 'AnyDesk' app from Play Store and read out the 9-digit address code on phone.",
            "footer": "Express Parcel Delivery Support"
        },
        "is_scam": True,
        "correct_answer": "scam",
        "explanation": {
            "te": "🚨 ఇది స్క్రీన్ షేరింగ్ మోసం! డెలివరీ ఏజెంట్లు ఎప్పుడూ మీ ఫోన్‌లో AnyDesk లేదా QuickSupport వంటి యాప్‌లను వేయమని అడగరు. ఆ 9 అంకెల కోడ్ చెబితే మీ ఫోన్ స్క్రీన్, పాస్‌వర్డ్‌లు వారికి కనిపిస్తాయి.",
            "en": "🚨 This is a SCREEN SHARING SCAM! Real courier agents never ask customers to install remote control apps like AnyDesk. Revealing that 9-digit code exposes your entire phone screen."
        },
        "red_flag_points": {
            "te": ["రిమోట్ కంట్రోల్ యాప్ (AnyDesk) ఇన్‌స్టాల్ చేయమని కోరడం", "స్క్రీన్ కోడ్ అడగడం", "తెలియని పార్శిల్ నెపం"],
            "en": ["Asking to install remote assistance app", "Demanding 9-digit screen sharing code", "Vague parcel refund excuse"]
        }
    },
    {
        "id": "scenario_job",
        "type": "Telegram / SMS",
        "sender": "+91 94401 98765",
        "sender_label": "Global HR Recruiter",
        "time": "Today, 3:45 PM",
        "message_mock": {
            "title": "PART-TIME WORK FROM HOME 💼",
            "body": "Earn ₹2,000 to ₹5,000 daily from your village using smartphone! Simple task: Like YouTube videos & review hotels. Daily payout guaranteed. Pay ₹500 enrollment fee to activate your VIP tasks account: bit.ly/wfh-task-job",
            "footer": "Certified Online Jobs India"
        },
        "is_scam": True,
        "correct_answer": "scam",
        "explanation": {
            "te": "🚨 ఇది నకిలీ ఆన్‌లైన్ జాబ్ మోసం! లైక్లు కొడితే రోజుకు వేల రూపాయలు ఎవరూ ఇవ్వరు. పని ఇవ్వడానికి ముందుగా రిజిస్ట్రేషన్ ఫీజు అడిగారంటే అది వంద శాతం మోసమే.",
            "en": "🚨 This is an ONLINE TASK SCAM! No genuine employer pays thousands of rupees for simply liking videos. Asking for advance enrollment fees is guaranteed fraud."
        },
        "red_flag_points": {
            "te": ["రోజుకు సులభంగా ₹5,000 వస్తుందనే ఆశ", "ముందుగా ₹500 ఫీజు డిమాండ్", "టెలిగ్రామ్/బిట్లీ లింక్"],
            "en": ["Unrealistic high daily pay promise", "Demanding advance security fee", "Telegram / shortened bit.ly links"]
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
            "en": "✅ This is a SAFE, legitimate bank SMS! Notice the official bank header (VK-SBIINB), no suspicious hyperlinks, no demands for OTP or PIN, and it warns you to stay safe."
        },
        "red_flag_points": {
            "te": ["అధికారిక బ్యాంక్ సెండర్ ఐడీ", "ఎలాంటి లింకులు లేదా ఫోన్ నంబర్లు లేవు", "కేవలం బ్యాలెన్స్ సమాచారం మాత్రమే ఇచ్చింది"],
            "en": ["Official verified bank sender ID", "Zero links or request for personal details", "Informational balance alert only"]
        }
    }
]

UPI_SIMULATOR_STEPS = {
    "scammer_request_amount": 5000,
    "buyer_name": "Ramesh Seeds & Fertilizers (Fake Buyer)",
    "scenario_intro": {
        "te": "ఒక గుర్తుతెలియని వ్యక్తి మీ వద్ద ధాన్యం కొంటానని చెప్పి, ₹5,000 మీకు పంపిస్తున్నానని నమ్మిస్తాడు. మీ ఫోన్‌పే లేదా గూగుల్ పే లో క్రింది విధంగా నోటిఫికేషన్ కనిపిస్తుంది.",
        "en": "A stranger pretends to purchase farm grain from you and claims he is transferring ₹5,000. Your payment app shows the simulated screen below."
    }
}
