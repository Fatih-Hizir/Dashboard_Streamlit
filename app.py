
import streamlit as st

from helpers.loader import load_data
from components.sidebar import render_sidebar


# ──────────────────────────────────────────────────────────────────────────────
# 1. PAGE CONFIG
# Must remain the first Streamlit command in the application.
# ──────────────────────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Bank XYZ CX Dashboard",
    page_icon="🏦",
    layout="wide",
    initial_sidebar_state="expanded",
)


# ──────────────────────────────────────────────────────────────────────────────
# 2. GLOBAL DESIGN SYSTEM
# ──────────────────────────────────────────────────────────────────────────────
st.markdown(
    """
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
    <link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Rounded:opsz,wght,FILL,GRAD@20..48,400,0,0" rel="stylesheet">

    <style>
    :root {
        --cx-blue: #0069FF;
        --cx-blue-dark: #0055D4;
        --cx-red: #BB2649;
        --cx-red-soft: #FFF0F4;
        --cx-green: #2FBF71;
        --cx-text-primary: #1D2433;
        --cx-text-secondary: #5E6677;
        --cx-text-muted: #98A1B3;
        --cx-page-bg: #FFF5F8;
        --cx-card-bg: #FFFFFF;
        --cx-chart-bg: #FCFDFF;
        --cx-border: #E8ECF2;
        --cx-shadow: 0 10px 22px rgba(29, 36, 51, 0.06);
        --cx-shadow-hover: 0 18px 30px rgba(29, 36, 51, 0.10);
    }

    html,
    body,
    [data-testid="stAppViewContainer"],
    button,
    input,
    textarea,
    select {
        font-family: "Inter", -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif !important;
        color: var(--cx-text-primary);
    }

    p,
    label,
    [data-testid="stCaptionContainer"] {
        font-family: "Inter", -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif !important;
        color: var(--cx-text-secondary);
    }

    [data-testid="stIconMaterial"],
    .material-symbols-rounded,
    .material-symbols-outlined {
        font-family: "Material Symbols Rounded" !important;
        font-weight: normal !important;
        font-style: normal !important;
        font-size: 20px !important;
        line-height: 1 !important;
        letter-spacing: normal !important;
        text-transform: none !important;
        white-space: nowrap !important;
        word-wrap: normal !important;
        direction: ltr !important;
        -webkit-font-feature-settings: "liga" !important;
        -webkit-font-smoothing: antialiased !important;
        font-feature-settings: "liga" !important;
    }

    [data-testid="stAppViewContainer"] {
        background: var(--cx-page-bg) !important;
    }

    [data-testid="stHeader"] {
        background: transparent !important;
    }

    .block-container {
        max-width: 100% !important;
        padding-top: 1.5rem !important;
        padding-right: 2rem !important;
        padding-bottom: 2rem !important;
        padding-left: 2rem !important;
    }

    h1,
    h2,
    h3 {
        color: var(--cx-text-primary) !important;
        letter-spacing: -0.03em !important;
    }

    h1 {
        font-size: 2rem !important;
        font-weight: 800 !important;
    }


    #MainMenu,
    footer,
    [data-testid="stSidebarCollapseButton"],
    [data-testid="collapsedControl"],
    [data-testid="stSidebarResizer"] {
        visibility: hidden !important;
        display: none !important;
    }

    /* KPI cards */
    .st-key-card_kpi_1,
    .st-key-card_kpi_2,
    .st-key-card_kpi_3,
    .st-key-card_kpi_4,
    .st-key-card_kpi_5,
    .st-key-kpi_comp_1,
    .st-key-kpi_comp_2,
    .st-key-kpi_comp_3,
    .st-key-kpi_comp_4 {
        height: 150px !important;
        display: flex !important;
        align-items: center !important;
        padding: 1.35rem !important;
        overflow: hidden !important;
        background: var(--cx-card-bg) !important;
        border: 1px solid rgba(232, 236, 242, 0.75) !important;
        border-radius: 18px !important;
        box-shadow: var(--cx-shadow) !important;
        transition: transform 0.22s ease, box-shadow 0.22s ease !important;
    }

    /* Chart and analysis containers */
    .st-key-large_card_1,
    .st-key-large_card_2,
    .st-key-medium_card_1,
    .st-key-medium_card_2,
    .st-key-geomap_card,
    .st-key-p2_large_card_1,
    .st-key-p2_card_filter,
    .st-key-p2_card_heatmap,
    .st-key-p2_card_bullet,
    .st-key-p1_card_bubble,
    .st-key-p1_card_persona,
    .st-key-p3_card_bar,
    .st-key-p3_card_radar,
    .st-key-p3_card_filter,
    .st-key-p3_card_heatmap {
        padding: 1.4rem !important;
        overflow: visible !important;
        background: var(--cx-chart-bg) !important;
        border: 1px solid rgba(232, 236, 242, 0.75) !important;
        border-radius: 18px !important;
        box-shadow: var(--cx-shadow) !important;
        transition: transform 0.22s ease, box-shadow 0.22s ease !important;
    }

    .st-key-p1_card_bubble,
    .st-key-p1_card_persona {
        height: 480px !important;
    }

    .st-key-card_kpi_1:hover,
    .st-key-card_kpi_2:hover,
    .st-key-card_kpi_3:hover,
    .st-key-card_kpi_4:hover,
    .st-key-card_kpi_5:hover,
    .st-key-kpi_comp_1:hover,
    .st-key-kpi_comp_2:hover,
    .st-key-kpi_comp_3:hover,
    .st-key-kpi_comp_4:hover,
    .st-key-large_card_1:hover,
    .st-key-large_card_2:hover,
    .st-key-medium_card_1:hover,
    .st-key-medium_card_2:hover,
    .st-key-geomap_card:hover,
    .st-key-p2_large_card_1:hover,
    .st-key-p2_card_filter:hover,
    .st-key-p2_card_heatmap:hover,
    .st-key-p2_card_bullet:hover,
    .st-key-p1_card_bubble:hover,
    .st-key-p1_card_persona:hover,
    .st-key-p3_card_bar:hover,
    .st-key-p3_card_radar:hover,
    .st-key-p3_card_filter:hover,
    .st-key-p3_card_heatmap:hover {
        transform: translateY(-2px);
        box-shadow: var(--cx-shadow-hover) !important;
    }

    /* Shared KPI typography */
    .kpi-title {
        color: var(--cx-text-secondary) !important;
        font-size: 12px !important;
        font-weight: 700 !important;
        letter-spacing: 0.02em !important;
        text-transform: uppercase;
    }

    .kpi-value-large {
        color: var(--cx-text-primary) !important;
        font-size: 30px !important;
        font-weight: 800 !important;
        line-height: 1 !important;
        letter-spacing: -0.04em !important;
    }

    .kpi-subtitle {
        color: var(--cx-text-muted) !important;
        font-size: 12px !important;
        font-weight: 600 !important;
    }

    .saving-positive {
        color: var(--cx-green) !important;
    }

    .saving-negative {
        color: var(--cx-red) !important;
    }

    /* Page-level tab radios only; sidebar navigation is handled separately. */
    .main div.stRadio > div[role="radiogroup"] {
        display: flex;
        flex-direction: row;
        gap: 8px;
    }

    .main div.stRadio > div[role="radiogroup"] label {
        min-height: 40px;
        padding: 9px 16px;
        cursor: pointer;
        background: #FFFFFF;
        border: 1px solid var(--cx-border);
        border-radius: 10px;
        transition: all 0.18s ease;
    }

    .main div.stRadio > div[role="radiogroup"] label:hover {
        border-color: rgba(0, 105, 255, 0.35);
        background: #F4F8FF;
    }

    .main div.stRadio > div[role="radiogroup"] label:has(input:checked) {
        color: #FFFFFF !important;
        background: linear-gradient(135deg, var(--cx-blue), var(--cx-blue-dark)) !important;
        border-color: transparent !important;
        box-shadow: 0 7px 16px rgba(0, 105, 255, 0.20);
    }

    .main div.stRadio > div[role="radiogroup"] label:has(input:checked) p {
        color: #FFFFFF !important;
        font-weight: 800 !important;
    }

    .js-plotly-plot .plotly .modebar {
        display: none !important;
    }

    @media (max-width: 1100px) {
        .block-container {
            padding-right: 1.2rem !important;
            padding-left: 1.2rem !important;
        }
    }
    </style>
    """,
    unsafe_allow_html=True,
)


# ──────────────────────────────────────────────────────────────────────────────
# 3. SHARED SIDEBAR
# ──────────────────────────────────────────────────────────────────────────────
sidebar_df = load_data()
render_sidebar(sidebar_df)


# ──────────────────────────────────────────────────────────────────────────────
# 4. PAGE ROUTING
# Native navigation is hidden because the custom sidebar renders the page links.
# ──────────────────────────────────────────────────────────────────────────────
pg = st.navigation(
    [
        st.Page(
            "pages/page1.py",
            title="Respondent Profile",
            icon=":material/groups:",
        ),
        st.Page(
            "pages/page2.py",
            title="Bank XYZ Performance",
            icon=":material/account_balance:",
        ),
        st.Page(
            "pages/page3.py",
            title="Competitor Performance",
            icon=":material/compare_arrows:",
        ),
    ],
    position="hidden",
)

pg.run()