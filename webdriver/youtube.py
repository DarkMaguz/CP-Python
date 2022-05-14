import os
import sys
import time
import pprint
pp = pprint.PrettyPrinter(indent=2)

from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service

from selenium.webdriver.remote import webelement

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


# Add path of the geckodriver to PATH.
os.environ['PATH'] += os.pathsep + 'bin/'

# Update Firefox and geckodriver.
os.system('check_for_updates.sh')

# Set option for headless.
options = Options()
options.binary_location = 'bin/firefox/firefox-bin'
options.add_argument('--private-window')
#options.add_argument('-headless')

service = Service('bin/geckodriver')

# Create a new Firefox session.
driver = webdriver.Firefox(service=service, options=options)

# Uncomment the next line to maximize the browser window.
#driver.maximize_window()

# Give the browser time to load before each command is executed.
driver.implicitly_wait(10)

# Navigate to the application home page.
driver.get('https://www.youtube.com')

# Accept the terms and conditions.
driver.find_element(By.XPATH, '//ytd-consent-bump-v2-lightbox//ytd-button-renderer[2]').click()

# Click on the search bar at the top.
driver.find_element(By.XPATH, '//*[@id="search-input"]').click()

# Type in something to search for and hit the enter button.
driver.find_element(By.XPATH, '//input[@id="search"]').send_keys('Alexander Husum' + Keys.ENTER)

# Select the first video returned by the search.
driver.find_element(By.XPATH, '//ytd-video-renderer[1]').click()

# View the video for 10 seconds.
time.sleep(10)

# Close the browser window.
driver.quit()
