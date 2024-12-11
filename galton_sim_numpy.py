import numpy as np
import matplotlib.pyplot as plt
# define number of points
n = 10000
# define number of steps
h = 10
plt.hist(
    # final destination of each point(n rows/sums)
    np.sum(
        # h steps of 1s or -1s.
        # n * h matrix of 1s or -1s for n points. each point has a row(steps)
        2 * np.random.randint(0,2,n * h).reshape(n, h) - 1
        , axis=1)
    )
plt.show()