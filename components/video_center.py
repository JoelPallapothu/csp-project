"""
CAVI - Cyber Aware Village Initiative
Awareness Videos Learning Center with Category Filter,
Official Government Resource Badges, "3 Things to Remember", and Interactive Feedback
"""

import streamlit as st
from data.videos_data import (
    VIDEO_CATEGORIES, filter_videos, OFFICIAL_GOV_VIDEO_PORTAL, RBI_KEHTA_HAI_PORTAL
)
from utils.helpers import get_current_lang, record_video_view
from utils.styling import render_html

def render_video_center():
    lang = get_current_lang()

    # Header section
    render_html("""
    <div style="margin-bottom: 22px;">
        <h2 style="color: #091b36; margin-bottom: 6px;">🎥 సైబర్ మోసాల అవగాహన వీడియో కేంద్రం (Video Learning Center)</h2>
        <p style="font-size: 1.15rem; color: #475569;">
            "సైబర్ మోసాలు ఎలా జరుగుతాయో వీడియోల ద్వారా సులభంగా చూసి నేర్చుకోండి – మీ కుటుంబాన్ని రక్షించుకోండి."
        </p>
    </div>
    """)

    # Official Video Portals Strip
    render_html(f"""
    <div style="background: #f0f9ff; border: 1.5px solid #bae6fd; border-radius: 18px; padding: 16px 22px; display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 12px; margin-bottom: 24px;">
        <div>
            <div style="font-weight: 900; color: #0369a1; font-size: 1.1rem; display: flex; align-items: center; gap: 8px;">
                <span>🏛️</span> <span>భారత ప్రభుత్వ అధికారిక సైబర్ అవగాహన వేదికలు:</span>
            </div>
            <div style="font-size: 0.95rem; color: #334155; margin-top: 3px;">
                National Cyber Crime Portal (I4C) & Reserve Bank of India (RBI Kehta Hai)
            </div>
        </div>
        <div style="display: flex; gap: 10px; flex-wrap: wrap;">
            <a href="{OFFICIAL_GOV_VIDEO_PORTAL}" target="_blank" style="background: #091b36; color: #ffffff; padding: 8px 16px; border-radius: 10px; text-decoration: none; font-weight: 800; font-size: 0.92rem; display: inline-flex; align-items: center; gap: 6px;">
                <span>🌐</span> <span>CyberAware Videos ↗</span>
            </a>
            <a href="{RBI_KEHTA_HAI_PORTAL}" target="_blank" style="background: #15803d; color: #ffffff; padding: 8px 16px; border-radius: 10px; text-decoration: none; font-weight: 800; font-size: 0.92rem; display: inline-flex; align-items: center; gap: 6px;">
                <span>🏦</span> <span>RBI Kehta Hai Portal ↗</span>
            </a>
        </div>
    </div>
    """)

    # Category Filter
    render_html("##### 🔍 మోసం వర్గాన్ని ఎంచుకోండి (Select Fraud Category):")
    selected_cat = st.selectbox(
        "Filter Category",
        options=VIDEO_CATEGORIES,
        index=0,
        label_visibility="collapsed",
        key="video_cat_filter"
    )

    filtered = filter_videos(selected_cat)
    render_html(f"<div style='font-size: 0.98rem; font-weight: 700; color: #0284c7; margin-bottom: 20px;'>అందుబాటులో ఉన్న అవగాహన వీడియోలు: <b>{len(filtered)}</b></div>")

    # Render video cards
    for vid in filtered:
        v_title = vid["title"].get(lang, vid["title"]["te"])
        v_desc = vid["description"].get(lang, vid["description"]["te"])
        three_things = vid["three_things_to_remember"].get(lang, vid["three_things_to_remember"]["te"])

        render_html(f"""
        <div class="cavi-card" style="border-top: 5px solid #0284c7; margin-bottom: 26px;">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px; flex-wrap: wrap; gap: 8px;">
                <span class="badge-pill badge-info">{vid['category']}</span>
                <span style="font-size: 0.88rem; font-weight: 800; color: #475569;">🌐 {vid['language']} • ⏱️ {vid['duration']}</span>
                <span class="badge-pill badge-safe">అధికారిక మూలం: {vid['source']}</span>
            </div>
            <h3 style="color: #091b36; margin-top: 0; font-size: 1.45rem;">🎥 {v_title}</h3>
            <p style="font-size: 1.08rem; color: #334155; line-height: 1.55; margin-bottom: 18px;">{v_desc}</p>
        </div>
        """)

        col_player, col_recap = st.columns([6, 5])

        with col_player:
            if vid["has_embed"]:
                st.video(vid["embed_url"])
                record_video_view(vid["id"])
            else:
                render_html(f"""
                <div style="background: #f8fafc; border: 2.5px dashed #94a3b8; border-radius: 20px; padding: 36px 24px; text-align: center;">
                    <div style="font-size: 3.2rem; margin-bottom: 8px;">🏛️</div>
                    <div style="font-weight: 900; color: #091b36; font-size: 1.2rem; margin-bottom: 6px;">
                        కేంద్ర ప్రభుత్వ అధికారిక అవగాహన వీడియో
                    </div>
                    <div style="font-size: 0.98rem; color: #64748b; margin-bottom: 16px; line-height: 1.45;">
                        {vid.get('placeholder_note', 'Official resource available via portal')}
                    </div>
                    <a href="{vid['official_source_url']}" target="_blank" 
                       style="background: linear-gradient(135deg, #0f2b5c 0%, #1d4ed8 100%); color: white; padding: 10px 22px; border-radius: 10px; text-decoration: none; font-weight: 800; font-size: 1.0rem; display: inline-block; box-shadow: 0 4px 12px rgba(15,43,92,0.25);">
                        అధికారిక పోర్టల్ లో చూడండి ↗
                    </a>
                </div>
                """)

        with col_recap:
            three_things_items = "".join([f'<li style="margin-bottom: 8px; font-weight: 600;">{item}</li>' for item in three_things])
            render_html(f"""
            <div style="background: #ffffff; border: 1px solid #e2e8f0; border-radius: 20px; padding: 22px; box-shadow: 0 4px 16px rgba(0,0,0,0.05); height: 100%; display: flex; flex-direction: column; justify-content: space-between;">
                <div>
                    <h4 style="color: #091b36; margin-top: 0; display: flex; align-items: center; gap: 8px; font-size: 1.2rem;">
                        <span>💡</span> 3 ముఖ్యమైన విషయాలు (3 Things to Remember):
                    </h4>
                    <ol style="font-size: 1.02rem; color: #1e293b; line-height: 1.6; padding-left: 20px; margin-bottom: 18px;">
                        {three_things_items}
                    </ol>
                </div>
                
                <div style="background: #f8fafc; border-radius: 14px; padding: 14px; border: 1px solid #cbd5e1;">
                    <div style="font-size: 0.95rem; font-weight: 800; color: #091b36; margin-bottom: 10px; text-align: center;">
                        ఈ వీడియోలోని విషయం మీకు అర్థమైందా? (Did you understand?)
                    </div>
                </div>
            </div>
            """)

            fb_col1, fb_col2 = st.columns(2)
            with fb_col1:
                if st.button("✅ అవును, అర్థమైంది", key=f"btn_yes_{vid['id']}", type="primary", use_container_width=True):
                    record_video_view(vid["id"])
                    st.success("చాలా మంచిది! మీ సైబర్ అవగాహన స్కోర్ పెరిగింది. 👏")
            with fb_col2:
                if st.button("🔄 మరోసారి నేర్చుకోండి", key=f"btn_again_{vid['id']}", use_container_width=True):
                    st.info("సందేహం లేదు, పైనున్న 3 ముఖ్య విషయాలను మరోసారి చదవండి!")

        render_html("<hr style='margin: 30px 0;'>")
