"""
Custom UI elements with retro gaming aesthetic.
"""

import streamlit as st
from .styles import COLORS


def arcade_header(text, level=1):
    """
    Create a retro arcade-style header.
    
    Parameters:
    -----------
    text : str
        The header text
    level : int
        Header level (1, 2, or 3)
    """
    font_size = "2.5em" if level == 1 else "1.8em" if level == 2 else "1.5em"
    color = COLORS['text'] if level == 1 else COLORS['accent3'] if level == 2 else COLORS['accent2']
    
    st.markdown(f"""
    <div style="
        font-family: 'Press Start 2P', monospace;
        font-size: {font_size};
        color: {color};
        text-shadow: 3px 3px 0px #000000;
        text-align: center;
        padding: 15px 0;
        margin: 20px 0;
        border-bottom: 4px solid {COLORS['accent3']};
        border-top: 4px solid {COLORS['accent3']};
        background-color: rgba(26, 26, 64, 0.7);
        letter-spacing: 2px;
    ">
        {text}
    </div>
    """, unsafe_allow_html=True)


def arcade_box(content, border_color=COLORS['accent2']):
    """
    Create a retro arcade-style box with custom content.
    
    Parameters:
    -----------
    content : str
        HTML content to display inside the box
    border_color : str
        Color for box border (hex code)
    """
    st.markdown(f"""
    <div style="
        background-color: rgba(26, 26, 64, 0.7);
        border: 4px solid {border_color};
        border-radius: 0px;
        padding: 20px;
        margin: 15px 0;
        box-shadow: 5px 5px 0px #000000;
        font-family: 'Space Mono', monospace;
        color: {COLORS['text']};
        text-shadow: 1px 1px 0px #000000;
    ">
        {content}
    </div>
    """, unsafe_allow_html=True)


def welcome_screen():
    """
    Display the initial welcome screen with retro gaming style.
    """
    arcade_box(f"""
    <div style="text-align: center;">
        <div style="
            font-family: 'Press Start 2P', monospace; 
            font-size: 28px; 
            color: {COLORS['accent3']};
            margin-bottom: 20px;
        ">
            WELCOME PLAYER ONE
        </div>
        <div style="
            font-family: 'VT323', monospace; 
            font-size: 24px; 
            color: {COLORS['text']};
            margin-bottom: 30px;
        ">
            Explore Brut's B Corp impact themes through this interactive dashboard
        </div>
        <div style="
            font-family: 'Press Start 2P', monospace; 
            font-size: 20px; 
            color: {COLORS['accent1']};
            animation: blink 1s infinite;
            margin-top: 30px;
        ">
            PRESS "START GAME" TO BEGIN
        </div>
    </div>
    """, COLORS['accent2'])


def game_sidebar():
    """
    Create the game controls sidebar with retro styling.
    """
    st.sidebar.markdown(f"""
    <div style="text-align: center; margin-bottom: 20px;">
        <div style="
            font-family: 'Press Start 2P', monospace; 
            font-size: 20px; 
            color: {COLORS['accent3']};
            text-shadow: 2px 2px 0px #000000;
            margin-bottom: 15px;
        ">
            GAME CONTROLS
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Game instructions
    st.sidebar.markdown(f"""
    <div style="
        font-family: 'Press Start 2P', monospace; 
        font-size: 16px; 
        color: {COLORS['accent1']};
        margin: 20px 0 10px 0;
    ">
        HOW TO PLAY:
    </div>
    """, unsafe_allow_html=True)
    
    # Instruction steps
    instructions = [
        "1. PRESS START GAME",
        "2. SELECT A THEME",
        "3. PRESS ANALYZE BUTTON",
        "4. EXPLORE IMPACT DATA"
    ]
    
    for instruction in instructions:
        st.sidebar.markdown(f"""
        <div style="
            font-family: 'VT323', monospace; 
            font-size: 20px; 
            color: {COLORS['text']};
            margin: 8px 0;
            text-shadow: 1px 1px 0px #000000;
        ">
            {instruction}
        </div>
        """, unsafe_allow_html=True)
    
    st.sidebar.markdown(f"<hr style='border-color: {COLORS['accent4']}; margin: 20px 0;'>", unsafe_allow_html=True)
    
    # Credits
    st.sidebar.markdown(f"""
    <div style="text-align: center; margin-top: 30px;">
        <div style="
            font-family: 'Press Start 2P', monospace; 
            font-size: 12px; 
            color: {COLORS['accent3']};
            margin-bottom: 5px;
        ">
            BRUT IMPACT EXPLORER v1.0
        </div>
        <div style="
            font-family: 'VT323', monospace; 
            font-size: 16px; 
            color: {COLORS['text']};
        ">
            © 2025 BRUT MEDIA
        </div>
    </div>
    """, unsafe_allow_html=True)