"""
Custom metric display components with retro gaming aesthetics.
"""

import streamlit as st
from .styles import COLORS


def pixel_metric(label, value, color=COLORS['text'], max_value=100, animate=False):
    """
    Display a metric in retro gaming style with pixel-art progress bar.
    
    Parameters:
    -----------
    label : str
        Metric label
    value : str or numeric
        Value to display
    color : str
        Color for the metric (hex code)
    max_value : numeric
        Maximum value for the progress bar
    animate : bool
        Whether to add animation effect
    """
    # Calculate percentage for the progress bar
    if isinstance(value, str):
        # Handle string values (like formatted numbers)
        try:
            # Remove commas and try to convert to float
            numeric_value = float(value.replace(',', ''))
            percent = min(100, max(0, (numeric_value / max_value) * 100))
        except ValueError:
            # If conversion fails, set to 50%
            percent = 50
    else:
        # Handle numeric values directly
        percent = min(100, max(0, (value / max_value) * 100))
    
    # Create pixel blocks for the progress bar
    blocks = int(percent / 5)  # 20 blocks for 100%
    progress_bar = ""
    
    for i in range(20):
        if i < blocks:
            progress_bar += f"<span style='color:{color}'>█</span>"
        else:
            progress_bar += "<span style='color:#333355'>█</span>"
    
    animation = "animation: pulse 2s infinite;" if animate else ""
    
    st.markdown(f"""
    <div style="
        background-color: rgba(26, 26, 64, 0.7);
        border: 4px solid {color};
        border-radius: 0px;
        padding: 15px;
        margin: 10px 0;
        box-shadow: 5px 5px 0px #000000;
        text-align: center;
        {animation}
    ">
        <div style="font-family: 'Press Start 2P', monospace; font-size: 0.9em; margin-bottom: 10px; color: {color};">
            {label}
        </div>
        <div style="font-family: 'VT323', monospace; font-size: 2em; color: {color}; text-shadow: 2px 2px 0px #000000;">
            {value}
        </div>
        <div style="font-family: monospace; font-size: 24px; letter-spacing: -1px; margin-top: 5px;">
            {progress_bar}
        </div>
    </div>
    """, unsafe_allow_html=True)


def display_metrics_row(metrics, col_count=4):
    """
    Display a row of metrics in an arcade style.
    
    Parameters:
    -----------
    metrics : list of dict
        List of metrics, each with 'label', 'value', 'color', and 'max' keys
    col_count : int
        Number of columns to use
    """
    # Create columns
    cols = st.columns(col_count)
    
    # Assign metrics to columns
    for i, metric in enumerate(metrics):
        with cols[i % col_count]:
            pixel_metric(
                label=metric['label'],
                value=metric['value'],
                color=metric.get('color', COLORS['text']),
                max_value=metric.get('max_value', 100),
                animate=metric.get('animate', False)
            )


def get_brut_impact_kpis():
    """
    Get predefined impact KPIs for Brut B Corp metrics.
    
    Returns:
    --------
    dict
        Dictionary with impact KPI values
    """
    # Hypothetical impact KPIs for B Corp status
    kpis = {
        'Percentage of Impact Content': 65,
        'Content Diversity Score': 82,
        'Environmental Footprint Reduction': 28,
        'Community Engagement Hours': 1250,
        'Inclusive Hiring Rate': 93,
        'Sustainability Score': 78
    }
    return kpis


def display_impact_scoreboard():
    """
    Display the B Corp impact metrics in a retro scoreboard style.
    """
    # Get impact KPIs
    impact_kpis = get_brut_impact_kpis()
    
    # Create columns for better layout
    kpi_cols = st.columns(3)
    
    with kpi_cols[0]:
        pixel_metric("IMPACT CONTENT", f"{impact_kpis['Percentage of Impact Content']}%", COLORS['accent2'], 100)
        pixel_metric("DIVERSITY SCORE", f"{impact_kpis['Content Diversity Score']}", COLORS['accent4'], 100)
    
    with kpi_cols[1]:
        pixel_metric("ENV. REDUCTION", f"{impact_kpis['Environmental Footprint Reduction']}%", COLORS['accent1'], 100)
        pixel_metric("COMMUNITY HRS", f"{impact_kpis['Community Engagement Hours']}", COLORS['accent3'], 2000)
    
    with kpi_cols[2]:
        pixel_metric("INCLUSIVE HIRING", f"{impact_kpis['Inclusive Hiring Rate']}%", COLORS['accent2'], 100)
        pixel_metric("SUSTAIN SCORE", f"{impact_kpis['Sustainability Score']}", COLORS['accent1'], 100)