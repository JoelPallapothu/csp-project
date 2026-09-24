"""
CAVI - Cyber Aware Village Initiative
Senior UI/UX Design System, Animations, Mobile Responsiveness, Accessibility Styling
and Safe HTML Rendering Engine
"""

import streamlit as st

def render_html(html_content: str):
    """
    Renders HTML safely using Streamlit's native st.html() engine, completely bypassing
    CommonMark markdown parsing to eliminate any possibility of raw code block leakage (<pre><code>).
    """
    if not html_content:
        return
    lines = html_content.strip().splitlines()
    cleaned = " ".join(line.strip() for line in lines if line.strip())
    if hasattr(st, "html"):
        st.html(cleaned)
    else:
        st.markdown(cleaned, unsafe_allow_html=True)

def get_custom_css(font_size_mode: str = "normal") -> str:
    """
    Returns production-grade, desktop-first public portal CSS with modern glassmorphism,
    pulsing alerts, responsive touch controls, and dynamic font accessibility.
    """
    base_font_size = "17px"
    heading_scale = "1.0"
    card_padding = "26px"
    
    if font_size_mode == "large":
        base_font_size = "20px"
        heading_scale = "1.15"
        card_padding = "30px"
    elif font_size_mode == "xlarge":
        base_font_size = "23px"
        heading_scale = "1.3"
        card_padding = "34px"

    return f"""
    <style>
        /* Google Fonts: Noto Sans Telugu for high-quality Telugu glyphs + Plus Jakarta Sans for English */
        @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800;900&family=Noto+Sans+Telugu:wght@400;500;600;700;800;900&display=swap');

        :root {{
            --font-main: 'Plus Jakarta Sans', 'Noto Sans Telugu', 'Segoe UI', system-ui, sans-serif;
            --font-telugu: 'Noto Sans Telugu', 'Segoe UI', sans-serif;
            --primary-navy: #063970;
            --primary-blue: #0b63ce;
            --cyber-blue: #1688d8;
            --cyber-light: #e0f2fe;
            --safe-green: #168447;
            --safe-light: #f0fdf4;
            --safe-border: #86efac;
            --danger-red: #d62828;
            --danger-dark: #991b1b;
            --danger-light: #fef2f2;
            --danger-border: #fca5a5;
            --warning-amber: #f4b400;
            --warning-light: #fffbeb;
            --bg-slate: #f8fafc;
            --card-border: #e2e8f0;
            --text-dark: #091b36;
            --text-muted: #475569;
        }}

        /* Base Typography & Background */
        html, body, [class*="css"], .stMarkdown, .stText, p, div, span, li, button {{
            font-family: var(--font-main) !important;
            font-size: {base_font_size};
            color: var(--text-dark);
            -webkit-font-smoothing: antialiased;
        }}

        /* Generous line-height for Telugu script to prevent vowel mark clipping */
        p, li, div {{
            line-height: 1.68 !important;
        }}

        /* Clean Streamlit Default Chrome */
        header[data-testid="stHeader"] {{
            background: rgba(248, 250, 252, 0.98) !important;
            backdrop-filter: blur(12px) !important;
            border-bottom: 1px solid #e2e8f0 !important;
        }}

        #MainMenu, footer {{
            visibility: hidden !important;
        }}

        /* Desktop Full-Screen Viewport Container */
        .block-container {{
            padding-top: 0.8rem !important;
            padding-bottom: 3.5rem !important;
            max-width: 1540px !important;
            width: 96% !important;
            padding-left: 2rem !important;
            padding-right: 2rem !important;
        }}

        /* Keyframe Animations */
        @keyframes fadeIn {{
            from {{ opacity: 0; transform: translateY(6px); }}
            to {{ opacity: 1; transform: translateY(0); }}
        }}

        @keyframes shieldFloat {{
            0%, 100% {{ transform: translateY(0px); }}
            50% {{ transform: translateY(-6px); }}
        }}

        @keyframes pulse-emergency {{
            0% {{
                box-shadow: 0 0 0 0 rgba(214, 40, 40, 0.5);
                transform: scale(1);
            }}
            50% {{
                box-shadow: 0 0 0 10px rgba(214, 40, 40, 0);
                transform: scale(1.004);
            }}
            100% {{
                box-shadow: 0 0 0 0 rgba(214, 40, 40, 0);
                transform: scale(1);
            }}
        }}

        /* Eradicate Any Errant Pre/Code Rendering of HTML */
        pre:has(div), pre:has(span), pre:has(p), pre:has(h1), pre:has(h2), pre:has(h3),
        code:has(div), code:has(span) {{
            background: transparent !important;
            border: none !important;
            padding: 0 !important;
            margin: 0 !important;
            box-shadow: none !important;
        }}

        /* Modern Glass Card */
        .cavi-card {{
            background: #ffffff;
            border-radius: 20px;
            padding: {card_padding};
            border: 1px solid var(--card-border);
            box-shadow: 0 4px 18px rgba(15, 43, 92, 0.05);
            transition: transform 0.22s ease, box-shadow 0.22s ease, border-color 0.22s ease;
            position: relative;
            overflow: hidden;
            margin-bottom: 22px;
        }}

        .cavi-card:hover {{
            transform: translateY(-4px);
            box-shadow: 0 14px 30px rgba(15, 43, 92, 0.1);
            border-color: #cbd5e1;
        }}

        /* Interactive Fraud Card */
        .fraud-grid-card {{
            background: #ffffff;
            border-radius: 20px;
            padding: 22px;
            border: 1px solid var(--card-border);
            box-shadow: 0 4px 16px rgba(15, 43, 92, 0.05);
            transition: all 0.25s cubic-bezier(0.16, 1, 0.3, 1);
            position: relative;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            min-height: 270px;
        }}

        .fraud-grid-card:hover {{
            transform: translateY(-6px);
            box-shadow: 0 16px 36px rgba(15, 43, 92, 0.12);
        }}

        /* Hero Banner */
        .hero-banner {{
            background: linear-gradient(135deg, #06152b 0%, #0c2349 45%, #1d4ed8 100%);
            border-radius: 26px;
            padding: 38px 36px;
            color: #ffffff;
            box-shadow: 0 12px 34px rgba(9, 27, 54, 0.28);
            margin-bottom: 26px;
            position: relative;
            border: 1px solid rgba(255, 255, 255, 0.14);
            overflow: hidden;
        }}

        .hero-banner h1 {{
            font-size: calc(2.35rem * {heading_scale}) !important;
            font-weight: 900 !important;
            color: #ffffff !important;
            margin-bottom: 12px !important;
            line-height: 1.25 !important;
            letter-spacing: -0.5px;
        }}

        .hero-banner p {{
            font-size: calc(1.15rem * {heading_scale}) !important;
            color: #e0f2fe !important;
            line-height: 1.55 !important;
            margin-bottom: 0 !important;
        }}

        /* Emergency Action Strip */
        .emergency-strip {{
            background: linear-gradient(90deg, #991b1b 0%, #dc2626 55%, #b91c1c 100%);
            border-radius: 18px;
            padding: 16px 24px;
            color: #ffffff;
            box-shadow: 0 6px 22px rgba(220, 38, 38, 0.28);
            margin-bottom: 22px;
            border: 2px solid #fecaca;
            display: flex;
            align-items: center;
            justify-content: space-between;
            flex-wrap: wrap;
            gap: 14px;
            animation: pulse-emergency 3.5s infinite;
        }}

        /* Navigation Buttons Enhancement */
        .stButton>button {{
            border-radius: 14px !important;
            padding: 12px 18px !important;
            font-weight: 700 !important;
            font-size: calc(1.0rem * {heading_scale}) !important;
            transition: all 0.2s cubic-bezier(0.16, 1, 0.3, 1) !important;
            border: none !important;
            box-shadow: 0 3px 10px rgba(15, 43, 92, 0.08) !important;
            min-height: 48px !important;
        }}

        .stButton>button:hover {{
            transform: translateY(-2px) !important;
            box-shadow: 0 8px 18px rgba(15, 43, 92, 0.16) !important;
        }}

        .stButton>button:active {{
            transform: translateY(1px) !important;
        }}

        /* Primary Buttons */
        .stButton>button[kind="primary"] {{
            background: linear-gradient(135deg, #0f2b5c 0%, #1d4ed8 100%) !important;
            color: #ffffff !important;
            box-shadow: 0 4px 14px rgba(29, 78, 216, 0.3) !important;
        }}

        /* Badges */
        .badge-pill {{
            display: inline-flex;
            align-items: center;
            gap: 5px;
            padding: 5px 13px;
            border-radius: 9999px;
            font-size: 0.85rem;
            font-weight: 800;
            letter-spacing: 0.3px;
        }}

        .badge-safe {{
            background: var(--safe-light);
            color: var(--safe-green);
            border: 1px solid var(--safe-border);
        }}

        .badge-danger {{
            background: var(--danger-light);
            color: var(--danger-red);
            border: 1px solid var(--danger-border);
        }}

        .badge-warning {{
            background: var(--warning-light);
            color: var(--warning-amber);
            border: 1px solid #fde68a;
        }}

        .badge-info {{
            background: var(--cyber-light);
            color: var(--cyber-blue);
            border: 1px solid #bae6fd;
        }}

        /* Flowchart Steps for Villagers */
        .workflow-step-box {{
            background: #ffffff;
            border-radius: 16px;
            padding: 16px;
            border: 1px solid #e2e8f0;
            box-shadow: 0 3px 10px rgba(0,0,0,0.03);
            text-align: center;
            position: relative;
            transition: all 0.2s ease;
        }}

        .workflow-step-box:hover {{
            border-color: #0284c7;
            transform: translateY(-2px);
        }}

        /* WhatsApp / Phone Chat Bubbles */
        .chat-bubble-scammer {{
            background: #fee2e2;
            color: #7f1d1d;
            border-radius: 20px 20px 20px 4px;
            padding: 16px 20px;
            margin-bottom: 14px;
            border: 1px solid #fecaca;
            font-size: calc(1.05rem * {heading_scale});
            line-height: 1.55;
            box-shadow: 0 2px 8px rgba(220, 38, 38, 0.06);
        }}

        .chat-bubble-villager {{
            background: #dcfce7;
            color: #14532d;
            border-radius: 20px 20px 4px 20px;
            padding: 16px 20px;
            margin-bottom: 14px;
            margin-left: 28px;
            border: 1px solid #bbf7d0;
            font-size: calc(1.05rem * {heading_scale});
            line-height: 1.55;
            box-shadow: 0 2px 8px rgba(22, 163, 74, 0.06);
        }}

        /* Do vs Don't Split Boards */
        .do-box {{
            background: var(--safe-light);
            border: 2px solid var(--safe-border);
            border-radius: 20px;
            padding: 24px;
            height: 100%;
            box-shadow: 0 4px 16px rgba(22, 163, 74, 0.06);
        }}

        .dont-box {{
            background: var(--danger-light);
            border: 2px solid var(--danger-border);
            border-radius: 20px;
            padding: 24px;
            height: 100%;
            box-shadow: 0 4px 16px rgba(220, 38, 38, 0.06);
        }}

        /* Footer */
        .cavi-footer {{
            background: #06152b;
            color: #cbd5e1;
            border-radius: 24px;
            padding: 36px 32px;
            margin-top: 45px;
            box-shadow: 0 8px 30px rgba(0,0,0,0.2);
            border: 1px solid rgba(255,255,255,0.08);
        }}

        /* Section Numbering & Headers */
        .section-header-box {{
            margin-bottom: 24px;
            padding-bottom: 12px;
            border-bottom: 2px solid #e2e8f0;
            display: flex;
            align-items: baseline;
            gap: 14px;
            flex-wrap: wrap;
        }}

        .section-number {{
            font-size: 1.15rem;
            font-weight: 900;
            color: var(--primary-blue);
            background: #e0f2fe;
            padding: 4px 12px;
            border-radius: 8px;
            letter-spacing: 1px;
        }}

        /* Responsive Mobile Layout Adjustments */
        @media (max-width: 768px) {{
            .hero-banner {{
                padding: 24px 18px !important;
            }}
            .cavi-card {{
                padding: 18px !important;
            }}
            .emergency-strip {{
                flex-direction: column !important;
                align-items: stretch !important;
                text-align: center !important;
            }}
            .chat-bubble-villager {{
                margin-left: 10px !important;
            }}
        }}
    </style>
    """
