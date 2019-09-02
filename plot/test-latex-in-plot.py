import numpy as np
import pylab as plt
from matplotlib import rc, rcParams
rc('text',usetex=True)
# Change all fonts to 'Computer Modern'
rc('font',**{'family':'serif','serif':['Computer Modern']})
t=np.linspace(0.0,15.0,1000)
f=1.0
signal1=np.sin(np.pi*f*t)
f=2.0
signal2=np.sin(np.pi*f*t)

plt.figure(1)
plt.plot(t,signal1,label='signal 1')
plt.plot(t,signal2,label='signal 2')
plt.title(r'different frequencies', fontsize=18)
plt.xticks(np.arange(min(t), max(t)+1, 2*np.pi))
plt.xlabel(r'time',fontsize=17)
plt.ylabel(r'signal', fontsize=17)
plt.legend(loc='upper right')
# plt.savefig('order_param_r.png')
# plt.savefig('order_param_r.eps', format='eps', dpi=1000)
plt.savefig('different_frequencies.eps', format='eps', dpi=300)
