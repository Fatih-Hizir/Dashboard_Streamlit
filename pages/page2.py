import streamlit as st
import pandas as pd

from helpers.loader import load_data
from components.sidebar import apply_global_filters

from components.experience_chart import (
    calculate_branch_performance,
    render_scorecards_2a,
    render_scatter_4_kuadran,
    render_controls_2b,
    render_touchpoint_heatmap,
    render_friction_alert
)

# ---------------------------------------------------------------------------
# 1. LOAD DATA & MAPPING
# ---------------------------------------------------------------------------
df = apply_global_filters(load_data())
if df.empty:
    st.warning(
        "No respondents match the currently selected sidebar filters. "
        "Reset or adjust the filters to display this page."
    )
    st.stop()

mapping_path = "data/Master Mapping.csv"
try:
    df_mapping = pd.read_csv(mapping_path)
except Exception as exc:
    st.error(
        f"Unable to load the mapping file from `{mapping_path}`. "
        "Verify that the file exists and that its filename is correct."
    )
    st.caption(f"Technical detail: {exc}")
    st.stop()

# ---------------------------------------------------------------------------
# PAGE TITLE AND ANALYSIS NAVIGATION
# ---------------------------------------------------------------------------
st.title("Branch & Touchpoint Experience")
st.caption(
    "Explore branch performance, customer loyalty, touchpoint comparisons, and queue-friction indicators."
)
st.markdown("<div style='height:8px;'></div>", unsafe_allow_html=True)

tabs = [
    "🏛️ Branch Performance & Loyalty Hub",
    "🔬 Touchpoint Deep-Dive Analysis",
]
selected_tab = st.radio(
    "Analysis Navigation",
    tabs,
    label_visibility="collapsed",
    horizontal=True,
)
st.markdown(
    "<hr style='margin-top:6px;margin-bottom:20px;border:none;border-top:1px solid #E8ECF2;'>",
    unsafe_allow_html=True,
)

# ---------------------------------------------------------------------------
# ANALYSIS ROUTING
# ---------------------------------------------------------------------------
if selected_tab == tabs[0]:
    # Branch performance and loyalty view
    branch_summary = calculate_branch_performance(df, df_mapping)
    render_scorecards_2a(df, branch_summary)

    with st.container(key="p2_large_card_1"):
        render_scatter_4_kuadran(branch_summary)

elif selected_tab == tabs[1]:
    # Touchpoint comparison and queue-friction view
    with st.container(key="p2_card_filter"):
        st.markdown("""
        <div style="font-size:18px;font-weight:800;color:#1D2433;margin-bottom:4px;">
            Head-to-Head Touchpoint Analysis
        </div>
        <div style="font-size:12px;color:#5E6677;margin-bottom:15px;">
            Compare selected branches across a consistent set of service attributes.
        </div>
        """, unsafe_allow_html=True)

        selected_branches, selected_category = render_controls_2b(df, df_mapping)

    st.markdown("<div style='height:15px;'></div>", unsafe_allow_html=True) # Spacing between analysis cards

    if selected_branches:
        # Touchpoint heatmap
        with st.container(key="p2_card_heatmap"):
            render_touchpoint_heatmap(df, df_mapping, selected_branches, selected_category)

        st.markdown("<div style='height:15px;'></div>", unsafe_allow_html=True) # Spacing between analysis cards

        # Queue-friction indicators
        with st.container(key="p2_card_bullet"):
            render_friction_alert(df, selected_branches)

    else:
        st.info(
            "Select up to three branch offices above to begin the comparative analysis."
        )