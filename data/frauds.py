"""
CAVI - Cyber Aware Village Initiative
12 Comprehensive Fraud Modules with Visual Flows, Red Flags, Action Steps, Real Dialogues & Audio Scripts
Bilingual: Telugu (Default) and English.
Zero Hindi entries.
"""

FRAUD_MODULES = [{'id': 'otp_fraud',
  'icon': '🔐',
  'badge': 'అత్యంత ప్రమాదకరం / Critical',
  'color': '#dc2626',
  'title': {'te': 'ఓటీపీ మోసం (OTP Fraud)', 'en': 'OTP Fraud (One-Time Password Scam)'},
  'short_desc': {'te': 'బ్యాంక్ మేనేజర్ లేదా ఆఫీసర్ అని చెప్పి ఫోన్ చేసి మీ మొబైల్\u200cకు వచ్చే ఓటీపీ అడుగుతారు.',
                 'en': 'Scammer calls claiming to be a bank official or courier agent asking for your OTP.'},
  'what_happens': {'te': 'మోసగాడు మీ బ్యాంకు ఖాతా బ్లాక్ అయిందని లేదా మీకు ప్రభుత్వ పథకం డబ్బులు వస్తున్నాయని '
                         'నమ్మిస్తాడు. మీ ఫోన్\u200cకు వచ్చే 4 లేదా 6 అంకెల ఓటీపీని చెబితే మీ ఖాతాలోని డబ్బు మొత్తం '
                         'మాయం చేస్తాడు.',
                   'en': 'The scammer induces fear or greed saying your account is suspended or scheme money is '
                         'credited. If you reveal the 4-6 digit OTP sent to your phone, your entire bank balance is '
                         'stolen instantly.'},
  'workflow': [{'step': '1', 'icon': '📞', 'te': 'అపరిచిత కాల్ వస్తుంది', 'en': 'Unknown call arrives'},
               {'step': '2',
                'icon': '🎭',
                'te': 'బ్యాంక్ మేనేజర్\u200cని అని చెబుతాడు',
                'en': 'Claims to be Bank Manager'},
               {'step': '3', 'icon': '📩', 'te': 'ఓటీపీ చెప్పమని అడుగుతాడు', 'en': 'Urges you to share OTP'},
               {'step': '4', 'icon': '💸', 'te': 'చెబితే మీ డబ్బు మొత్తం మాయం!', 'en': 'Money stolen instantly!'}],
  'red_flags': {'te': ["కాల్ చేసిన వ్యక్తి 'ఖాతా ఆగిపోతుంది, వెంటనే ఓటీపీ చెప్పండి' అని భయపెడతాడు.",
                       'లక్కీ డ్రా లేదా రేషన్ కార్డు బోనస్ కోసం ఓటీపీ చెప్పమంటాడు.',
                       'ఫోన్ కట్ చేయకుండా వెంటనే నంబర్లు చెప్పాలని ఒత్తిడి చేస్తాడు.'],
                'en': ['Caller urgently threatens that your account or SIM card will be blocked immediately.',
                       'Offers lucky lottery winnings or government subsidies in exchange for an OTP.',
                       'Pressures you to stay on the call and reads out the numbers without delay.']},
  'what_to_do': {'te': ['కాల్\u200cను వెంటనే కట్ చేయండి. ఎవరికీ ఎలాంటి ఓటీపీ చెప్పకండి.',
                        'బ్యాంక్ లేదా ప్రభుత్వం ఎప్పుడూ ఫోన్\u200cలో ఓటీపీ అడగవని గుర్తుంచుకోండి.',
                        'సందేహం ఉంటే మీ ఊరిలోని బ్యాంక్ బ్రాంచ్\u200cకి నేరుగా వెళ్లి మేనేజర్\u200cను కలవండి.',
                        'మోసం జరిగితే వెంటనే 1930 కి ఫోన్ చేయండి.'],
                 'en': ['Hang up the phone call immediately. Never speak or send your OTP.',
                        'Remember: Banks and Government bodies NEVER ask for your OTP over phone.',
                        'Visit your nearest bank branch in person if you have any doubts.',
                        'Dial 1930 immediately if money has been debited.']},
  'dialogue': {'scammer_te': 'నమస్కారం సార్, నేను మీ స్టేట్ బ్యాంక్ హెడ్ ఆఫీస్ నుండి మాట్లాడుతున్నాను. మీ ఖాతా ఆధార్ '
                             'లింక్ కాకపోవడంతో బ్లాక్ అయింది. మీ ఫోన్\u200cకు 6 అంకెల ఓటీపీ వచ్చింది, వెంటనే చెప్పండి '
                             'లేకపోతే ఖాతా రద్దవుతుంది!',
               'villager_te': 'బ్యాంకు వారు ఫోన్ లో ఓటీపీ అడగరని మా గ్రామ సచివాలయంలో చెప్పారు. నేను ఓటీపీ చెప్పను! '
                              'నేను నేరుగా మా ఊరి బ్యాంక్ బ్రాంచ్\u200cకి వెళ్లి కనుక్కుంటాను.',
               'outcome_te': '✅ సరైన నిర్ణయం! కాల్ కట్ చేసి ఫోన్ బ్లాక్ చేశారు. బ్యాంక్ ఖాతా సురక్షితంగా ఉంది.',
               'scammer_en': 'Hello sir, I am calling from State Bank Head Office. Your account is blocked due to '
                             'pending Aadhaar link. You received a 6-digit OTP, tell me immediately or your account '
                             'will be deleted permanently!',
               'villager_en': 'Our Village Secretariat warned us that banks NEVER ask for OTP over phone. I will NOT '
                              'give you my OTP! I will visit my local branch directly.',
               'outcome_en': '✅ Safe Choice! Call disconnected. Bank balance protected.'},
  'audio_text': {'te': 'ఓటీపీ అంటే మీ బ్యాంకు ఖాతాకు ఉండే తాళం చెవి లాంటిది. బ్యాంక్ మేనేజర్ అయినా, ఎవరైనా ఫోన్ చేసి '
                       'ఓటీపీ అడిగితే ఎట్టి పరిస్థితుల్లోనూ చెప్పకండి. వెంటనే కాల్ కట్ చేయండి.',
                 'en': 'OTP is the secret key to your bank account. No bank manager or police officer will ever ask '
                       'for your OTP. Never share your OTP with anyone.'}},
 {'id': 'upi_fraud',
  'icon': '💳',
  'badge': 'చాలా సాధారణం / Common',
  'color': '#ea580c',
  'title': {'te': 'యూపీఐ మోసం (UPI Pin Scam)', 'en': 'UPI PIN Scam (Money Receiving Fraud)'},
  'short_desc': {'te': 'డబ్బులు పంపిస్తున్నామని చెప్పి, రిసీవ్ చేసుకోవడానికి యూపీఐ పిన్ కొట్టమని అడుగుతారు.',
                 'en': "Scammer claims to send money and tricks you into entering your UPI PIN to 'receive' it."},
  'what_happens': {'te': 'మోసగాడు మీ పంట లేదా దుకాణంలోని వస్తువులు కొంటానని ఫోన్ చేస్తాడు. మీకు ₹5,000 పంపించాను, అది '
                         'మీ అకౌంట్\u200cలోకి రావాలంటే మీ PhonePe లేదా Google Pay లో పిన్ కొట్టండి లేదా క్యూఆర్ కోడ్ '
                         'స్కాన్ చేయండి అంటాడు. పిన్ కొట్టగానే మీ అకౌంట్ నుండి డబ్బులు పోతాయి!',
                   'en': 'Scammer pretends to buy farm produce or goods. He sends a fake payment request and asks you '
                         "to enter your UPI PIN or scan a QR code to 'receive' the money. Entering PIN sends YOUR "
                         'money to him!'},
  'workflow': [{'step': '1', 'icon': '🌾', 'te': 'వస్తువు కొంటానని అబద్ధం చెబుతాడు', 'en': 'Offers to buy farm goods'},
               {'step': '2', 'icon': '📲', 'te': 'డబ్బుల కోసం రిక్వెస్ట్ పంపుతాడు', 'en': 'Sends payment request / QR'},
               {'step': '3',
                'icon': '🔢',
                'te': 'రిసీవ్ చేసుకోవడానికి పిన్ కొట్టమంటాడు',
                'en': 'Tells you to enter UPI PIN'},
               {'step': '4',
                'icon': '🚨',
                'te': 'పిన్ కొడితే మీ అకౌంట్ ఖాళీ!',
                'en': 'Entering PIN steals your money!'}],
  'red_flags': {'te': ['బంగారు నియమం: డబ్బులు రావడానికి (Receive) ఎప్పుడూ యూపీఐ పిన్ అవసరం లేదు!',
                       'క్యూఆర్ కోడ్ స్కాన్ చేసి పిన్ కొడితే డబ్బులు వస్తాయని ఎవరైనా చెబితే అది 100% మోసం.',
                       "గూగుల్ పే లేదా ఫోన్\u200cపేలో 'Pay' అనే బటన్ ఉన్నప్పుడు నొక్కితే డబ్బులు మీ నుండి ఎదుటివారికి "
                       'వెళ్తాయి.'],
                'en': ['GOLDEN RULE: UPI PIN is ONLY needed to SEND money, NEVER to receive money!',
                       'Anyone telling you to scan a QR code or enter PIN to accept funds is 100% a scammer.',
                       "If the app shows 'Pay' with an amount, it will deduct money from YOUR bank account."]},
  'what_to_do': {'te': ['డబ్బులు రావడానికి ఎవరికీ పిన్ కొట్టకండి.',
                        'చెల్లింపు వచ్చినట్లు నిర్ధారించుకోవడానికి మీ బ్యాంక్ పాస్\u200cబుక్ లేదా బ్యాంక్ ఎస్ఎంఎస్ '
                        'మాత్రమే చూడండి.',
                        "అనుమానాస్పద చెల్లింపు అభ్యర్థనలను వెంటనే 'Decline' (రద్దు) చేయండి."],
                 'en': ['NEVER enter your UPI PIN to receive money.',
                        'Verify credits only through official bank SMS balance updates, not caller claims.',
                        'Decline any suspicious payment requests on PhonePe, GPay, or Paytm.']},
  'dialogue': {'scammer_te': 'అన్నా, మీ ధాన్యం బస్తాలకు ₹10,000 పంపాను. మీ ఫోన్\u200cపేలో లింక్ పెట్టాను, దాన్ని '
                             'నొక్కి మీ యూపీఐ పిన్ కొట్టండి, వెంటనే డబ్బులు మీ చేతికి వస్తాయి!',
               'villager_te': 'డబ్బులు రావడానికి పిన్ కొట్టనక్కర్లేదని మాకు తెలుసు! పిన్ కొడితే నా డబ్బులే పోతాయి. '
                              'నేను పిన్ కొట్టను.',
               'outcome_te': '✅ రైతు మోసాన్ని గుర్తించారు! పిన్ కొట్టకుండా మోసగాడి నుండి తప్పించుకున్నారు.',
               'scammer_en': 'Brother, I sent ₹10,000 for your grain sacks. Tap the link in your PhonePe and enter '
                             'your UPI PIN to collect the money right now!',
               'villager_en': 'I know the rule! UPI PIN is never required to receive money. If I enter my PIN, my '
                              'money will be stolen. I will not enter it!',
               'outcome_en': '✅ Smart Farmer! Refused to enter PIN and avoided financial theft.'},
  'audio_text': {'te': 'ఎల్లప్పుడూ గుర్తుంచుకోండి: మీ ఖాతాలోకి డబ్బులు రావడానికి యూపీఐ పిన్ కొట్టవలసిన అవసరం లేదు. '
                       'పిన్ కొట్టారంటే మీ డబ్బులు ఎదుటివారికి వెళ్ళిపోతాయి.',
                 'en': 'Remember this rule: You NEVER need to enter your UPI PIN to receive money. UPI PIN is only '
                       'used when sending money out.'}},
 {'id': 'kyc_fraud',
  'icon': '🏦',
  'badge': 'ప్రమాదకరం / High Alert',
  'color': '#b91c1c',
  'title': {'te': 'బ్యాంక్ కేవైసీ మోసం (KYC Update Fraud)', 'en': 'Bank KYC Update Scam'},
  'short_desc': {'te': 'మీ పాన్ కార్డు లేదా కేవైసీ అప్\u200cడేట్ చేయకపోతే బ్యాంక్ అకౌంట్ ఆగిపోతుందని నకిలీ మెసేజ్ '
                       'పంపుతారు.',
                 'en': 'Fake SMS claiming your bank account or SIM will be blocked unless you click a link to update '
                       'KYC.'},
  'what_happens': {'te': "మీ మొబైల్\u200cకు 'Dear customer, your bank account is suspended. Update KYC now at link...' "
                         'అని ఎస్ఎంఎస్ వస్తుంది. ఆ లింక్ నొక్కగానే బ్యాంక్ లాంటి నకిలీ పేజీ ఓపెన్ అవుతుంది. మీ ఆధార్, '
                         'అకౌంట్ నంబర్, పాస్\u200cవర్డ్ కొట్టగానే అకౌంట్ లూటీ అవుతుంది.',
                   'en': 'You receive a panic-inducing SMS with a link to update KYC. The link opens a clone bank '
                         'website where entering your account details and password gives scammers complete control '
                         'over your money.'},
  'workflow': [{'step': '1', 'icon': '📩', 'te': 'భయపెట్టే ఎస్ఎంఎస్ వస్తుంది', 'en': 'Threatening SMS received'},
               {'step': '2', 'icon': '🔗', 'te': 'లింక్ నొక్కమని అడుగుతారు', 'en': 'Prompts to click link'},
               {'step': '3', 'icon': '📄', 'te': 'నకిలీ పేజీలో వివరాలు అడుగుతారు', 'en': 'Fake form collects data'},
               {'step': '4', 'icon': '💸', 'te': 'ఖాతాలో డబ్బులు కొట్టేస్తారు!', 'en': 'Account cleaned out!'}],
  'red_flags': {'te': ['అపరిచిత ఫోన్ నంబర్ నుండి వచ్చే ఎస్ఎంఎస్\u200cలలోని లింకులు (bit.ly లేదా ngrok లింకులు).',
                       '24 గంటల్లో అకౌంట్ లేదా ఏటీఎం కార్డు ఆగిపోతుందని తొందరపెట్టడం.',
                       'ఆన్\u200cలైన్ ఫారమ్\u200cలో మీ డెబిట్ కార్డు నంబర్, సీవీవీ (CVV), ఏటీఎం పిన్ అడగడం.'],
                'en': ['SMS sent from random 10-digit mobile numbers containing suspicious short links.',
                       'Threats that your account or ATM card will be blocked within 24 hours.',
                       'Online forms demanding your 16-digit debit card number, CVV, and ATM PIN.']},
  'what_to_do': {'te': ['మెసేజ్\u200cలోని ఎలాంటి లింకులనూ నొక్కవద్దు.',
                        'కేవైసీ అప్\u200cడేట్ ఎప్పుడూ మీ స్వంత బ్యాంక్ బ్రాంచ్\u200cలో మాత్రమే చేయించుకోండి.',
                        'సందేహం ఉంటే మీ పాస్\u200cబుక్ పై ఉన్న అధికారిక టోల్ ఫ్రీ నంబర్\u200cకు మాత్రమే కాల్ చేయండి.'],
                 'en': ['Never tap on links received in unsolicited text messages.',
                        'Always complete KYC directly at your local physical bank branch.',
                        'Call only the verified official toll-free number printed on your bank passbook.']},
  'dialogue': {'scammer_te': 'సార్, ఎస్ఎంఎస్ వచ్చింది చూడండి. వెంటనే లింక్ నొక్కి మీ పాన్ కార్డు, బ్యాంక్ కార్డు '
                             'నంబర్, ఓటీపీ ఎంటర్ చేయండి. లేకపోతే సాయంత్రానికి మీ అకౌంట్ పర్మనెంట్\u200cగా క్లోజ్ '
                             'అవుతుంది!',
               'villager_te': 'నా బ్యాంక్ మేనేజర్ నాకు తెలుసు. ఏదైనా ఉంటే నేను నేరుగా రేపు బ్యాంక్\u200cకి వెళ్తాను. '
                              'మీ లింక్ నేను ఓపెన్ చేయను.',
               'outcome_te': '✅ నకిలీ లింక్ నొక్కకుండా తప్పించుకున్నారు. సమాచారం లీక్ కాలేదు.',
               'scammer_en': 'Sir, open the SMS link immediately and enter your PAN, Card details, and OTP, otherwise '
                             'your account will be closed permanently by this evening!',
               'villager_en': 'I know my local bank manager personally. If there is any KYC issue, I will visit the '
                              'branch tomorrow. I will not click your link.',
               'outcome_en': '✅ Prevented credential phishing! Account safe.'},
  'audio_text': {'te': 'బ్యాంకు ఖాతా ఆగిపోతుందని వచ్చే మెసేజ్ లలోని లింకులను ఎప్పుడూ నొక్కకండి. కేవైసీ అప్\u200cడేట్ '
                       'కోసం ఎల్లప్పుడూ మీ ఊరిలోని బ్యాంక్ బ్రాంచ్\u200cకు నేరుగా వెళ్లండి.',
                 'en': 'Never click on links claiming your bank account is blocked. For KYC updates, always visit your '
                       'nearest bank branch in person.'}},
 {'id': 'lottery_fraud',
  'icon': '🎁',
  'badge': 'ఆశ చూపి మోసం / Greed Trap',
  'color': '#d97706',
  'title': {'te': 'లాటరీ / బహుమతి మోసం (Fake Prize & Lottery Scam)', 'en': 'Fake Prize & Lottery Scam'},
  'short_desc': {'te': 'మీకు ₹25 లక్షల లాటరీ లేదా ఉచిత కారు వచ్చిందని వాట్సాప్\u200cలో మెసేజ్ పంపి ప్రాసెసింగ్ ఫీజు '
                       'పేరిట డబ్బులు లాగుతారు.',
                 'en': "Scammer claims you won a ₹25 Lakh lottery or car and asks for 'processing fees' or taxes "
                       'upfront.'},
  'what_happens': {'te': 'మీరు ఎన్నడూ కొనని లక్కీ డ్రాలో మీకు 25 లక్షలు వచ్చాయని కేబీసీ (KBC) లేదా కంపెనీ పేరుతో నకిలీ '
                         'చెక్కు ఫోటో పంపుతారు. ఆ డబ్బు మీకు రావాలంటే మొదట ₹5,000 లేదా ₹10,000 టాక్స్ కట్టాలని చెప్పి '
                         'డబ్బులు తీసుకొని ఫోన్ స్విచ్ఛాఫ్ చేస్తారు.',
                   'en': 'You receive a message with photos of fake cheques or celebrities claiming a prize. To '
                         'release the crores, you are asked to pay ₹5,000 - ₹25,000 as government tax or registration '
                         'fee. Once paid, the fraudster disappears.'},
  'workflow': [{'step': '1', 'icon': '🎉', 'te': 'లాటరీ తగిలిందని మెసేజ్', 'en': 'Wins fake lottery message'},
               {'step': '2', 'icon': '🧾', 'te': 'నకిలీ చెక్కు ఫోటో చూపిస్తారు', 'en': 'Shows fake award cheque'},
               {'step': '3', 'icon': '💰', 'te': 'టాక్స్ లేదా ఫీజు కట్టమంటారు', 'en': 'Demands tax/processing fee'},
               {'step': '4', 'icon': '🏃', 'te': 'డబ్బులు తీస్కొని పారిపోతారు!', 'en': 'Scammer vanishes forever!'}],
  'red_flags': {'te': ['మీరు టికెట్ కొనకుండానే లాటరీ తగలడం అసాధ్యం!',
                       'బహుమతి లేదా లాటరీ ఇవ్వడానికి ముందుగా డబ్బులు అడిగితే అది 100% మోసం.',
                       'వాట్సాప్\u200cలో వచ్చే విదేశీ నంబర్ కాల్స్ (+92 లేదా ఇతర దేశాల కోడ్\u200cలు).'],
                'en': ['You cannot win a lottery or raffle that you never participated in or bought tickets for.',
                       'Any prize that requires you to pay upfront fees or advance tax is guaranteed to be fake.',
                       'WhatsApp voice notes or messages sent from foreign country codes like +92.']},
  'what_to_do': {'te': ['అలాంటి మెసేజ్\u200cలను వెంటనే డిలీట్ చేయండి మరియు నంబర్\u200cను బ్లాక్ చేయండి.',
                        'ఎవరికీ ఒక్క రూపాయి కూడా అడ్వాన్స్ లేదా ప్రాసెసింగ్ ఫీజుగా పంపకండి.',
                        'మీ గ్రామస్తులను, స్నేహితులను కూడా ఈ మోసం గురించి అప్రమత్తం చేయండి.'],
                 'en': ['Delete such messages immediately and block the sender.',
                        'Never pay any advance money or fee to claim prizes or gifts.',
                        'Warn your family and villagers about fake lottery messages.']},
  'dialogue': {'scammer_te': 'అభినందనలు! మీ నంబర్\u200cకు ₹25,00,000 లాటరీ తగిలింది. గవర్నమెంట్ ఆర్బీఐ టాక్స్ కింద '
                             '₹12,500 ఈ యూపీఐ నంబర్\u200cకు పంపండి, అరగంటలో మీ అకౌంట్\u200cలో 25 లక్షలు పడతాయి!',
               'villager_te': 'నేను అసలు లాటరీ టికెట్టే కొనలేదు, నాకు డబ్బులు ఎలా వస్తాయి? ముందు డబ్బులు '
                              'కట్టమంటున్నారంటే ఇది మోసమే! నేను ఒక్క పైసా కూడా పంపను.',
               'outcome_te': '✅ అత్యాశకు పోకుండా మోసాన్ని గ్రహించారు. కష్టపడి సంపాదించిన డబ్బు మిగిలింది.',
               'scammer_en': 'Congratulations! You won ₹25,00,000 cash in KBC draw! Just transfer ₹12,500 government '
                             'clearance tax to this UPI ID, and the money will be in your account within 30 minutes!',
               'villager_en': 'I never bought any lottery ticket! Real prizes never ask for money upfront. This is a '
                              'scam and I will not send a single rupee!',
               'outcome_en': '✅ Greed trap rejected. Hard-earned money saved.'},
  'audio_text': {'te': 'మీరు టికెట్ కొనకుండా ఏ లాటరీ రాదు. బహుమతి ఇస్తామని చెప్పి ముందుగా డబ్బులు అడిగితే అది మోసగాళ్ల '
                       'పనే. ఎవరికీ పైసా కూడా పంపకండి.',
                 'en': 'You cannot win a lottery you never entered. If anyone asks for money before giving a prize, it '
                       'is definitely a fraud. Never pay.'}},
 {'id': 'screen_share_fraud',
  'icon': '📱',
  'badge': 'మొబైల్ హ్యాకింగ్ / Screen Hijack',
  'color': '#7c3aed',
  'title': {'te': 'స్క్రీన్ షేరింగ్ మోసం (Screen Sharing / AnyDesk Scam)', 'en': 'Screen Sharing / Remote App Scam'},
  'short_desc': {'te': 'బ్యాంక్ సమస్య సరిచేస్తామని చెప్పి AnyDesk, TeamViewer వంటి యాప్స్ డౌన్\u200cలోడ్ చేయించి మీ '
                       'ఫోన్ స్క్రీన్ చూస్తారు.',
                 'en': 'Scammer instructs you to install apps like AnyDesk or QuickSupport, allowing them to view your '
                       'screen and passwords.'},
  'what_happens': {'te': 'కరెంట్ బిల్ లేదా రీఛార్జ్ ఫెయిల్ అయిందని చెప్పి ఒక యాప్ (AnyDesk / RustDesk / QuickSupport) '
                         'ఇన్\u200cస్టాల్ చేయమంటారు. ఆ యాప్ కోడ్ చెప్పగానే మీ ఫోన్ స్క్రీన్ మొత్తం మోసగాడి '
                         'కంప్యూటర్\u200cలో కనిపిస్తుంది. మీరు బ్యాంక్ పిన్ కొట్టగానే చూసి మీ అకౌంట్ నుండి డబ్బులు '
                         'కాజేస్తారు.',
                   'en': 'Under the guise of fixing a failed recharge or bill, the scammer makes you install a '
                         'remote-viewing app and asks for a 9-digit code. Now they see your screen live, watch you '
                         'enter passwords and OTPs, and empty your funds.'},
  'workflow': [{'step': '1', 'icon': '🛠️', 'te': 'సమస్య సరిచేస్తామని ఫోన్', 'en': 'Offers technical assistance'},
               {'step': '2', 'icon': '📥', 'te': 'యాప్ ఇన్\u200cస్టాల్ చేయిస్తారు', 'en': 'Installs remote app'},
               {'step': '3',
                'icon': '👀',
                'te': 'మీ స్క్రీన్, పాస్\u200cవర్డ్లు చూస్తారు',
                'en': 'Views your screen live'},
               {'step': '4', 'icon': '💸', 'te': 'మీ కళ్ల ముందే డబ్బులు దొంగిలిస్తారు!', 'en': 'Money stolen live!'}],
  'red_flags': {'te': ['అపరిచిత వ్యక్తులు AnyDesk, TeamViewer, QuickSupport వంటి యాప్\u200cలను ఇన్\u200cస్టాల్ చేయమని '
                       'చెప్పడం.',
                       'యాప్\u200cలోని 9 అంకెల కోడ్ లేదా అనుమతులు (Permissions) ఇవ్వమని బలవంతం చేయడం.',
                       'ఫోన్\u200cలో ₹10 లేదా ₹1 టెస్ట్ పేమెంట్ చేయమని చెప్పడం.'],
                'en': ['Unknown caller insisting you install apps like AnyDesk, RustDesk, or TeamViewer.',
                       'Demanding the 9-digit access code generated on your screen.',
                       'Asking you to make a ₹1 or ₹10 test transfer while the app is active.']},
  'what_to_do': {'te': ['ఎవరి మాట వినీ అపరిచిత యాప్\u200cలను ఫోన్\u200cలో ఇన్\u200cస్టాల్ చేయవద్దు.',
                        'ఒకవేళ పొరపాటున ఇన్\u200cస్టాల్ చేస్తే వెంటనే ఇంటర్నెట్/వైఫై ఆపివేసి ఆ యాప్\u200cను వెంటనే '
                        'అన్\u200cఇన్\u200cస్టాల్ (Uninstall) చేయండి.',
                        'బ్యాంక్ ఖాతా లేదా ఏటీఎం కార్డును వెంటనే బ్లాక్ చేయండి.'],
                 'en': ['NEVER install any app on the instruction of an unknown telephone caller.',
                        'If installed accidentally, immediately turn off mobile internet/WiFi and delete the app.',
                        'Block your bank cards and net banking credentials immediately.']},
  'dialogue': {'scammer_te': "సార్ మీ గ్యాస్ సబ్సిడీ ఆగిపోయింది. ప్లేస్టోర్ నుండి 'AnyDesk' అనే ప్రభుత్వ సహాయ యాప్ "
                             'డౌన్\u200cలోడ్ చేసి అందులో వచ్చే 9 నంబర్లు చదవండి, నేను మీ ఫోన్ నుండి సర్వీస్ ఆన్ '
                             'చేస్తాను.',
               'villager_te': 'నా ఫోన్\u200cను వేరేవారికి కంట్రోల్ ఇచ్చే యాప్స్ ఎక్కించకూడదని పోలీసులు చెప్పారు. నేను '
                              'ఎలాంటి యాప్ ఇన్\u200cస్టాల్ చేయను!',
               'outcome_te': '✅ రిమోట్ యాప్ ఇన్\u200cస్టాల్ చేయకుండా ఫోన్ హ్యాకింగ్ నుండి కాపాడుకున్నారు.',
               'scammer_en': "Sir, your gas subsidy failed. Open PlayStore and install 'AnyDesk' government helper app "
                             'and tell me the 9 digits so I can activate your subsidy from my computer.',
               'villager_en': 'Police have warned us never to install screen sharing apps for strangers. I will NOT '
                              'install this app!',
               'outcome_en': '✅ Refused remote access. Phone and bank safe.'},
  'audio_text': {'te': 'ఎవరైనా ఫోన్ చేసి యానిడెస్క్ లేదా టీమ్\u200cవ్యూయర్ లాంటి యాప్\u200cలు ఎక్కించమంటే ఎట్టి '
                       'పరిస్థితుల్లోనూ ఎక్కించకండి. అవి ఎక్కిస్తే మీ ఫోన్ లోని రహస్యాలు మోసగాళ్లకు తెలిసిపోతాయి.',
                 'en': 'Never install remote control apps like AnyDesk on the instructions of any caller. They can '
                       'view your passwords and steal your money.'}},
 {'id': 'digital_arrest',
  'icon': '🚨',
  'badge': 'తీవ్ర భయం సృష్టించే మోసం / Severe',
  'color': '#991b1b',
  'title': {'te': 'డిజిటల్ అరెస్ట్ మోసం (Digital Arrest Scam)', 'en': 'Digital Arrest Scam (Fake Police / CBI Call)'},
  'short_desc': {'te': 'పోలీసులు లేదా సీబీఐ అధికారులమని వీడియో కాల్ చేసి బెదిరించి, కేసు నుండి తప్పించాలంటే డబ్బులు '
                       'కట్టమంటారు.',
                 'en': 'Scammers pose in police/CBI uniforms over video call, claiming your Aadhaar is linked to '
                       'crimes, demanding huge money.'},
  'what_happens': {'te': 'మోసగాళ్లు పోలీస్ యూనిఫాం వేసుకొని లేదా నకిలీ పోలీస్ స్టేషన్ సెటప్\u200cలో వీడియో కాల్ '
                         'చేస్తారు. మీ ఆధార్ కార్డుపై డ్రగ్స్ పార్శిల్ వచ్చిందని, లేదా మనీ లాండరింగ్ జరిగిందని '
                         "భయపెడతారు. 'డిజిటల్ అరెస్ట్' చేసామని గదిలో నుండి బయటకు వెళ్ళనివ్వకుండా బెదిరించి లక్షల "
                         'రూపాయలు బదిలీ చేయిస్తారు.',
                   'en': 'Criminals wear fake police uniforms and video call you from fake office setups. They claim a '
                         'parcel with illegal drugs or passports was booked in your name. They claim you are under '
                         "'Digital Arrest' and force you to transfer your savings to 'government clearance accounts'."},
  'workflow': [{'step': '1',
                'icon': '👮',
                'te': 'పోలీస్ డ్రెస్\u200cలో వీడియో కాల్',
                'en': 'Video call in police uniform'},
               {'step': '2', 'icon': '⚠️', 'te': 'మీపై కేసు ఉందని భయపెడతారు', 'en': 'Threatens crime charges'},
               {'step': '3', 'icon': '🔒', 'te': 'గది నుండి కదలవద్దని బెదిరింపు', 'en': "Claims 'Digital Arrest'"},
               {'step': '4',
                'icon': '💸',
                'te': 'కేసు మాఫీ పేరిట డబ్బులు దోపిడీ!',
                'en': 'Extorts money to settle case!'}],
  'red_flags': {'te': ["చట్టంలో 'డిజిటల్ అరెస్ట్' అనే పదమే లేదు! భారతీయ చట్టంలో ఫోన్\u200cలో లేదా వీడియో కాల్\u200cలో "
                       'అరెస్ట్ చేయడం ఉండదు.',
                       'పోలీసులు లేదా సీబీఐ ఎప్పుడూ వీడియో కాల్స్\u200cలో విచారణ జరిపి డబ్బులు అడగరు.',
                       'ఎవరికీ చెప్పకూడదని, కుటుంబ సభ్యులకు కూడా తెలియనివ్వవద్దని ఒత్తిడి చేయడం.'],
                'en': ["There is NO such thing as 'Digital Arrest' in Indian law! No agency can arrest anyone over a "
                       'phone or video call.',
                       'Real police, CBI, ED, or judges NEVER demand money transfers to verify your innocence.',
                       'Scammers forbid you from disconnecting or informing your family members.']},
  'what_to_do': {'te': ['భయపడకండి! కాల్\u200cను వెంటనే కట్ చేయండి.',
                        'వెంటనే మీ స్థానిక గ్రామ పోలీస్ స్టేషన్\u200cకు లేదా 1930 హెల్ప్\u200cలైన్\u200cకు సమాచారం '
                        'ఇవ్వండి.',
                        'ఎలాంటి గుర్తుతెలియని బ్యాంకు ఖాతాలకూ డబ్బులు పంపవద్దు.'],
                 'en': ['Do NOT panic! Disconnect the call immediately.',
                        'Inform your nearest local police station or dial 1930 without delay.',
                        "Never transfer your money to any unknown 'security verification' accounts."]},
  'dialogue': {'scammer_te': 'నేను ముంబై క్రైమ్ బ్రాంచ్ డీఎస్పీని! మీ ఆధార్ కార్డుపై విదేశాలకు డ్రగ్స్ పంపారు. మీరు '
                             'డిజిటల్ అరెస్ట్\u200cలో ఉన్నారు. ఫోన్ కట్ చేస్తే పోలీసులు మీ ఇంటికి వచ్చి పట్టుకుంటారు. '
                             'కేసు క్లియర్ కావాలంటే ₹50,000 ప్రభుత్వ సెక్యూరిటీ డిపాజిట్ చేయండి!',
               'villager_te': 'వీడియో కాల్\u200cలో అరెస్ట్ చేయడం చట్టంలో లేదని నాకు తెలుసు. మా ఊరి ఎస్ఐ గారితో కలిసి '
                              'నేను స్వయంగా స్టేషన్\u200cకు వస్తాను. మీ బెదిరింపులకు నేను భయపడను!',
               'outcome_te': '✅ ధైర్యంగా నిలబడి నకిలీ పోలీసు బెదిరింపులను తిప్పికొట్టారు.',
               'scammer_en': 'I am Crime Branch DSP! An illegal narcotics parcel was booked using your Aadhaar. You '
                             'are under Digital Arrest! If you cut the call, police will raid your house. Transfer '
                             '₹50,000 security deposit immediately to prove innocence!',
               'villager_en': 'There is no such thing as Digital Arrest! I will go straight to my local police station '
                              'with our village elders. I will not pay a single rupee!',
               'outcome_en': '✅ Called the bluff of fake police. Zero financial loss.'},
  'audio_text': {'te': 'భారతీయ చట్టంలో వీడియో కాల్ ద్వారా డిజిటల్ అరెస్ట్ చేయడం అనేది ఉండదు. ఎవరైనా పోలీసులు లేదా '
                       'జడ్జి అని చెప్పి వీడియో కాల్ చేసి డబ్బులు అడిగితే భయపడకుండా వెంటనే కాల్ కట్ చేసి 1930 కి ఫోన్ '
                       'చేయండి.',
                 'en': 'There is no provision for Digital Arrest in Indian law. No police or judge will arrest you '
                       'over video call or ask for money. Stay calm and dial 1930.'}},
 {'id': 'job_fraud',
  'icon': '💼',
  'badge': 'ఉద్యోగాల పేరుతో మోసం / Job Scam',
  'color': '#0284c7',
  'title': {'te': 'ఆన్\u200cలైన్ పార్ట్ టైమ్ జాబ్ మోసం (Work From Home Scam)',
            'en': 'Online Job & Part-Time Task Scam'},
  'short_desc': {'te': 'రోజూ ఇంట్లో ఉండి యూట్యూబ్ లైక్\u200cలు కొడితే లేదా రివ్యూలు రాస్తే ₹3,000 వస్తుందని '
                       'టెలిగ్రామ్\u200cలో మోసం చేస్తారు.',
                 'en': 'Promises easy money for liking YouTube videos or rating hotels, then steals your deposit '
                       'money.'},
  'what_happens': {'te': "వాట్సాప్ లేదా టెలిగ్రామ్\u200cలో మెసేజ్ వస్తుంది: 'ఇంట్లో ఉండే సులభంగా రోజుకు ₹2000 "
                         "సంపాదించండి'. మొదట 2 వీడియోలు లైక్ చేయగానే నిజంగానే ₹200 పంపి నమ్మకం కలిగిస్తారు. ఆ తర్వాత "
                         'పెద్ద లాభం కోసం ₹10,000, ₹50,000 టాస్క్ అమౌంట్ కట్టమని చెప్పి, డబ్బులు తీసుకుని గ్రూప్ నుండి '
                         'తీసేస్తారు.',
                   'en': 'You get a message promising ₹2,000/day for liking videos. Initially they credit small '
                         "amounts like ₹150 to build trust. Later they demand 'prepaid task investments' of ₹10,000 to "
                         '₹1 Lakh to unlock your profit, and freeze everything.'},
  'workflow': [{'step': '1', 'icon': '💬', 'te': 'వాట్సాప్\u200cలో జాబ్ ఆఫర్ మెసేజ్', 'en': 'Job offer message arrives'},
               {'step': '2', 'icon': '👍', 'te': 'చిన్న టాస్క్\u200cలకు ₹150 పంపుతారు', 'en': 'Pays ₹150 for tiny task'},
               {'step': '3',
                'icon': '💸',
                'te': 'పెద్ద టాస్క్ కోసం డబ్బులు కట్టమంటారు',
                'en': 'Demands high prepaid deposit'},
               {'step': '4',
                'icon': '🚫',
                'te': 'డబ్బులు కాజేసి బ్లాక్ చేస్తారు!',
                'en': 'Blocks account and vanishes!'}],
  'red_flags': {'te': ['కేవలం వీడియోలు లైక్ కొడితే వేల రూపాయలు ఇస్తామనే అబద్ధపు ప్రకటనలు.',
                       'ఉద్యోగం లేదా టాస్క్ పూర్తి చేయడానికి మీరే ముందు డబ్బులు డిపాజిట్ చేయాలని చెప్పడం.',
                       'టెలిగ్రామ్ గ్రూపుల్లో గుర్తుతెలియని వ్యక్తులు కోట్లలో లాభాలు వచ్చాయని పెట్టే '
                       'స్క్రీన్\u200cషాట్లు.'],
                'en': ['Unrealistic promises of high daily earnings for brainless tasks like liking videos.',
                       "Requiring candidates to deposit 'prepaid funds' or 'security fees' to unlock salary.",
                       'Communication exclusively managed through anonymous Telegram or WhatsApp groups.']},
  'what_to_do': {'te': ['ముందు డబ్బులు కట్టమనే ఏ ఉద్యోగ ఆఫర్\u200cనూ నమ్మవద్దు.',
                        'అపరిచిత టెలిగ్రామ్ లేదా వాట్సాప్ ఇన్వెస్ట్\u200cమెంట్ గ్రూపుల నుండి వెంటనే లెఫ్ట్ అవ్వండి.',
                        'ఎవరికీ టాస్క్ అమౌంట్ పేరుతో డబ్బులు పంపకండి.'],
                 'en': ['Never pay money to get a job. Legitimate companies never charge applicants.',
                        'Exit and report anonymous Telegram and WhatsApp task groups immediately.',
                        'Never invest your personal savings in unverified online task platforms.']},
  'dialogue': {'scammer_te': 'మేడమ్ గారూ, మా కంపెనీలో 3 హోటల్ రివ్యూలు రాస్తే మీకు ₹3,000 వస్తాయి. సూపర్ టాస్క్ కోసం '
                             'ముందు ₹5,000 డిపాజిట్ చేస్తే గంటలో ₹8,000 వాపస్ ఇస్తాం!',
               'villager_te': 'ఉద్యోగం ఇచ్చేవారు జీతం ఇస్తారు కానీ ముందు డబ్బులు కట్టమని అడగరు. ఇదంతా మోసమని నాకు '
                              'అర్థమైంది, నేను చేరను.',
               'outcome_te': '✅ నకిలీ జాబ్ ఆఫర్\u200cను తిరస్కరించి డబ్బులు కాపాడుకున్నారు.',
               'scammer_en': 'Madam, just rate 3 hotels on Google to earn ₹3,000 today. For the VIP task, deposit '
                             '₹5,000 now and we will refund ₹8,000 within 1 hour!',
               'villager_en': 'Genuine employers pay salary to workers; they never ask workers to pay money upfront. '
                              'This is a fraud and I will not join!',
               'outcome_en': '✅ Refused fake part-time task scam.'},
  'audio_text': {'te': 'వీడియోలు లైక్ కొడితే లేదా రివ్యూలు రాస్తే వేల రూపాయలు వస్తాయనే ఉద్యోగాలన్నీ మోసాలే. ఉద్యోగం '
                       'కోసం ముందుగా డబ్బులు అడిగితే ఒక్క రూపాయి కూడా కట్టకండి.',
                 'en': 'Tasks offering thousands of rupees just for liking videos are traps. Never pay money upfront '
                       'to get an online job.'}},
 {'id': 'investment_fraud',
  'icon': '📈',
  'badge': 'అధిక వడ్డీ ఆశ / High Profit Scam',
  'color': '#059669',
  'title': {'te': 'నకిలీ పెట్టుబడి మోసం (Fake Investment Scam)', 'en': 'Fake Investment & Stock Trading Scam'},
  'short_desc': {'te': 'నెలకు డబుల్ డబ్బులు లేదా రోజూ 10% లాభం వస్తుందని నకిలీ యాప్స్ ద్వారా పెట్టుబడులు పెట్టించి '
                       'ముంచుతారు.',
                 'en': 'Promises unrealistic double returns in days through fake crypto or trading apps, then locks '
                       'your money.'},
  'what_happens': {'te': "సోషల్ మీడియాలో '₹1,000 పెడితే నెలకు ₹10,000' అని ప్రకటనలు చూపిస్తారు. మీరు డౌన్\u200cలోడ్ "
                         'చేసుకునే నకిలీ యాప్\u200cలో మీ డబ్బులు లక్షలుగా పెరిగినట్లు బొమ్మలు చూపిస్తారు. కానీ మీరు ఆ '
                         "డబ్బును విత్\u200cడ్రా చేసుకోబోతే 'మరింత టాక్స్ కట్టాలి' అని మరిన్ని డబ్బులు లాగి "
                         'యాప్\u200cను మూసివేస్తారు.',
                   'en': 'Advertised as guaranteed stock tips or crypto goldmines. Fraudulent apps show fake graphical '
                         'profits multiplying on screen. When victims attempt withdrawal, the scammer demands 30% '
                         'withdrawal fees before vanishing.'},
  'workflow': [{'step': '1', 'icon': '📢', 'te': 'డబుల్ డబ్బుల ప్రకటన', 'en': 'Double-money advertisement'},
               {'step': '2', 'icon': '📲', 'te': 'నకిలీ ట్రేడింగ్ యాప్ ఎక్కిస్తారు', 'en': 'Installs fake trading app'},
               {'step': '3',
                'icon': '📊',
                'te': 'యాప్\u200cలో నకిలీ లాభాలు కనిపిస్తాయి',
                'en': 'Displays fake screen profits'},
               {'step': '4', 'icon': '🔒', 'te': 'డబ్బులు రావు, అకౌంట్ బంద్!', 'en': 'Withdrawals blocked forever!'}],
  'red_flags': {'te': ['కొద్ది రోజుల్లోనే డబ్బులు రెట్టింపు అవుతాయనే వాగ్దానాలు (ఏ ప్రభుత్వ బ్యాంక్ కూడా అలా ఇవ్వదు).',
                       'ప్లేస్టోర్\u200cలో కాకుండా వాట్సాప్ లేదా వెబ్\u200cసైట్ ద్వారా APK ఫైల్ డౌన్\u200cలోడ్ చేయమని '
                       'చెప్పడం.',
                       'సెబీ (SEBI) లేదా ఆర్బీఐ (RBI) అనుమతి లేని అనధికారిక ప్లాట్\u200cఫారమ్\u200cలు.'],
                'en': ['Guaranteed promises of doubling money within weeks or 10% daily profits.',
                       'Unregistered APK files shared over WhatsApp instead of official app stores.',
                       'Lack of SEBI or RBI registration for fund management.']},
  'what_to_do': {'te': ['అధిక లాభాల పేరుతో వచ్చే పథకాలను అస్సలు నమ్మవద్దు.',
                        'కేవలం పోస్టాఫీసు, అధికారిక బ్యాంకులు లేదా ప్రభుత్వ ధ్రువీకరించిన పథకాలలోనే పొదుపు చేసుకోండి.',
                        'వాట్సాప్\u200cలో వచ్చే ఏపికె (APK) ఫైల్స్\u200cను ఎప్పుడూ ఇన్\u200cస్టాల్ చేయవద్దు.'],
                 'en': ['Never trust get-rich-quick investment schemes.',
                        'Invest only through regulated banks, Post Offices, or registered mutual funds.',
                        'Never install unknown APK files received on chat apps.']},
  'dialogue': {'scammer_te': 'అన్నా, ఈ యాప్\u200cలో ₹10,000 పెడితే ప్రతివారం ₹4,000 వడ్డీ వస్తుంది. మా గ్రూప్\u200cలో '
                             'అందరూ లక్షలు సంపాదించారు. ఇప్పుడే పెట్టుబడి పెట్టండి!',
               'villager_te': 'బ్యాంకులో కూడా ఇంత వడ్డీ రాదు. ఇంత సులభంగా డబ్బులు వచ్చే మార్గం ఉండదు. కష్టపడి '
                              'సంపాదించిన డబ్బును ఇలాంటి మోసగాళ్లకు ఇవ్వను.',
               'outcome_te': '✅ అత్యాశను జయించి జీవితకాల సంపాదనను కాపాడుకున్నారు.',
               'scammer_en': 'Invest just ₹10,000 in this secret trading app to earn ₹4,000 profit every single week! '
                             'All village members are getting rich. Join today!',
               'villager_en': 'Even authorized national banks do not offer such returns. High return without risk is a '
                              'complete scam. I will keep my money safe!',
               'outcome_en': '✅ Avoided predatory ponzi trap.'},
  'audio_text': {'te': 'తక్కువ రోజుల్లో డబ్బులు రెట్టింపు అవుతాయని చెప్పే ఏ పథకాన్నీ నమ్మకండి. ప్రభుత్వ బ్యాంకులు లేదా '
                       'పోస్టాఫీసులలో మాత్రమే మీ డబ్బును భద్రంగా దాచుకోండి.',
                 'en': 'Never believe schemes promising to double your wealth overnight. Save your hard-earned money '
                       'only in recognized banks or post offices.'}},
 {'id': 'fake_customer_care',
  'icon': '📞',
  'badge': 'గూగుల్ సెర్చ్ ట్రాప్ / Search Trap',
  'color': '#0369a1',
  'title': {'te': 'నకిలీ కస్టమర్ కేర్ మోసం (Fake Customer Care Scam)', 'en': 'Fake Customer Care Search Scam'},
  'short_desc': {'te': 'గూగుల్\u200cలో బ్యాంక్ లేదా గ్యాస్ నంబర్ వెతికినప్పుడు మోసగాళ్ల నకిలీ నంబర్లు వచ్చి మోసపోతారు.',
                 'en': 'Searching for bank or gas numbers on Google leads to fraudster numbers posted on fake pages.'},
  'what_happens': {'te': "గూగుల్ సెర్చ్\u200cలో 'SBI కస్టమర్ కేర్' లేదా 'PhonePe హెల్ప్\u200cలైన్' అని వెతికినప్పుడు "
                         'మోసగాళ్లు పెట్టిన మొబైల్ నంబర్ కనిపిస్తుంది. ఆ నంబర్\u200cకు ఫోన్ చేయగానే మీ సమస్య '
                         'పరిష్కరిస్తామని చెప్పి ఓటీపీ లేదా రీఫండ్ లింక్ ద్వారా మీ అకౌంట్ ఖాళీ చేస్తారు.',
                   'en': 'When searching for helpline numbers on Google, fraudsters post their personal phone numbers '
                         'pretending to be PhonePe, SBI, or Gas agencies. Calling them leads to fake refunds and '
                         'drained bank accounts.'},
  'workflow': [{'step': '1',
                'icon': '🔍',
                'te': 'గూగుల్\u200cలో హెల్ప్\u200cలైన్ వెతుకుతారు',
                'en': 'Searches helpline on Google'},
               {'step': '2', 'icon': '📞', 'te': 'నకిలీ నంబర్\u200cకు కాల్ వెళుతుంది', 'en': "Calls fraudster's number"},
               {'step': '3', 'icon': '🔗', 'te': 'రీఫండ్ లింక్ పంపిస్తారు', 'en': 'Sends fake refund link/app'},
               {'step': '4',
                'icon': '💸',
                'te': 'పరిష్కారం బదులు అకౌంట్ లూటీ!',
                'en': 'Funds drained instead of help!'}],
  'red_flags': {'te': ['కస్టమర్ కేర్ నంబర్ సాధారణ మొబైల్ నంబర్ (10 అంకెలు) లాగా ఉండటం.',
                       'రీఫండ్ డబ్బులు ఇవ్వడానికి మీ ఏటీఎం పిన్ లేదా యూపీఐ పిన్ అడగడం.',
                       'గూగుల్ రివ్యూలలో లేదా మ్యాప్స్\u200cలో గుర్తుతెలియని వ్యక్తులు రాసిన ఫోన్ నంబర్లు.'],
                'en': ['Customer care listed as an ordinary 10-digit private mobile number instead of an 1800 '
                       'toll-free number.',
                       "Helpline agent asking for your card PIN or sending payment requests to 'refund' money.",
                       'Unverified numbers retrieved from Google Maps listings.']},
  'what_to_do': {'te': ['హెల్ప్\u200cలైన్ నంబర్ల కోసం గూగుల్\u200cలో వెతకవద్దు. మీ బ్యాంక్ పాస్\u200cబుక్ లేదా ఏటీఎం '
                        'కార్డు వెనుక ఉన్న నంబర్\u200cను మాత్రమే చూడండి.',
                        "PhonePe లేదా GPay లో సహాయం కోసం యాప్ లోపల ఉండే 'Help' ఆప్షన్ మాత్రమే వాడండి.",
                        'ఎప్పుడూ రిఫండ్ రావడానికి పిన్ కొట్టకండి.'],
                 'en': ['Never search for bank helplines on Google search. Always use numbers printed on passbooks or '
                        'cards.',
                        "For PhonePe/GPay issues, use only the in-app official 'Help' support tickets.",
                        'Remember: Refunds never require you to enter a UPI PIN.']},
  'dialogue': {'scammer_te': 'నమస్కారం, నేను PhonePe కస్టమర్ కేర్ మేనేజర్\u200cని. మీ ఆగిపోయిన ₹2,000 రీఫండ్ చేయడానికి '
                             'నేను ఒక లింక్ పంపుతున్నాను, దానిపై క్లిక్ చేసి పిన్ కొట్టండి వెంటనే డబ్బులు వస్తాయి!',
               'villager_te': 'కస్టమర్ కేర్ వారు ఎప్పుడూ పిన్ కొట్టమని అడగరని నాకు తెలుసు. నేను ఫోన్\u200cపే యాప్ లోపల '
                              'నుంచే సపోర్ట్ తీసుకుంటాను. మీతో మాట్లాడను.',
               'outcome_te': '✅ నకిలీ నంబర్\u200cను పసిగట్టి ఆర్థిక నష్టం తప్పించుకున్నారు.',
               'scammer_en': 'Hello, I am PhonePe Customer Care Manager. To refund your failed ₹2,000 transaction, I '
                             'sent a payment link. Just click it and enter your PIN to get refund instantly!',
               'villager_en': 'Official support never tells users to enter a PIN to receive a refund. I will raise a '
                              'complaint only through the PhonePe app itself!',
               'outcome_en': '✅ Recognized fake support scam.'},
  'audio_text': {'te': 'గూగుల్\u200cలో కనిపించే ఫోన్ నంబర్లన్నీ నమ్మకండి. బ్యాంకు నంబర్ల కోసం మీ పాస్\u200cబుక్ లేదా '
                       'ఏటీఎం కార్డు వెనుక ఉన్న అధికారిక నంబర్లను మాత్రమే ఉపయోగించండి.',
                 'en': 'Do not trust helpline numbers found on Google search. Always call the official toll-free '
                       'numbers printed on your bank passbook or ATM card.'}},
 {'id': 'sim_swap_fraud',
  'icon': '📲',
  'badge': 'నెట్\u200cవర్క్ మోసం / Identity Hijack',
  'color': '#4f46e5',
  'title': {'te': 'సిమ్ స్వాప్ మోసం (SIM Swap Fraud)', 'en': 'SIM Swap & 5G Upgrade Fraud'},
  'short_desc': {'te': 'మీ సిమ్ 5G కి అప్\u200cగ్రేడ్ చేస్తామని చెప్పి మీ సిమ్ కార్డును డూప్లికేట్ చేసి మీ బ్యాంక్ '
                       'ఓటీపీలను దొంగిలిస్తారు.',
                 'en': 'Scammer poses as telecom agent to upgrade SIM to 5G, cloning your SIM to hijack banking OTPs.'},
  'what_happens': {'te': 'ఎయిర్\u200cటెల్ లేదా జియో కంపెనీ నుండి ఫోన్ చేస్తున్నామని, మీ 4G సిమ్ త్వరలో పనిచేయదని, 5G '
                         'కి మార్చడానికి ఎస్ఎంఎస్ పంపమని అడుగుతారు. మీరు ఆ ఎస్ఎంఎస్ పంపగానే మీ ఫోన్ సిగ్నల్ పూర్తిగా '
                         'పోతుంది. మోసగాడు మీ నంబర్\u200cతో కొత్త సిమ్ ఆన్ చేసి మీ బ్యాంక్ ఓటీపీలన్నీ పొంది డబ్బులు '
                         'ఖాళీ చేస్తాడు.',
                   'en': 'Scammer calls pretending to be telecom staff offering free 5G SIM upgrades. They trick you '
                         'into sending an SMS with their 20-digit SIM number. Your phone immediately loses network, '
                         'while the scammer receives all your banking OTPs.'},
  'workflow': [{'step': '1', 'icon': '📶', 'te': '5G అప్\u200cగ్రేడ్ పేరిట కాల్', 'en': '5G upgrade call received'},
               {'step': '2', 'icon': '📩', 'te': 'ఎస్ఎంఎస్ పంపమని కోరతారు', 'en': 'Tricked into sending SMS'},
               {'step': '3', 'icon': '📵', 'te': 'మీ ఫోన్ సిగ్నల్ పోతుంది', 'en': 'Your phone loses network'},
               {'step': '4', 'icon': '💸', 'te': 'మోసగాడి వద్దకు మీ ఓటీపీలు!', 'en': 'OTPs intercepted by fraudster!'}],
  'red_flags': {'te': ['టెలికాం సిబ్బంది అని చెప్పి 121 లేదా 1900 కు ప్రత్యేక కోడ్\u200cతో మెసేజ్ పంపమని చెప్పడం.',
                       'మీ సిమ్ కార్డు వెనుక ఉండే 20 అంకెల నంబర్ అడగడం.',
                       'ఎలాంటి కారణం లేకుండా మీ మొబైల్ సిగ్నల్ గంటల తరబడి పూర్తిగా రాకపోవడం.'],
                'en': ['Caller asking you to forward or send SMS containing codes to 121 or 1900.',
                       'Demanding the 20-digit unique number printed on the back of your SIM card.',
                       'Unexplained total loss of cellular signal and network bars for several hours.']},
  'what_to_do': {'te': ['ఫోన్ ద్వారా ఎప్పుడూ సిమ్ అప్\u200cగ్రేడ్ ప్రక్రియలను చేయవద్దు.',
                        'సిమ్ అప్\u200cగ్రేడ్ కోసం మీ సమీప అధికారిక జియో/ఎయిర్\u200cటెల్ స్టోర్\u200cకు స్వయంగా '
                        'వెళ్లండి.',
                        'అకస్మాత్తుగా సిగ్నల్ పోతే వెంటనే టెలికాం ఆఫీస్ లేదా బ్యాంక్\u200cకు తెలియజేయండి.'],
                 'en': ['Never initiate SIM card upgrades over phone instructions.',
                        'Visit your local authorized Jio/Airtel/BSNL store in person with Aadhaar for SIM changes.',
                        'If phone signals disappear suddenly, immediately contact your network provider and bank.']},
  'dialogue': {'scammer_te': 'సార్, జియో టవర్ ఆఫీస్ నుండి మాట్లాడుతున్నాను. రేపటి నుండి మీ 4G సిమ్ పని చేయదు. ఉచిత 5G '
                             "కోసం 'SIM 123456789' అని 121 కి ఎస్ఎంఎస్ పంపండి!",
               'villager_te': 'నేను ఫోన్\u200cలో ఎలాంటి ఎస్ఎంఎస్ పంపను. నాకు ఏమైనా కావాలంటే నేను నేరుగా మా ఊరి '
                              'బజారులోని జియో దుకాణానికి వెళ్తాను.',
               'outcome_te': '✅ సిమ్ స్వాప్ కాకుండా తన మొబైల్ నంబర్ మరియు బ్యాంక్ అకౌంట్ కాపాడుకున్నారు.',
               'scammer_en': 'Sir, calling from Jio tower team. Your 4G will stop tomorrow. To activate 5G free of '
                             'cost, just forward SMS with this code to 121 right now!',
               'villager_en': 'I will not send any SMS on phone instructions. If I need a 5G SIM, I will walk into the '
                              'authorized telecom store myself.',
               'outcome_en': '✅ Thwarted SIM swap attack.'},
  'audio_text': {'te': 'ఎవరైనా ఫోన్ చేసి 5G సిమ్ ఇస్తామని మెసేజ్\u200cలు పంపమంటే పంపకండి. సిమ్ మార్చడానికి ఎల్లప్పుడూ '
                       'నేరుగా కంపెనీ దుకాణానికి మాత్రమే వెళ్లండి.',
                 'en': 'Never send text messages to upgrade your SIM over phone calls. Always visit the authorized '
                       'telecom store directly for SIM upgrades.'}},
 {'id': 'phishing_links',
  'icon': '🔗',
  'badge': 'నకిలీ లింకులు / Trap Links',
  'color': '#c026d3',
  'title': {'te': 'నకిలీ లింకులు & ఫిషింగ్ మెసేజ్\u200cలు (Phishing SMS Scam)', 'en': 'Phishing & Fake Message Links'},
  'short_desc': {'te': 'ఉచిత రీఛార్జ్, రేషన్ బియ్యం బోనస్ లేదా కరెంట్ బిల్ ఆగిపోతుందని వచ్చే నకిలీ లింకులు.',
                 'en': 'SMS links offering free recharges, electricity bill warnings, or government bonuses to steal '
                       'passwords.'},
  'what_happens': {'te': "వాట్సాప్ లేదా ఎస్ఎంఎస్\u200cలో 'ఈ రాత్రి 9 గంటలకు మీ కరెంట్ కట్ అవుతుంది, బిల్ "
                         "చెల్లించడానికి ఈ లింక్ నొక్కండి' లేదా 'ప్రభుత్వ పథకం కింద అందరికీ ₹5,000 ఉచితం' అని లింక్ "
                         'పంపుతారు. ఆ లింక్ నొక్కితే వైరస్ ఎక్కడం లేదా మీ బ్యాంక్ వివరాలు దొంగిలించబడతాయి.',
                   'en': 'Scammers send urgent SMS messages claiming your electricity power will be disconnected '
                         'tonight, or offering free ₹5,000 government subsidy. Clicking the link downloads malware or '
                         'captures your net banking credentials.'},
  'workflow': [{'step': '1',
                'icon': '⚡',
                'te': 'కరెంట్ కట్ లేదా ఫ్రీ బోనస్ మెసేజ్',
                'en': 'Electricity cutoff fake alert'},
               {'step': '2', 'icon': '🔗', 'te': 'అనుమానాస్పద లింక్ ఉంటుంది', 'en': 'Contains suspicious link'},
               {'step': '3',
                'icon': '⚠️',
                'te': 'లింక్ నొక్కితే వైరస్ లేదా నకిలీ ఫారమ్',
                'en': 'Opens malware or phishing page'},
               {'step': '4',
                'icon': '💸',
                'te': 'బ్యాంక్ అకౌంట్ నుండి డబ్బుల దోపిడీ!',
                'en': 'Secret credentials harvested!'}],
  'red_flags': {'te': ["వ్యక్తిగత మొబైల్ నంబర్ నుండి 'విద్యుత్ శాఖ' లేదా 'బ్యాంకు' పేరిట వచ్చే ఎస్ఎంఎస్\u200cలు.",
                       'లింక్ అడ్రస్\u200cలలో తప్పు స్పెల్లింగ్\u200cలు ఉండటం (ఉదాహరణకు: sbi-secure-update.xyz).',
                       'ఉచితంగా రీఛార్జ్ లేదా ఉచిత స్మార్ట్\u200cఫోన్ ఇస్తామని చెప్పే వాట్సాప్ ఫార్వర్డ్ '
                       'మెసేజ్\u200cలు.'],
                'en': ['Official utility or bank alerts originating from ordinary 10-digit mobile phone numbers.',
                       'Strange website domains ending in .xyz, .top, .live, or misspelled bank names.',
                       'WhatsApp viral forwards promising free government laptops or ₹500 recharges.']},
  'what_to_do': {'te': ['అపరిచిత మెసేజ్\u200cలలోని ఎలాంటి లింకులను క్లిక్ చేయవద్దు.',
                        'విద్యుత్ బిల్లుల కోసం మీ ఊరి విద్యుత్ శాఖ కార్యాలయంలో లేదా అధికారిక యాప్\u200cలలో మాత్రమే '
                        'చెల్లించండి.',
                        'అలాంటి సందేశాలను వెంటనే డిలీట్ చేయండి, వేరే గ్రూపులకు ఫార్వర్డ్ చేయకండి.'],
                 'en': ['NEVER tap on links found in unverified SMS or WhatsApp forwards.',
                        'Pay utility bills only at local electricity sub-stations or via official authorized '
                        'government apps.',
                        'Delete suspicious messages and never forward them to village groups.']},
  'dialogue': {'scammer_te': 'డియర్ కస్టమర్, మీ గత నెల కరెంట్ బిల్ అప్\u200cడేట్ కాలేదు. ఈ రాత్రి 9:30 గంటలకు మీ ఇంటి '
                             'విద్యుత్ సరఫరా నిలిపివేయబడుతుంది. వెంటనే ఈ లింక్ నొక్కి ₹11 చెల్లించండి!',
               'villager_te': 'మా కరెంట్ బిల్లు నేను ఎప్పుడూ మా ఊరి సచివాలయంలోనే కడతాను. ఫోన్\u200cలో వచ్చిన లింకులు '
                              'నేను నొక్కను.',
               'outcome_te': '✅ నకిలీ లింక్ నొక్కకుండా స్మార్ట్\u200cఫోన్ మరియు బ్యాంక్ ఖాతాను కాపాడుకున్నారు.',
               'scammer_en': 'Dear consumer, your electricity bill was not updated. Power will be cut at 9:30 PM '
                             'tonight. Tap this link immediately and pay ₹11 to avoid disconnection!',
               'villager_en': 'I always pay our electricity bill at our Village Secretariat. I will not click random '
                              'text links on my phone!',
               'outcome_en': '✅ Phishing link ignored safely.'},
  'audio_text': {'te': 'కరెంట్ కట్ అవుతుందని లేదా ఉచితంగా డబ్బులు ఇస్తామని వచ్చే ఎలాంటి లింకులను నొక్కకండి. లింక్ '
                       'నొక్కితే మీ ఫోన్ మోసగాళ్ల చేతుల్లోకి వెళ్ళిపోతుంది.',
                 'en': 'Never tap on SMS links warning of electricity disconnections or free money gifts. Clicking '
                       'them gives hackers access to your phone.'}},
 {'id': 'loan_fraud',
  'icon': '💰',
  'badge': 'బ్లాక్\u200cమెయిల్ మోసం / Extortion App',
  'color': '#e11d48',
  'title': {'te': 'నకిలీ లోన్ యాప్స్ మోసం (Illegal Loan App Scam)', 'en': 'Illegal Loan App Blackmail Scam'},
  'short_desc': {'te': 'ఆధార్ కార్డుతో నిమిషాల్లో లోన్ ఇస్తామని చెప్పి మీ ఫోటోలు, కాంటాక్టులు దొంగిలించి అసభ్యంగా '
                       'మార్చి బ్లాక్\u200cమెయిల్ చేస్తారు.',
                 'en': 'Instant loan apps that steal your contact list and photos, then blackmail you and your '
                       'relatives with morphed images.'},
  'what_happens': {'te': 'కేవలం పాన్, ఆధార్ కార్డుతో ₹10,000 లోన్ 5 నిమిషాల్లో ఇస్తామని ప్రకటనలు ఇస్తారు. యాప్ '
                         'డౌన్\u200cలోడ్ చేయగానే మీ ఫోన్\u200cలోని కాంటాక్ట్\u200cలు, గ్యాలరీ ఫోటోలను కాపీ '
                         'చేసుకుంటారు. కేవలం ₹3,000 చేతికి ఇచ్చి, 5 రోజులకే ₹15,000 కట్టాలని, లేకపోతే మీ ఫోటోలను '
                         'అసభ్యంగా మార్చి మీ ఊరి పెద్దలకు, బంధువులకు పంపుతామని బెదిరిస్తారు.',
                   'en': 'Fly-by-night loan apps promise instant cash without collateral. On installation, they demand '
                         'full permissions to access your contacts and camera roll. They disburse a fraction of the '
                         'loan and charge 300% interest within 5 days, blackmailing families with morphed nude '
                         'photos.'},
  'workflow': [{'step': '1', 'icon': '📱', 'te': 'నిమిషాల్లో లోన్ ప్రకటన', 'en': 'Instant loan ad on phone'},
               {'step': '2', 'icon': '🔓', 'te': 'ఫోటోలు, కాంటాక్ట్స్ అనుమతులు', 'en': 'Steals photos & contacts'},
               {'step': '3',
                'icon': '💸',
                'te': 'కొద్ది డబ్బు ఇచ్చి భారీ వడ్డీ డిమాండ్',
                'en': 'Gives small cash, huge fees'},
               {'step': '4',
                'icon': '📸',
                'te': 'ఫోటోలు మార్చి బంధువులకు పంపి బెదిరింపు!',
                'en': 'Blackmails family with morphs!'}],
  'red_flags': {'te': ['ఎలాంటి పత్రాలు లేదా హామీ లేకుండా క్షణాల్లో లోన్ ఇస్తామనే యాప్స్.',
                       'ఇన్\u200cస్టాల్ చేసేటప్పుడు మీ ఫోన్ కాంటాక్ట్\u200cలు, గ్యాలరీ ఫోటోలను యాక్సెస్ చేయాలని అడగడం.',
                       'ఆర్బీఐ (RBI) గుర్తింపు లేని మరియు ప్లేస్టోర్ బయట ఉండే చట్టవిరుద్ధ యాప్స్.'],
                'en': ['Unrealistic offers of collateral-free instant loans with zero credit history checks.',
                       'Apps requesting full access permissions to your contact directory and private photo gallery.',
                       'Non-banking entities not registered with the Reserve Bank of India (RBI).']},
  'what_to_do': {'te': ['అనధికారిక లోన్ యాప్\u200cలను ఎప్పుడూ ఫోన్\u200cలో ఇన్\u200cస్టాల్ చేయకండి.',
                        'రుణాల కోసం మీ ఊరిలోని అధికారిక బ్యాంకులు లేదా ప్రభుత్వ డ్వాక్రా సంఘాలను మాత్రమే సంప్రదించండి.',
                        'బ్లాక్\u200cమెయిల్ చేస్తే భయపడకండి! ఎలాంటి డబ్బులు కట్టకుండా వెంటనే 1930 లేదా సైబర్ పోలీసులను '
                        'ఆశ్రయించండి.'],
                 'en': ['NEVER install unverified instant lending apps on your smartphone.',
                        'Approach only regulated commercial banks, rural cooperative banks, or SHGs for loans.',
                        'If blackmailed, do NOT pay out of shame. Report immediately to 1930 and local police.']},
  'dialogue': {'scammer_te': 'నువ్వు తీసుకున్న ₹3,000 లోన్\u200cకి ఈరోజే ₹12,000 కట్టాలి! కట్టకపోతే నీ ఫోటోలను '
                             'అసభ్యంగా మార్చి నీ ఫోన్ బుక్\u200cలోని నీ చెల్లెలికి, మీ ఊరి వారందరికీ వాట్సాప్\u200cలో '
                             'పంపుతాం!',
               'villager_te': 'నేను మీ బెదిరింపులకు భయపడను. ఆర్బీఐ నిబంధనలు ఉల్లంఘించి బ్లాక్\u200cమెయిల్ '
                              'చేస్తున్నారని నేను ఇప్పుడే 1930 సైబర్ క్రైమ్ పోలీసులకు ఫిర్యాదు చేస్తున్నాను!',
               'outcome_te': '✅ భయపడకుండా పోలీసులకు సమాచారం ఇచ్చి మోసగాళ్ల భరతం పట్టారు.',
               'scammer_en': 'You took a ₹3,000 loan, now pay ₹12,000 today! If you fail, we will morph your face onto '
                             'indecent photos and send them to your sister and all your village contacts!',
               'villager_en': 'I will not succumb to your illegal blackmail! I am reporting your numbers and threats '
                              'to 1930 Cyber Police right now!',
               'outcome_en': '✅ Refused extortion; stood strong with law enforcement.'},
  'audio_text': {'te': 'సులభంగా లోన్ ఇస్తామని చెప్పే నకిలీ యాప్\u200cలను నమ్మకండి. అవి మీ ఫోటోలను, కాంటాక్ట్\u200cలను '
                       'దొంగిలించి మిమ్మల్ని బ్లాక్\u200cమెయిల్ చేస్తాయి. లోన్ కావాలంటే బ్యాంకులకు మాత్రమే వెళ్లండి.',
                 'en': 'Never install untrusted loan apps. They steal your private photos and blackmail your loved '
                       'ones. Always borrow from legitimate banks.'}}]

def get_all_frauds():
    return FRAUD_MODULES

def get_fraud_by_id(fraud_id: str):
    for fraud in FRAUD_MODULES:
        if fraud["id"] == fraud_id:
            return fraud
    return None
