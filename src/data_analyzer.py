import pandas as pd
import numpy as np
from sqlalchemy import create_engine, text
import logging
from typing import Dict, List
from config.config import Config

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class DataAnalyzer:
    """Advanced data analysis for OTT platforms"""
    
    def __init__(self):
        self.config = Config()
        self.engine = create_engine(self.config.DATABASE_URL)
        
    def get_revenue_analysis(self) -> Dict:
        """Analyze revenue trends across platforms"""
        try:
            # Netflix revenue analysis
            netflix_query = """
            SELECT Year, Revenue, 
                   LAG(Revenue) OVER (ORDER BY Year) as prev_revenue,
                   ((Revenue - LAG(Revenue) OVER (ORDER BY Year)) / 
                    LAG(Revenue) OVER (ORDER BY Year)) * 100 as growth_rate
            FROM netflix_revenue 
            ORDER BY Year
            """
            
            netflix_df = pd.read_sql(netflix_query, self.engine)
            
            # Hulu revenue analysis
            hulu_query = """
            SELECT Year, Revenue,
                   LAG(Revenue) OVER (ORDER BY Year) as prev_revenue,
                   ((Revenue - LAG(Revenue) OVER (ORDER BY Year)) / 
                    LAG(Revenue) OVER (ORDER BY Year)) * 100 as growth_rate
            FROM hulu_revenue 
            ORDER BY Year
            """
            
            hulu_df = pd.read_sql(hulu_query, self.engine)
            
            analysis = {
                'netflix': {
                    'total_revenue': netflix_df['Revenue'].sum(),
                    'avg_growth_rate': netflix_df['growth_rate'].mean(),
                    'max_revenue_year': netflix_df.loc[netflix_df['Revenue'].idxmax(), 'Year'],
                    'data': netflix_df.to_dict('records')
                },
                'hulu': {
                    'total_revenue': hulu_df['Revenue'].sum(),
                    'avg_growth_rate': hulu_df['growth_rate'].mean(),
                    'max_revenue_year': hulu_df.loc[hulu_df['Revenue'].idxmax(), 'Year'],
                    'data': hulu_df.to_dict('records')
                }
            }
            
            logger.info("Revenue analysis completed")
            return analysis
            
        except Exception as e:
            logger.error(f"Error in revenue analysis: {e}")
            return {}
    
    def get_subscriber_analysis(self) -> Dict:
        """Analyze subscriber trends"""
        try:
            # Netflix subscriber analysis
            netflix_query = """
            SELECT Year, Subscribers,
                   LAG(Subscribers) OVER (ORDER BY Year) as prev_subscribers,
                   (Subscribers - LAG(Subscribers) OVER (ORDER BY Year)) as subscriber_growth
            FROM netflix_numsubscribers 
            ORDER BY Year
            """
            
            netflix_df = pd.read_sql(netflix_query, self.engine)
            
            analysis = {
                'netflix': {
                    'total_subscribers_latest': netflix_df['Subscribers'].iloc[-1],
                    'total_growth': netflix_df['Subscribers'].iloc[-1] - netflix_df['Subscribers'].iloc[0],
                    'avg_annual_growth': netflix_df['subscriber_growth'].mean(),
                    'data': netflix_df.to_dict('records')
                }
            }
            
            logger.info("Subscriber analysis completed")
            return analysis
            
        except Exception as e:
            logger.error(f"Error in subscriber analysis: {e}")
            return {}
    
    def get_content_library_analysis(self) -> Dict:
        """Analyze content library across platforms"""
        try:
            query = """
            SELECT 
                `Streaming platform` as platform,
                Movies,
                `TV Shows` as tv_shows,
                Total_Content,
                Content_Ratio,
                CASE 
                    WHEN Content_Ratio > 2 THEN 'Movie-Heavy'
                    WHEN Content_Ratio < 0.5 THEN 'TV-Heavy'
                    ELSE 'Balanced'
                END as content_strategy
            FROM library_size
            ORDER BY Total_Content DESC
            """
            
            df = pd.read_sql(query, self.engine)
            
            analysis = {
                'total_platforms': len(df),
                'largest_library': df.iloc[0]['platform'],
                'largest_library_size': df.iloc[0]['Total_Content'],
                'content_strategies': df['content_strategy'].value_counts().to_dict(),
                'data': df.to_dict('records')
            }
            
            logger.info("Content library analysis completed")
            return analysis
            
        except Exception as e:
            logger.error(f"Error in content library analysis: {e}")
            return {}
    
    def get_market_share_analysis(self) -> Dict:
        """Analyze market share based on different metrics"""
        try:
            # Get latest subscriber data for major platforms
            platforms_data = {}
            
            # Netflix
            netflix_query = "SELECT Subscribers FROM netflix_numsubscribers ORDER BY Year DESC LIMIT 1"
            netflix_subs = pd.read_sql(netflix_query, self.engine)['Subscribers'].iloc[0]
            platforms_data['Netflix'] = netflix_subs
            
            # Hulu
            hulu_query = "SELECT Subscribers FROM hulu_numsubscribers ORDER BY Year DESC LIMIT 1"
            hulu_subs = pd.read_sql(hulu_query, self.engine)['Subscribers'].iloc[0]
            platforms_data['Hulu'] = hulu_subs
            
            total_subscribers = sum(platforms_data.values())
            
            market_share = {
                platform: (subs / total_subscribers) * 100 
                for platform, subs in platforms_data.items()
            }
            
            analysis = {
                'total_market_size': total_subscribers,
                'market_share_percentage': market_share,
                'market_leader': max(market_share, key=market_share.get),
                'subscriber_data': platforms_data
            }
            
            logger.info("Market share analysis completed")
            return analysis
            
        except Exception as e:
            logger.error(f"Error in market share analysis: {e}")
            return {}
    
    def generate_insights_report(self) -> str:
        """Generate comprehensive insights report"""
        try:
            # Get all analyses
            revenue_analysis = self.get_revenue_analysis()
            subscriber_analysis = self.get_subscriber_analysis()
            content_analysis = self.get_content_library_analysis()
            market_analysis = self.get_market_share_analysis()
            
            # Generate report
            report = f"""
            
OTT ANALYTICS INSIGHTS REPORT
{'='*50}

1. REVENUE INSIGHTS:
-------------------
Netflix Total Revenue: ${revenue_analysis.get('netflix', {}).get('total_revenue', 0):.1f}B
Netflix Avg Growth Rate: {revenue_analysis.get('netflix', {}).get('avg_growth_rate', 0):.1f}% per year
Hulu Total Revenue: ${revenue_analysis.get('hulu', {}).get('total_revenue', 0):.1f}B
Hulu Avg Growth Rate: {revenue_analysis.get('hulu', {}).get('avg_growth_rate', 0):.1f}% per year

2. SUBSCRIBER INSIGHTS:
----------------------
Netflix Latest Subscribers: {subscriber_analysis.get('netflix', {}).get('total_subscribers_latest', 0):.1f}M
Netflix Total Growth: {subscriber_analysis.get('netflix', {}).get('total_growth', 0):.1f}M subscribers
Netflix Avg Annual Growth: {subscriber_analysis.get('netflix', {}).get('avg_annual_growth', 0):.1f}M per year

3. CONTENT LIBRARY INSIGHTS:
----------------------------
Total Platforms Analyzed: {content_analysis.get('total_platforms', 0)}
Largest Content Library: {content_analysis.get('largest_library', 'N/A')}
Largest Library Size: {content_analysis.get('largest_library_size', 0):,} titles

Content Strategies:
{chr(10).join([f"  - {strategy}: {count} platforms" for strategy, count in content_analysis.get('content_strategies', {}).items()])}

4. MARKET SHARE INSIGHTS:
------------------------
Total Market Size: {market_analysis.get('total_market_size', 0):.1f}M subscribers
Market Leader: {market_analysis.get('market_leader', 'N/A')}

Market Share Distribution:
{chr(10).join([f"  - {platform}: {share:.1f}%" for platform, share in market_analysis.get('market_share_percentage', {}).items()])}

5. KEY RECOMMENDATIONS:
----------------------
- Netflix shows strong revenue growth with consistent subscriber acquisition
- Content strategy varies significantly across platforms
- Market is dominated by a few key players
- Investment in content diversity could be a differentiator
- Revenue growth rates indicate healthy market expansion

{'='*50}
Report Generated Successfully
{'='*50}
            """
            
            logger.info("Insights report generated successfully")
            return report
            
        except Exception as e:
            logger.error(f"Error generating insights report: {e}")
            return "Error generating insights report"

if __name__ == "__main__":
    analyzer = DataAnalyzer()
    report = analyzer.generate_insights_report()
    print(report)
