import matplotlib.pyplot as plt

def my_plot(x, y):
    plt.plot(x, y, marker="*", color="C1")
    plt.title("new plot title")
    plt.grid()
    plt.show()
