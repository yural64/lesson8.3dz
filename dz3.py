# 3. Необходимо спарсить цены на диваны с сайта divan.ru в csv файл, обработать данные, найти среднюю
# цену и вывести ее, а также сделать гистограмму цен на диваны

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import csv

# Инициализируем драйвер
driver = webdriver.Chrome()

url = 'https://www.divan.ru/kaluga/category/divany-i-kresla?types%5B%5D=1&types%5B%5D=4'

try:
    # Открываем страницу
    driver.get(url)

    # Даем время на загрузку страницы
    time.sleep(10)

    # Находим элементы с ценами
    price_elements = driver.find_elements(By.XPATH, '//span[contains(@class, "price__main-value")]')

    # Извлекаем текст из элементов
    prices = [price.text for price in price_elements]

    # Сохраняем цены в CSV
    with open("prices.csv", "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Цена"])
        for price in prices:
            writer.writerow([price])

    # Выводим цены
    for price in prices:
        print(price)

finally:
    # Закрываем драйвер
    driver.quit()
