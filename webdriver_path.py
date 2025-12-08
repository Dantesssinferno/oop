from selenium import webdriver
from selenium.webdriver.chrome.service import Service

chrome_options = webdriver.ChromeOptions()
service = Service()  # без указания пути

driver = webdriver.Chrome(options=chrome_options, service=service)

print("Путь к драйверу:", service.path)