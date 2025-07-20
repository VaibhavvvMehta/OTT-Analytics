"""
Simplified Data Preview Script - OTT Analytics Data Processing
This script processes the data without database dependencies
"""

import pandas as pd
import numpy as np
import os

def clean_numeric_columns(df, columns):
    """Clean numeric columns by removing commas and converting to float"""
    df_clean = df.copy()
    for col in columns:
        if col in df_clean.columns:
            df_clean[col] = df_clean[col].astype(str).str.replace(',', '').str.replace('"', '')
            df_clean[col] = pd.to_numeric(df_clean[col], errors='coerce')
    return df_clean

def process_library_size(data_path):
    """Process library size data"""
    try:
        df = pd.read_csv(os.path.join(data_path, 'LibrarySize.csv'))
        df = clean_numeric_columns(df, ['Movies', 'TV Shows'])
        df['Total_Content'] = df['Movies'] + df['TV Shows']
        df['Content_Ratio'] = df['Movies'] / df['TV Shows']
        return df
    except Exception as e:
        print(f"Error processing library size: {e}")
        return pd.DataFrame()

def process_platform_data(data_path, platform):
    """Process data for a specific platform"""
    platform_data = {}
    platform_path = os.path.join(data_path, platform)
    
    if not os.path.exists(platform_path):
        return platform_data
        
    try:
        for file in os.listdir(platform_path):
            if file.endswith('.csv'):
                file_path = os.path.join(platform_path, file)
                table_name = f"{platform.lower().replace(' ', '_')}_{file.replace('.csv', '').lower()}"
                
                df = pd.read_csv(file_path)
                
                # Clean numeric columns based on file type
                if 'revenue' in file.lower():
                    numeric_cols = ['Revenue']
                elif 'subscribers' in file.lower():
                    numeric_cols = ['Subscribers']
                elif 'profit' in file.lower():
                    numeric_cols = ['Profit']
                elif 'users' in file.lower():
                    numeric_cols = ['Users']
                else:
                    numeric_cols = []
                
                if numeric_cols:
                    df = clean_numeric_columns(df, numeric_cols)
                
                df['Platform'] = platform
                platform_data[table_name] = df
                
    except Exception as e:
        print(f"Error processing {platform}: {e}")
        
    return platform_data

def preview_ott_data():
    """Preview OTT analytics data processing"""
    print("="*60)
    print("     OTT ANALYTICS - DATA PREVIEW")
    print("="*60)
    
    data_path = "OTT Dataset"
    
    if not os.path.exists(data_path):
        print(f"❌ Data directory not found: {data_path}")
        return False
    
    print(f"\\n📁 Processing data from: {data_path}")
    print("-" * 40)
    
    all_data = {}
    
    # Process general files
    print("\\n1. Processing general data files...")
    library_df = process_library_size(data_path)
    if not library_df.empty:
        all_data['library_size'] = library_df
        print(f"   ✅ Library Size: {len(library_df)} platforms")
    
    # Process minute sharing if exists
    minute_sharing_path = os.path.join(data_path, 'MinuteSharing.csv')
    if os.path.exists(minute_sharing_path):
        try:
            minute_df = pd.read_csv(minute_sharing_path)
            all_data['minute_sharing'] = minute_df
            print(f"   ✅ Minute Sharing: {len(minute_df)} records")
        except Exception as e:
            print(f"   ❌ Error processing minute sharing: {e}")
    
    # Define platforms to process
    platforms = [
        'Netflix', 'Hulu', 'Disney Plus', 'Youtube', 'Tiktok', 'Twitch',
        'China Video Streaming Apps Overview',
        'UK Video Streaming Apps Overview',
        'USA Video Streaming Apps Overview'
    ]
    
    print(f"\\n2. Processing platform-specific data...")
    platform_count = 0
    
    for platform in platforms:
        platform_data = process_platform_data(data_path, platform)
        if platform_data:
            all_data.update(platform_data)
            file_count = len(platform_data)
            platform_count += 1
            print(f"   ✅ {platform}: {file_count} files processed")
    
    print(f"\\n📊 Data Processing Summary:")
    print("-" * 40)
    print(f"• Total platforms processed: {platform_count}")
    print(f"• Total datasets created: {len(all_data)}")
    
    total_rows = 0
    for table_name, df in all_data.items():
        rows = len(df)
        cols = len(df.columns)
        total_rows += rows
        print(f"• {table_name}: {rows:,} rows, {cols} columns")
    
    print(f"\\n📈 Total Records: {total_rows:,}")
    
    # Key insights
    print("\\n🔍 Key Data Insights:")
    print("-" * 40)
    
    # Library analysis
    if 'library_size' in all_data:
        lib_df = all_data['library_size']
        print(f"\\n📚 Content Library Analysis:")
        print(f"   • Total platforms: {len(lib_df)}")
        
        if not lib_df.empty:
            largest = lib_df.loc[lib_df['Total_Content'].idxmax()]
            print(f"   • Largest library: {largest['Streaming platform']} ({largest['Total_Content']:,} titles)")
            print(f"   • Total content: {lib_df['Total_Content'].sum():,} titles")
            print(f"   • Average content per platform: {lib_df['Total_Content'].mean():.0f} titles")
            
            print(f"\\n   Top 5 Platforms by Content:")
            top_5 = lib_df.nlargest(5, 'Total_Content')[['Streaming platform', 'Movies', 'TV Shows', 'Total_Content']]
            for _, row in top_5.iterrows():
                print(f"     • {row['Streaming platform']}: {row['Total_Content']:,} ({row['Movies']:,} movies, {row['TV Shows']:,} shows)")
    
    # Netflix analysis
    netflix_revenue_key = next((k for k in all_data.keys() if 'netflix_revenue' in k), None)
    netflix_subs_key = next((k for k in all_data.keys() if 'netflix' in k and 'subscribers' in k), None)
    
    if netflix_revenue_key and netflix_subs_key:
        revenue_df = all_data[netflix_revenue_key]
        subs_df = all_data[netflix_subs_key]
        
        print(f"\\n🎬 Netflix Analysis:")
        if not revenue_df.empty and not subs_df.empty:
            revenue_growth = ((revenue_df['Revenue'].iloc[-1] - revenue_df['Revenue'].iloc[0]) / revenue_df['Revenue'].iloc[0]) * 100
            subscriber_growth = subs_df['Subscribers'].iloc[-1] - subs_df['Subscribers'].iloc[0]
            
            print(f"   • Revenue growth: {revenue_growth:.1f}% over {len(revenue_df)} years")
            print(f"   • Latest revenue: ${revenue_df['Revenue'].iloc[-1]:.1f}B")
            print(f"   • Subscriber growth: {subscriber_growth:.1f}M subscribers")
            print(f"   • Current subscribers: {subs_df['Subscribers'].iloc[-1]:.1f}M")
    
    # Show sample data
    print(f"\\n📋 Sample Data Preview:")
    print("-" * 40)
    
    if 'library_size' in all_data:
        print("\\nLibrary Size Data:")
        print(all_data['library_size'].head(3).to_string(index=False))
    
    if netflix_revenue_key:
        print(f"\\nNetflix Revenue Data:")
        print(all_data[netflix_revenue_key].head(3).to_string(index=False))
    
    print("\\n🚀 Next Steps for Complete Implementation:")
    print("-" * 50)
    print("1. Database Setup:")
    print("   • Install MySQL Server")
    print("   • Create database 'ott_analytics'")
    print("   • Update .env file with credentials")
    print("\\n2. Python Environment:")
    print("   • Install: pip install pymysql sqlalchemy python-dotenv")
    print("   • Run: python main.py")
    print("\\n3. Power BI Dashboard:")
    print("   • Connect to MySQL database")
    print("   • Follow guide: powerbi_guides/PowerBI_Dashboard_Guide.md")
    print("   • Create executive, content, financial, and engagement dashboards")
    
    print("\\n4. Database Tables to be Created:")
    for table_name in all_data.keys():
        print(f"   • {table_name}")
    
    print("\\n" + "="*60)
    print("     ✅ DATA PREVIEW COMPLETED SUCCESSFULLY!")
    print("=" * 60)
    
    return True

if __name__ == "__main__":
    preview_ott_data()
