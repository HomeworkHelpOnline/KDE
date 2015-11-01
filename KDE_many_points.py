import numpy as np
import matplotlib.pyplot as plt

#https://en.wikipedia.org/wiki/Gaussian_function
def gaussian(x,b=1):
    return np.exp(-x**2/(2*b**2))/(b*np.sqrt(2*np.pi))

#Let's take any value
X=np.random.normal(2.5, 0.9, 14)
N=len(X)
# Plot all available kernels
X_plot = np.linspace(-1, 7, 100)[:, None]
bins = np.linspace(-1, 5, 20)
bins[1]-bins[0]
fig, ax = plt.subplots(2, 3, sharex=True, figsize=(14,8))
fig.subplots_adjust(left=0.05, right=0.95, hspace=0.05, wspace=0.05)
ax[0, 0].set_ylim([0,3.1])


ax[0, 0].hist(X[:], bins=bins + 0.75, fc='#AAAAFF', normed=False)
ax[0, 0].text(0, 2.8, "Histogram, bin=0.32")

bins = np.linspace(-1, 5, 9)
bins[1]-bins[0]
ax[0, 1].hist(X[:], bins=bins + 0.75, fc='#AAAAFF', normed=True)
ax[0, 1].text(0, 0.9, "Histogram, normed, bin=0.75")

bins = np.linspace(-1, 5, 5)
bins[1]-bins[0]
ax[0, 2].hist(X[:], bins=bins + 0.75, fc='#AAAAFF', normed=True)
ax[0, 2].text(0, 0.9, "Histogram, normed, bin=1.5")

sum1=np.zeros(len(X_plot))
sum2=np.zeros(len(X_plot))
sum3=np.zeros(len(X_plot))
for i in range(0, N):
    ax[1, 0].plot(X_plot, (gaussian(X_plot-X[i]))/N, '-k', linestyle="dashed")
    sum1+=((gaussian(X_plot-X[i]))/N)[:,0]
    ax[1, 1].plot(X_plot, (gaussian(X_plot-X[i],0.6))/N, '-k', linestyle="dashed")
    sum2+=((gaussian(X_plot-X[i],0.6))/N)[:,0]
    ax[1, 2].plot(X_plot, (gaussian(X_plot-X[i],0.35))/N, '-k', linestyle="dashed")
    sum3+=((gaussian(X_plot-X[i],0.35))/N)[:,0]    
    
ax[1, 0].fill(X_plot, sum1, '-k', fc='#AAAAFF')
ax[1, 0].text(0, 0.9, "Gaussian, b=1")
ax[1, 1].fill(X_plot, sum2, '-k', fc='#AAAAFF')
ax[1, 1].text(0, 0.9, "Gaussian, b=0.6")
ax[1, 2].fill(X_plot, sum3, '-k', fc='#AAAAFF')
ax[1, 2].text(0, 0.9, "Gaussian, b=0.35")

fig.savefig("Many_Points_Example.jpg")