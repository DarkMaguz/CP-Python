import os
import sys
import time
import pprint
import threading
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
os.environ['PATH'] += os.pathsep + '../bin/'

# Update Firefox and geckodriver.
os.system('check_for_updates.sh')

# Set option for headless.
options = Options()
options.binary_location = '../bin/firefox/firefox-bin'
options.add_argument('--private-window')
# options.add_argument('-headless')

service = Service('../bin/geckodriver')

# Create a new Firefox session.
driver = webdriver.Firefox(service=service, options=options)

# Uncomment the next line to maximize the browser window.
#driver.maximize_window()

# Give the browser time to load before each command is executed.
driver.implicitly_wait(10)

def load():
  with open('savedGame.txt', 'r') as file:
    data = file.read().strip()
    driver.execute_script("window.localStorage.setItem('CookieClickerGame', '{}');".format(data))

def save():
  data = driver.execute_script("return window.localStorage.getItem('CookieClickerGame');")
  with open('savedGame.txt', 'w') as file:
    file.write(data)

def hackCoockie():
  driver.execute_script('''
  document.getElementById('bigCookie').setAttribute('target', '_blank');
  ''')
#
# clickHackScript = ""
# with open('clickHack.js', 'r') as file:
#   clickHackScript = file.read().strip()
#
#
# def clickHack(clicks=50):
#   pass
  # threads = list()
  # for i in range(clicks):
  #   x = threading.Thread(target=driver.execute_script, args=(clickHackScript,))
  #   threads.append(x)
  #   x.start()
  # for t in threads:
  #   t.join()
