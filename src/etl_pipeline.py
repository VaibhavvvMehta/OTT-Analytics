import pandas as pd
import numpy as np
from sqlalchemy import create_engine, text
import pymysql
import os
import logging
from typing import Dict, List, Tuple
from urllib.parse import quote_plus
from config.config import Config

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class DatabaseManager:
    """Handles database connections and operations"""
    
    def __init__(self):
        self.config = Config()
        self.engine = None
        
    def create_database(self):
        """Create the database if it doesn't exist"""
        try:
            # Connect without specifying database to create it
            temp_url = f"mysql+pymysql://{self.config.DB_USER}:{quote_plus(self.config.DB_PASSWORD)}@{self.config.DB_HOST}:{self.config.DB_PORT}"
            temp_engine = create_engine(temp_url)
            
            with temp_engine.connect() as conn:
                conn.execute(text(f"CREATE DATABASE IF NOT EXISTS {self.config.DB_NAME}"))
                conn.commit()
                logger.info(f"Database '{self.config.DB_NAME}' created successfully")
                
        except Exception as e:
            logger.error(f"Error creating database: {e}")
            raise
            
    def get_engine(self):
        """Get database engine"""
        if not self.engine:
            try:
                self.engine = create_engine(self.config.DATABASE_URL)
                logger.info("Database engine created successfully")
            except Exception as e:
                logger.error(f"Error creating engine: {e}")
                raise
        return self.engine
    
    def test_connection(self):
        """Test database connection"""
        try:
            engine = self.get_engine()
            with engine.connect() as conn:
                result = conn.execute(text("SELECT 1"))
                logger.info("Database connection successful")
                return True
        except Exception as e:
            logger.error(f"Database connection failed: {e}")
            return False

class DataProcessor:
    """Handles data processing and transformation"""
    
    def __init__(self, data_path: str):
        self.data_path = data_path
        self.processed_data = {}
        
    def clean_numeric_columns(self, df: pd.DataFrame, columns: List[str]) -> pd.DataFrame:
        """Clean numeric columns by removing commas and converting to float"""
        df_clean = df.copy()
        for col in columns:
            if col in df_clean.columns:
                df_clean[col] = df_clean[col].astype(str).str.replace(',', '').str.replace('"', '')
                df_clean[col] = pd.to_numeric(df_clean[col], errors='coerce')
        return df_clean
    
    def process_library_size(self) -> pd.DataFrame:
        """Process library size data"""
        try:
            df = pd.read_csv(os.path.join(self.data_path, 'LibrarySize.csv'))
            df = self.clean_numeric_columns(df, ['Movies', 'TV Shows'])
            df['Total_Content'] = df['Movies'] + df['TV Shows']
            df['Content_Ratio'] = df['Movies'] / df['TV Shows']
            logger.info("Library size data processed successfully")
            return df
        except Exception as e:
            logger.error(f"Error processing library size data: {e}")
            return pd.DataFrame()
    
    def process_minute_sharing(self) -> pd.DataFrame:
        """Process minute sharing data"""
        try:
            df = pd.read_csv(os.path.join(self.data_path, 'MinuteSharing.csv'))
            logger.info("Minute sharing data processed successfully")
            return df
        except Exception as e:
            logger.error(f"Error processing minute sharing data: {e}")
            return pd.DataFrame()
    
    def process_platform_data(self, platform: str) -> Dict[str, pd.DataFrame]:
        """Process data for a specific platform"""
        platform_data = {}
        platform_path = os.path.join(self.data_path, platform)
        
        if not os.path.exists(platform_path):
            logger.warning(f"Platform directory not found: {platform}")
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
                        df = self.clean_numeric_columns(df, numeric_cols)
                    
                    # Add platform identifier
                    df['Platform'] = platform
                    
                    platform_data[table_name] = df
                    logger.info(f"Processed {file} for {platform}")
                    
        except Exception as e:
            logger.error(f"Error processing platform data for {platform}: {e}")
            
        return platform_data
    
    def process_all_data(self) -> Dict[str, pd.DataFrame]:
        """Process all data from the dataset"""
        all_data = {}
        
        # Process general files
        all_data['library_size'] = self.process_library_size()
        all_data['minute_sharing'] = self.process_minute_sharing()
        
        # Define platforms to process
        platforms = [
            'Netflix', 'Hulu', 'Disney Plus', 'Youtube', 'Tiktok', 'Twitch',
            'China Video Streaming Apps Overview',
            'UK Video Streaming Apps Overview',
            'USA Video Streaming Apps Overview'
        ]
        
        # Process each platform
        for platform in platforms:
            platform_data = self.process_platform_data(platform)
            all_data.update(platform_data)
        
        self.processed_data = all_data
        logger.info(f"Processed {len(all_data)} datasets successfully")
        return all_data

class ETLPipeline:
    """Main ETL pipeline for OTT Analytics"""
    
    def __init__(self, data_path: str):
        self.data_path = data_path
        self.db_manager = DatabaseManager()
        self.data_processor = DataProcessor(data_path)
        self.processed_data = {}
        
    def extract(self) -> Dict[str, pd.DataFrame]:
        """Extract and process data from CSV files"""
        logger.info("Starting data extraction...")
        return self.data_processor.process_all_data()
    
    def transform(self, data: Dict[str, pd.DataFrame]) -> Dict[str, pd.DataFrame]:
        """Transform data for analysis"""
        logger.info("Starting data transformation...")
        transformed_data = {}
        
        for table_name, df in data.items():
            if df.empty:
                continue
                
            # Add metadata columns
            df['created_at'] = pd.Timestamp.now()
            df['data_source'] = table_name
            
            # Handle missing values
            df = df.fillna(0)
            
            transformed_data[table_name] = df
            
        logger.info("Data transformation completed")
        return transformed_data
    
    def load(self, data: Dict[str, pd.DataFrame]) -> bool:
        """Load data into MySQL database"""
        logger.info("Starting data loading...")
        
        try:
            # Create database
            self.db_manager.create_database()
            
            # Get engine
            engine = self.db_manager.get_engine()
            
            # Load each dataset
            for table_name, df in data.items():
                if df.empty:
                    logger.warning(f"Skipping empty dataset: {table_name}")
                    continue
                    
                # Load to database
                df.to_sql(
                    name=table_name,
                    con=engine,
                    if_exists='replace',
                    index=False,
                    chunksize=1000
                )
                logger.info(f"Loaded {len(df)} rows into table: {table_name}")
            
            logger.info("Data loading completed successfully")
            return True
            
        except Exception as e:
            logger.error(f"Error during data loading: {e}")
            return False
    
    def run_pipeline(self) -> bool:
        """Run the complete ETL pipeline"""
        try:
            logger.info("Starting OTT Analytics ETL Pipeline...")
            
            # Test database connection
            if not self.db_manager.test_connection():
                logger.error("Database connection failed. Please check your configuration.")
                return False
            
            # Extract
            raw_data = self.extract()
            if not raw_data:
                logger.error("No data extracted")
                return False
            
            # Transform
            transformed_data = self.transform(raw_data)
            
            # Load
            success = self.load(transformed_data)
            
            if success:
                logger.info("ETL Pipeline completed successfully!")
                self.processed_data = transformed_data
                return True
            else:
                logger.error("ETL Pipeline failed during loading")
                return False
                
        except Exception as e:
            logger.error(f"ETL Pipeline failed: {e}")
            return False
    
    def get_data_summary(self) -> Dict:
        """Get summary of processed data"""
        summary = {}
        for table_name, df in self.processed_data.items():
            summary[table_name] = {
                'rows': len(df),
                'columns': len(df.columns),
                'column_names': list(df.columns)
            }
        return summary

if __name__ == "__main__":
    # Run the ETL pipeline
    data_path = "OTT Dataset"
    pipeline = ETLPipeline(data_path)
    
    if pipeline.run_pipeline():
        print("\\n" + "="*50)
        print("ETL PIPELINE COMPLETED SUCCESSFULLY!")
        print("="*50)
        
        # Print data summary
        summary = pipeline.get_data_summary()
        print("\\nData Summary:")
        for table, info in summary.items():
            print(f"\\n{table}:")
            print(f"  Rows: {info['rows']}")
            print(f"  Columns: {info['columns']}")
            print(f"  Column Names: {', '.join(info['column_names'])}")
    else:
        print("ETL Pipeline failed. Please check the logs.")
