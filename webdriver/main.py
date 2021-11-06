import os
import sys
import time

from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


# Add path of the geckodriver to PATH.
os.environ["PATH"] += os.pathsep + 'bin/'

# Update Firefox and geckodriver.
os.system('check_for_updates.sh')

# Set option for headless.
options = Options()
options.binary_location = 'bin/firefox/firefox-bin'
#options.add_argument('-headless')

service = Service('bin/geckodriver')

# Create a new Firefox session.
driver = webdriver.Firefox(service=service, options=options)

def Aborting():
    print("Aborting...")
    driver.quit()
    sys.exit(1)

#driver.implicitly_wait(10)
driver.maximize_window()

# Navigate to the application home page.
driver.get("https://www.google.com")

#/html/body/div[2]/div[2]/div[3]/span/div/div/div[3]/button[2]/div
driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[3]/span/div/div/div[3]/button[2]/div").click()

time.sleep(30)

# Close the browser window.
driver.quit()
