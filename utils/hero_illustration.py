"""
CAVI - Cyber Aware Village Initiative
Rich Visual Composition Graphic for the Home Page Light Hero Section.
Depicts village landscape, rural family, smartphone, cybersecurity shield, lock, and network lines.
"""

def get_hero_composition_svg(lang: str = "te") -> str:
    """
    Returns an SVG illustration depicting the Cyber Aware Village Security Shield.
    High-contrast vector composition suitable for a clean light hero section.
    """
    badge_title = "గ్రామీణ సైబర్ రక్షణ కవచం" if lang == "te" else "Village Cyber Defense Network"
    badge_sub = "కుటుంబ భద్రత • 24x7 రక్షణ" if lang == "te" else "Family Protection • 24x7 Security"
    badge_free = "100% ఉచిత ప్రజా సేవ" if lang == "te" else "100% Free Public Initiative"

    return f"""
    <svg viewBox="0 0 420 280" width="100%" height="270" xmlns="http://www.w3.org/2000/svg" style="border-radius: 24px; background: linear-gradient(135deg, #FFFFFF 0%, #F0F9FF 50%, #E0F2FE 100%); border: 2px solid #BAE6FD; box-shadow: 0 10px 30px rgba(11, 99, 206, 0.12);">
        <!-- Soft Ambient Cyber Glow Grids -->
        <circle cx="210" cy="140" r="125" fill="#E0F2FE" opacity="0.6"/>
        <circle cx="210" cy="140" r="85" fill="#BAE6FD" opacity="0.4"/>
        
        <!-- Background Network Hex Pattern Lines -->
        <path d="M 60 40 L 110 70 L 110 130 L 60 160 L 10 130 L 10 70 Z" fill="none" stroke="#93C5FD" stroke-width="1.5" stroke-dasharray="4,4" opacity="0.5"/>
        <path d="M 360 40 L 410 70 L 410 130 L 360 160 L 310 130 L 310 70 Z" fill="none" stroke="#93C5FD" stroke-width="1.5" stroke-dasharray="4,4" opacity="0.5"/>
        <line x1="110" y1="100" x2="160" y2="100" stroke="#60A5FA" stroke-width="1.5" stroke-dasharray="3,3"/>
        <line x1="260" y1="100" x2="310" y2="100" stroke="#60A5FA" stroke-width="1.5" stroke-dasharray="3,3"/>

        <!-- Village Landscape Base (Green Fields & Hills) -->
        <path d="M 0 240 Q 100 210, 210 230 T 420 220 L 420 280 L 0 280 Z" fill="#DCFCE7" opacity="0.8"/>
        <path d="M 0 255 Q 120 235, 230 250 T 420 245 L 420 280 L 0 280 Z" fill="#86EFAC" opacity="0.6"/>

        <!-- Village Farmer & Family Emojis / Glyphs -->
        <g transform="translate(30, 160)">
            <circle cx="35" cy="35" r="28" fill="#FEF3C7" stroke="#F59E0B" stroke-width="2"/>
            <text x="17" y="44" font-size="28">🧑‍🌾</text>
            <text x="8" y="75" font-size="11" font-weight="900" fill="#14532D">రైతు కుటుంబం</text>
        </g>
        <g transform="translate(325, 160)">
            <circle cx="35" cy="35" r="28" fill="#FEF3C7" stroke="#F59E0B" stroke-width="2"/>
            <text x="17" y="44" font-size="28">👨‍👩‍👧</text>
            <text x="10" y="75" font-size="11" font-weight="900" fill="#14532D">గ్రామ ప్రజలు</text>
        </g>

        <!-- Centerpiece: Smartphone Protected by Cyber Shield -->
        <g transform="translate(150, 40)">
            <!-- Outer Holographic Glow -->
            <path d="M 60 5 L 115 28 C 115 85, 60 125, 60 125 C 60 125, 5 85, 5 28 Z" fill="rgba(11,99,206,0.12)" stroke="#38BDF8" stroke-width="2" stroke-dasharray="6,4"/>

            <!-- Smartphone Device -->
            <rect x="25" y="25" width="70" height="120" rx="12" fill="#0F172A" stroke="#334155" stroke-width="2.5" filter="drop-shadow(0 6px 16px rgba(15,23,42,0.25))"/>
            <rect x="30" y="35" width="60" height="92" rx="6" fill="#F8FAFC"/>
            <circle cx="60" cy="138" r="3" fill="#94A3B8"/>

            <!-- Phone Screen UI: Digital Payment Protection -->
            <rect x="35" y="42" width="50" height="18" rx="4" fill="#0284C7"/>
            <text x="42" y="55" font-size="8.5" font-weight="900" fill="#FFFFFF">UPI / BANK</text>
            <circle cx="60" cy="75" r="14" fill="#DCFCE7" stroke="#16A34A" stroke-width="1.5"/>
            <text x="51" y="82" font-size="14">🔒</text>
            <rect x="36" y="96" width="48" height="12" rx="3" fill="#168447"/>
            <text x="40" y="105" font-size="7.5" font-weight="900" fill="#FFFFFF">SAFE & SECURE</text>

            <!-- Foreground Security Shield -->
            <g transform="translate(22, 50)">
                <path d="M 38 0 L 70 14 C 70 52, 38 74, 38 74 C 38 74, 6 52, 6 14 Z" fill="linear-gradient(135deg, #0B63CE 0%, #063970 100%)" stroke="#93C5FD" stroke-width="2.5" filter="drop-shadow(0 4px 12px rgba(11,99,206,0.4))"/>
                <path d="M 26 36 L 34 44 L 52 24" stroke="#FFFFFF" stroke-width="4.5" stroke-linecap="round" stroke-linejoin="round" fill="none"/>
            </g>
        </g>

        <!-- Dynamic Header Banner Badge -->
        <g transform="translate(100, 18)">
            <rect x="0" y="0" width="220" height="28" rx="14" fill="#063970" stroke="#38BDF8" stroke-width="1.5"/>
            <text x="22" y="19" font-size="12" font-weight="900" fill="#FFFFFF">🛡️ {badge_title}</text>
        </g>

        <!-- Bottom Informational Floating Pills -->
        <g transform="translate(45, 238)">
            <rect x="0" y="0" width="150" height="26" rx="13" fill="#FFFFFF" stroke="#86EFAC" stroke-width="1.5" filter="drop-shadow(0 2px 6px rgba(0,0,0,0.06))"/>
            <text x="14" y="17" font-size="10" font-weight="900" fill="#15803D">🌾 {badge_sub}</text>
        </g>
        <g transform="translate(235, 238)">
            <rect x="0" y="0" width="145" height="26" rx="13" fill="#FFFFFF" stroke="#38BDF8" stroke-width="1.5" filter="drop-shadow(0 2px 6px rgba(0,0,0,0.06))"/>
            <text x="16" y="17" font-size="10" font-weight="900" fill="#0284C7">🇮🇳 {badge_free}</text>
        </g>
    </svg>
    """
