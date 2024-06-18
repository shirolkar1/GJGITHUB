from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Set up Chrome options
chrome_options = Options()
chrome_options.add_argument('--headless')  # Run in headless mode
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

# Path to your ChromeDriver
chromedriver_path = r"C:\Users\User\Downloads\chromedriver-win64 (1)\chromedriver-win64\chromedriver.exe"  # Update this path

# Set up Chrome service
service = Service(chromedriver_path)

# Initialize the web driver
driver = webdriver.Chrome(service=service, options=chrome_options)

# Define the login URL and login credentials
login_url = "https://gjcportal.xchangefusion.com"
username = "varungupta58@yahoo.com"
password = "BS34GJC"  # Replace with the actual password

try:
    # Open the login page
    driver.get(login_url)

    # Wait until the username input field is present
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@type='text']"))
    )

    # Find the username and password fields and enter the login credentials
    driver.find_element(By.XPATH, "//input[@type='text']").send_keys(username)
    driver.find_element(By.XPATH, "//input[@type='password']").send_keys(password)

    # Click the login button
    driver.find_element(By.XPATH, "//button[text()='Log in']").click()

    # Wait for login to complete
    time.sleep(5)

    # Add your post-login actions here
    # For example, navigate to a specific page and scrape data

    # Placeholder for further actions
    print("Login successful. Add further actions here.")

finally:
    # Close the web driver
    driver.quit()
