#간단한 2차원 그래프 그리기
import matplotlib.pyplot as plt
plt.plot([10, 14, 19, 20])
plt.show()

#x값과 y값이 모두 있는 2차원 데이터
import numpy as np
x = np.arange(-4.5, 5, 0.5)
y = 2*x**2
y

[x, y]
plt.plot(x,y)
plt.show()

#하나의 그래프 창에 여러개의 데이터를 선 그래프로 표시
x = np.arange(-4.5, 5, 0.5)
y1 = 2*x**2
y2 = 5*x + 30
y3 = 4*x**2 + 30

plt.plot(x, y1)
plt.plot(x, y2)
plt.plot(x, y3)
plt.show() #한번에 여러개의 그래프를 출력

plt.plot(x, y1, x, y2, x, y3)
plt.show()

#다른 창에 그리기
plt.figure(1)
plt.plot(x, y1)
plt.figure(2)
plt.plot(x, y2)
plt.show()


import math as mt

x = 2*np.arange(4.5, 8, 0.1)
plt.semilogy(x)
plt.show()

