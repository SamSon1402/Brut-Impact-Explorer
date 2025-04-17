"""
CSS styles and theme configuration for retro gaming aesthetics.
"""

# Define retro gaming colors
COLORS = {
    'background': '#0D0D2B',
    'text': '#33FF33',
    'accent1': '#FF3333',
    'accent2': '#33CCFF',
    'accent3': '#FFCC00',
    'accent4': '#CC33FF',
    'grid': '#1A1A40'
}


def get_retro_css():
    """
    Returns CSS for the retro gaming theme.
    """
    return f"""
    <style>
        /* Import retro fonts */
        @import url('https://fonts.googleapis.com/css2?family=VT323&family=Press+Start+2P&family=Space+Mono&display=swap');
        
        /* Main background and text */
        .stApp {{
            background-color: {COLORS['background']};
            color: {COLORS['text']};
            background-image: 
                linear-gradient(0deg, rgba(0,0,0,0.1) 50%, transparent 50%),
                linear-gradient(90deg, rgba(255,255,255,0.05), rgba(255,255,255,0.05));
            background-size: 4px 4px, 100% 100%;
        }}
        
        /* Headers */
        h1, h2, h3 {{
            font-family: 'Press Start 2P', monospace !important;
            color: {COLORS['text']};
            text-shadow: 3px 3px 0px #000000;
            border-bottom: 4px solid {COLORS['accent3']};
            padding-bottom: 15px;
            margin-bottom: 20px;
            letter-spacing: 2px;
        }}
        
        h1 {{
            font-size: 2.5em !important;
            text-align: center;
            margin-top: 20px;
            animation: pulse 2s infinite;
        }}
        
        h2 {{
            font-size: 1.8em !important;
            border-left: 5px solid {COLORS['accent1']};
            padding-left: 15px;
        }}
        
        h3 {{
            font-size: 1.3em !important;
        }}
        
        /* Text elements */
        p, li, .stMarkdown {{
            font-family: 'Space Mono', monospace !important;
            color: {COLORS['text']};
            text-shadow: 1px 1px 0px #000000;
        }}
        
        /* Widget styling */
        .stButton button {{
            font-family: 'Press Start 2P', monospace !important;
            background-color: {COLORS['accent3']};
            color: #000000;
            border: 4px solid #000000;
            border-radius: 0px !important;
            box-shadow: 5px 5px 0px #000000;
            padding: 10px 20px;
            transition: all 0.1s ease;
            font-size: 14px;
        }}
        
        .stButton button:hover {{
            background-color: {COLORS['accent2']};
            transform: translate(2px, 2px);
            box-shadow: 3px 3px 0px #000000;
        }}
        
        .stButton button:active {{
            transform: translate(5px, 5px);
            box-shadow: none;
        }}
        
        /* Selectbox and multiselect styling */
        .stSelectbox div[data-baseweb="select"] > div, 
        .stMultiSelect div[data-baseweb="select"] > div {{
            background-color: #1A1A40;
            border: 3px solid {COLORS['accent2']};
            border-radius: 0px !important;
            color: {COLORS['text']};
            font-family: 'Space Mono', monospace !important;
            box-shadow: 3px 3px 0px #000000;
        }}
        
        /* Checkbox styling */
        .stCheckbox label {{
            font-family: 'Space Mono', monospace !important;
        }}
        
        /* Make dataframes look pixelated */
        .dataframe {{
            font-family: 'Space Mono', monospace !important;
            border: 3px solid {COLORS['accent2']};
            border-radius: 0px !important;
            box-shadow: 5px 5px 0px #000000;
        }}
        
        .dataframe th {{
            background-color: {COLORS['accent3']};
            color: #000000;
            font-weight: bold;
            border: 2px solid #000000;
            text-align: center;
            font-family: 'Press Start 2P', cursive;
            font-size: 0.7em;
            padding: 10px;
        }}
        
        .dataframe td {{
            background-color: #1A1A40;
            border: 1px solid #333355;
            text-align: center;
        }}
        
        /* Sidebar styling */
        .css-1d391kg, .css-12oz5g7 {{
            background-color: #191933;
            border-right: 5px solid {COLORS['accent4']};
        }}
        
        /* Sidebar header */
        .sidebar .stHeader h1 {{
            font-size: 1.5em !important;
            text-align: center;
            border-bottom: 3px solid {COLORS['accent4']};
        }}
        
        /* Progress bar with pixelated look */
        .stProgress > div > div {{
            background-color: {COLORS['accent2']};
            border-radius: 0px !important;
            height: 20px;
        }}
        
        /* Container styling */
        .stAlert {{
            background-color: #1A1A40;
            border: 4px solid {COLORS['accent1']};
            border-radius: 0px !important;
            box-shadow: 5px 5px 0px #000000;
        }}
        
        /* Success message styling */
        .element-container .stAlert[data-baseweb="notification"] {{
            background-color: #1A1A40;
            border: 4px solid {COLORS['accent2']};
            border-radius: 0px !important;
            box-shadow: 5px 5px 0px #000000;
            font-family: 'Press Start 2P', monospace;
            font-size: 0.7em;
            animation: blink 1s 3;
        }}
        
        /* CRT Monitor Effect - Scanlines */
        .stApp::before {{
            content: "";
            display: block;
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: linear-gradient(
                rgba(10, 10, 30, 0),
                rgba(10, 10, 30, 0.1) 50%,
                rgba(10, 10, 30, 0) 50%,
                rgba(10, 10, 30, 0)
            );
            background-size: 100% 4px;
            pointer-events: none;
            z-index: 999;
            opacity: 0.3;
        }}
        
        /* Screen flicker effect */
        .stApp::after {{
            content: "";
            display: block;
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: rgba(255, 255, 255, 0.03);
            pointer-events: none;
            z-index: 999;
            animation: flicker 10s infinite;
        }}
        
        /* Custom divider */
        .retro-divider {{
            border: none;
            height: 4px;
            background: linear-gradient(to right, 
                transparent 0%, 
                {COLORS['accent3']} 10%, 
                {COLORS['accent3']} 90%, 
                transparent 100%);
            margin: 20px 0;
        }}
        
        /* Animations */
        @keyframes blink {{
            0%, 100% {{ opacity: 1; }}
            50% {{ opacity: 0.5; }}
        }}
        
        @keyframes pulse {{
            0%, 100% {{ transform: scale(1); }}
            50% {{ transform: scale(1.02); }}
        }}
        
        @keyframes flicker {{
            0%, 100% {{ opacity: 0; }}
            92% {{ opacity: 0; }}
            93% {{ opacity: 0.03; }}
            94% {{ opacity: 0; }}
            96% {{ opacity: 0; }}
            97% {{ opacity: 0.03; }}
            98% {{ opacity: 0; }}
        }}
    </style>
    """


def apply_retro_css():
    """
    Apply retro gaming CSS to Streamlit app.
    """
    import streamlit as st
    st.markdown(get_retro_css(), unsafe_allow_html=True)


def retro_divider():
    """
    Create a retro-themed divider.
    """
    import streamlit as st
    st.markdown('<hr class="retro-divider">', unsafe_allow_html=True)