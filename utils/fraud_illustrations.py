"""
CAVI - Cyber Aware Village Initiative
Rich Inline SVG Visual Threat Illustrations for 12 Cyber Fraud Categories.
Provides vivid, visual-first storytelling for rural and semi-literate audiences.
"""

def get_fraud_illustration_svg(fraud_id: str) -> str:
    """
    Returns a responsive, beautifully styled inline SVG illustration
    specifically representing the cyber fraud scenario.
    """
    svg_map = {
        "otp_fraud": """
        <svg viewBox="0 0 400 180" width="100%" height="160" xmlns="http://www.w3.org/2000/svg" style="border-radius: 14px; background: linear-gradient(135deg, #FEF2F2 0%, #FEE2E2 100%); border: 1.5px solid #FECACA;">
            <!-- Background Accent Circles -->
            <circle cx="340" cy="40" r="50" fill="#FCA5A5" opacity="0.3"/>
            <circle cx="50" cy="140" r="40" fill="#FCA5A5" opacity="0.2"/>
            
            <!-- Smartphone Body -->
            <rect x="130" y="20" width="140" height="145" rx="14" fill="#0F172A" stroke="#334155" stroke-width="3"/>
            <rect x="140" y="32" width="120" height="115" rx="8" fill="#FFFFFF"/>
            <circle cx="200" cy="155" r="4" fill="#94A3B8"/>
            
            <!-- Incoming SMS Badge -->
            <rect x="148" y="40" width="104" height="24" rx="6" fill="#FEE2E2" stroke="#F87171" stroke-width="1"/>
            <text x="156" y="56" font-size="11" font-weight="900" fill="#991B1B">📩 BANK OTP SMS</text>
            
            <!-- 6 Digit OTP Display -->
            <rect x="152" y="72" width="96" height="30" rx="6" fill="#0F2942"/>
            <text x="160" y="93" font-size="16" font-weight="900" fill="#38BDF8" letter-spacing="4">5 8 2 9</text>
            
            <!-- Scammer Threat Hand & Handcuffs / Stop Hand -->
            <g transform="translate(20, 35)">
                <circle cx="45" cy="45" r="32" fill="#DC2626" opacity="0.15"/>
                <text x="25" y="55" font-size="34">🎭</text>
                <text x="8" y="95" font-size="11" font-weight="900" fill="#991B1B">మోసగాడి కాల్ / Fake Call</text>
            </g>
            
            <!-- Warning Arrow to Phone -->
            <path d="M 90 70 L 125 70" stroke="#DC2626" stroke-width="3" stroke-dasharray="4,4"/>
            <polygon points="128,70 120,65 120,75" fill="#DC2626"/>
            
            <!-- Security Shield Overlay -->
            <g transform="translate(285, 45)">
                <path d="M 35 10 L 65 22 C 65 55 35 75 35 75 C 35 75 5 55 5 22 Z" fill="#168447" stroke="#86EFAC" stroke-width="2"/>
                <path d="M 23 42 L 31 50 L 48 33" stroke="#FFFFFF" stroke-width="4" stroke-linecap="round" stroke-linejoin="round" fill="none"/>
                <text x="8" y="92" font-size="11" font-weight="900" fill="#166534">రహస్యం! OTP షేర్ చేయొద్దు</text>
            </g>
        </svg>
        """,
        
        "upi_fraud": """
        <svg viewBox="0 0 400 180" width="100%" height="160" xmlns="http://www.w3.org/2000/svg" style="border-radius: 14px; background: linear-gradient(135deg, #FFF7ED 0%, #FFEDD5 100%); border: 1.5px solid #FED7AA;">
            <!-- UPI App Interface Mockup -->
            <rect x="110" y="15" width="180" height="150" rx="16" fill="#FFFFFF" stroke="#FDBA74" stroke-width="2" filter="drop-shadow(0 4px 10px rgba(234,88,12,0.1))"/>
            
            <!-- UPI Header Bar -->
            <rect x="110" y="15" width="180" height="34" rx="16" fill="#EA580C"/>
            <text x="145" y="38" font-size="13" font-weight="900" fill="#FFFFFF">PhonePe / GPay Fake</text>
            
            <!-- Fake Request Content -->
            <text x="125" y="70" font-size="12" font-weight="800" fill="#334155">రైతుకు డబ్బు పంపే రిక్వెస్ట్</text>
            <text x="145" y="92" font-size="18" font-weight="950" fill="#DC2626">₹5,000 PAY ❌</text>
            
            <!-- Scammer Trick: "Enter PIN to Receive" Warning -->
            <rect x="122" y="105" width="156" height="28" rx="8" fill="#FEE2E2" stroke="#DC2626" stroke-width="1.5"/>
            <text x="128" y="123" font-size="10.5" font-weight="900" fill="#991B1B">⚠️ పిన్ కొడితే డబ్బు మీవే పోతాయి!</text>
            
            <!-- QR Code Graphic on Left -->
            <g transform="translate(18, 40)">
                <rect x="0" y="0" width="70" height="70" rx="10" fill="#0F172A"/>
                <!-- QR Inner Patterns -->
                <rect x="8" y="8" width="22" height="22" fill="#FFFFFF"/>
                <rect x="13" y="13" width="12" height="12" fill="#0F172A"/>
                <rect x="40" y="8" width="22" height="22" fill="#FFFFFF"/>
                <rect x="45" y="13" width="12" height="12" fill="#0F172A"/>
                <rect x="8" y="40" width="22" height="22" fill="#FFFFFF"/>
                <rect x="13" y="45" width="12" height="12" fill="#0F172A"/>
                <rect x="40" y="40" width="10" height="10" fill="#FFFFFF"/>
                <rect x="52" y="52" width="10" height="10" fill="#FFFFFF"/>
                <text x="4" y="90" font-size="10.5" font-weight="900" fill="#C2410C">QR స్కాన్ వల</text>
            </g>
            
            <!-- Safe Badge on Right -->
            <g transform="translate(305, 45)">
                <circle cx="40" cy="35" r="28" fill="#168447"/>
                <text x="24" y="42" font-size="24">✅</text>
                <text x="2" y="80" font-size="10.5" font-weight="900" fill="#166534">రిసీవ్ కి PIN అవసరం లేదు!</text>
            </g>
        </svg>
        """,
        
        "kyc_fraud": """
        <svg viewBox="0 0 400 180" width="100%" height="160" xmlns="http://www.w3.org/2000/svg" style="border-radius: 14px; background: linear-gradient(135deg, #FEF2F2 0%, #FFF1F2 100%); border: 1.5px solid #FECDD3;">
            <!-- Fake Bank Document / Passbook Card -->
            <rect x="100" y="20" width="200" height="140" rx="12" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="2" filter="drop-shadow(0 4px 10px rgba(0,0,0,0.06))"/>
            
            <!-- Top Bank Header Mock -->
            <rect x="100" y="20" width="200" height="32" rx="12" fill="#063970"/>
            <text x="130" y="42" font-size="12" font-weight="900" fill="#FFFFFF">🏛️ STATE BANK NOTICE</text>
            
            <!-- Fake Notice Lines -->
            <rect x="115" y="65" width="120" height="8" rx="4" fill="#E2E8F0"/>
            <rect x="115" y="80" width="90" height="8" rx="4" fill="#E2E8F0"/>
            
            <!-- Prominent Red EXPIRED / BLOCKED Stamp -->
            <g transform="translate(135, 75) rotate(-10)">
                <rect x="0" y="0" width="140" height="36" rx="6" fill="#FEE2E2" stroke="#DC2626" stroke-width="2"/>
                <text x="8" y="24" font-size="14" font-weight="950" fill="#DC2626">KYC EXPIRED! ❌</text>
            </g>
            
            <!-- Left Phishing SMS Indicator -->
            <g transform="translate(15, 45)">
                <circle cx="35" cy="35" r="26" fill="#DC2626" opacity="0.15"/>
                <text x="20" y="44" font-size="28">⚠️</text>
                <text x="2" y="80" font-size="10.5" font-weight="800" fill="#991B1B">24 గంటల్లో బ్లాక్ బెదిరింపు</text>
            </g>
            
            <!-- Right Safe Bank Branch Guide -->
            <g transform="translate(315, 45)">
                <circle cx="35" cy="35" r="26" fill="#0B63CE" opacity="0.15"/>
                <text x="20" y="44" font-size="28">🏛️</text>
                <text x="5" y="80" font-size="10.5" font-weight="900" fill="#063970">బ్రాంచ్\u200cకే వెళ్లండి</text>
            </g>
        </svg>
        """,
        
        "lottery_fraud": """
        <svg viewBox="0 0 400 180" width="100%" height="160" xmlns="http://www.w3.org/2000/svg" style="border-radius: 14px; background: linear-gradient(135deg, #FEFCE8 0%, #FEF9C3 100%); border: 1.5px solid #FDE047;">
            <!-- Golden Trophy / Wheel Mockup -->
            <g transform="translate(40, 25)">
                <circle cx="50" cy="50" r="40" fill="#EAB308" stroke="#CA8A04" stroke-width="3"/>
                <circle cx="50" cy="50" r="32" fill="#FEF08A"/>
                <text x="32" y="58" font-size="30">🏆</text>
                <text x="12" y="108" font-size="11" font-weight="900" fill="#854D0E">నకిలీ లక్కీ డ్రా</text>
            </g>
            
            <!-- Prize Voucher Card -->
            <rect x="150" y="25" width="220" height="130" rx="14" fill="#FFFFFF" stroke="#EAB308" stroke-width="2" stroke-dasharray="6,4"/>
            <rect x="160" y="35" width="200" height="30" rx="6" fill="#CA8A04"/>
            <text x="175" y="56" font-size="13" font-weight="950" fill="#FFFFFF">🎉 ₹25 LAKHS KBC LOTTERY</text>
            
            <text x="165" y="90" font-size="12" font-weight="800" fill="#475569">బహుమతి కావాలంటే మొదట</text>
            <rect x="165" y="100" width="170" height="26" rx="6" fill="#FEE2E2" stroke="#DC2626" stroke-width="1.5"/>
            <text x="172" y="118" font-size="11" font-weight="950" fill="#DC2626">₹2,500 ట్యాక్స్ ఫీజు కట్టండి ❌</text>
            <text x="165" y="145" font-size="10.5" font-weight="900" fill="#168447">నియమం: ఫీజు కట్టమంటే 100% మోసం!</text>
        </svg>
        """,
        
        "screen_share_fraud": """
        <svg viewBox="0 0 400 180" width="100%" height="160" xmlns="http://www.w3.org/2000/svg" style="border-radius: 14px; background: linear-gradient(135deg, #F1F5F9 0%, #E2E8F0 100%); border: 1.5px solid #CBD5E1;">
            <!-- Smartphone on Left -->
            <rect x="40" y="25" width="80" height="130" rx="10" fill="#0F172A" stroke="#475569" stroke-width="2"/>
            <rect x="46" y="35" width="68" height="105" rx="6" fill="#FFFFFF"/>
            <text x="56" y="70" font-size="10" font-weight="800" fill="#334155">మీ మొబైల్</text>
            <text x="52" y="95" font-size="20">📱</text>
            <text x="52" y="125" font-size="9" font-weight="900" fill="#DC2626">AnyDesk / TeamViewer</text>
            
            <!-- Connection Cable with Danger Sparks -->
            <path d="M 125 90 C 170 50, 190 130, 235 90" stroke="#DC2626" stroke-width="3" stroke-dasharray="5,5"/>
            <circle cx="180" cy="90" r="14" fill="#DC2626"/>
            <text x="174" y="96" font-size="14" fill="#FFFFFF">⚠️</text>
            
            <!-- Scammer's Laptop on Right -->
            <rect x="240" y="45" width="120" height="80" rx="8" fill="#1E293B" stroke="#0F172A" stroke-width="2"/>
            <rect x="248" y="53" width="104" height="64" rx="4" fill="#091B36"/>
            <polygon points="225,125 375,125 365,135 235,135" fill="#475569"/>
            
            <!-- Scammer Screen Peek -->
            <text x="260" y="80" font-size="10" font-weight="900" fill="#38BDF8">రిమోట్ కంట్రోల్</text>
            <text x="260" y="100" font-size="11" font-weight="950" fill="#F87171">పాస్‌వర్డ్ చౌర్యం 👁️</text>
            
            <text x="120" y="165" font-size="11" font-weight="900" fill="#991B1B">నియమం: ఎవరి మాటలు విని స్క్రీన్ షేర్ యాప్స్ ఎక్కించవద్దు!</text>
        </svg>
        """,
        
        "digital_arrest": """
        <svg viewBox="0 0 400 180" width="100%" height="160" xmlns="http://www.w3.org/2000/svg" style="border-radius: 14px; background: linear-gradient(135deg, #FEF2F2 0%, #FEE2E2 100%); border: 1.5px solid #FCA5A5;">
            <!-- Video Call Screen Frame -->
            <rect x="70" y="15" width="260" height="150" rx="14" fill="#0F172A" stroke="#DC2626" stroke-width="2.5"/>
            
            <!-- Red Police Flashing Siren -->
            <g transform="translate(185, 20)">
                <circle cx="15" cy="12" r="12" fill="#DC2626" filter="drop-shadow(0 0 8px #EF4444)"/>
                <text x="7" y="19" font-size="16">🚨</text>
            </g>
            
            <!-- Fake Officer Profile -->
            <g transform="translate(90, 48)">
                <rect x="0" y="0" width="80" height="85" rx="8" fill="#1E293B"/>
                <text x="18" y="45" font-size="34">👮‍♂️</text>
                <text x="10" y="72" font-size="9" font-weight="900" fill="#F87171">నకిలీ పోలీస్ / CBI</text>
            </g>
            
            <!-- Fake Warrant & Arrest Notice -->
            <rect x="185" y="48" width="130" height="85" rx="8" fill="#FFFFFF"/>
            <text x="195" y="68" font-size="11" font-weight="950" fill="#991B1B">ARREST WARRANT</text>
            <text x="195" y="85" font-size="9" font-weight="700" fill="#475569">మనీలాండరింగ్ కేస్</text>
            <rect x="195" y="95" width="110" height="22" rx="4" fill="#FEE2E2"/>
            <text x="200" y="110" font-size="9.5" font-weight="900" fill="#DC2626">కెమెరా ఆఫ్ చేయొద్దు!</text>
            
            <!-- Golden Truth Pill -->
            <rect x="85" y="142" width="230" height="20" rx="10" fill="#168447"/>
            <text x="96" y="156" font-size="10" font-weight="900" fill="#FFFFFF">భారత చట్టంలో 'డిజిటల్ అరెస్ట్' అనేదే లేదు! కాల్ కట్ చేయండి.</text>
        </svg>
        """,
        
        "job_fraud": """
        <svg viewBox="0 0 400 180" width="100%" height="160" xmlns="http://www.w3.org/2000/svg" style="border-radius: 14px; background: linear-gradient(135deg, #F0FDF4 0%, #DCFCE7 100%); border: 1.5px solid #86EFAC;">
            <!-- Social Messaging Chat Bubble -->
            <rect x="40" y="20" width="320" height="110" rx="14" fill="#FFFFFF" stroke="#86EFAC" stroke-width="2" filter="drop-shadow(0 4px 10px rgba(0,0,0,0.05))"/>
            
            <text x="60" y="46" font-size="13" font-weight="900" fill="#0B63CE">💬 Telegram / WhatsApp జాబ్ ఆఫర్</text>
            
            <!-- Fake Task Promise -->
            <rect x="60" y="58" width="280" height="30" rx="8" fill="#F0FDF4" stroke="#22C55E" stroke-width="1"/>
            <text x="70" y="78" font-size="12" font-weight="900" fill="#15803D">👍 వీడియో లైక్ చేస్తే రోజుకు ₹3,000 సంపాదించండి</text>
            
            <!-- Trap Deposit Request -->
            <rect x="60" y="94" width="280" height="26" rx="6" fill="#FEE2E2"/>
            <text x="70" y="112" font-size="11" font-weight="900" fill="#DC2626">వల: పెద్ద కమిషన్ కోసం ₹5,000 డిపాజిట్ చేయండి ❌</text>
            
            <!-- Alert Badge -->
            <rect x="80" y="140" width="240" height="24" rx="12" fill="#DC2626"/>
            <text x="92" y="156" font-size="10.5" font-weight="900" fill="#FFFFFF">ఉద్యోగం కోసం డబ్బు కట్టమంటే 100% మోసం!</text>
        </svg>
        """,
        
        "investment_fraud": """
        <svg viewBox="0 0 400 180" width="100%" height="160" xmlns="http://www.w3.org/2000/svg" style="border-radius: 14px; background: linear-gradient(135deg, #FAF5FF 0%, #F3E8FF 100%); border: 1.5px solid #D8B4FE;">
            <!-- Exponential Growth Chart with Trap Pit -->
            <rect x="40" y="20" width="220" height="120" rx="12" fill="#FFFFFF" stroke="#C084FC" stroke-width="1.5"/>
            
            <!-- Stock / Trading Surge Line -->
            <path d="M 60 115 L 100 95 L 140 80 L 180 50 L 225 35" fill="none" stroke="#22C55E" stroke-width="4" stroke-linecap="round"/>
            <circle cx="225" cy="35" r="5" fill="#22C55E"/>
            <text x="160" y="32" font-size="11" font-weight="950" fill="#15803D">+500% లాభం</text>
            
            <!-- Fake App Name -->
            <text x="55" y="42" font-size="11" font-weight="900" fill="#7E22CE">నకిలీ ట్రేడింగ్ యాప్</text>
            <text x="55" y="60" font-size="10" font-weight="700" fill="#64748B">₹10,000 వేస్తే ₹50,000</text>
            
            <!-- Trap Pit / Lock on Right -->
            <g transform="translate(280, 25)">
                <rect x="0" y="0" width="90" height="115" rx="10" fill="#FEE2E2" stroke="#EF4444" stroke-width="2"/>
                <text x="25" y="40" font-size="34">🔒</text>
                <text x="10" y="70" font-size="10.5" font-weight="950" fill="#991B1B">డ్రా చేయలేరు!</text>
                <text x="6" y="90" font-size="9" font-weight="800" fill="#DC2626">మరింత డబ్బు డిమాండ్</text>
            </g>
            
            <text x="80" y="162" font-size="11" font-weight="900" fill="#6B21A8">అతి తక్కువ రోజుల్లో రెట్టింపు లాభాలు అంటే వల!</text>
        </svg>
        """,
        
        "fake_customer_care": """
        <svg viewBox="0 0 400 180" width="100%" height="160" xmlns="http://www.w3.org/2000/svg" style="border-radius: 14px; background: linear-gradient(135deg, #F0F9FF 0%, #E0F2FE 100%); border: 1.5px solid #BAE6FD;">
            <!-- Google Search Bar Mock -->
            <rect x="40" y="20" width="320" height="38" rx="19" fill="#FFFFFF" stroke="#93C5FD" stroke-width="2" filter="drop-shadow(0 2px 8px rgba(0,0,0,0.06))"/>
            <text x="58" y="44" font-size="12" font-weight="700" fill="#475569">🔍 గ్యాస్ సిలిండర్ / బ్యాంక్ కస్టమర్ కేర్</text>
            
            <!-- Fake Ad Search Result (Red Hazard) -->
            <rect x="40" y="70" width="320" height="65" rx="10" fill="#FEF2F2" stroke="#F87171" stroke-width="2"/>
            <rect x="52" y="78" width="28" height="16" rx="4" fill="#DC2626"/>
            <text x="56" y="90" font-size="10" font-weight="900" fill="#FFFFFF">Ad</text>
            
            <text x="86" y="91" font-size="11.5" font-weight="900" fill="#991B1B">హెల్ప్‌లైన్: 98480-XXXXX ❌ (ప్రైవేట్ మొబైల్)</text>
            <text x="52" y="115" font-size="10.5" font-weight="800" fill="#475569">గూగుల్\u200cలో వచ్చే నంబర్లు మోసగాళ్లవే కావచ్చు!</text>
            
            <!-- Safety Rule -->
            <rect x="70" y="145" width="260" height="22" rx="11" fill="#0369A1"/>
            <text x="82" y="160" font-size="10.5" font-weight="900" fill="#FFFFFF">బ్యాంక్ పాస్\u200cబుక్ లేదా యాప్ లోని అధికారిక నంబర్లనే వాడండి</text>
        </svg>
        """,
        
        "sim_swap_fraud": """
        <svg viewBox="0 0 400 180" width="100%" height="160" xmlns="http://www.w3.org/2000/svg" style="border-radius: 14px; background: linear-gradient(135deg, #FFF1F2 0%, #FFE4E6 100%); border: 1.5px solid #FECDD3;">
            <!-- Broken Signal Tower on Left -->
            <g transform="translate(30, 25)">
                <path d="M 40 120 L 40 40 M 20 60 L 60 60 M 25 80 L 55 80 M 15 100 L 65 100" stroke="#475569" stroke-width="3" stroke-linecap="round"/>
                <!-- Cut Signal Waves -->
                <path d="M 40 25 C 20 25, 10 15, 5 5" stroke="#DC2626" stroke-width="2.5" stroke-dasharray="3,3" fill="none"/>
                <line x1="15" y1="15" x2="65" y2="45" stroke="#DC2626" stroke-width="3"/>
                <text x="12" y="136" font-size="10.5" font-weight="900" fill="#991B1B">సిగ్నల్ కట్!</text>
            </g>
            
            <!-- Mobile Displaying "No SIM / Emergency Only" -->
            <rect x="130" y="20" width="130" height="135" rx="12" fill="#0F172A" stroke="#334155" stroke-width="2"/>
            <rect x="140" y="32" width="110" height="110" rx="6" fill="#FFFFFF"/>
            <text x="148" y="55" font-size="10" font-weight="900" fill="#DC2626">🚫 NO SERVICE</text>
            <text x="148" y="75" font-size="9" font-weight="700" fill="#64748B">SIM Inactive</text>
            <rect x="146" y="90" width="98" height="35" rx="6" fill="#FEE2E2"/>
            <text x="150" y="106" font-size="8.5" font-weight="900" fill="#991B1B">నకిలీ 5G అప్\u200cగ్రేడ్</text>
            <text x="150" y="120" font-size="8.5" font-weight="800" fill="#DC2626">OTP దొంగిలింపు</text>
            
            <!-- Duplicate SIM on Right -->
            <g transform="translate(285, 35)">
                <path d="M 10 15 L 55 15 L 75 35 L 75 95 L 10 95 Z" fill="#E2E8F0" stroke="#94A3B8" stroke-width="2"/>
                <rect x="25" y="45" width="35" height="35" rx="4" fill="#F59E0B"/>
                <text x="8" y="116" font-size="10.5" font-weight="900" fill="#DC2626">మోసగాడి డూప్లికేట్ SIM</text>
            </g>
            
            <text x="70" y="170" font-size="10.5" font-weight="900" fill="#991B1B">సిగ్నల్ ఆగిపోతే వెంటనే టెలికాం ఆఫీస్ లేదా 1930 కి తెలపండి</text>
        </svg>
        """,
        
        "phishing_links": """
        <svg viewBox="0 0 400 180" width="100%" height="160" xmlns="http://www.w3.org/2000/svg" style="border-radius: 14px; background: linear-gradient(135deg, #F0FDF4 0%, #E0F2FE 100%); border: 1.5px solid #BAE6FD;">
            <!-- Fishing Hook Dangling Over Smartphone -->
            <path d="M 200 10 L 200 55 C 200 80, 230 80, 230 65 L 230 60" fill="none" stroke="#DC2626" stroke-width="3.5" stroke-linecap="round"/>
            <polygon points="230,55 224,65 236,65" fill="#DC2626"/>
            
            <!-- SMS Card with Blue Phishing Link -->
            <rect x="60" y="55" width="280" height="90" rx="12" fill="#FFFFFF" stroke="#0284C7" stroke-width="2" filter="drop-shadow(0 4px 12px rgba(2,132,199,0.1))"/>
            <text x="75" y="80" font-size="11.5" font-weight="900" fill="#0F172A">📩 ఉచిత పథకం నిధులు / విద్యుత్ బిల్లు మెసేజ్</text>
            
            <!-- Suspicious Link Pill -->
            <rect x="75" y="92" width="240" height="26" rx="6" fill="#FEE2E2" stroke="#EF4444" stroke-width="1"/>
            <text x="85" y="109" font-size="11" font-weight="900" fill="#DC2626" text-decoration="underline">http://bit.ly/ap-free-subsidy-xyz ❌</text>
            
            <text x="75" y="134" font-size="10" font-weight="800" fill="#15803D">నియమం: గుర్తుతెలియని లింక్స్ ఎప్పుడూ నొక్కవద్దు!</text>
            
            <!-- Hazard Alert Symbol -->
            <g transform="translate(20, 75)">
                <text x="0" y="25" font-size="28">🎣</text>
                <text x="-5" y="50" font-size="10" font-weight="900" fill="#DC2626">ఫిషింగ్ వల</text>
            </g>
        </svg>
        """,
        
        "loan_fraud": """
        <svg viewBox="0 0 400 180" width="100%" height="160" xmlns="http://www.w3.org/2000/svg" style="border-radius: 14px; background: linear-gradient(135deg, #FEF2F2 0%, #FEE2E2 100%); border: 1.5px solid #F87171;">
            <!-- Instant 5-Minute Loan Ad Mockup -->
            <rect x="40" y="20" width="200" height="120" rx="12" fill="#FFFFFF" stroke="#DC2626" stroke-width="2"/>
            <rect x="40" y="20" width="200" height="30" rx="12" fill="#DC2626"/>
            <text x="55" y="40" font-size="12" font-weight="950" fill="#FFFFFF">⚡ 2 నిమిషాల్లో ₹50,000 లోన్</text>
            
            <text x="50" y="70" font-size="10.5" font-weight="800" fill="#334155">ఎటువంటి గ్యారెంటీ లేకుండానే!</text>
            
            <!-- Dangerous Permissions Pop-up -->
            <rect x="50" y="82" width="180" height="46" rx="6" fill="#FEE2E2" stroke="#EF4444" stroke-width="1"/>
            <text x="58" y="100" font-size="10" font-weight="900" fill="#991B1B">⚠️ కాంటాక్ట్స్, ఫోటోలు యాక్సెస్?</text>
            <text x="58" y="118" font-size="9" font-weight="900" fill="#DC2626">[ ALLOW నొక్కితే బ్లాక్\u200cమెయిల్ ]</text>
            
            <!-- Blackmail Skull on Right -->
            <g transform="translate(265, 30)">
                <circle cx="50" cy="45" r="38" fill="#7F1D1D"/>
                <text x="28" y="58" font-size="40">💀</text>
                <text x="8" y="104" font-size="10.5" font-weight="950" fill="#991B1B">బ్లాక్\u200cమెయిల్ ముఠా</text>
            </g>
            
            <text x="75" y="162" font-size="11" font-weight="900" fill="#991B1B">RBI గుర్తింపు లేని లోన్ యాప్స్ ఫోన్ లోకి ఎక్కించవద్దు!</text>
        </svg>
        """
    }
    
    # Return matched SVG or fallback default illustration
    return svg_map.get(fraud_id, """
    <svg viewBox="0 0 400 180" width="100%" height="160" xmlns="http://www.w3.org/2000/svg" style="border-radius: 14px; background: #F8FAFC; border: 1.5px solid #E2E8F0;">
        <circle cx="200" cy="80" r="45" fill="#0B63CE" opacity="0.1"/>
        <text x="180" y="95" font-size="45">🛡️</text>
        <text x="120" y="150" font-size="14" font-weight="900" fill="#063970">గ్రామీణ సైబర్ రక్షణ కవచం</text>
    </svg>
    """)
