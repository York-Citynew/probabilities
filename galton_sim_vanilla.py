from random import randint
import matplotlib.pyplot as plt
# define number of points
n = 10000
# define number of steps
s = 100
# create a distribution of points in every bucket with size n
hist = [
    # final destination of each point(sum of consecutive +1s and -1s)
    sum(
        # creating -1 or +1 for s steps
        [
            2 * randint(0,1) - 1 for step in range(s)]
        )
      for data in range(n)]
plt.hist(hist)
plt.show()

# or create a distribution of numbers in range [-s, s]. results are identical