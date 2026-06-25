import streamlit as st
import pandas as pd
import os
from helpers.loader import load_data
from components.sidebar import apply_global_filters

from components.competitor_chart import (
    render_competitor_kpis,
    render_competitor_macro_charts,
    render_competitor_heatmap
)

##################################################################
# DATA
##################################################################

df = apply_global_filters(load_data())
if df.empty:
    st.warning(
        "No respondents match the currently selected sidebar filters. "
        "Reset or adjust the filters to display this page."
    )
    st.stop()

# Logic Cerdas: Mengamankan path pembacaan file mapping kompetitor
path_1 = "data/Kompetitor Mapping.csv"
path_2 = "data/Mapping Touchpoint Bank XYZ vs Kompetitor - Page 3 - Mapping Touchpoint Bank XYZ vs Kompetitor - Page 3.csv"

if os.path.exists(path_1):
    df_mapping_p3 = pd.read_csv(path_1)
elif os.path.exists(path_2):
    df_mapping_p3 = pd.read_csv(path_2)
else:
    st.error("File mapping Page 3 tidak ditemukan. Harap pastikan file mapping diletakkan di folder 'data/'.")
    st.stop()

##################################################################
# HEADER
##################################################################

st.title("Competitor Performance & Benchmarking")
st.markdown("<div style='height:10px;'></div>", unsafe_allow_html=True)

##################################################################
# ROW 1 — KPI CARDS
##################################################################

df_processed = render_competitor_kpis(df, df_mapping_p3)

st.markdown(
    "<div style='height:18px;'></div>",
    unsafe_allow_html=True
)

##################################################################
# ROW 2 — MACRO CHARTS (BAR TOP 5 & RADAR CHART)
##################################################################

render_competitor_macro_charts(df_processed, df_mapping_p3)

st.markdown(
    "<div style='height:18px;'></div>",
    unsafe_allow_html=True
)

##################################################################
# ROW 3 — MICRO HEATMAP DEEP-DIVE
##################################################################

render_competitor_heatmap(df_processed, df_mapping_p3)