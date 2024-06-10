from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
import os
import math
link = " http://suninjuly.github.io/alert_accept.html"

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)
    button = browser.find_element(By.TAG_NAME, "button")
    button.click()
    confirm = browser.switch_to.alert
    confirm.accept()
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)
    input1 = browser.find_element(By.TAG_NAME, "input")
    input1.send_keys(y)
    button1 = browser.find_element(By.TAG_NAME, "button")
    button1.click()
    

finally:
   
   time.sleep(10)

   browser.quit()