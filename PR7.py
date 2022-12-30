import numpy as np
import matplotlib.pyplot as plt

def main():
    x = np.arange(0, 5, 0.01)

    plt.subplot(3, 3, 1)
    y = (x - 5) ** 2 * np.cos(x ** 2 - 7)
    plt.plot(x, y, 'r')
    plt.scatter(x[np.argmax(y)], y.max(), color='r')
    plt.scatter(x[np.argmin(y)], y.min(), color='r')
    #plt.scatter(np.where(y == max(y)), max(y))
    plt.title('График 1 (Функция)')

    plt.subplot(3, 3, 3)
    y = (2*(x - 5) * np.cos(x**2 - 7)) + ((x - 5)**2 * -np.sin(x**2 - 7)*2*x)
    print("I производная: (2x-10)*cos(x^2 - 7) + ((x - 5)^2 * -2x*sin(x^2 - 7))")
    plt.plot(x, y, 'r')
    plt.title('График 2 (I производная)')

    plt.subplot(3, 3, 7)
    y = ((2 * np.cos(x ** 2 - 7) + 2*(x - 5)*-np.sin(x**2 - 7)*2*x) +
        (2*(x - 5) * -np.sin(x ** 2 - 7)*2*x + (x - 5)**2 * -np.cos(x ** 2 - 7)*2*x))
    print("II производная: (2cos(x^2 - 7) + (2x-10)*-2x*sin(x^2 -7)) +"
          "((2x-10)*-2x*sin(x^2 - 7) + (2x-10)*-2x*cos(x^2 - 7))")
    plt.plot(x, y, 'r')
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