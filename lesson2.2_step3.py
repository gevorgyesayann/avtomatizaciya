from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
from selenium.webdriver.support.ui import Select    

link = " https://suninjuly.github.io/selects1.html"


try:
    browser = webdriver.Chrome()
    browser.get(link)
    x = browser.find_element(By.ID, "num1")
    num1 = x.text
    y = browser.find_element(By.ID, "num2")
    num2 = y.text
    res = int(num1) + int(num2)
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(str(res))
    

finally:
   
   time.sleep(10)

   browser.quit()