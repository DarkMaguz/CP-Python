from coockieClickerUtils import *
# import os
# import time
#
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# os.environ['PATH'] += os.pathsep + 'bin/'
# driver = webdriver.Chrome()


driver.get("https://clickspeedtest.com/5-seconds.html")

driver.find_element(By.ID, 'ez-accept-all').click()
time.sleep(1)

driver.execute_script('''
document.getElementById('clicker').setAttribute('target', '_blank');
''')

print('Start clicking')
id = driver.find_element(By.ID, 'clicker')
while True: # click for ever
  try:
    id.click()
  except Exception as ex: # until it breaks
    print('Time is over')
    break

time.sleep(1) # results are slow
result = driver.find_element(By.CSS_SELECTOR, '.times')
print(f'Result: {result.text}')
driver.close()
