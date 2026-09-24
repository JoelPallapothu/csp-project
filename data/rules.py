"""
CAVI - Cyber Aware Village Initiative
10 Golden Rules of Cyber Safety and High-Contrast Do's vs Don'ts
Bilingual: Telugu (Default) and English.
"""

GOLDEN_RULES = [
    {
        "number": 1,
        "icon": "🔐",
        "title": {"te": "ఎవరికీ ఓటీపీ (OTP) చెప్పకండి", "en": "Never Share Your OTP"},
        "desc": {
            "te": "బ్యాంక్ మేనేజర్ లేదా పోలీస్ అధికారి అయినా సరే ఫోన్‌లో ఓటీపీ అడగరు. ఓటీపీ అనేది మీ బ్యాంక్ ఖాతాకు తాళం చెవి లాంటిది.",
            "en": "Bank managers, police, or courier executives will NEVER ask for your OTP. OTP is the secret key to your money."
        }
    },
    {
        "number": 2,
        "icon": "💳",
        "title": {"te": "ఏటీఎం పిన్ (ATM PIN) ఎవరితోనూ పంచుకోవద్దు", "en": "Never Reveal ATM PIN"},
        "desc": {
            "te": "మీ ఏటీఎం పిన్ మీ ఒక్కరికే తెలియాలి. కార్డుపై పిన్ రాయకండి లేదా ఫోన్‌లో ఎవరికీ చెప్పకండి.",
            "en": "Your 4-digit ATM PIN must remain strictly confidential. Never write it on the card or tell anyone."
        }
    },
    {
        "number": 3,
        "icon": "📲",
        "title": {"te": "డబ్బులు రావడానికి యూపీఐ పిన్ అవసరం లేదు", "en": "Never Enter PIN to Receive Money"},
        "desc": {
            "te": "డబ్బులు పంపేటప్పుడు (Send) మాత్రమే పిన్ కొట్టాలి. డబ్బులు మీ ఖాతాలోకి రావడానికి (Receive) పిన్ అస్సలు కొట్టకూడదు.",
            "en": "UPI PIN is used strictly to SEND money. You NEVER need to enter a PIN to receive or claim money."
        }
    },
    {
        "number": 4,
        "icon": "🔗",
        "title": {"te": "అపరిచిత లింకులను నొక్కకండి", "en": "Don't Click Unknown Links"},
        "desc": {
            "te": "ఉచిత రీఛార్జ్, కరెంట్ బిల్ కట్ లేదా లక్కీ డ్రా పేరిట ఎస్ఎంఎస్ లేదా వాట్సాప్‌లో వచ్చే లింకులను ఎప్పుడూ టచ్ చేయకండి.",
            "en": "Never tap links in text messages offering free recharges, electricity bill fixes, or lucky prizes."
        }
    },
    {
        "number": 5,
        "icon": "📥",
        "title": {"te": "వాట్సాప్‌లో వచ్చే యాప్‌లను (APK) ఇన్‌స్టాల్ చేయవద్దు", "en": "Don't Install Unknown APKs"},
        "desc": {
            "te": "వాట్సాప్ లేదా టెలిగ్రామ్‌లో పంపే ఫైల్స్ మీ ఫోన్‌ను హ్యాక్ చేస్తాయి. యాప్‌లను కేవలం అధికారిక గూగుల్ ప్లేస్టోర్ నుండే డౌన్‌లోడ్ చేసుకోండి.",
            "en": "Files sent on messaging apps often carry viruses. Only install apps from the official Google Play Store."
        }
    },
    {
        "number": 6,
        "icon": "📱",
        "title": {"te": "స్క్రీన్ షేరింగ్ యాప్స్ వేయవద్దు", "en": "Never Allow Screen Sharing Apps"},
        "desc": {
            "te": "AnyDesk, TeamViewer, QuickSupport వంటి యాప్‌లను అపరిచితుల మాట విని ఎక్కించవద్దు. అవి మీ స్క్రీన్ రహస్యాలను చూస్తాయి.",
            "en": "Never install remote access apps like AnyDesk or TeamViewer on caller instructions. They view your passwords."
        }
    },
    {
        "number": 7,
        "icon": "🔍",
        "title": {"te": "డబ్బులు పంపే ముందు పేరు సరిచూసుకోండి", "en": "Verify Identity Before Paying"},
        "desc": {
            "te": "బంధువులు లేదా దుకాణదారుల పేరుతో ఫోన్ వస్తే, నేరుగా పాత నంబర్‌కు ఫోన్ చేసి మాట్లాడాకే డబ్బులు పంపండి.",
            "en": "If a caller claims to be a distressed friend or relative, call their known phone number to verify first."
        }
    },
    {
        "number": 8,
        "icon": "🎁",
        "title": {"te": "లాటరీ లేదా బహుమతుల ఆశ పడకండి", "en": "Don't Trust Unexpected Prizes"},
        "desc": {
            "te": "మీరు టికెట్ కొనకుండా ఏ లాటరీ రాదు. బహుమతి ఇవ్వడానికి ముందుగా ఫీజు లేదా టాక్స్ అడిగితే అది 100% మోసమే.",
            "en": "You cannot win a contest you never entered. Legitimate giveaways never demand upfront tax or fee deposits."
        }
    },
    {
        "number": 9,
        "icon": "🆔",
        "title": {"te": "బ్యాంక్ పాస్‌బుక్, ఆధార్ ఫోటోలు పంపవద్దు", "en": "Protect Personal Documents"},
        "desc": {
            "te": "గుర్తుతెలియని వాట్సాప్ నంబర్లకు మీ ఆధార్ కార్డు, పాన్ కార్డు, బ్యాంక్ పాస్‌బుక్ ఫోటోలను ఎట్టి పరిస్థితుల్లోనూ పంపకండి.",
            "en": "Never share pictures of your Aadhaar card, PAN card, or bank passbook with unknown online contacts."
        }
    },
    {
        "number": 10,
        "icon": "🚨",
        "title": {"te": "మోసం జరిగితే వెంటనే 1930 కు కాల్ చేయండి", "en": "Report Financial Fraud Within 2-3 Hours"},
        "desc": {
            "te": "డబ్బులు కట్ అయిన వెంటనే ఆలస్యం చేయకుండా 1930 హెల్ప్‌లైన్‌కు ఫోన్ చేయండి. మొదటి 2-3 గంటల్లో (గోల్డెన్ అవర్) ఫిర్యాదు చేస్తే మీ డబ్బులు తిరిగి వచ్చే అవకాశం ఎక్కువ.",
            "en": "If money is debited fraudulently, immediately call National Helpline 1930. The first 2-3 hours are crucial to freeze stolen funds."
        }
    }
]

DOS_AND_DONTS = {
    "dos": [
        {
            "icon": "✅",
            "te": "ఏదైనా అనుమానం వస్తే మీ గ్రామ సచివాలయం లేదా మీ బ్యాంక్ బ్రాంచ్‌ను స్వయంగా సంప్రదించండి.",
            "en": "Always consult your local Grama Sachivalayam (Village Secretariat) or Bank Branch in person."
        },
        {
            "icon": "✅",
            "te": "డబ్బులు ఖాతాలో పడ్డాయో లేదో తెలుసుకోవడానికి బ్యాంక్ పాస్‌బుక్ లేదా మీ బ్యాంక్ మెసేజ్ మాత్రమే చూడండి.",
            "en": "Verify money credit only by checking your bank account statement or official SMS alerts."
        },
        {
            "icon": "✅",
            "te": "ఫోన్ నంబర్లు, బ్యాంక్ వివరాలు అడిగే కాల్స్ వచ్చినప్పుడు వెంటనే మీ కుటుంబ సభ్యులతో మాట్లాడండి.",
            "en": "Discuss with your trusted family members whenever anyone calls asking for financial details."
        },
        {
            "icon": "✅",
            "te": "మోసం జరిగిన వెంటనే మీ బ్యాంక్ కస్టమర్ కేర్‌కు ఫోన్ చేసి మీ ఏటీఎం కార్డు లేదా అకౌంట్‌ను తాత్కాలికంగా బ్లాక్ చేయించండి.",
            "en": "Immediately contact your bank to block your ATM card and net banking if an incident occurs."
        },
        {
            "icon": "✅",
            "te": "1930 జాతీయ సైబర్ హెల్ప్‌లైన్ నంబర్‌ను మీ ఫోన్‌లో సేవ్ చేసి పెట్టుకోండి.",
            "en": "Save the 1930 National Cyber Crime Helpline number in your phone contacts."
        }
    ],
    "donts": [
        {
            "icon": "❌",
            "te": "బ్యాంక్ మేనేజర్, పోలీస్ లేదా ప్రభుత్వ అధికారి అని ఎవరు చెప్పినా సరే ఓటీపీ (OTP) ఎవరికీ చెప్పవద్దు.",
            "en": "NEVER share your OTP with anyone, even if they claim to be police, bank manager, or delivery person."
        },
        {
            "icon": "❌",
            "te": "డబ్బులు మీ ఖాతాలోకి రావడానికి యూపీఐ పిన్ (UPI PIN) లేదా ఏటీఎం పిన్ ఎప్పుడూ కొట్టవద్దు.",
            "en": "NEVER enter your UPI PIN or ATM PIN to receive money into your account."
        },
        {
            "icon": "❌",
            "te": "కరెంట్ కట్ అవుతుందని లేదా ఉచిత లాటరీ వచ్చిందని వచ్చే ఎస్ఎంఎస్ లింకులను ఎప్పుడూ నొక్కవద్దు.",
            "en": "NEVER click on links claiming electricity cutoff, lucky draws, or free gifts."
        },
        {
            "icon": "❌",
            "te": "ఎవరి ఆదేశాలతోనూ మీ ఫోన్‌లో AnyDesk, TeamViewer వంటి యాప్‌లను ఇన్‌స్టాల్ చేయవద్దు.",
            "en": "NEVER install remote control apps like AnyDesk, RustDesk, or TeamViewer for strangers."
        },
        {
            "icon": "❌",
            "te": "ఎక్కువ లాభాలు లేదా తక్కువ సమయంలో రెట్టింపు డబ్బులు ఇస్తామనే మోసపూరిత పథకాల్లో డబ్బులు పెట్టవద్దు.",
            "en": "NEVER invest money in schemes promising to double your money in a few days."
        }
    ]
}
