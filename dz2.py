# 2. Построй диаграмму рассеяния для двух наборов случайных данных, сгенерированных с помощью
# функции `numpy.random.rand`.

import numpy as np
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
random_array_x = np.random.rand(5)  # массив из 5 случайных чисел
random_array_y = np.random.rand(5)

print(random_array_x)
print()
print(random_array_y)

plt.scatter(random_array_x, random_array_y, c='green')

plt.title("Диаграмма рассеивания случайных данных")
plt.xlabel("Ось X")
plt.ylabel("Ось Y")

plt.show()
