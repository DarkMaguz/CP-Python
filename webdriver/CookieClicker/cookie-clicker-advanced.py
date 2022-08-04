from cookieClickerUtils import *
# import threading

# Navigate to the application home page.
driver.get('https://orteil.dashnet.org/cookieclicker/')

load()

# Wait 2 seconds for the page to finish loading.
time.sleep(2)

# Load a script to speed up clicking.
hackCoockie()

# Accept cookies and chose English as language.
driver.find_element(By.XPATH, '/html/body/div[1]/div/a[1]').click()
driver.find_element(By.XPATH, '//div[@id="langSelect-EN"]').click()

# Wait 2 seconds for the page to finish loading.
time.sleep(3)

bigCookie = driver.find_element(By.XPATH, '//button[@id="bigCookie"]')
cookieCounter = driver.find_element(By.XPATH, '//div[@id="cookies"]')
goldenCookie = driver.find_element(By.XPATH, '//div[@id="goldenCookie"]')
shimmers = driver.find_element(By.XPATH, '//div[@id="shimmers"]')
# upgradeStore = driver.find_element(By.XPATH, '//div[@id="upgrades"]')

def cookieCount():
  text = cookieCounter.text
  # print('text:', text)
  return text

def buyUpgrades():
  upgrades = list()
  try:
    for i in range(200):
      upgrade = driver.find_element(By.XPATH, '//*[@id="upgrade{}"]'.format(i))
      upgrades.append(upgrade)
  except Exception as e:
    pass
  upgrades.reverse()
  for upgrade in upgrades:
    classes = upgrade.get_attribute("class")
    if "enabled" in classes:
      upgrade.click()
      return

def buyBuildings():
  for i in range(18, 0, -1):
    product = driver.find_element(By.XPATH, '//div[@id="product{}"]'.format(i))
    classes = product.get_attribute("class")
    if "enabled" in classes:
      product.click()
      return

def everyMinut():
  # while True:
  for i in range(5):
    time.sleep(120)
    save()
    buyUpgrades()
    buyBuildings()
    print(cookieCount())

minutThread = threading.Thread(target=everyMinut)
minutThread.start()

# for i in range(5000):
while minutThread.is_alive():
  bigCookie.click()

minutThread.join()
save()

# while True:
#   buyUpgrades()
#   time.sleep(5)

# Close the browser window.
driver.quit()
