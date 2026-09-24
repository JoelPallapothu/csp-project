"""
CAVI - Cyber Aware Village Initiative
Awareness Videos Learning Center with Fraud Category & Language Filter,
Official Government Resource Badges, "3 Things to Remember", Safety Tips, and Audio Narration.
Bilingual: Telugu (Default) and English.
"""

import streamlit as st
from data.videos_data import (
    VIDEO_CATEGORIES, filter_videos, OFFICIAL_GOV_VIDEO_PORTAL, RBI_KEHTA_HAI_PORTAL
)
from utils.helpers import get_current_lang, record_video_view, render_speech_audio_button
from utils.styling import render_html

def render_video_center():
    lang = get_current_lang()

    # Subtitle & Purpose
    sub_text = (
        '"సైబర్ మోసాలు ఎలా జరుగుతాయో వీడియోల ద్వారా సులభంగా చూసి నేర్చుకోండి – మీ కుటుంబాన్ని రక్షించుకోండి."'
        if lang == "te" else
        '"Learn how cyber fraud happens through official videos — protect yourself and your family."'
    )
    render_html(f"""
    <div style="margin-bottom: 24px;">
        <p style="font-size: 1.2rem; color: #475569; margin: 0; font-weight: 500;">
            {sub_text}
        </p>
    </div>
    """)

    # Official Video Portals Strip
    gov_heading = "భారత ప్రభుత్వ అధికారిక సైబర్ అవగాహన వేదికలు:" if lang == "te" else "Official Government Cyber Awareness Portals:"
    render_html(f"""
    <div style="background: #f0f9ff; border: 1.5px solid #bae6fd; border-radius: 20px; padding: 18px 24px; display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 14px; margin-bottom: 26px;">
        <div>
            <div style="font-weight: 900; color: #063970; font-size: 1.15rem; display: flex; align-items: center; gap: 8px;">
                <span>🏛️</span> <span>{gov_heading}</span>
            </div>
            <div style="font-size: 0.95rem; color: #334155; margin-top: 3px;">
                National Cyber Crime Portal (I4C, MHA) & Reserve Bank of India (RBI Kehta Hai)
            </div>
        </div>
        <div style="display: flex; gap: 12px; flex-wrap: wrap;">
            <a href="{OFFICIAL_GOV_VIDEO_PORTAL}" target="_blank" style="background: #063970; color: #ffffff; padding: 10px 18px; border-radius: 12px; text-decoration: none; font-weight: 800; font-size: 0.95rem; display: inline-flex; align-items: center; gap: 6px;">
                <span>🌐</span> <span>CyberAware Portal ↗</span>
            </a>
            <a href="{RBI_KEHTA_HAI_PORTAL}" target="_blank" style="background: #168447; color: #ffffff; padding: 10px 18px; border-radius: 12px; text-decoration: none; font-weight: 800; font-size: 0.95rem; display: inline-flex; align-items: center; gap: 6px;">
                <span>🏦</span> <span>RBI Kehta Hai Portal ↗</span>
            </a>
        </div>
    </div>
    """)

    # Two Filters: Fraud Category + Language
    filter_col1, filter_col2 = st.columns([7, 3])
    with filter_col1:
        cat_label = "🔍 మోసం వర్గాన్ని ఎంచుకోండి (Filter Category):" if lang == "te" else "🔍 Filter by Fraud Category:"
        render_html(f"<div style='font-size: 0.92rem; font-weight: 800; color: #063970; margin-bottom: 6px;'>{cat_label}</div>")
        selected_cat = st.selectbox(
            "Filter Category",
            options=VIDEO_CATEGORIES,
            index=0,
            label_visibility="collapsed",
            key="video_cat_filter"
        )
    with filter_col2:
        lang_filter_label = "🌐 వీడియో భాష (Video Language):" if lang == "te" else "🌐 Video Language:"
        render_html(f"<div style='font-size: 0.92rem; font-weight: 800; color: #063970; margin-bottom: 6px;'>{lang_filter_label}</div>")
        selected_vlang = st.selectbox(
            "Video Language",
            options=["అన్నీ (All Languages)", "తెలుగు (Telugu)", "English"],
            index=0,
            label_visibility="collapsed",
            key="video_lang_filter"
        )

    filtered = filter_videos(selected_cat, lang=lang)
    avail_text = f"అందుబాటులో ఉన్న అవగాహన వీడియోలు: <b>{len(filtered)}</b>" if lang == "te" else f"Available Awareness Videos: <b>{len(filtered)}</b>"
    render_html(f"<div style='font-size: 1.05rem; font-weight: 800; color: #0b63ce; margin: 12px 0 24px 0;'>{avail_text}</div>")

    # Render video cards
    for vid in filtered:
        v_title = vid["title"].get(lang, vid["title"]["te"])
        v_desc = vid["description"].get(lang, vid["description"]["te"])
        three_things = vid["three_things_to_remember"].get(lang, vid["three_things_to_remember"]["te"])
        safety_tip = vid.get("safety_tip", {}).get(lang, vid.get("safety_tip", {}).get("te", ""))
        source_label = "అధికారిక మూలం: " if lang == "te" else "Official Source: "

        render_html(f"""
        <div class="cavi-card" style="border-top: 5px solid #0b63ce; margin-bottom: 30px;">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 14px; flex-wrap: wrap; gap: 8px;">
                <span class="badge-pill badge-info">{vid['category']}</span>
                <span style="font-size: 0.9rem; font-weight: 800; color: #475569;">🌐 {vid['language']} • ⏱️ {vid['duration']}</span>
                <span class="badge-pill badge-safe">{source_label}{vid['source']}</span>
            </div>
            <h3 style="color: #063970; margin: 0 0 10px 0; font-size: 1.55rem; font-weight: 900;">🎥 {v_title}</h3>
            <p style="font-size: 1.12rem; color: #334155; line-height: 1.6; margin-bottom: 14px;">{v_desc}</p>
        </div>
        """)

        col_player, col_recap = st.columns([6, 5])

        with col_player:
            if vid["has_embed"]:
                st.video(vid["embed_url"])
                record_video_view(vid["id"])
            else:
                # Required coming soon placeholder card
                cs_title = "🎥 Awareness Video Coming Soon"
                cs_desc = "An official awareness video can be added here."
                cs_portal_btn = "అధికారిక పోర్టల్ లో చూడండి ↗" if lang == "te" else "Watch on Official Portal ↗"
                render_html(f"""
                <div style="background: #f8fafc; border: 2.5px dashed #94a3b8; border-radius: 20px; padding: 36px 24px; text-align: center;">
                    <div style="font-size: 3.2rem; margin-bottom: 10px;">🏛️</div>
                    <div style="font-weight: 950; color: #063970; font-size: 1.3rem; margin-bottom: 6px;">
                        {cs_title}
                    </div>
                    <div style="font-size: 1.05rem; color: #64748b; margin-bottom: 18px; line-height: 1.5;">
                        "{cs_desc}"
                    </div>
                    <a href="{vid['official_source_url']}" target="_blank" 
                       style="background: linear-gradient(135deg, #063970 0%, #0b63ce 100%); color: white; padding: 12px 24px; border-radius: 12px; text-decoration: none; font-weight: 800; font-size: 1.0rem; display: inline-block; box-shadow: 0 4px 14px rgba(6,57,112,0.25);">
                        {cs_portal_btn}
                    </a>
                </div>
                """)

        with col_recap:
            three_things_title = "💡 3 ముఖ్యమైన విషయాలు (3 Things to Remember):" if lang == "te" else "💡 3 Things to Remember:"
            three_things_items = "".join([f'<li style="margin-bottom: 8px; font-weight: 600;">{item}</li>' for item in three_things])
            
            render_html(f"""
            <div style="background: #ffffff; border: 1px solid #e2e8f0; border-radius: 20px; padding: 22px; box-shadow: 0 4px 16px rgba(0,0,0,0.05); height: 100%; display: flex; flex-direction: column; justify-content: space-between;">
                <div>
                    <h4 style="color: #063970; margin-top: 0; display: flex; align-items: center; gap: 8px; font-size: 1.25rem; font-weight: 900;">
                        {three_things_title}
                    </h4>
                    <ol style="font-size: 1.05rem; color: #1e293b; line-height: 1.65; padding-left: 20px; margin-bottom: 16px;">
                        {three_things_items}
                    </ol>
                    
                    <!-- Safety Tip Banner -->
                    <div style="background: #f0fdf4; border-left: 4px solid #168447; border-radius: 10px; padding: 12px 14px; margin-bottom: 14px; font-size: 0.98rem; color: #166534; font-weight: 700; line-height: 1.5;">
                        {safety_tip}
                    </div>
                </div>
                
                <div>
                    <!-- Audio TTS Listen Button for video explanation -->
                    <div style="margin-bottom: 10px;">
                        <span style="font-size: 0.88rem; font-weight: 800; color: #475569;">🔊 వివరణ వినండి (Listen):</span>
                    </div>
                </div>
            </div>
            """)
            render_speech_audio_button(v_desc + " " + safety_tip, lang=lang, key_id=f"vid_tts_{vid['id']}")

            understood_prompt = "ఈ వీడియోలోని విషయం మీకు అర్థమైందా?" if lang == "te" else "Did you understand this lesson?"
            yes_btn = "✅ అవును, అర్థమైంది" if lang == "te" else "✅ Yes, Understood"
            again_btn = "🔄 మరోసారి చూడండి" if lang == "te" else "🔄 Review Again"
            
            render_html(f"<div style='font-size: 0.92rem; font-weight: 800; color: #063970; margin: 12px 0 6px 0; text-align: center;'>{understood_prompt}</div>")
            fb_col1, fb_col2 = st.columns(2)
            with fb_col1:
                if st.button(yes_btn, key=f"btn_yes_{vid['id']}", type="primary", use_container_width=True):
                    record_video_view(vid["id"])
                    st.success("చాలా మంచిది! మీ అవగాహన స్కోర్ పెరిగింది. 👏" if lang == "te" else "Great! Your Cyber Safety score updated. 👏")
            with fb_col2:
                if st.button(again_btn, key=f"btn_again_{vid['id']}", use_container_width=True):
                    st.info("పైనున్న 3 ముఖ్య విషయాలను మరోసారి చదవండి!" if lang == "te" else "Review the 3 Things to Remember above!")

        render_html("<hr style='margin: 32px 0;'>")
