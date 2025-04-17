"""
Sample data generator for Brut Impact Explorer.
Creates synthetic content engagement data and impact KPIs for demo purposes.
"""

import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import os

# Define constants
IMPACT_THEMES = [
    'Environment', 'Climate Action', 'Sustainable Living',
    'Social Justice', 'Equality', 'Diversity & Inclusion',
    'Community Impact', 'Mental Health', 'Workers Rights'
]

OUTPUT_DIR = os.path.join(os.path.dirname(__file__), 'sample_data')


def generate_content_data(num_posts=500, seed=42):
    """
    Generate synthetic content engagement data.
    
    Parameters:
    -----------
    num_posts : int
        Number of posts to generate
    seed : int
        Random seed for reproducibility
    
    Returns:
    --------
    pd.DataFrame
        DataFrame with synthetic content data
    """
    # Set random seed for reproducibility
    np.random.seed(seed)
    
    # Generate dates for the past 6 months
    end_date = datetime.now()
    start_date = end_date - timedelta(days=180)
    date_range = pd.date_range(start=start_date, end=end_date, freq='D')
    
    # Generate data
    data = []
    
    for theme in IMPACT_THEMES:
        # 15-30 posts per theme over 6 months
        num_theme_posts = np.random.randint(15, 30)
        post_dates = np.random.choice(date_range, size=num_theme_posts, replace=False)
        
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


def generate_impact_kpis():
    """
    Generate synthetic B Corp impact KPIs.
    
    Returns:
    --------
    dict
        Dictionary with impact KPI metrics
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


def save_sample_data():
    """
    Generate and save all sample data files.
    """
    # Create output directory if it doesn't exist
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    
    # Generate and save content data
    content_df = generate_content_data()
    content_df.to_csv(os.path.join(OUTPUT_DIR, 'brut_content_data.csv'), index=False)
    
    # Generate and save impact KPIs
    kpis_df = pd.DataFrame([generate_impact_kpis()])
    kpis_df.to_csv(os.path.join(OUTPUT_DIR, 'brut_impact_kpis.csv'), index=False)
    
    print(f"Generated {len(content_df)} content posts across {content_df['content_theme'].nunique()} themes.")
    print(f"Sample data saved to {OUTPUT_DIR}")


if __name__ == "__main__":
    save_sample_data()