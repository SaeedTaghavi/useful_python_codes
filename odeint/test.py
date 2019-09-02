import numpy as np
from scipy.integrate import odeint
import matplotlib.pylab as plt


def odesys(x, t, b, c):
    theta, omega = x
    dxdt = [omega, -b*omega - c*np.sin(theta)]
    # dxdt = [omega, - np.sin(theta)]
    return dxdt

b = 0.25
c = 5.0
x0 = [np.pi - 0.1, 0.0]
t = np.linspace(0, 100, 1001)

sol = odeint(odesys, x0, t, args=(b, c))
plt.figure(1)
plt.plot(t, sol[:, 0], 'b', label='theta(t)')
plt.plot(t, sol[:, 1], 'g', label='omega(t)')
plt.legend(loc='best')
plt.xlabel('t')
plt.grid()
plt.show()
