from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
import os

link = " http://suninjuly.github.io/file_input.html"


with open('test1.txt', 'w') as file:
   file.write('test1 for mls 228')
try:
    browser = webdriver.Chrome()
    browser.get(link)
    name = browser.find_element(By.NAME, "firstname")
    name.send_keys("Gevorg")
    surname = browser.find_element(By.NAME, "lastname")
    surname.send_keys("Yesayan")
    email = browser.find_element(By.NAME, "email")
    email.send_keys("sitosi2000@gmail.com")
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file.txt')
    element = browser.find_element(By.ID, "file")
    element.send_keys(file_path)
finally:
   
   time.sleep(10)

   browser.quit()