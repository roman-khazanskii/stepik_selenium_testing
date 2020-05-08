from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

import math

try: 
    link = "https://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    # ask for a jorney
    browser.find_element_by_css_selector("button.btn").click()
    
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
        
    
    x = int( browser.find_element_by_id("input_value").text )
    
    input = browser.find_element_by_id("answer")
    input.send_keys(str( math.log(abs(12*math.sin(x))) ) )
    
    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    print("Complete")
    # закрываем браузер после всех манипуляций
    browser.quit()
