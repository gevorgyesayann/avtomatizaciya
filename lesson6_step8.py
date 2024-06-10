from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/find_xpath_form")
    elements = browser.find_elements(By.TAG_NAME, "input")
    for element in elements:
        element.send_keys("koko")

    button = browser.find_element(By.XPATH, "//div[@class='btn']/div[3]")
    button.click()

finally:

    time.sleep(10)

    browser.quit()