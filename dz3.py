# 3. Необходимо спарсить цены на диваны с сайта divan.ru в csv файл, обработать данные, найти среднюю
# цену и вывести ее, а также сделать гистограмму цен на диваны

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import csv

# Инициализируем драйвер
driver = webdriver.Chrome()

url = 'https://www.divan.ru/kaluga/category/divany-i-kresla?types%5B%5D=1&types%5B%5D=4'

# Имя CSV-файла
file_name = "divan_prices.csv"

try:
    # Открываем страницу
    driver.get(url)

    # Даем время на загрузку страницы
    time.sleep(10)

    # Находим элементы с ценами
    price_elements = driver.find_elements(By.XPATH, '//span[@data-testid="price"]')

    # Извлекаем текст из элементов
    prices = [price.text.replace('\u00a0', '').replace('₽', '').strip() for price in price_elements if price.text]

    # Обрабатываем цены
    prices = []
    for price_element in price_elements:
        price_text = price_element.text.strip().replace('\u00a0', '').replace(' ', '').replace('руб.', '')
        try:
            price = int(price_text)
            prices.append(price)
        except ValueError:
            print(f"Ошибка обработки цены: {price_element.text}")

    # Сохраняем цены в CSV
    with open(file_name, "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Цена"])
        for price in prices:
            writer.writerow([price])

    print(f"Цены успешно сохранены в файл {file_name}")

except Exception as e:
    print("Произошла ошибка при парсинге:", e)

finally:
    # Закрываем драйвер
    driver.quit()
