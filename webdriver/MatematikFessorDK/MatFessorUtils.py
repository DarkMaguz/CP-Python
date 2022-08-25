from multiprocessing.connection import answer_challenge
import os
import sys
import time
import atexit

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from selenium.webdriver.remote import webelement

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# # Add path to our drivers to PATH.
os.environ['PATH'] += os.pathsep + '../bin/'

# # Update Firefox and geckodriver.
# os.system('check_for_updates.sh')

# # Set option for headless.
options = Options()
# options.headless = True
options.add_argument('--incognito')

# # Create a new Chrome session.
driver = webdriver.Chrome(chrome_options=options)

# Function to close the driver and Firefox window after script has ended.
def exitHandler():
  driver.close()

# Register the exitHandler function
atexit.register(exitHandler)

# Uncomment the next line to maximize the browser window.
# driver.maximize_window()

# Give the browser time to load before each command is executed.
driver.implicitly_wait(10)

def login(email, password):
  # Go to matematikfessor.dk.
  driver.get('https://matematikfessor.dk/')
  time.sleep(1)
  # Handle the cookie wall.
  driver.find_element(By.ID, 'lm-accept-necessary').click()
  time.sleep(1)
  # Open the login form.
  driver.find_element(By.ID, 'topLoginEmailButton').click()
  time.sleep(1)
  # Find the email and password input fields.
  emailElements = driver.find_elements(By.ID, 'TopLoginEmail')
  passwordElements = driver.find_elements(By.ID, 'TopLoginPassword')
  submitElements = driver.find_elements(By.XPATH, '//div[@id="emailLoginTop"]//input[@type="submit"]')
  # Apply actions to the elements.
  actions = ActionChains(driver)
  actions.send_keys_to_element(emailElements[1], email)
  actions.send_keys_to_element(passwordElements[1], password)
  actions.move_to_element(submitElements[1])
  actions.click()
  actions.perform()
  time.sleep(3)

def chooseGrade(grade):
  # Open the dropdown menu containing lessons.
  menuLessonElement = driver.find_element(By.XPATH, '//i[@title="Lektioner"]')
  actions = ActionChains(driver)
  actions.move_to_element(menuLessonElement)
  actions.click()
  actions.pause(1)
  actions.perform()
  # Find our grade in the dropdown menu.
  gradeText = '{}. klasse'.format(grade)
  gradeXPath = '//a[contains(text(), "{}")]'.format(gradeText)
  gradeLinkElement = driver.find_element(By.XPATH, gradeXPath)
  actions.reset_actions()
  actions.move_to_element(gradeLinkElement)
  actions.click()
  actions.perform()
  time.sleep(3)

def chooseLesson(lessonNumber):
  lessonXPath = '//li[@id="lesson_{}"]/a'.format(lessonNumber)
  lessonElement = driver.find_element(By.XPATH, lessonXPath)
  actions = ActionChains(driver)
  actions.move_to_element(lessonElement)
  actions.click()
  actions.perform()
  time.sleep(3)

def startTest():
  startButtonElement = driver.find_element(By.ID, 'startTestMain')
  startButtonElement.click()
  time.sleep(1)
  readyButtonXPath = '//button[contains(text(), "Start")]'
  readyButtonElement = driver.find_elements(By.XPATH, readyButtonXPath)
  readyButtonElement[0].click()
  time.sleep(3)

def findPageNumber():
  pageIndicatorXPath = '//span[@class="question-index-indicator"]'
  pageIndicatorElement = driver.find_element(By.XPATH, pageIndicatorXPath)
  pageNumber = pageIndicatorElement.text[-3]
  print('pageNumber:', pageNumber)
  return pageNumber

def findQuestion(regression=0):
  questionXPath = "//div[@class='question-text-content']/p/span[2]"
  try:
    questionElement = driver.find_element(By.XPATH, questionXPath)
    question = questionElement.text.strip('\n').strip()
  except:
    regression += 1
    print('regression #{} of findQuestion()'.format(regression))
    if regression > 10:
      return
    return findQuestion(regression)
  return question

def findChoices(regression=0):
  choicesXPath = '//label[@class="multiple-choice-answer-label"]/p/span/span'
  try:
    WebDriverWait(driver, 10).until(
      EC.presence_of_element_located((By.XPATH, choicesXPath))
    )
  except:
    regression += 1
    print('regression #{} of findChoices()'.format(regression))
    if regression > 10:
      return
    return findChoices(regression)
  choicesElements = driver.find_elements(By.XPATH, choicesXPath)
  choices = []
  for choice in choicesElements:
    choices.append(choice.text.replace('\n', ''))
  return choices

def setAnswer(solutionNumber, regression=0):
  answersXPath = '//input[@class="multiple-choice-radio-input"]'
  try:
    WebDriverWait(driver, 10).until(
      EC.presence_of_element_located((By.XPATH, answersXPath))
    )
  except:
    regression += 1
    print('regression #{} of setAnswer()'.format(regression))
    if regression > 10:
      return
    return setAnswer(solutionNumber, regression)
  answersElements = driver.find_elements(By.XPATH, answersXPath)
  actions = ActionChains(driver)
  actions.move_to_element(answersElements[solutionNumber])
  actions.click()
  actions.perform()
  time.sleep(1)

def submitAnswer():
  submitButtonXPath = '//button[contains(text(), "Svar")]'
  submitButtonElement = driver.find_element(By.XPATH, submitButtonXPath)
  actions = ActionChains(driver)
  actions.move_to_element(submitButtonElement)
  actions.click()
  actions.perform()
  time.sleep(3)

def turnInTest(regression=0):
  submitButtonXPath = '//button[contains(text(), "Aflever")]'
  try:
    WebDriverWait(driver, 10).until(
      EC.presence_of_element_located((By.XPATH, submitButtonXPath))
    )
  except:
    regression += 1
    print('regression #{} of turnInTest()'.format(regression))
    if regression > 10:
      return
    return turnInTest(regression)
  submitButtonElement = driver.find_element(By.XPATH, submitButtonXPath)
  actions = ActionChains(driver)
  actions.move_to_element(submitButtonElement)
  actions.click()
  actions.perform()
  time.sleep(1)
  confirmButtonXPath = '//article//button[2]'
  confirmButtonElement = driver.find_element(By.XPATH, confirmButtonXPath)
  actions.reset_actions()
  actions.move_to_element(confirmButtonElement)
  actions.click()
  actions.perform()

def again():
  startButtonElement = driver.find_element(By.ID, 'recreateTestBtn')
  startButtonElement.click()
  time.sleep(1)
  readyButtonXPath = '//button[contains(text(), "Start")]'
  readyButtonElement = driver.find_elements(By.XPATH, readyButtonXPath)
  readyButtonElement[0].click()
  time.sleep(3)

# def findAnwser(solution):
#   pageNumber = findPageNumber()
#   for