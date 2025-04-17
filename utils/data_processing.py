"""
Data processing utilities for Brut Impact Explorer.
"""

import pandas as pd
import numpy as np
from datetime import datetime, timedelta


def calculate_theme_metrics(df, theme):
    """
    Calculate performance metrics for a specific content theme.
    
    Parameters:
    -----------
    df : pd.DataFrame
        DataFrame with content engagement data
    theme : str
        Content theme to analyze
    
    Returns:
    --------
    dict
        Dictionary with calculated metrics
    """
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


def get_simulated_trend_data(theme, dates):
    """
    Generate simulated public interest trend data for a theme.
    
    Parameters:
    -----------
    theme : str
        Content theme to generate trend data for
    dates : list
        List of dates to generate data for
    
    Returns:
    --------
    pd.DataFrame
        DataFrame with trend data
    """
    # Set random seed for reproducibility
    np.random.seed(42)
    
    # Base interest value for each theme
    theme_base = {
        'Environment': 60,
        'Climate Action': 55,
        'Social Justice': 65,
        'Equality': 70, 
        'Diversity & Inclusion': 75,
        'Mental Health': 80,
        'Community Impact': 45,
        'Workers Rights': 50,
        'Sustainable Living': 65
    }.get(theme, 50)
    
    # Add seasonal factors based on theme
    def get_seasonal_factor(date, theme):
        # Default factor
        factor = 1.0
        
        # Environment themes peak around Earth Day and summer
        if theme in ['Environment', 'Climate Action', 'Sustainable Living']:
            if date.month == 4:  # Earth Day month
                factor = 1.5
            elif date.month in [6, 7, 8]:  # Summer
                factor = 1.3
        
        # Social justice themes have different peak times
        if theme in ['Social Justice', 'Equality', 'Diversity & Inclusion']:
            if date.month == 2:  # Black History Month
                factor = 1.6
            elif date.month == 6:  # Pride Month
                factor = 1.7
        
        # Add some weekly cycle (weekend peaks)
        if date.weekday() >= 5:  # Weekend
            factor *= 1.1
            
        return factor
    
    # Generate trend data for each date
    trend_data = []
    for date in dates:
        # Get seasonal factor
        seasonal_factor = get_seasonal_factor(date, theme)
        
        # Add some random variation
        random_factor = np.random.uniform(0.85, 1.15)
        
        # Calculate interest value
        interest = int(theme_base * seasonal_factor * random_factor)
        
        # Ensure within range 0-100
        interest = max(0, min(100, interest))
        
        trend_data.append({
            'date': date,
            theme: interest
        })
    
    return pd.DataFrame(trend_data)


def format_recent_posts(df, theme, n=5):
    """
    Format recent posts for a theme for display.
    
    Parameters:
    -----------
    df : pd.DataFrame
        DataFrame with content data
    theme : str
        Content theme to filter by
    n : int
        Number of posts to return
    
    Returns:
    --------
    pd.DataFrame
        Formatted DataFrame with recent posts
    """
    # Filter to the selected theme
    theme_data = df[df['content_theme'] == theme].sort_values('timestamp', ascending=False).head(n)
    
    if not theme_data.empty:
        # Format for display
        display_posts = theme_data.copy()
        display_posts['timestamp'] = display_posts['timestamp'].dt.strftime('%Y-%m-%d')
        
        # Select columns for display
        display_cols = ['timestamp', 'views', 'likes', 'comments', 'shares', 'engagement_rate']
        if 'post_id' in display_posts.columns:
            display_cols.insert(0, 'post_id')
        
        # Format column names
        display_posts = display_posts[display_cols]
        display_posts.columns = ['ID', 'DATE', 'VIEWS', 'LIKES', 'COMMENTS', 'SHARES', 'ENG. RATE (%)'] if 'post_id' in display_cols else ['DATE', 'VIEWS', 'LIKES', 'COMMENTS', 'SHARES', 'ENG. RATE (%)']
        
        # Format engagement rate
        display_posts['ENG. RATE (%)'] = display_posts['ENG. RATE (%)'].apply(lambda x: f"{x:.2f}%")
        
        return display_posts
    
    return pd.DataFrame()