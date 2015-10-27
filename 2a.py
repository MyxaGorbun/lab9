def f(x):
    return ((108 - 815 * (x ** (-1)) + 1500 * (x ** (-2))) - x)

import numpy as np
import matplotlib.pyplot as plt
x=np.arange(1, 6.01, 0.01)
plt.plot(x, f(x))
plt.show()