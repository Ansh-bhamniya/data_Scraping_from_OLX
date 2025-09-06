from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def scrape_olx_with_selenium():
    """
    Scrapes OLX using Selenium WebDriver to handle JavaScript and anti-bot protection
    """
    # Configure Chrome options
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run in background
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36")
    
    try:
        # Initialize the driver
        driver = webdriver.Chrome(options=chrome_options)
        
        print("Opening OLX search page...")
        driver.get("https://www.olx.in/items/q-car-cover")
        
        # Wait for page to load
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "body"))
        )
        
        print(f"Page loaded successfully!")
        print(f"Page title: {driver.title}")
        
        # Look for ad listings - try multiple selectors
        print("Looking for ads with updated selectors...")
        
        # Try the correct selectors based on the HTML structure
        selectors_to_try = [
            "li[data-aut-id='itemBox3']",  # The actual selector used by OLX
            "[data-aut-id='itemBox3']",
            "li._1DNjI",  # The class name from the HTML
            ".fTZT3",  # Content wrapper class
            "li[data-aut-category-id]"  # Alternative by category attribute
        ]
        
        ads = []
        working_selector = None
        
        for selector in selectors_to_try:
            ads = driver.find_elements(By.CSS_SELECTOR, selector)
            print(f"Selector '{selector}': Found {len(ads)} elements")
            if ads:
                working_selector = selector
                break
        
        # If still no ads, let's see what's on the page
        if not ads:
            print("Still no ads found. Let's examine the page structure...")
            
            # Try to find any list items that might contain listings
            all_li = driver.find_elements(By.TAG_NAME, "li")
            print(f"Found {len(all_li)} li elements on page")
            
            # Look for elements with data-aut-id attributes
            elements_with_data_aut = driver.find_elements(By.CSS_SELECTOR, "[data-aut-id]")
            print(f"Found {len(elements_with_data_aut)} elements with data-aut-id")
            
            # Save the page source for debugging
            page_source = driver.page_source
            print(f"Page source length: {len(page_source)} characters")
            
            with open("olx_page_debug.html", "w", encoding="utf-8") as f:
                f.write(page_source)
            print("Page source saved to olx_page_debug.html for inspection")
        else:
            print(f"Successfully found ads using selector: {working_selector}")
        
        print(f"Found {len(ads)} potential listings")
        
        # Get current timestamp for the filename
        timestamp = time.strftime("%Y%m%d-%H%M%S")
        filename = f"olx_car_covers_selenium_{timestamp}.txt"
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(f"Search Results for 'Car Cover' from OLX (Selenium)\n")
            f.write(f"Scraped on: {time.strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write("=" * 50 + "\n\n")
            
            for i, ad in enumerate(ads[:10], 1):  # Limit to first 10 ads
                try:
                    # Use the correct selectors based on the actual HTML structure
                    title = "N/A"
                    price = "N/A"
                    location = "N/A"
                    
                    # Try to extract title using the correct selector
                    try:
                        title_elem = ad.find_element(By.CSS_SELECTOR, "[data-aut-id='itemTitle']")
                        title = title_elem.text.strip()
                    except:
                        try:
                            title_elem = ad.find_element(By.CSS_SELECTOR, "._2poNJ")
                            title = title_elem.text.strip()
                        except:
                            # Fallback to any span or div containing text
                            title_elem = ad.find_element(By.CSS_SELECTOR, "span, div")
                            title = title_elem.text.strip()[:100]
                    
                    # Try to extract price using the correct selector
                    try:
                        price_elem = ad.find_element(By.CSS_SELECTOR, "[data-aut-id='itemPrice']")
                        price = price_elem.text.strip()
                    except:
                        try:
                            price_elem = ad.find_element(By.CSS_SELECTOR, "._2Ks63")
                            price = price_elem.text.strip()
                        except:
                            price = "Price not available"
                    
                    # Try to extract location using the correct selector
                    try:
                        location_elem = ad.find_element(By.CSS_SELECTOR, "[data-aut-id='item-location']")
                        location = location_elem.text.strip()
                    except:
                        try:
                            location_elem = ad.find_element(By.CSS_SELECTOR, "._2VQu4")
                            location = location_elem.text.strip()
                        except:
                            location = "Location not available"
                    
                    # If we couldn't find structured data, get the text content
                    if title == "N/A":
                        all_text = ad.text.strip()
                        title = all_text[:100] if all_text else f"Listing {i}"
                    
                    f.write(f"--- Listing #{i} ---\n")
                    f.write(f"Title: {title}\n")
                    f.write(f"Price: {price}\n")
                    f.write(f"Location: {location}\n\n")
                    
                except Exception as e:
                    f.write(f"--- Listing #{i} ---\n")
                    f.write(f"Could not parse this listing. Error: {e}\n\n")
        
        print(f"Scraping complete! Results saved to {filename}")
        
    except Exception as e:
        print(f"Error: {e}")
        print("This might be due to:")
        print("1. ChromeDriver not installed")
        print("2. Chrome browser not found")
        print("3. Website blocking even browser automation")
        
    finally:
        try:
            driver.quit()
        except:
            pass

if __name__ == "__main__":
    print("Note: This requires ChromeDriver to be installed.")
    print("Install with: brew install chromedriver")
    scrape_olx_with_selenium()
