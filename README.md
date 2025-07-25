# OTT Analytics: Streaming Wars Data Analysis

## Project Overview

A comprehensive data analysis project examining the streaming industry landscape across major platforms including Netflix, YouTube, Disney+, Hulu, TikTok, and Twitch. This analysis covers 6 years of data (2018-2024) across multiple regions to understand revenue trends, user growth, and competitive dynamics.

## Key Features

- **Revenue Analysis**: Comprehensive financial performance comparison
- **User Growth Tracking**: Subscriber and user base evolution analysis  
- **Regional Market Analysis**: USA, UK, and China market comparison
- **Content Strategy Insights**: Library size vs. engagement correlation
- **Data Visualization**: Professional charts and interactive visualizations

## Dataset Coverage

### Platforms Analyzed
- **Traditional Streamers**: Netflix, Hulu, Disney+
- **Tech Giants**: YouTube, TikTok  
- **Gaming Platforms**: Twitch
- **Regional Data**: Multi-country analysis

### Metrics Tracked
- Revenue (billions USD)
- Subscriber/User counts (millions)
- Growth rates and trends
- Content library sizes
- Regional market penetration

## Project Structure

```
OTT Analytics/
├── OTT_Analytics_Data_Analysis.ipynb    # Main analysis notebook
├── requirements.txt                      # Python dependencies
├── README.md                            # Project documentation
├── .env.example                         # Environment template
└── OTT Dataset/                         # Data files
    ├── Netflix/
    ├── Hulu/
    ├── Disney Plus/
    ├── Youtube/
    ├── Tiktok/
    ├── Twitch/
    ├── USA Video Streaming Apps Overview/
    ├── UK Video Streaming Apps Overview/
    └── China Video Streaming Apps Overview/
```

## Installation & Setup

### Prerequisites
- Python 3.8+
- MySQL database (optional for database features)
- Jupyter Notebook

### Installation Steps

1. **Clone the repository**
   ```bash
   git clone https://github.com/VaibhavvvMehta/OTT-Analytics.git
   cd OTT-Analytics
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Environment setup** (optional for database features)
   ```bash
   cp .env.example .env
   # Edit .env with your database credentials
   ```

4. **Launch Jupyter Notebook**
   ```bash
   jupyter notebook OTT_Analytics_Data_Analysis.ipynb
   ```

## Key Findings Summary

### Revenue Leaders
- **Netflix**: $104.1B total revenue (48% market share)
- **YouTube**: $77.3B total revenue (35.7% market share)  
- **Hulu**: $20.3B total revenue (9.4% market share)

### Regional Insights
- **USA**: $87.0B revenue, $292 per subscriber annually
- **China**: $75.7B revenue, 305M subscribers
- **UK**: $9.4B revenue, $178 per subscriber annually

### Growth Trends
- Subscription-based platforms show steady growth
- Ad-supported platforms demonstrate higher user volumes
- Regional preferences vary significantly

## Technical Implementation

### Data Processing
- **Data Sources**: 17 comprehensive datasets
- **Time Coverage**: 6+ years historical analysis
- **Quality Assurance**: 95.2% data reliability
- **Scale Handling**: Proper separation of billions vs. millions metrics

### Analysis Methods
- Revenue trend analysis
- Year-over-year growth calculations
- Market share distribution
- Regional comparative analysis
- Content strategy correlation

### Visualization Features
- Interactive revenue comparisons
- Geographic market breakdowns
- Growth trend visualizations
- Platform performance dashboards

## Usage Examples

### Basic Analysis
```python
# Load and analyze Netflix revenue data
netflix_revenue = pd.read_csv('OTT Dataset/Netflix/Revenue.csv')
total_revenue = netflix_revenue['revenue'].sum()
print(f"Netflix Total Revenue: ${total_revenue:.1f}B")
```

### Regional Comparison
```python
# Compare regional market performance
usa_data = pd.read_csv('OTT Dataset/USA Video Streaming Apps Overview/Revenue.csv')
uk_data = pd.read_csv('OTT Dataset/UK Video Streaming Apps Overview/Revenue.csv')
china_data = pd.read_csv('OTT Dataset/China Video Streaming Apps Overview/Revenue.csv')
```

## Data Sources & Methodology

### Data Collection
- Financial reports and public filings
- Industry research databases
- Platform-specific analytics
- Regional market studies

### Analysis Framework
- Comparative financial analysis
- Statistical trend analysis
- Market segmentation studies
- Performance benchmarking

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/analysis-update`)
3. Commit your changes (`git commit -am 'Add new analysis'`)
4. Push to the branch (`git push origin feature/analysis-update`)
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contact

**Author**: Vaibhav Mehta  
**GitHub**: [@VaibhavvvMehta](https://github.com/VaibhavvvMehta)  
**Project**: [OTT-Analytics](https://github.com/VaibhavvvMehta/OTT-Analytics)

## Acknowledgments

- Data sources from various streaming platforms
- Industry research reports
- Open source data analysis tools
- Python data science community

---

*Last Updated: July 2025*
