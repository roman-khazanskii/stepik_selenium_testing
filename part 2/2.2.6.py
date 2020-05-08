from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

import math

try: 
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    x = int( browser.find_element_by_id("input_value").text )
    
    ans = math.log(abs(12*math.sin(x)))
    
    input = browser.find_element_by_id("answer")
    
    input.send_keys(str(ans))
    browser.execute_script("window.scrollBy(0, 100);")
    
    check = browser.find_element_by_id("robotCheckbox")
    browser.execute_script("window.scrollBy(0, 100);")
    check.click()
    
    radio = browser.find_element_by_id("robotsRule")
    browser.execute_script("window.scrollBy(0, 100);")
    radio.click()
    
    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    browser.execute_script("window.scrollBy(0, 100);")
    
    
    browser.execute_script("return arguments[0].scrollIntoView({block: 'center'});", button)
    #browser.execute_script('return alert("Fuck you")')
    browser.execute_script("window.scrollBy(0, 100);")
    
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    print("Complete")
    # закрываем браузер после всех манипуляций
    browser.quit()
