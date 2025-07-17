"""
🎬 My OTT Analytics Project - Let's Explore the Streaming World!

This is my main script that brings everything together - the data pipeline, 
analysis, and insights generation. I'm excited to see what we discover
about Netflix, Hulu, and the streaming industry!
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from src.etl_pipeline import ETLPipeline
from src.data_analyzer import DataAnalyzer
import logging

# Setting up logging to track our progress
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('ott_analytics.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

def main():
    """Let's run the complete OTT analytics pipeline and see what we discover!"""
    print("="*60)
    print("     🎬 MY OTT ANALYTICS ADVENTURE - LET'S BEGIN!")
    print("="*60)
    
    try:
        # Time to fire up the data pipeline!
        logger.info("Starting my OTT analytics journey...")
        data_path = "OTT Dataset"
        pipeline = ETLPipeline(data_path)
        
        # Running the ETL magic
        print("\\n🚀 Step 1: Running My Data Pipeline...")
        print("-" * 40)
        print("This is where I process all the Netflix, Hulu, and other platform data!")
        success = pipeline.run_pipeline()
        
        if not success:
            logger.error("Oh no! The pipeline hit a snag. Let me check what went wrong...")
            return False
        
        # Let me see what data we've got to work with
        print("\\n📊 Step 2: Here's What I've Collected:")
        print("-" * 40)
        summary = pipeline.get_data_summary()
        print("Wow! Look at all this streaming data:")
        for table, info in summary.items():
            emoji = "📈" if "revenue" in table else "👥" if "subscriber" in table else "📚"
            print(f"{emoji} {table}: {info['rows']} records, {info['columns']} data points")
        
        # Time for the fun part - analysis and insights!
        print("\\n🧠 Step 3: Generating Insights (This is the exciting part!)...")
        print("-" * 40)
        print("Let me analyze all this data and see what stories it tells...")
        analyzer = DataAnalyzer()
        insights_report = analyzer.generate_insights_report()
        print(insights_report)
        
        # Saving the insights for later
        with open('ott_analytics_insights.txt', 'w') as f:
            f.write(insights_report)
        print("\\n💾 Insights saved! Check out 'ott_analytics_insights.txt' for all the details")
        
        # What's next?
        print("\\n🎯 Step 4: What You Can Do Next:")
        print("-" * 50)
        print("Now that we have all this great data, here are your options:")
        print("1. 📊 Open the Jupyter notebook to explore interactive visualizations")
        print("2. 🔗 Connect Power BI to the MySQL database for dashboards")
        print("3. 📈 Use the data for your own analysis and insights")
        print("4. 🚀 Share your findings with the world!")
        print("\\nDatabase connection: localhost:3306/ott_analytics")
        print("All the tables are ready and waiting for you!")
        
        print("\\n" + "="*60)
        print("     ✨ SUCCESS! Your OTT Analytics Project is Complete! ✨")
        print("     🎉 Time to explore and discover amazing insights! 🎉")
        print("="*60)
        
        return True
        
    except Exception as e:
        logger.error(f"Oops! Something unexpected happened: {e}")
        print(f"\\n❌ Error: {e}")
        print("Don't worry - check the logs and we can figure this out together!")
        return False

if __name__ == "__main__":
    success = main()
    if not success:
        sys.exit(1)
