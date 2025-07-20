"""
Data Preview Script - Preview OTT Analytics Data Processing
This script processes the data and shows what would be loaded into the database
"""

import pandas as pd
import numpy as np
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from src.etl_pipeline import DataProcessor

def preview_data_processing():
    """Preview the data processing without database connection"""
    print("="*60)
    print("     OTT ANALYTICS - DATA PREVIEW")
    print("="*60)
    
    # Initialize data processor
    data_path = "OTT Dataset"
    processor = DataProcessor(data_path)
    
    print(f"\\n📁 Processing data from: {data_path}")
    print("-" * 40)
    
    # Process all data
    try:
        processed_data = processor.process_all_data()
        
        if not processed_data:
            print("❌ No data found. Please check the data path.")
            return
        
        print(f"\\n✅ Successfully processed {len(processed_data)} datasets")
        print("\\n📊 Data Summary:")
        print("-" * 40)
        
        total_rows = 0
        for table_name, df in processed_data.items():
            if not df.empty:
                rows = len(df)
                cols = len(df.columns)
                total_rows += rows
                print(f"• {table_name}: {rows:,} rows, {cols} columns")
                
                # Show sample data for key tables
                if table_name in ['library_size', 'netflix_revenue', 'netflix_numsubscribers']:
                    print(f"  Sample data:")
                    print(f"  {df.head(3).to_string(index=False)}")
                    print()
        
        print(f"\\n📈 Total Records: {total_rows:,}")
        
        # Key insights from the data
        print("\\n🔍 Key Data Insights:")
        print("-" * 40)
        
        # Library size analysis
        if 'library_size' in processed_data and not processed_data['library_size'].empty:
            lib_df = processed_data['library_size']
            total_platforms = len(lib_df)
            largest_library = lib_df.loc[lib_df['Total_Content'].idxmax()]
            print(f"• {total_platforms} streaming platforms analyzed")
            print(f"• Largest content library: {largest_library['Streaming platform']} ({largest_library['Total_Content']:,} titles)")
            print(f"• Total content across all platforms: {lib_df['Total_Content'].sum():,} titles")
        
        # Netflix revenue analysis
        if 'netflix_revenue' in processed_data and not processed_data['netflix_revenue'].empty:
            netflix_df = processed_data['netflix_revenue']
            revenue_growth = ((netflix_df['Revenue'].iloc[-1] - netflix_df['Revenue'].iloc[0]) / netflix_df['Revenue'].iloc[0]) * 100
            print(f"• Netflix revenue growth: {revenue_growth:.1f}% over {len(netflix_df)} years")
            print(f"• Netflix latest revenue: ${netflix_df['Revenue'].iloc[-1]:.1f}B")
        
        # Subscriber analysis
        if 'netflix_numsubscribers' in processed_data and not processed_data['netflix_numsubscribers'].empty:
            subs_df = processed_data['netflix_numsubscribers']
            subscriber_growth = subs_df['Subscribers'].iloc[-1] - subs_df['Subscribers'].iloc[0]
            print(f"• Netflix subscriber growth: {subscriber_growth:.1f}M subscribers")
            print(f"• Netflix current subscribers: {subs_df['Subscribers'].iloc[-1]:.1f}M")
        
        print("\\n🎯 Next Steps:")
        print("-" * 40)
        print("1. Set up MySQL database:")
        print("   - Install MySQL Server")
        print("   - Create database 'ott_analytics'")
        print("   - Update credentials in .env file")
        print("\\n2. Run the full ETL pipeline:")
        print("   - python main.py")
        print("\\n3. Create Power BI dashboards:")
        print("   - Follow guide in powerbi_guides/PowerBI_Dashboard_Guide.md")
        
        print("\\n" + "="*60)
        print("     ✅ DATA PREVIEW COMPLETED SUCCESSFULLY!")
        print("="*60)
        
        return True
        
    except Exception as e:
        print(f"❌ Error during data processing: {e}")
        return False

if __name__ == "__main__":
    success = preview_data_processing()
    if not success:
        sys.exit(1)
