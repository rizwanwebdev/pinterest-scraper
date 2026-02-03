# pinterestScraper.py

import os
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import urllib.parse
from selenium.webdriver.chrome.options import Options

options = Options()
options.binary_location = r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"

options.add_argument(
    r"--user-data-dir=C:\Users\Rizwan\AppData\Local\BraveSoftware\Brave-Browser\User Data"
)
options.add_argument("--profile-directory=Default")


class PinterestScraper:
    def __init__(self):
        self.driver = webdriver.Chrome(options=options)
        self.wait = WebDriverWait(self.driver, 10)
        self.downloaded_count = 1 #initial count or 0
        self.download_folder = "pinterest_downloads"
        
        # Create download folder
        os.makedirs(self.download_folder, exist_ok=True)
    
    def find_original_image_url(self, img_element):
        """Extract original quality image URL from srcset"""
        try:
            srcset = img_element.get_attribute("srcset")
            if srcset:
                # Parse srcset to find the 4x (original) version
                sources = srcset.split(", ")
                for source in sources:
                    if "originals" in source and "4x" in source:
                        return source.split(" ")[0]
            
            # Fallback: Try to construct original URL from smaller version
            src = img_element.get_attribute("src")
            if src and "pinimg.com" in src:
                parts = src.split("/")
                filename = parts[-1]
                # Construct original URL
                return f"https://i.pinimg.com/originals/{filename[0:2]}/{filename[2:4]}/{filename}"
            
            return None
        except:
            return None
    
    def download_image(self, url, pin_id):
        """Download image from URL"""
        try:
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
            }
            
            response = requests.get(url, headers=headers, timeout=10)
            
            if response.status_code == 200:
                # Extract file extension
                content_type = response.headers.get('content-type', '')
                if 'jpeg' in content_type or 'jpg' in content_type:
                    ext = '.jpg'
                elif 'png' in content_type:
                    ext = '.png'
                elif 'webp' in content_type:
                    ext = '.webp'
                else:
                    ext = '.jpg'  # Default
                
                # Save image
                filename = f"{self.download_folder}/pin_{pin_id}_{self.downloaded_count}{ext}"
                with open(filename, 'wb') as f:
                    f.write(response.content)
                
                print(f"Downloaded: {filename}")
                self.downloaded_count += 1
                return True
                
        except Exception as e:
            print(f"Error downloading {url}: {e}")
            return False
    
    def scroll_and_download(self, search_keyword, images_to_download):
        """Main scraping function"""
        # URL encode search keyword
        encoded_keyword = urllib.parse.quote(search_keyword)
        url = f"https://www.pinterest.com/search/pins/?q={encoded_keyword}"
        
        print(f"Opening Pinterest search: {search_keyword}")
        self.driver.get(url)
        
        # Wait for initial load
        time.sleep(3)
        
        last_height = self.driver.execute_script("return document.body.scrollHeight")
        seen_urls = set()
        
        while self.downloaded_count < images_to_download:
            # Find all image elements
            img_elements = self.driver.find_elements(By.CSS_SELECTOR, "img[src*='pinimg.com']")
            
            for img in img_elements:
                if self.downloaded_count >= images_to_download:
                    break
                
                # Get original image URL
                original_url = self.find_original_image_url(img)
                
                if original_url and original_url not in seen_urls:
                    seen_urls.add(original_url)
                    
                    # Download the image
                    success = self.download_image(original_url, f"img_{self.downloaded_count}")
                    
                    if success:
                        print(f"Progress: {self.downloaded_count}/{images_to_download}")
            
            # Scroll down to load more images
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2)
            
            # Check if we've reached the bottom
            new_height = self.driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                print("Reached bottom of page or no more images loading")
                break
            last_height = new_height
        
        print(f"\nDownloaded {self.downloaded_count} images to '{self.download_folder}' folder")
    
    def close(self):
        """Close the browser"""
        self.driver.quit()

# Fast usage example
if __name__ == "__main__":
    scraper = PinterestScraper()
    
    try:
        # Quick configuration
        search_query = "men smiling teeth"
        images_to_download = 5  # Change this number
        
        # Start scraping
        scraper.scroll_and_download(search_query, images_to_download)
        
    finally:
        scraper.close()