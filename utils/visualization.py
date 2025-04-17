"""
Visualization utilities for Brut Impact Explorer.
"""

import plotly.graph_objects as go
import pandas as pd
from components.styles import COLORS


def create_theme_plot(df, theme, trends_df=None):
    """
    Create a retro-styled visualization for theme engagement and trends.
    
    Parameters:
    -----------
    df : pd.DataFrame
        DataFrame with content data
    theme : str
        Content theme to visualize
    trends_df : pd.DataFrame, optional
        DataFrame with trend data
    
    Returns:
    --------
    plotly.graph_objects.Figure
        Plotly figure with retro styling
    """
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