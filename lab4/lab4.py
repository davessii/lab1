import math
import matplotlib.pyplot as plt


def func(x):
    return x**2


start = float(input('Введите начальное значение: '))
stop = float(input('Введите конечное значение: '))
step = float(input('Введите шаг: '))


x_list = []
y_list = []


x = start
while x <= stop:
    y = func(x)
    x_list.append(x)
    y_list.append(y)
    x += step


filename = 'results.txt'
with open(filename, 'w') as f:
    for i in range(len(x_list)):
        f.write(str(x_list[i]) + '\t' + str(y_list[i]) + '\n')


with open(filename, 'r') as f:
    lines = f.readlines()
    x_list = []
    y_list = []
    for line in lines:
        x, y = line.split('\t')
        x_list.append(float(x))
        y_list.append(float(y))

plt.plot(x_list, y_list)
plt.xlabel('x')
plt.ylabel('y')
plt.title('График функции y=x^2')
plt.show()

filename = 'graph.svg'
plt.savefig(filename, format='svg')