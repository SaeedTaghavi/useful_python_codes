import matplotlib.pyplot as plt;
import numpy as np;
import scipy.optimize as opt;

data = np.loadtxt("M-R.txt")

data=np.transpose(data)
# print(np.shape(data))
data.sort(axis=1)
# plt.loglog(data[0],data[1],'.')
# plt.loglog(data[0],data[1])
# plt.show()

# This is the function we are trying to fit to the data.
def funcR(M, theta, iota, kappa, lambd, mu, nu, xi, omicron, pi ):
     return (theta*M**2.5 + iota*M**6.5 + kappa*M**11.0 + lambd*M**19.0 + mu*M**19.5 )/(nu + xi*M**2.0 + omicron*M**8.5 + M**18.5 + pi*M**19.5 )

Mdata = data[0]
Rdata = data[1]
plt.plot(Mdata, Rdata, ".", label="Data");
# plt.show()
optimizedParameters, pcov = opt.curve_fit(funcR, Mdata, Rdata);
print(optimizedParameters);
plt.loglog(Mdata, funcR(Mdata, *optimizedParameters), label="fit");
plt.legend();
plt.show();

exit()


# This is the function we are trying to fit to the data.
def func(x, a, b, c):
     return a * np.exp(-b * x) + c

# Generate some data, you don't have to do this, as you already have your data
xdata = np.linspace(0, 4, 50)
y = func(xdata, 2.5, 1.3, 0.5)
y_noise = 0.2 * np.random.normal(size=xdata.size)
ydata = y + y_noise

# Plot the actual data
plt.plot(xdata, ydata, ".", label="Data");

# The actual curve fitting happens here
optimizedParameters, pcov = opt.curve_fit(func, xdata, ydata);

# Use the optimized parameters to plot the best fit
plt.plot(xdata, func(xdata, *optimizedParameters), label="fit");

# Show the graph
plt.legend();
plt.show();
