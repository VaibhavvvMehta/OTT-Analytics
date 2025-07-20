"""
Simple MySQL connection test
"""
import pymysql
from urllib.parse import quote_plus
import os
from dotenv import load_dotenv

load_dotenv()

def test_mysql_connection():
    """Test MySQL connection with proper password encoding"""
    
    # Get credentials from environment
    host = os.getenv('DB_HOST', 'localhost')
    port = int(os.getenv('DB_PORT', 3306))
    user = os.getenv('DB_USER', 'root')
    password = os.getenv('DB_PASSWORD', '')
    
    print(f"Testing MySQL connection to {host}:{port}")
    print(f"User: {user}")
    print(f"Password: {'*' * len(password)}")
    
    try:
        # Test direct pymysql connection
        connection = pymysql.connect(
            host=host,
            port=port,
            user=user,
            password=password
        )
        
        print("✅ MySQL connection successful!")
        
        # Test database creation
        with connection.cursor() as cursor:
            cursor.execute("CREATE DATABASE IF NOT EXISTS ott_analytics")
            cursor.execute("SHOW DATABASES LIKE 'ott_analytics'")
            result = cursor.fetchone()
            if result:
                print("✅ Database 'ott_analytics' exists or created successfully!")
            else:
                print("❌ Failed to create database")
        
        connection.close()
        return True
        
    except pymysql.Error as e:
        print(f"❌ MySQL connection failed: {e}")
        return False
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        return False

if __name__ == "__main__":
    success = test_mysql_connection()
    if success:
        print("\\n🎉 MySQL is ready for the ETL pipeline!")
    else:
        print("\\n⚠️  Please check MySQL installation and credentials.")
        print("\\nTroubleshooting steps:")
        print("1. Ensure MySQL Server is running")
        print("2. Verify credentials in .env file")
        print("3. Check if MySQL service is started")
        print("4. Test connection with MySQL Workbench or command line")
