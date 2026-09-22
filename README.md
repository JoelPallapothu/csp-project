# 🛡️ Cyber Aware Village Initiative (CAVI)
### *"Raising Awareness to Prevent Cyber Fraud Among Illiterate and Semi-Literate Villagers"*

**A Comprehensive Community Service Project (CSP) Web Application**  
*Tailored for Grassroots Digital Safety in Rural Andhra Pradesh, India*

---

## 🌟 Executive Summary

**Cyber Aware Village Initiative (CAVI)** is a production-grade, accessible, Telugu-first cybersecurity learning and emergency reporting platform. Designed specifically for low-literacy villagers, farmers, women, self-help groups (SHGs/DWCRA), senior citizens, and first-time digital payment users, CAVI replaces complicated cybersecurity jargon with **visual storytelling, real-life dialogue simulations, voice audio playback (`🔊 వినండి`), and interactive practice labs**.

---

## 🚀 Key Highlights & Demonstration Features

1. **🌐 Trilingual by Default (Telugu First)**:
   - **తెలుగు (Telugu - Default)**, **English**, and **हिंदी (Hindi)**.
   - Comprehensive translations across navigation, fraud explanations, real-life dialogues, quiz questions, and emergency guides.

2. **♿ Rural Accessibility Controls**:
   - **Text Sizer (`A-`, `A`, `A+`)**: Dynamically scales typography across cards and headings for senior citizens and users with visual limitations.
   - **Voice Narration (`🔊 వినండి / Listen`)**: Built-in client-side Web Speech API audio synthesis speaks warnings aloud in Telugu (`te-IN`), Hindi (`hi-IN`), or English (`en-IN`) without requiring paid third-party API keys.
   - **High-Contrast Color Indicators**: Green for Safe (సురక్షితం), Red for Danger/Fraud (మోసం), Amber for Warning.

3. **🔐 12 Common Village Cyber Frauds (Know the Fraud)**:
   - 🔐 OTP Fraud (ఓటీపీ మోసం)
   - 💳 UPI PIN Scam (డబ్బులు రావడానికి పిన్ అవసరం లేదు)
   - 🏦 Bank KYC Expiry Scam (నకిలీ కేవైసీ లింకులు)
   - 🎁 Fake Prize & Lottery Scam (లక్కీ డ్రా మోసం)
   - 📱 Screen Sharing Fraud (AnyDesk / QuickSupport హైజాక్)
   - 🚨 Digital Arrest Scam (నకిలీ పోలీస్ / సీబీఐ వీడియో కాల్)
   - 💼 Online Job / Work From Home Scam (యూట్యూబ్ లైక్స్ మోసం)
   - 📈 Fake Investment & Trading Scam (డబుల్ డబ్బుల పథకాలు)
   - 📞 Fake Customer Care Search Scam (గూగుల్ నకిలీ నంబర్లు)
   - 📲 SIM Swap / 5G Upgrade Fraud (సిమ్ క్లోనింగ్)
   - 🔗 Phishing & Electricity Cutoff Alerts (విద్యుత్ బిల్ కట్ మెసేజ్‌లు)
   - 💰 Illegal Loan App Blackmail Scam (ఫోటో మార్ఫింగ్ వేధింపులు)
   
   *Each fraud module includes:*
   - Visual 4-stage flowchart diagram
   - Red Flags (గుర్తించడం ఎలా - ❌)
   - Actionable Safe Steps (ఏం చేయాలి - ✅)
   - Real-Life Dialogue simulation (Scammer vs Villager)
   - Voice audio read-aloud button (`🔊 వినండి`)

4. **🎭 Interactive Practical Simulators**:
   - **Spot the Scam (మోసాన్ని గుర్తించండి)**: Simulated WhatsApp and SMS notification screens where the user chooses `🟢 SAFE` or `🔴 SCAM` with instant feedback and red flag breakdown.
   - **UPI PIN Safety Simulator**: Interactive mock PhonePe/GPay payment request demonstrating why **UPI PIN is only used to SEND money, NEVER to receive money**.

5. **🎥 Awareness Videos Learning Center**:
   - Filterable by 15 fraud categories and languages.
   - Verified official government awareness embeds from **I4C (Indian Cyber Crime Coordination Centre)** and **RBI Kehta Hai**.
   - Structured "3 Things to Remember" takeaways and "Did you understand?" learner feedback tracker.

6. **🛡️ 10 Golden Rules of Cyber Safety & DO vs DON'T**:
   - 10 beautifully illustrated safety rule cards.
   - Side-by-side high-contrast comparison matrix for quick village awareness.

7. **🧠 Interactive Cyber Safety Quiz**:
   - 10 village-oriented questions with large touch-friendly buttons.
   - Immediate feedback with clear explanations.
   - Final **Cyber Safety Score** and **CAVI Village Cyber Guardian (గ్రామ సైబర్ రక్షకుడు)** certificate status.

8. **🚨 Emergency Fraud Reporting (1930 & Golden Hour)**:
   - Direct 1-click dialer for **1930 National Cyber Crime Helpline**.
   - Direct integration with **[cybercrime.gov.in](https://cybercrime.gov.in/)**.
   - **The Golden Hour Protocol**: Explains why reporting within 2 to 3 hours allows banks and police to freeze stolen funds.
   - 5-step visual action plan and evidence checklist (UTR, SMS screenshots, caller ID).

9. **🖼️ Original Community Awareness Poster Showcase**:
   - High-definition rendering of the original community poster created for Village Secretariats (Grama Sachivalayam) and Panchayats.
   - Full-screen viewer and **Downloadable High-Res SVG** button.

---

## 💻 How to Run the Application

### Prerequisites
- Python 3.10+ (Python 3.12 recommended)

### Quick Start (Using existing virtual environment)
```powershell
# Navigate to the project directory
cd c:\Users\joelp\csp-project

# Run with Streamlit
.\venv\Scripts\python.exe -m streamlit run app.py
```

The application will launch in your default web browser at:
`http://localhost:8501`

---

## 📁 Project Architecture

```
csp-project/
├── app.py                      # Main entrypoint, page routing, global CSS & navigation
├── requirements.txt            # Python dependencies
├── README.md                   # Complete documentation and faculty demonstration guide
├── data/
│   ├── __init__.py
│   ├── translations.py         # Full UI translations (Telugu default, English, Hindi)
│   ├── frauds.py               # 12 detailed fraud modules with visual workflows, dialogs & audio
│   ├── rules.py                # 10 Golden Rules & Do's vs Don'ts matrix
│   ├── quiz_data.py            # 10 Village-oriented interactive quiz questions
│   ├── videos_data.py          # Official verified awareness videos registry
│   └── simulations_data.py     # "Spot the Scam" scenarios & UPI Simulator configuration
├── components/
│   ├── __init__.py
│   ├── header_nav.py           # Top utility bar, language switch, font size controls, 1930 strip
│   ├── fraud_card.py           # Fraud cards grid & detailed drilldown learning view
│   ├── simulations.py          # "Spot the Scam" & UPI PIN Simulator
│   ├── video_center.py         # Awareness video center with category filters & feedback
│   ├── safety_guide.py         # 10 Golden Rules & Do's vs Don'ts comparison
│   ├── quiz.py                 # Interactive quiz with score calculator & badge
│   ├── emergency_view.py       # 1930 helpline, Golden Hour tips, cybercrime.gov.in portal guidance
│   ├── poster_showcase.py      # Original CSP Awareness Poster viewer & download
│   ├── about_view.py           # Project background, objectives, and rural methodology
│   └── footer.py               # Official helpline links, CSP attribution, trust badges
├── assets/
│   ├── logo.svg                # CAVI brand logo emblem
│   └── poster/
│       └── cavi_awareness_poster.svg  # Original Community Awareness Poster (1200x1680)
└── utils/
    ├── __init__.py
    ├── styling.py              # Modern CSS (glassmorphism, high contrast, responsive cards)
    └── helpers.py              # Accessibility helpers, state managers, audio speech synthesis script
```

---

## 🎓 Faculty Demonstration Walkthrough Guide

When presenting this project to college faculty, evaluators, or during a community exhibition, follow this recommended 5-minute demonstration flow:

1. **Introduction & Identity (Home Page)**:
   - Highlight that the app loads in **Telugu by default**, acknowledging the reality of rural Andhra Pradesh where digital literacy barriers exist.
   - Demonstrate the **Text Sizer (`A-`, `A`, `A+`)** at the top right to showcase accessibility for senior citizens.
   - Point to the **1930 Emergency Banner** at the top.
   - Show the **Original Community Awareness Poster** right on the home page with the download button.

2. **Know the Fraud (Visual Storytelling & Dialogue)**:
   - Click on **🔐 సైబర్ మోసాలు (Know the Fraud)**.
   - Open **ఓటీపీ మోసం (OTP Fraud)** or **యూపీఐ మోసం (UPI Fraud)**.
   - Tap the **🔊 వినండి (Listen)** button to hear the audio narration.
   - Show the 4-step visual flow diagram and the realistic **Scammer vs Villager dialogue**.

3. **Interactive Scam Simulators**:
   - Click on **🎭 మోసాల డెమోలు (Simulators)**.
   - Demonstrate **"Spot the Scam"**: Walk through a simulated WhatsApp lottery message, click `🔴 SCAM`, and show the instant red flag explanation.
   - Switch to **UPI Safety Simulator**: Tap `👉 PAY / ENTER PIN` to trigger the **BIG RED WARNING SCREEN** teaching that entering a PIN debits money rather than credits it.

4. **Awareness Video Learning Center**:
   - Click on **🎥 వీడియోలు (Videos)**.
   - Use the dropdown to filter by fraud type (e.g. OTP or UPI).
   - Show the official government source attribution (**I4C / RBI Kehta Hai**).
   - Show the "3 Things to Remember" recap and the "Did you understand?" feedback buttons.

5. **Cyber Safety Quiz & 1930 Reporting Protocol**:
   - Complete the **10-question quiz** to display the final **Cyber Safety Score** and **CAVI Village Cyber Guardian badge**.
   - Navigate to **🚨 ఫిర్యాదు చేయండి (1930 Report)** to showcase the **Golden Hour protocol** (reporting within 2-3 hours) and the official link to **cybercrime.gov.in**.

---

## 🔒 Security & Privacy Ethics
- **No Personal Data Collection**: The application does not collect, store, or transmit any sensitive personal data (Aadhaar numbers, bank account numbers, PINs, or passwords).
- **Educational Only**: All simulated interfaces clearly state *"EDUCATIONAL DEMONSTRATION ONLY"*.
