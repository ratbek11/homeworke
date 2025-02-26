import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Данные из таблицы
data = {
    "t": [60]*5 + [80]*5 + [100]*5 + [120]*5 + [140]*5,
    "bi": [12.4, 13.5, 12.7, 13.4, 12.6, 12.6, 12.5, 12.1, 13.1, 12.8, 13.3, 13.1, 12.9, 12.4, 12.1, 12.5, 12.9, 12.6, 12.8, 13.0, 12.5, 12.6, 12.3, 12.9, 13.3],
    "hi": [4.1, 4.1, 4.3, 4.2, 4.1, 4.2, 4.1, 4.3, 4.3, 4.2, 4.4, 4.3, 4.2, 4.3, 4.2, 4.3, 4.2, 4.1, 4.3, 4.2, 4.3, 4.3, 4.2, 4.2, 4.5],
    "Ai": [4.9, 4.7, 4.2, 4.3, 3.7, 5.6, 5.4, 5.8, 5.9, 5.2, 4.6, 4.5, 5.6, 5.0, 4.2, 4.3, 4.0, 3.8, 3.7, 3.7, 2.2, 2.1, 2.8, 2.9, 2.4]
}
df = pd.DataFrame(data)

# Вычисление ударной вязкости KC
df["KC"] = df["Ai"] / (df["bi"] * df["hi"])

# Группировка по температуре
kc_mean = df.groupby("t")["KC"].mean()
kc_std = df.groupby("t")["KC"].std()
n = df.groupby("t")["KC"].count()

# Погрешность методом Корнфельда
delta_kc = 2 * kc_std / np.sqrt(n)

# Доверительный интервал
kc_min = kc_mean - delta_kc
kc_max = kc_mean + delta_kc

# Функция для аппроксимации (полином 2-й степени)
def model(x, a, b, c):
    return a*x**2 + b*x + c

# Найдем коэффициенты
params, _ = curve_fit(model, kc_mean.index, kc_mean.values)
a, b, c = params

# Прогноз для t = 85, 110, 145
predict_temps = [85, 110, 145]
predictions = {t: model(t, a, b, c) for t in predict_temps}

# График
plt.figure(figsize=(8,5))
t_values = np.linspace(50, 150, 100)
plt.scatter(kc_mean.index, kc_mean.values, color='red', label='Экспериментальные данные')
plt.plot(t_values, model(t_values, a, b, c), label=f'Аппроксимация: {a:.5f}x² + {b:.5f}x + {c:.5f}')
plt.xlabel('Температура, °C')
plt.ylabel('Ударная вязкость KC')
plt.legend()
plt.grid()
plt.show()

# Вывод результатов
print("Средние значения KC:")
print(kc_mean)
print("\nПогрешность Δt:")
print(delta_kc)
print("\nПрогнозируемые KC:")
print(predictions)
