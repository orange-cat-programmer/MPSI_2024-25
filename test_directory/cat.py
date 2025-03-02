import matplotlib.pyplot as plt
import numpy as np

if __name__ == '__main__':
    fig, ax = plt.subplots()
    x = np.linspace(0,10,2000)
    y = np.sin(x*np.pi)
    ax.plot(x,y)
    plt.show()
    fig.savefig("cat_function.png")
