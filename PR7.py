from sympy import *
import numpy as np
import matplotlib.pyplot as plt

def main():
    x = np.arange(0, 5, 0.01)

    plt.subplot(3, 3, 1)
    j = Symbol('j')
    y = (j - 5) ** 2 * cos(j ** 2 - 7)
    plt.plot(x, lambdify(j, y, 'numpy')(x), 'r')
    plt.scatter(x[np.argmax(lambdify(j, y, 'numpy')(x))], lambdify(j, y, 'numpy')(x).max(), color='r')
    plt.scatter(x[np.argmin(lambdify(j, y, 'numpy')(x))], lambdify(j, y, 'numpy')(x).min(), color='r')
    #plt.scatter(np.where(y == max(y)), max(y))
    plt.title('График 1 (Функция)')

    plt.subplot(3, 3, 3)
    first_der = y.diff(j)
    print("I производная:", first_der)
    plt.plot(x, lambdify(j, first_der, 'numpy')(x), 'r')
    plt.title('График 2 (I производная)')

    plt.subplot(3, 3, 7)
    second_der = first_der.diff(j)
    print("II производная:", second_der)
    plt.plot(x, lambdify(j, second_der, 'numpy')(x), 'r')
    plt.title('График 3 (II производная)')

    x0 = 2.5
    plt.subplot(3, 3, 1)
    fx0 = (x0 - 5) ** 2 * np.cos(x0 ** 2 - 7)  #f
    f_x0 = (2 * (x0 - 5) * np.cos(x0 ** 2 - 7)) + ((x0 - 5) ** 2 * -np.sin(x0 ** 2 - 7) * 2 * x0) #f'
    yk = fx0 + f_x0*(x-x0)
    yn = fx0 - (x-x0)/f_x0
    plt.plot(x, yk, 'b', linestyle='dashed')
    plt.plot(x, yn, 'g', linestyle='dashed')

    plt.subplot(3, 3, 9)
    for x0 in range(0, 6, 2):
        fx0 = (x0 - 5) ** 2 * np.cos(x0 ** 2 - 7)  # f
        f_x0 = (2 * (x0 - 5) * np.cos(x0 ** 2 - 7)) + ((x0 - 5) ** 2 * -np.sin(x0 ** 2 - 7) * 2 * x0)  # f'
        yk = fx0 + f_x0 * (x - x0)
        plt.plot(x, yk, 'r', linestyle='dashed')
    y = (x - 5) ** 2 * np.cos(x ** 2 - 7)
    plt.plot(x, y, 'b')
    plt.title('График 4 (Касательные)')


    plt.show()
if __name__ == '__main__':
    main()