import numpy as np
import pylab as pl
from matplotlib import rc, rcParams
rc('text',usetex=True)
# Change all fonts to 'Computer Modern'
rc('font',**{'family':'serif','serif':['Computer Modern']})

for i in range(1,5):
    name="file-"+str(i)+".txt"
    print(name)
