# Pinterest Image Scraper

A Python-based tool for downloading high-quality images from Pinterest using Selenium and requests.

![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)
![Selenium](https://img.shields.io/badge/Selenium-4.0+-orange.svg)

## 🌟 Features

- **High-Quality Downloads**: Automatically extracts original resolution images from Pinterest
- **Smart Scrolling**: Infinite scroll implementation to load more images dynamically
- **Automatic Organization**: Saves images to organized folders with sequential naming
- **Browser Automation**: Uses Selenium with Brave/Chrome for reliable scraping
- **Error Handling**: Robust error handling for network issues and image processing

## 📋 Prerequisites

Before using this scraper, ensure you have:

- Python 3.7 or higher
- Brave Browser or Google Chrome installed
- Appropriate browser drivers

## 🚀 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/rizwanwebdev/pintrest-scraper.git
cd pintrest-scraper
```

### 2. Install Required Packages

```bash
pip install selenium requests
```

### 3. Download ChromeDriver

Download the appropriate ChromeDriver version for your browser from:
https://chromedriver.chromium.org/

Place it in your system PATH or in the project directory.

## ⚙️ Configuration

### Browser Setup

The script is configured to use Brave Browser by default. If you want to use Chrome:

1. Remove or modify these lines in `pinterestScraper.py`:

```python
options.binary_location = r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"
options.add_argument(
    r"--user-data-dir=C:\Users\Rizwan\AppData\Local\BraveSoftware\Brave-Browser\User Data"
)
```

2. For Chrome, use:

```python
# options = Options()
# driver = webdriver.Chrome()  # Simple Chrome initialization
```

### User Data Directory (Optional)

To maintain login sessions, the script uses a specific user profile. Update this path to match your system:

```python
options.add_argument(r"--user-data-dir=YOUR_USER_DATA_PATH")
```

## 🎯 Usage

### Basic Usage

Run the script with default settings:

```bash
python pinterestScraper.py
```

### Customize Search

Modify the search query and number of images in the main section:

```python
# In the __main__ section of pinterestScraper.py
search_query = "your search term here"  # e.g., "nature landscapes", "minimalist art"
images_to_download = 10  # Number of images to download
```

### Advanced Usage

Create a custom script using the PinterestScraper class:

```python
from pinterestScraper import PinterestScraper

# Initialize scraper
scraper = PinterestScraper()

try:
    # Configure your search
    search_term = "cat photos"
    download_limit = 20

    # Start scraping
    scraper.scroll_and_download(search_term, download_limit)

finally:
    # Clean up
    scraper.close()
```

## 📁 Project Structure

```
pintrest-scraper/
├── pinterestScraper.py      # Main scraper script
├── pinterest_downloads/     # Downloaded images folder (auto-created)
├── README.md               # This file
└── requirements.txt        # Dependencies (optional)
```

## 🔧 How It Works

1. **Search Initialization**: Opens Pinterest with the encoded search query
2. **Image Detection**: Finds all Pinterest image elements using CSS selectors
3. **Quality Extraction**: Parses `srcset` attributes to get original quality URLs
4. **Download Management**: Downloads images with proper headers and file naming
5. **Infinite Scroll**: Automatically scrolls to load more images until target count is reached

## ⚠️ Important Notes

### Legal Considerations

- Use this tool responsibly and respect Pinterest's Terms of Service
- Only download images for personal use or with proper permissions
- Check image licenses before commercial use
- Consider adding delays between requests to avoid overloading servers

### Limitations

- Requires a stable internet connection
- May be affected by Pinterest's anti-scraping measures
- Image availability depends on search results

## 🛠️ Troubleshooting

### Common Issues

1. **"ChromeDriver executable needs to be in PATH"**
   - Download ChromeDriver and add it to your system PATH
   - Or specify the path directly: `webdriver.Chrome(executable_path='path/to/chromedriver')`

2. **Images not downloading**
   - Check your internet connection
   - Verify Pinterest hasn't changed its HTML structure
   - Ensure you're logged into Pinterest in your browser session

3. **Browser not opening**
   - Verify the browser installation path is correct
   - Try using Chrome instead of Brave

### Debug Mode

Add these options for debugging:

```python
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--verbose")
```

## 🔄 Updates & Maintenance

To keep the scraper working:

1. Monitor Pinterest for HTML structure changes
2. Update CSS selectors if necessary
3. Keep Selenium and browser drivers updated

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 👨‍💻 Author

**Rizwan**

- GitHub: [@rizwanwebdev](https://github.com/rizwanwebdev)
- Portfolio: [https://rizwan.one](https://rizwan.one)

## 🙏 Acknowledgments

- Built with [Selenium](https://www.selenium.dev/)
- Inspired by various web scraping tutorials
- Thanks to the open-source community

## ⭐ Support

If you find this project useful, please give it a star on GitHub!
