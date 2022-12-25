import numpy as np
import math as ma
q = int(input('Введите количество чисел: '))
w = [0] * q
for i in range (q):
    w[i] = int(input('Введите число: '))
print(w, '- заданный массив чисел')
y = list(set(w))
exp = 0
for j in range (len(y)):
    v = w.count(y[j])/len(w)
    print('Вероятность выпадения', y[j], 'равна', v)
    exp += (v * y[j])
print(exp, '- матаматическое ожидание')
hvalue = 0
for i in range(q):
    h = (w[i] - exp)**2
    hvalue += h
    disp = hvalue/len(w)
print(disp, '- значение дисперсии')
otkl = ma.sqrt(disp)
print(otkl, '- среднеквадратическое отклонение')
import matplotlib.pyplot as plt
x1 = []
k = 1
for j in range(len(w)):
    x1.append(k)
    k = k + 1
y1 = w
c = np.polyfit(x1, y1, 1)
ka = c[0]
kb = c[1]
x = np.linspace(0, len(w) + 1, 100)
y = ka * x + kb
plt.scatter(x1, y1)
plt.grid()
plt.plot(x, y)
plt.show()