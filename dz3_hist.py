# Построение гистограммы цен

import csv
import matplotlib.pyplot as plt
import numpy as np

# Имя CSV-файла
file_name = "divan_prices.csv"

# Список для хранения цен
prices = []

try:
    # Чтение данных из файла
    with open(file_name, "r", encoding="utf-8") as csvfile:
        reader = csv.reader(csvfile)
        header = next(reader)  # Пропускаем заголовок
        for row in reader:
            if row:  # Проверяем, что строка не пустая
                try:
                    prices.append(int(row[0]))  # Преобразуем цены в числа
                except ValueError:
                    print(f"Ошибка обработки строки: {row}")

    # Построение гистограммы
    plt.figure(figsize=(10, 6))
    plt.hist(prices, bins=20, color='blue', edgecolor='black', alpha=0.7)
    plt.title("Распределение цен на диваны")
    plt.xlabel("Цена, руб.")
    plt.ylabel("Количество")
    plt.grid(axis='y', linestyle='--', alpha=0.7)

    # Устанавливаем шаг шкалы по оси X
    max_price = max(prices) if prices else 0
    plt.xticks(np.arange(0, max_price + 10000, 10000))

    # Сохранение гистограммы как изображения (опционально)
    # plt.savefig("divan_prices_histogram.png")

    # Отображение гистограммы
    plt.show()

except Exception as e:
    print("Произошла ошибка при чтении файла или построении графика:", e)
