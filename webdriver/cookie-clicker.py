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

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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
driver.get('https://orteil.dashnet.org/cookieclicker/')

# Wait 5 seconds for the page to finish loading.
time.sleep(5)

# Find the cookie and click it.
driver.find_element(By.XPATH, '//div[@id="bigCookie"]').click()

# Wait 5 seconds.
time.sleep(5)

# Close the browser window.
driver.quit()
