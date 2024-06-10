from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
import math

link = "http://suninjuly.github.io/get_attribute.html"

def calc(ape):
  return str(math.log(abs(12*math.sin(int(ape)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)
    tiv = browser.find_element(By.TAG_NAME, "img")
    ape = tiv.get_attribute("valuex")
    y = calc(ape)
    input1 = browser.find_element(By.TAG_NAME,"input")
    input1.send_keys(y)

    option1 = browser.find_element(By.CSS_SELECTOR, "[id='robotCheckbox']")
    option1.click()

    option2 = browser.find_element(By.CSS_SELECTOR, "[value='robots']")
    option2.click()

    button = browser.find_element(By.XPATH, "//buttton[type='submit']")
    button.click()

finally:
   
   time.sleep(10)

   browser.quit()