from selenium import webdriver

# Create a new instance of the Chrome driver
driver = webdriver.Chrome()

# Navigate to Google's homepage
driver.get("https://www.google.com")

# Wait for a few seconds (optional)
import time
time.sleep(50)

# Wait for user input before closing the browser
input("Press Enter to close the browser...")

# Close the browser window
driver.quit()






