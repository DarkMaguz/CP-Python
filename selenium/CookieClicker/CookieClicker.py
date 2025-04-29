import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# Create a new Firefox session.
driver = webdriver.Firefox()

# Navigate to the application home page.
driver.get('https://orteil.dashnet.org/cookieclicker/')

# Accept cookies and chose English as language.
driver.find_element(By.CSS_SELECTOR, '.fc-cta-consent > p:nth-child(2)').click()
driver.find_element(By.CSS_SELECTOR, '#langSelect-EN').click()

# Wait 2 seconds for the page to finish loading.
time.sleep(2)

bigCookie = driver.find_element(By.ID, 'bigCookie')
cookieCounter = driver.find_element(By.ID, 'cookies')

for i in range(10):
  # Find the cookie and click it.
  bigCookie.click()

# Count the number of cookies.
print("Number of cookies: " + cookieCounter.text.split()[0])

# Wait 2 seconds.
time.sleep(2)

# Close the browser window.
driver.quit()
