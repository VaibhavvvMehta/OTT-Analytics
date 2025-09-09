# 🎬 OTT Analytics Platform

A comprehensive analytics platform for streaming services (Netflix, Amazon Prime, Disney+) using Python, MySQL, and interactive visualizations.

## 📊 Project Overview

This project analyzes OTT (Over-The-Top) streaming platforms data to generate insights for dashboard creation. It provides comprehensive analytics across Netflix, Amazon Prime Video, and Disney+ platforms with advanced rating analysis using IMDb, Rotten Tomatoes, and Metacritic scores.

## 🎯 Key Features

- **Multi-Platform Analysis**: Netflix, Amazon Prime, Disney+ comparative analytics
- **Advanced Rating Insights**: IMDb, Rotten Tomatoes, Metacritic integration
- **Interactive Visualizations**: Plotly-based charts and graphs
- **Database Integration**: MySQL storage with SQLAlchemy ORM
- **Dashboard Metrics**: Ready-to-use KPIs for Power BI/dashboard creation
- **Genre Analysis**: Content categorization and popularity trends
- **Quality Assessment**: Content rating distribution and quality insights

## 📈 Dashboard Metrics Generated

### Netflix Analytics
- **Total Shows**: 8,807 titles
- **Content Split**: 70% Movies, 30% Series
- **Average Ratings**: IMDb 6.5/10, RT 59.5%, Metacritic 56.8/100
- **Quality Content**: 8.8% high-quality content (IMDb ≥8.0)
- **Top Genres**: Drama, Comedy, Action, Thriller, Romance

### Amazon Prime Analytics
- **Total Shows**: 9,668 titles
- **Content Split**: 81% Movies, 19% Series
- **Duration Focus**: Strong movie library with diverse content

### Disney+ Analytics
- **Total Shows**: 1,450 titles
- **Content Split**: 73% Movies, 27% Series
- **Family Focus**: Premium family-oriented content

## 🛠️ Technologies Used

- **Python 3.8+**: Core programming language
- **Pandas 2.2.3**: Data manipulation and analysis
- **Plotly 5.17.0**: Interactive visualizations
- **SQLAlchemy**: Database ORM
- **MySQL**: Database storage
- **Jupyter Notebook**: Analysis environment
- **Advanced Analytics**: 
  - User engagement metrics
  - Content performance analysis
  - Viewing pattern insights
  - Revenue analytics
  - Churn prediction models
  - Retention analysis

## Project Structure

```
├── Dataset/
│   ├── amazon_prime_titles.csv
│   ├── disney_plus_titles.csv
│   ├── netflix-rotten-tomatoes-metacritic-imdb.csv
│   └── netflix_titles.csv
├── notebooks/
│   └── OTT_Analytics_Analysis.ipynb
├── reports/
│   └── etl_report.json
├── Dashboards.pbix
├── README.md
├── requirements.txt
```

## Setup Instructions

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Set up MySQL database and configure connection in `.env` file

3. Run data processing pipeline:
   ```bash
   python src/main.py
   ```

4. Launch analytics dashboard:
   ```bash
   python src/dashboard_app.py
   ```

## Key Components

- **Data Pipeline**: Processes and combines data from multiple OTT platforms
- **Synthetic Data Generator**: Creates realistic streaming and user engagement data
- **Analytics Engine**: Comprehensive analysis of viewing patterns and performance
- **Interactive Dashboard**: Real-time insights and visualizations

## Technologies Used

- **Python**: Pandas, NumPy, Scikit-learn
- **Visualisation**: Plotly, Matplotlib, Seaborn
- **Database**: MySQL, SQLAlchemy
- **Analysis**: Jupyter Notebooks

## Dashboard Features

- User engagement metrics and trends
- Content performance analytics
- Revenue and subscription insights
- Geographic viewing patterns
- Content recommendation insights


