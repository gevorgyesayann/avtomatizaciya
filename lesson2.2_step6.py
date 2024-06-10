from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time 
from selenium.webdriver.support.ui import Select    

link = " https://SunInJuly.github.io/execute_script.html"


def calc(num1):
  return str(math.log(abs(12*math.sin(int(num1)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)
    x = browser.find_element(By.ID, "input_value")
    num1 = x.text
    num2 = calc(num1)
    print(num2)
    "return arguments[0].scrollIntoView(true);"
    input1 = browser.find_element(By.TAG_NAME, "input")
    input1.send_keys(num2)
    option1 = browser.find_element(By.CSS_SELECTOR, "[id='robotCheckbox']")
    option1.click()

    option2 = browser.find_element(By.CSS_SELECTOR, "[value='robots']")
    option2.click()

    

finally:
   
   time.sleep(5)

   browser.quit()