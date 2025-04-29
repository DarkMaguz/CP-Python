import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

# Create a new Firefox session.
driver = webdriver.Firefox()

# Navigate to the application home page.
driver.get('http://123mat.dk/')

multiplicationFactor = 8
numberOfExercises = 30

# Select exorcise from the header menu.
driver.find_element(By.CSS_SELECTOR, '#menu > li:nth-child(1) > a:nth-child(2)').click()
# Select the multiplication exercise.
driver.find_element(By.ID, 'MainContent_A2').click()
# Select 8 as the multiplication factor.
Select(driver.find_element(By.ID, 'MainContent_DropDownList1')).select_by_value(str(multiplicationFactor))
# Select 5 for the number of exercises.
Select(driver.find_element(By.ID, 'MainContent_DropDownList2')).select_by_value(str(numberOfExercises))

# Prepare the exercise.
driver.find_element(By.ID, 'MainContent_Button1').click()
# Start the exercise.
driver.find_element(By.ID, 'MainContent_Button2').click()

while True:
  # Get the multiplication factors.
  firstValue = driver.find_element(By.ID, 'MainContent_TextBox2').get_attribute('value')
  secondValue = driver.find_element(By.ID, 'MainContent_TextBox4').get_attribute('value')
  # Calculate the result.
  result = str(int(firstValue) * int(secondValue))
  # Set the result.
  driver.find_element(By.ID, 'MainContent_TextBox1').send_keys(result)
  # Submit the result.
  driver.find_element(By.ID, 'MainContent_Button3').click()
  # Check if the exercise is finished.
  if driver.find_element(By.ID, 'MainContent_Label9').text == str(numberOfExercises):
    break
  # Next question.
  driver.find_element(By.ID, 'MainContent_Button2').click()

testResult = driver.find_element(By.ID, 'MainContent_Label3').text

print("Exercise finished.")
print(testResult)

# Wait 2 seconds.
time.sleep(2)

# Close the browser window.
driver.quit()
