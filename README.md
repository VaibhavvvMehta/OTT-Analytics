# 📊 OTT Analytics - Netflix vs Hulu Streaming Analysis

A comprehensive data analysis comparing Netflix and Hulu performance across revenue, subscribers, and market dynamics in the streaming industry.

## 🎯 Project Overview

This project provides a **simple and clear analysis** of two major streaming platforms - Netflix and Hulu. Using real-world data, we explore which platform is performing better and what insights we can gain from their competition.

## 📈 Key Findings

- **Netflix dominates** with **$104.1B** total revenue vs Hulu's **$20.3B**
- Netflix has **4.5x more subscribers** than Hulu (**192.9M** vs **43.0M**)
- Netflix makes **5.1x more revenue** than Hulu
- Both platforms show strong growth patterns but at different scales

## 🔍 Analysis Areas

### 💰 Revenue Analysis
- Annual revenue trends over time
- Total revenue comparison
- Latest year performance metrics

### 👥 Subscriber Analysis  
- Subscriber growth patterns
- Market share distribution
- Growth rate comparisons

### 📊 Summary Insights
- Clear winner identification
- Key performance metrics
- Business intelligence conclusions

## 🛠️ Technologies Used

- **Python** - Main programming language
- **Pandas** - Data manipulation and analysis
- **Matplotlib** - Data visualization
- **NumPy** - Numerical computations
- **SQLAlchemy** - Database connectivity
- **MySQL** - Database management
- **Jupyter Notebook** - Interactive analysis environment

## 📁 Project Structure

```
OTT Analytics/
├── 📄 OTT_Analytics_Data_Analysis.ipynb  # Main analysis notebook
├── 📄 main.py                            # Automated execution script
├── 📄 .env.example                       # Environment configuration template
├── 📄 .gitignore                         # Git ignore rules
├── 📄 README.md                          # Project documentation
└── 📄 requirements.txt                   # Python dependencies
```

## 🚀 Getting Started

### Prerequisites
- Python 3.7+
- MySQL Database
- Jupyter Notebook

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/ott-analytics.git
   cd ott-analytics
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure environment**
   ```bash
   cp .env.example .env
   # Edit .env with your database credentials
   ```

4. **Run the analysis**
   ```bash
   # Option 1: Run the automated script
   python main.py
   
   # Option 2: Open Jupyter Notebook
   jupyter notebook OTT_Analytics_Data_Analysis.ipynb
   ```

## 📊 Sample Visualizations

The analysis includes several key visualizations:

- **Revenue Comparison Charts** - Side-by-side annual revenue trends
- **Market Share Pie Charts** - Current subscriber distribution
- **Growth Analysis** - Year-over-year growth patterns
- **Summary Dashboards** - Key metrics overview

## 🎯 Business Insights

### Netflix Advantages
- **Market Leadership**: Clear dominance in both revenue and subscribers
- **Scale Benefits**: Massive subscriber base enables content investment
- **Revenue Generation**: Superior monetization per user

### Hulu Opportunities  
- **Growth Potential**: Smaller scale allows for faster percentage growth
- **Market Position**: Strong #2 position with room for expansion
- **Niche Strategy**: Focused approach vs Netflix's broad strategy

## 📝 Key Metrics Summary

| Metric | Netflix | Hulu | Netflix Advantage |
|--------|---------|------|-------------------|
| Total Revenue | $104.1B | $20.3B | 5.1x |
| Current Subscribers | 192.9M | 43.0M | 4.5x |
| Latest Year Revenue | $24.9B | $4.4B | 5.7x |
| Market Share | 81.8% | 18.2% | Dominant |

## 🔧 Configuration

### Database Setup
1. Create a MySQL database named `ott_analytics`
2. Import your streaming data tables
3. Configure connection in `.env` file

### Environment Variables
```env
DB_HOST=localhost
DB_PORT=3306
DB_USER=your_username
DB_PASSWORD=your_password
DB_NAME=ott_analytics
```

## 📚 Dependencies

Install required packages:
```bash
pip install pandas matplotlib numpy sqlalchemy pymysql python-dotenv jupyter
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 📞 Contact

- **Author**: Your Name
- **Email**: your.email@example.com
- **LinkedIn**: [Your LinkedIn Profile](https://linkedin.com/in/yourprofile)
- **GitHub**: [Your GitHub Profile](https://github.com/yourusername)

## 🙏 Acknowledgments

- Data sources and streaming industry reports
- Open source Python data science community
- Netflix and Hulu for their transparent reporting

---

⭐ **If you found this analysis helpful, please consider giving it a star!** ⭐

*Last updated: July 2025*
# Install required packages
pip install -r requirements.txt

# Install MySQL and create database
# Update credentials in .env file
```

### Configuration
1. Copy `.env.example` to `.env`
2. Update database credentials:
```env
DB_HOST=localhost
DB_PORT=3306
DB_USER=your_username
DB_PASSWORD=your_password
DB_NAME=ott_analytics
```

### Run the ETL Pipeline
```bash
python main.py
```

This will:
1. Extract data from CSV files
2. Transform and clean the data
3. Load data into MySQL database
4. Generate analytics insights
5. Prepare data for Power BI integration

## 📁 Project Structure

```
OTT Analytics/
├── OTT Dataset/                 # Raw CSV data files
├── src/
│   ├── etl_pipeline.py         # Main ETL pipeline
│   ├── data_analyzer.py        # Analytics and insights
│   └── __init__.py
├── config/
│   └── config.py               # Configuration management
├── sql/
│   └── schema.sql              # Database schema
├── powerbi_guides/
│   └── PowerBI_Dashboard_Guide.md  # Detailed Power BI guide
├── main.py                     # Main execution script
├── requirements.txt            # Python dependencies
├── .env                        # Environment variables
└── README.md                   # This file
```

## 🗄️ Database Schema

The project creates an optimized star schema with:

### Dimension Tables
- `dim_platforms`: Platform information
- `dim_content`: Content metadata
- `dim_geography`: Regional data
- `dim_time`: Time dimensions

### Fact Tables
- `fact_subscribers`: Subscriber metrics
- `fact_revenue`: Revenue data
- `fact_content_performance`: Content analytics
- `fact_user_engagement`: User behavior

### Views
- `view_monthly_revenue`: Revenue summaries
- `view_subscriber_growth`: Growth analytics
- `view_content_library`: Content insights

## 📈 Analytics Features

### Key Metrics Calculated
- **Revenue Growth Rate**: Year-over-year revenue changes
- **Subscriber Growth**: Net subscriber additions and churn
- **Content ROI**: Return on content investment
- **Market Share**: Platform positioning analysis
- **User Engagement**: Session duration, bounce rates
- **Content Performance**: View counts, completion rates

### Advanced Analytics
- Cohort analysis for subscriber retention
- Seasonal trend identification
- Competitive benchmarking
- Content strategy optimization
- Revenue forecasting models

## 📊 Power BI Dashboard Creation

### Phase 1: Data Connection
1. Connect Power BI to MySQL database
2. Import all fact and dimension tables
3. Establish relationships in data model

### Phase 2: Dashboard Development
Create four main dashboards:

#### 1. Executive Summary Dashboard
- KPI cards for key metrics
- Revenue and subscriber trend lines
- Market share visualizations
- Growth rate indicators

#### 2. Content Analysis Dashboard
- Content library comparisons
- Content strategy analysis
- Performance vs investment metrics
- Genre and type distributions

#### 3. Financial Performance Dashboard
- Revenue breakdowns and waterfalls
- Profitability analysis
- Cost per acquisition metrics
- ROI calculations

#### 4. User Engagement Dashboard
- Demographic analysis
- Geographic distribution
- Engagement patterns
- Churn analysis

### Detailed Guide
See `powerbi_guides/PowerBI_Dashboard_Guide.md` for complete step-by-step instructions.

## 🔄 ETL Pipeline Details

### Extract Phase
- Reads CSV files from multiple platform directories
- Handles various file formats and naming conventions
- Validates data integrity and completeness

### Transform Phase
- Cleans and standardizes data formats
- Handles missing values and outliers
- Creates calculated fields and metrics
- Establishes data relationships

### Load Phase
- Creates optimized database schema
- Bulk loads data with proper indexing
- Implements data validation checks
- Sets up views for easy querying

## 🎯 Key Insights Generated

### Revenue Analytics
- Netflix shows 25%+ annual revenue growth
- Subscription model outperforms ad-supported models
- Regional variations in revenue per subscriber

### Content Strategy
- Movie-heavy vs TV-heavy platform strategies
- Content volume correlation with subscriber growth
- Original content ROI analysis

### Market Dynamics
- Netflix maintains market leadership
- Emerging platforms gaining traction
- Streaming wars intensifying competition

### User Behavior
- Binge-watching patterns vary by platform
- Demographics influence content preferences
- Geographic factors affect platform adoption

## 🛠️ Customization

### Adding New Data Sources
1. Place CSV files in appropriate directory structure
2. Update `DataProcessor.process_platform_data()` method
3. Modify database schema if needed
4. Run ETL pipeline to process new data

### Custom Analytics
1. Add new methods to `DataAnalyzer` class
2. Create custom DAX measures in Power BI
3. Implement additional visualizations
4. Update dashboard layouts

## 📋 Requirements

### Software Requirements
- Python 3.8+
- MySQL 8.0+
- Power BI Desktop
- MySQL ODBC Driver

### Python Libraries
```txt
pandas==2.1.4
numpy==1.24.3
sqlalchemy==2.0.23
pymysql==1.1.0
mysql-connector-python==8.2.0
plotly==5.17.0
matplotlib==3.7.2
seaborn==0.13.0
openpyxl==3.1.2
python-dotenv==1.0.0
```

## 🚀 Performance Optimization

### Database Optimizations
- Indexed columns for fast queries
- Partitioned tables for large datasets
- Materialized views for common aggregations
- Query optimization for Power BI

### ETL Optimizations
- Batch processing for large files
- Parallel processing where applicable
- Memory-efficient data transformations
- Error handling and recovery

### Power BI Optimizations
- DirectQuery for real-time data
- Aggregation tables for performance
- Optimized DAX calculations
- Efficient data model design

## 🔧 Troubleshooting

### Common Issues
1. **Database Connection Errors**
   - Verify MySQL service is running
   - Check credentials in .env file
   - Ensure firewall allows connections

2. **Data Loading Issues**
   - Validate CSV file formats
   - Check for encoding issues
   - Verify file paths are correct

3. **Power BI Connection Problems**
   - Install MySQL ODBC driver
   - Use correct connection string
   - Check user permissions

### Debug Mode
Enable detailed logging by setting log level to DEBUG in configuration.

## 📝 Future Enhancements

### Planned Features
- Real-time data streaming integration
- Machine learning models for churn prediction
- Advanced forecasting algorithms
- Automated report generation
- Mobile dashboard optimization

### Scalability Improvements
- Cloud database migration (AWS RDS, Azure SQL)
- Data lake integration for big data
- Microservices architecture
- Container deployment with Docker

## 🤝 Contributing

1. Fork the repository
2. Create feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open Pull Request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- OTT industry data providers
- Open-source community
- Power BI and MySQL documentation
- Data visualization best practices

---

## 📞 Support

For questions and support:
- Create an issue in the repository
- Check the troubleshooting guide
- Review the Power BI guide documentation

**Happy Analyzing! 📊🚀**
