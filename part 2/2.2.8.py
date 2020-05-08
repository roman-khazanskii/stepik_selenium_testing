from selenium import webdriver
import time

import os 


try: 
    link = " http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    elem = browser.find_element_by_css_selector("[placeholder*='first name']")
    elem.send_keys("Lala")
    elem = browser.find_element_by_css_selector("[placeholder*='last name']")
    elem.send_keys("Lalasdottir")
    elem = browser.find_element_by_css_selector("[placeholder*='email']")
    elem.send_keys("lalala@lololo.com")


    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
    file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла 
    
    print(file_path)

    # находим элемент, содержащий текст
    choose_file = browser.find_element_by_css_selector("[type=file]")
    choose_file.send_keys(file_path)
    
    button = browser.find_element_by_css_selector("button.btn")
    button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()