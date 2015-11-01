import numpy as np
import matplotlib.pyplot as plt

#https://en.wikipedia.org/wiki/Gaussian_function
def gaussian(x,b=1):
    return np.exp(-x**2/(2*b**2))/(b*np.sqrt(2*np.pi))

#Let's take any value
X=np.array([2.2])

# Plot all available kernels
X_plot = np.linspace(-1, 6, 100)[:, None]
bins = np.linspace(-1, 5, 20)
bins[1]-bins[0]
fig, ax = plt.subplots(2, 3, sharex=True, sharey=True, figsize=(14,8))
fig.subplots_adjust(left=0.05, right=0.95, hspace=0.05, wspace=0.05)

ax[0, 0].hist(X[:], bins=bins + 0.75, fc='#AAAAFF', normed=False)
ax[0, 0].text(0, 1.25, "Histogram, bin=0.32")

bins = np.linspace(-1, 5, 9)
bins[1]-bins[0]
ax[0, 1].hist(X[:], bins=bins + 0.75, fc='#AAAAFF', normed=True)
ax[0, 1].text(0, 1.25, "Histogram, normed, bin=0.75")

bins = np.linspace(-1, 5, 5)
bins[1]-bins[0]
ax[0, 2].hist(X[:], bins=bins + 0.75, fc='#AAAAFF', normed=True)
ax[0, 2].text(0, 1.25, "Histogram, normed, bin=1.5")

ax[1, 0].fill(X_plot, gaussian(X_plot-X[0]), '-k', fc='#AAAAFF')
ax[1, 0].text(0, 1.25, "Gaussian, middle on X=2.2, b=1")

ax[1, 1].fill(X_plot, gaussian(X_plot-X[0],0.6), '-k', fc='#AAAAFF')
ax[1, 1].text(0, 1.25, "Gaussian, middle on X=2.2, b=0.6")

ax[1, 2].fill(X_plot, gaussian(X_plot-X[0],0.35), '-k', fc='#AAAAFF')
ax[1, 2].text(0, 1.25, "Gaussian, middle on X=2.2, b=0.35")

fig.savefig("One_Point_Example.jpg")