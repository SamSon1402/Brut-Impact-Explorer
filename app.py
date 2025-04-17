import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from datetime import datetime, timedelta

# Set page configuration
st.set_page_config(
    page_title="Brut Impact Explorer",
    page_icon="🎮",
    layout="wide",
    initial_sidebar_state="expanded"
)

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

# Apply enhanced retro gaming CSS
def apply_retro_css():
    st.markdown("""
    <style>
        /* Import retro fonts */
        @import url('https://fonts.googleapis.com/css2?family=VT323&family=Press+Start+2P&family=Space+Mono&display=swap');
        
        /* Main background and text */
        .stApp {
            background-color: """ + COLORS['background'] + """;
            color: """ + COLORS['text'] + """;
            background-image: 
                linear-gradient(0deg, rgba(0,0,0,0.1) 50%, transparent 50%),
                linear-gradient(90deg, rgba(255,255,255,0.05), rgba(255,255,255,0.05));
            background-size: 4px 4px, 100% 100%;
        }
        
        /* Headers */
        h1, h2, h3 {
            font-family: 'Press Start 2P', monospace !important;
            color: """ + COLORS['text'] + """;
            text-shadow: 3px 3px 0px #000000;
            border-bottom: 4px solid """ + COLORS['accent3'] + """;
            padding-bottom: 15px;
            margin-bottom: 20px;
            letter-spacing: 2px;
        }
        
        h1 {
            font-size: 2.5em !important;
            text-align: center;
            margin-top: 20px;
            animation: pulse 2s infinite;
        }
        
        h2 {
            font-size: 1.8em !important;
            border-left: 5px solid """ + COLORS['accent1'] + """;
            padding-left: 15px;
        }
        
        h3 {
            font-size: 1.3em !important;
        }
        
        /* Text elements */
        p, li, .stMarkdown {
            font-family: 'Space Mono', monospace !important;
            color: """ + COLORS['text'] + """;
            text-shadow: 1px 1px 0px #000000;
        }
        
        /* Widget styling */
        .stButton button {
            font-family: 'Press Start 2P', monospace !important;
            background-color: """ + COLORS['accent3'] + """;
            color: #000000;
            border: 4px solid #000000;
            border-radius: 0px !important;
            box-shadow: 5px 5px 0px #000000;
            padding: 10px 20px;
            transition: all 0.1s ease;
            font-size: 14px;
        }
        
        .stButton button:hover {
            background-color: """ + COLORS['accent2'] + """;
            transform: translate(2px, 2px);
            box-shadow: 3px 3px 0px #000000;
        }
        
        .stButton button:active {
            transform: translate(5px, 5px);
            box-shadow: none;
        }
        
        /* Selectbox and multiselect styling */
        .stSelectbox div[data-baseweb="select"] > div, 
        .stMultiSelect div[data-baseweb="select"] > div {
            background-color: #1A1A40;
            border: 3px solid """ + COLORS['accent2'] + """;
            border-radius: 0px !important;
            color: """ + COLORS['text'] + """;
            font-family: 'Space Mono', monospace !important;
            box-shadow: 3px 3px 0px #000000;
        }
        
        /* Checkbox styling */
        .stCheckbox label {
            font-family: 'Space Mono', monospace !important;
        }
        
        /* Make dataframes look pixelated */
        .dataframe {
            font-family: 'Space Mono', monospace !important;
            border: 3px solid """ + COLORS['accent2'] + """;
            border-radius: 0px !important;
            box-shadow: 5px 5px 0px #000000;
        }
        
        .dataframe th {
            background-color: """ + COLORS['accent3'] + """;
            color: #000000;
            font-weight: bold;
            border: 2px solid #000000;
            text-align: center;
            font-family: 'Press Start 2P', cursive;
            font-size: 0.7em;
            padding: 10px;
        }
        
        .dataframe td {
            background-color: #1A1A40;
            border: 1px solid #333355;
            text-align: center;
        }
        
        /* Sidebar styling */
        .css-1d391kg, .css-12oz5g7 {
            background-color: #191933;
            border-right: 5px solid """ + COLORS['accent4'] + """;
        }
        
        /* Sidebar header */
        .sidebar .stHeader h1 {
            font-size: 1.5em !important;
            text-align: center;
            border-bottom: 3px solid """ + COLORS['accent4'] + """;
        }
        
        /* Progress bar with pixelated look */
        .stProgress > div > div {
            background-color: """ + COLORS['accent2'] + """;
            border-radius: 0px !important;
            height: 20px;
        }
        
        /* Container styling */
        .stAlert {
            background-color: #1A1A40;
            border: 4px solid """ + COLORS['accent1'] + """;
            border-radius: 0px !important;
            box-shadow: 5px 5px 0px #000000;
        }
        
        /* Success message styling */
        .element-container .stAlert[data-baseweb="notification"] {
            background-color: #1A1A40;
            border: 4px solid """ + COLORS['accent2'] + """;
            border-radius: 0px !important;
            box-shadow: 5px 5px 0px #000000;
            font-family: 'Press Start 2P', monospace;
            font-size: 0.7em;
            animation: blink 1s 3;
        }
        
        /* CRT Monitor Effect - Scanlines */
        .stApp::before {
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
        }
        
        /* Screen flicker effect */
        .stApp::after {
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
        }
        
        /* Custom divider */
        .retro-divider {
            border: none;
            height: 4px;
            background: linear-gradient(to right, 
                transparent 0%, 
                """ + COLORS['accent3'] + """ 10%, 
                """ + COLORS['accent3'] + """ 90%, 
                transparent 100%);
            margin: 20px 0;
        }
        
        /* Animations */
        @keyframes blink {
            0%, 100% { opacity: 1; }
            50% { opacity: 0.5; }
        }
        
        @keyframes pulse {
            0%, 100% { transform: scale(1); }
            50% { transform: scale(1.02); }
        }
        
        @keyframes flicker {
            0%, 100% { opacity: 0; }
            92% { opacity: 0; }
            93% { opacity: 0.03; }
            94% { opacity: 0; }
            96% { opacity: 0; }
            97% { opacity: 0.03; }
            98% { opacity: 0; }
        }
    </style>
    """, unsafe_allow_html=True)

# Apply CSS
apply_retro_css()

# Custom header component
def arcade_header(text, level=1):
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

# Custom box component
def arcade_box(content, border_color=COLORS['accent2']):
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

# Custom metric display
def pixel_metric(label, value, color=COLORS['text'], max_value=100, animate=False):
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

# Generate sample data
def get_sample_data():
    # Set random seed for reproducibility
    np.random.seed(42)
    
    # Define content themes relevant to B Corp values
    impact_themes = [
        'Environment', 'Climate Action', 'Social Justice', 
        'Equality', 'Diversity & Inclusion', 'Mental Health'
    ]
    
    # Generate dates for the past 6 months
    end_date = datetime.now()
    start_date = end_date - timedelta(days=180)
    date_range = pd.date_range(start=start_date, end=end_date, freq='D')
    
    # Generate data for each theme
    data = []
    
    for theme in impact_themes:
        # Create posts for this theme (3-5 posts per month)
        num_posts = np.random.randint(18, 30)
        post_dates = np.random.choice(date_range, size=num_posts, replace=False)
        
        for date in post_dates:
            # Generate engagement metrics
            views = int(np.random.lognormal(10, 0.8))
            likes = int(views * np.random.beta(2, 10))
            comments = int(views * np.random.beta(1, 20))
            shares = int(views * np.random.beta(1, 15))
            
            # Calculate engagement rate
            engagement_rate = (likes + comments + shares) / max(views, 1) * 100
                
            data.append({
                'post_id': f'P{len(data) + 1000}',
                'timestamp': date,
                'content_theme': theme,
                'views': views,
                'likes': likes,
                'comments': comments,
                'shares': shares,
                'engagement_rate': engagement_rate
            })
    
    return pd.DataFrame(data)

# Generate simulated trend data
def get_simulated_trend_data(theme, dates):
    # Base interest value for each theme
    theme_base = {
        'Environment': 60,
        'Climate Action': 55,
        'Social Justice': 65,
        'Equality': 70, 
        'Diversity & Inclusion': 75,
        'Mental Health': 80
    }.get(theme, 50)
    
    # Generate trend data for each date
    trend_data = []
    for date in dates:
        # Add some random variation
        interest = theme_base + np.random.randint(-15, 15)
        # Ensure within range 0-100
        interest = max(0, min(100, interest))
        
        trend_data.append({
            'date': date,
            theme: interest
        })
    
    return pd.DataFrame(trend_data)

# Calculate theme metrics
def calculate_theme_metrics(df, theme):
    # Filter to the selected theme
    theme_data = df[df['content_theme'] == theme]
    
    # Calculate metrics
    metrics = {
        'total_posts': len(theme_data),
        'total_views': int(theme_data['views'].sum()),
        'total_engagement': int(theme_data['likes'].sum() + theme_data['comments'].sum() + theme_data['shares'].sum()),
        'avg_engagement_rate': float(theme_data['engagement_rate'].mean())
    }
    
    return metrics

# Create visualization
def create_theme_plot(df, theme, trends_df=None):
    # Filter to the selected theme
    theme_data = df[df['content_theme'] == theme].copy()
    
    # Convert timestamp to date for grouping
    theme_data['date'] = pd.to_datetime(theme_data['timestamp']).dt.date
    
    # Aggregate by date
    daily_data = theme_data.groupby('date').agg({
        'engagement_rate': 'mean'
    }).reset_index()
    
    # Sort by date
    daily_data = daily_data.sort_values('date')
    
    # Create figure with retro styling
    fig = go.Figure()
    
    # Add engagement rate line with pixel-like step interpolation
    fig.add_trace(go.Scatter(
        x=daily_data['date'], 
        y=daily_data['engagement_rate'],
        mode='lines+markers',
        name='Engagement Rate (%)',
        line=dict(
            color=COLORS['accent1'], 
            width=4,
            shape='hv'  # Step interpolation for a more pixelated look
        ),
        marker=dict(
            size=10,
            symbol='square',
            color=COLORS['accent1'],
            line=dict(width=2, color='#000000')
        )
    ))
    
    # Add trend data if available with pixel-like step interpolation
    if trends_df is not None:
        trends_df = trends_df.reset_index()
        trends_df['date'] = pd.to_datetime(trends_df['date']).dt.date
        
        fig.add_trace(go.Scatter(
            x=trends_df['date'],
            y=trends_df[theme],
            mode='lines+markers',
            name='Public Interest',
            line=dict(
                color=COLORS['accent3'], 
                width=4,
                shape='hv',  # Step interpolation for a more pixelated look
                dash='dot'
            ),
            marker=dict(
                size=8,
                symbol='diamond',
                color=COLORS['accent3'],
                line=dict(width=2, color='#000000')
            ),
            yaxis="y2"
        ))
    
    # Update layout with retro gaming aesthetic
    fig.update_layout(
        title={
            'text': f"{theme} ENGAGEMENT vs PUBLIC INTEREST",
            'font': {
                'family': 'Press Start 2P',
                'size': 20,
                'color': COLORS['text']
            },
            'y': 0.95
        },
        plot_bgcolor='#1A1A40',
        paper_bgcolor=COLORS['background'],
        font=dict(
            family="Space Mono",
            size=14,
            color=COLORS['text']
        ),
        xaxis=dict(
            title="DATE",
            titlefont=dict(
                family="Press Start 2P",
                size=14
            ),
            showgrid=True,
            gridcolor='#333355',
            gridwidth=2,
            zeroline=False
        ),
        yaxis=dict(
            title="ENGAGEMENT RATE (%)",
            titlefont=dict(
                family="Press Start 2P",
                size=14
            ),
            showgrid=True,
            gridcolor='#333355',
            gridwidth=2,
            zeroline=False
        ),
        yaxis2=dict(
            title="PUBLIC INTEREST",
            titlefont=dict(
                family="Press Start 2P",
                size=14
            ),
            overlaying="y",
            side="right",
            showgrid=False,
            range=[0, 100],
            zeroline=False
        ),
        legend=dict(
            font=dict(
                family="Press Start 2P",
                size=12,
                color=COLORS['text']
            ),
            bgcolor='rgba(26, 26, 64, 0.7)',
            bordercolor=COLORS['accent2'],
            borderwidth=2
        ),
        margin=dict(t=100)
    )
    
    # Add grid lines for a more retro feel
    fig.update_xaxes(
        showline=True, 
        linewidth=2, 
        linecolor='#333355',
        mirror=True
    )
    fig.update_yaxes(
        showline=True, 
        linewidth=2, 
        linecolor='#333355',
        mirror=True
    )
    
    return fig

# Create a retro-themed divider
def retro_divider():
    st.markdown('<hr class="retro-divider">', unsafe_allow_html=True)

# Get impact KPIs
def get_brut_impact_kpis():
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

# Main application
def main():
    # Title with arcade style
    st.markdown("""
    <div style="text-align: center; margin-bottom: 30px;">
        <div style="
            font-family: 'Press Start 2P', monospace; 
            font-size: 40px; 
            color: """ + COLORS['text'] + """; 
            text-shadow: 4px 4px 0px #000000;
            letter-spacing: 3px;
            animation: pulse 2s infinite;
        ">
            BRUT IMPACT EXPLORER
        </div>
        <div style="
            font-family: 'VT323', monospace; 
            font-size: 24px; 
            color: """ + COLORS['accent3'] + """;
            margin-top: 10px;
            text-shadow: 2px 2px 0px #000000;
        ">
            &lt;&lt; B CORP THEME ANALYSIS &gt;&gt;
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Game-themed sidebar
    with st.sidebar:
        st.markdown("""
        <div style="text-align: center; margin-bottom: 20px;">
            <div style="
                font-family: 'Press Start 2P', monospace; 
                font-size: 20px; 
                color: """ + COLORS['accent3'] + """;
                text-shadow: 2px 2px 0px #000000;
                margin-bottom: 15px;
            ">
                GAME CONTROLS
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # Add animated button for demo data
        if st.button("▶ START GAME", help="Load demo data and begin analysis"):
            # Generate sample data
            df = get_sample_data()
            st.session_state['data'] = df
            
            # Custom success message
            st.markdown("""
            <div style="
                background-color: rgba(26, 26, 64, 0.7);
                border: 4px solid """ + COLORS['accent2'] + """;
                border-radius: 0px;
                padding: 15px;
                margin: 15px 0;
                box-shadow: 5px 5px 0px #000000;
                font-family: 'Press Start 2P', monospace;
                font-size: 0.8em;
                color: """ + COLORS['accent2'] + """;
                text-align: center;
                animation: blink 0.5s 3;
            ">
                GAME DATA LOADED!
                <br><br>
                """ + str(len(get_sample_data())) + """ POSTS
                <br>
                6 IMPACT THEMES
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown("<hr style='border-color: " + COLORS['accent4'] + "; margin: 20px 0;'>", unsafe_allow_html=True)
        
        # Game instructions
        st.markdown("""
        <div style="
            font-family: 'Press Start 2P', monospace; 
            font-size: 16px; 
            color: """ + COLORS['accent1'] + """;
            margin-bottom: 10px;
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
        
        for i, instruction in enumerate(instructions):
            st.markdown(f"""
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
        
        st.markdown("<hr style='border-color: " + COLORS['accent4'] + "; margin: 20px 0;'>", unsafe_allow_html=True)
        
        # Credits section
        st.markdown("""
        <div style="text-align: center; margin-top: 30px;">
            <div style="
                font-family: 'Press Start 2P', monospace; 
                font-size: 12px; 
                color: """ + COLORS['accent3'] + """;
                margin-bottom: 5px;
            ">
                BRUT IMPACT EXPLORER v1.0
            </div>
            <div style="
                font-family: 'VT323', monospace; 
                font-size: 16px; 
                color: """ + COLORS['text'] + """;
            ">
                © 2025 BRUT MEDIA
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    # Main game content
    if 'data' in st.session_state:
        df = st.session_state['data']
        
        # Theme selection section
        arcade_header("SELECT YOUR IMPACT THEME", 2)
        
        # Get unique themes
        themes = sorted(df['content_theme'].unique())
        
        # Create columns for better layout
        col1, col2 = st.columns([2, 1])
        
        with col1:
            # Theme selection with game-style select box
            selected_theme = st.selectbox(
                "CHOOSE A THEME", 
                themes,
                help="Select a content theme to analyze"
            )
        
        with col2:
            # Show trend data option with custom checkbox
            show_trends = st.checkbox(
                "SHOW PUBLIC INTEREST TRENDS", 
                value=True,
                help="Include simulated public interest data in the analysis"
            )
        
        # Analyze button with game styling
        if st.button("🎮 ANALYZE THEME", help="Run the analysis for the selected theme"):
            # Display loading animation
            with st.spinner("LOADING GAME DATA..."):
                # Calculate metrics
                metrics = calculate_theme_metrics(df, selected_theme)
                
                # Generate trend data if needed
                trend_data = None
                if show_trends:
                    # Get unique dates from the data
                    unique_dates = sorted(df['timestamp'].dt.date.unique())
                    # Generate trend data
                    trend_data = get_simulated_trend_data(selected_theme, unique_dates)
                
                # Arcade-style header
                arcade_header(f"{selected_theme.upper()} STATS", 2)
                
                # Create metric columns with game-style display
                m1, m2, m3, m4 = st.columns(4)
                
                with m1:
                    pixel_metric("POSTS", metrics['total_posts'], COLORS['accent2'], 100, animate=True)
                
                with m2:
                    pixel_metric("VIEWS", f"{metrics['total_views']:,}", COLORS['accent1'], 1000000)
                
                with m3:
                    pixel_metric("ENGAGEMENT", f"{metrics['total_engagement']:,}", COLORS['accent3'], 100000)
                
                with m4:
                    pixel_metric("ENG. RATE", f"{metrics['avg_engagement_rate']:.2f}%", COLORS['accent4'], 20)
                
                # Retro divider
                retro_divider()
                
                # Create and display visualization with arcade style
                arcade_header("ENGAGEMENT ANALYSIS", 2)
                
                fig = create_theme_plot(df, selected_theme, trend_data)
                st.plotly_chart(fig, use_container_width=True)
                
                # Retro divider
                retro_divider()
                
                # Show recent posts with game styling
                arcade_header("RECENT CONTENT", 2)
                
                recent_posts = df[df['content_theme'] == selected_theme].sort_values('timestamp', ascending=False).head(5)
                
                # Format for display with arcade style
                if not recent_posts.empty:
                    display_posts = recent_posts.copy()
                    display_posts['timestamp'] = display_posts['timestamp'].dt.strftime('%Y-%m-%d')
                    display_posts = display_posts[['timestamp', 'views', 'likes', 'comments', 'shares', 'engagement_rate']]
                    
                    # Add column headers with more readable names
                    display_posts.columns = ['DATE', 'VIEWS', 'LIKES', 'COMMENTS', 'SHARES', 'ENG. RATE (%)']
                    
                    # Format engagement rate
                    display_posts['ENG. RATE (%)'] = display_posts['ENG. RATE (%)'].apply(lambda x: f"{x:.2f}%")
                    
                    st.dataframe(display_posts, use_container_width=True)
                
                # Retro divider
                retro_divider()
                
                # BRUT Impact KPIs section
                arcade_header("IMPACT SCOREBOARD", 2)
                
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
                
                # Victory message with arcade style
                arcade_box("""
                <div style="text-align: center;">
                    <div style="
                        font-family: 'Press Start 2P', monospace; 
                        font-size: 24px; 
                        color: """ + COLORS['accent3'] + """;
                        margin-bottom: 15px;
                        animation: pulse 2s infinite;
                    ">
                        ANALYSIS COMPLETE!
                    </div>
                    <div style="
                        font-family: 'VT323', monospace; 
                        font-size: 20px; 
                        color: """ + COLORS['text'] + """;
                    ">
                        Select another theme to continue exploring
                    </div>
                </div>
                """, COLORS['accent3'])
    
    else:
        # Initial welcome screen with arcade game style
        arcade_box("""
        <div style="text-align: center;">
            <div style="
                font-family: 'Press Start 2P', monospace; 
                font-size: 28px; 
                color: """ + COLORS['accent3'] + """;
                margin-bottom: 20px;
            ">
                WELCOME PLAYER ONE
            </div>
            <div style="
                font-family: 'VT323', monospace; 
                font-size: 24px; 
                color: """ + COLORS['text'] + """;
                margin-bottom: 30px;
            ">
                Explore Brut's B Corp impact themes through this interactive dashboard
            </div>
            <div style="
                font-family: 'Press Start 2P', monospace; 
                font-size: 20px; 
                color: """ + COLORS['accent1'] + """;
                animation: blink 1s infinite;
                margin-top: 30px;
            ">
                PRESS "START GAME" TO BEGIN
            </div>
        </div>
        """, COLORS['accent2'])
        
        # Game preview image (stylized text)
        st.markdown("""
        <div style="
            text-align: center;
            margin: 50px 0;
            padding: 30px;
            background-color: rgba(26, 26, 64, 0.7);
            border: 4px solid """ + COLORS['accent4'] + """;
        ">
            <div style="
                font-family: 'Press Start 2P', monospace; 
                font-size: 18px; 
                color: """ + COLORS['accent3'] + """;
                margin-bottom: 20px;
            ">
                GAME PREVIEW
            </div>
            <div style="
                font-family: 'VT323', monospace;
                font-size: 100px;
                line-height: 1;
                color: """ + COLORS['text'] + """;
                text-shadow: 4px 4px 0px #000000;
                margin: 20px 0;
                animation: pulse 2s infinite;
            ">
                BRUT IMPACT
            </div>
            <div style="
                font-family: 'Press Start 2P', monospace; 
                font-size: 16px; 
                color: """ + COLORS['accent1'] + """;
                animation: blink 1s infinite;
            ">
                INSERT COIN TO CONTINUE
            </div>
        </div>
        """, unsafe_allow_html=True)

# Run the app
if __name__ == "__main__":
    main()