from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

import math

try: 
    link = "https://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    num1 = int( browser.find_element_by_id("num1").text )
    num2 = int( browser.find_element_by_id("num2").text )

    select = Select(browser.find_element_by_id("dropdown"))
    select.select_by_value( str(num1+num2) )

    # answer_el = browser.find_element_by_id("answer")
    # answer_el.send_keys(y)

    # checkbox = browser.find_element_by_id("robotCheckbox")
    # checkbox.click()

    # rbut = browser.find_element_by_id("robotsRule")
    # rbut.click()    

    # # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
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
