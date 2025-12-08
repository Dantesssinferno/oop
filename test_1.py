from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#=============================================================BROWSER_SETUP==============================================
# инициилизируем chrome_options
chrome_options = webdriver.ChromeOptions()
# оставить окно открытым после завершения скрипта (удобно при обучении)
chrome_options.add_experimental_option('detach', True)
# chrome_options.add_argument('--headless') # запуск теста в безголовом режиме, не запуская окно браузера
# 🔑 запуск в гостевом режиме
# chrome_options.add_argument('--guest')
# 🔑 отключаем переводчик и выставляем язык
prefs = {
     "intl.accept_languages": "en,en_US"
 }
chrome_options.add_experimental_option("prefs", prefs)
chrome_options.add_argument("--lang=en")
g = Service()
# переменная драйвер в которой храним экземпляр класса webdriver
driver = webdriver.Chrome(options=chrome_options, service=g)
# переменная в которой храним URL по которому хотим ходить
base_url = "https://www.saucedemo.com/"
# При помощи метода get получаем base url и открываем его
driver.get(base_url)
# явное ожидание при помощи экземпляра класса WebDriverWait, driver ожидает до 10 секунд
wait = WebDriverWait(driver, 10)
driver.maximize_window()