# OLX Car Cover Scraper 🚗

A Python web scraper built with Selenium to extract car cover listings from OLX India. This project demonstrates how to overcome modern anti-bot protection and scrape dynamic websites effectively.

## 🎯 Project Overview

This scraper searches for "car cover" listings on OLX India and extracts:
- Product titles
- Prices (in Indian Rupees)
- Locations
- Saves results to timestamped text files

## 🛠️ Technologies Used

- **Python 3.x**
- **Selenium WebDriver** - Browser automation
- **Chrome/ChromeDriver** - Web browser for automation
- **BeautifulSoup** - HTML parsing (attempted but blocked)

## 📋 Prerequisites

- Python 3.x installed on your system
- Google Chrome browser
- Terminal/Command line access

## 🚀 Installation & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/Ansh-bhamniya/data_Scraping_from_OLX.git
cd data_Scraping_from_OLX
```

### 2. Install Required Packages
```bash
# Install Python packages
pip3 install selenium beautifulsoup4 requests

# Install ChromeDriver (macOS with Homebrew)
brew install chromedriver

# For other systems, download ChromeDriver from:
# https://chromedriver.chromium.org/
```

### 3. Verify Installation
```bash
# Check ChromeDriver installation
chromedriver --version

# Check Python packages
python3 -c "import selenium; print('Selenium installed successfully')"
```

## 🎮 Usage

### Run the Scraper
```bash
python3 olx_selenium.py
```

### Expected Output
```
Opening OLX search page...
Page loaded successfully!
Page title: Car Cover in India, Free classifieds in India | OLX
Looking for ads with updated selectors...
Selector 'li[data-aut-id='itemBox3']': Found 40 elements
Successfully found ads using selector: li[data-aut-id='itemBox3']
Found 40 potential listings
Scraping complete! Results saved to olx_car_covers_selenium_YYYYMMDD-HHMMSS.txt
```

## 📁 Project Structure

```
data_Scraping_from_OLX/
├── README.md                           # This file
├── olx_selenium.py                     # Main scraper script
├── PROJECT_DOCUMENTATION.txt          # Detailed project documentation
├── olx_car_covers_selenium_*.txt      # Scraped results (timestamped)
└── .git/                              # Git repository files
```

## 📊 Sample Output

The scraper generates a text file with results like:

```
Search Results for 'Car Cover' from OLX (Selenium)
Scraped on: 2025-09-06 09:26:14
==================================================

--- Listing #1 ---
Title: Car body cover available in wholesale market price
Price: ₹ 500
Location: PERIYAMET, CHENNAI

--- Listing #2 ---
Title: All cars side mirror batman cover abs plastic piano black
Price: ₹ 2,499
Location: GANGTOK PRIVATE ESTATE, GANGTOK
```

## 🔧 Key Features

- **Anti-Bot Protection Bypass**: Uses Selenium to simulate real browser behavior
- **Dynamic Content Handling**: Waits for JavaScript-rendered content to load
- **Robust Element Selection**: Multiple fallback selectors for reliability
- **Error Handling**: Comprehensive try-catch blocks for stability
- **Timestamped Output**: Organized results with timestamps
- **Headless Operation**: Runs in background without opening browser window

## 🚨 Challenges Overcome

### 1. Anti-Bot Protection
- **Problem**: OLX blocks traditional HTTP requests
- **Solution**: Selenium WebDriver browser automation

### 2. Dynamic Content
- **Problem**: JavaScript-rendered listings not visible to requests library
- **Solution**: WebDriverWait for proper page loading

### 3. Changing Selectors
- **Problem**: OLX updated HTML structure
- **Solution**: Analyzed current page structure and updated selectors

## ⚠️ Important Notes

### Rate Limiting
- The script includes reasonable delays to avoid overwhelming the server
- Use responsibly and respect OLX's terms of service

### Legal Considerations
- This tool is for educational purposes
- Ensure compliance with OLX's robots.txt and terms of service
- Consider using official APIs when available

### Browser Requirements
- Requires Chrome browser to be installed
- ChromeDriver version should match your Chrome browser version

## 🐛 Troubleshooting

### Common Issues

**ChromeDriver not found:**
```bash
# Install ChromeDriver
brew install chromedriver  # macOS
# Or download from https://chromedriver.chromium.org/
```

**Permission denied for ChromeDriver:**
```bash
# macOS: Allow ChromeDriver in Security & Privacy settings
# Or run with --disable-web-security flag
```

**No listings found:**
- Check internet connection
- Verify OLX website is accessible
- Website structure may have changed (update selectors)

## 📈 Performance

- **Average Runtime**: 10-30 seconds
- **Typical Results**: 30-50 listings per run
- **Success Rate**: ~95% with proper setup

## 🔮 Future Enhancements

- [ ] Database storage (SQLite/PostgreSQL)
- [ ] Proxy rotation for large-scale scraping
- [ ] Price change monitoring and alerts
- [ ] Multiple category support
- [ ] GUI interface
- [ ] Scheduled scraping with cron jobs
- [ ] Data visualization dashboard

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/new-feature`)
3. Commit your changes (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature/new-feature`)
5. Create a Pull Request

## 📄 License

This project is for educational purposes only. Please respect OLX's terms of service and use responsibly.

## 👨‍💻 Author

**Ansh Bhamniya**
- GitHub: [@Ansh-bhamniya](https://github.com/Ansh-bhamniya)

## 📞 Support

If you encounter any issues or have questions:
1. Check the troubleshooting section
2. Review the `PROJECT_DOCUMENTATION.txt` file
3. Open an issue on GitHub

---

⭐ **Star this repository if you found it helpful!**
