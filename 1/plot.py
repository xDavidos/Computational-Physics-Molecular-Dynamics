import numpy as np
import matplotlib.pyplot as plt
import sys
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
filename = sys.argv[1]

data = np.genfromtxt(dir_path + '/' + filename+'.dat', delimiter=' ')

Y = data[:,1:]
X = data[:,0]

fig = plt.figure()

ax1 = fig.add_subplot(111)

#ax1.set_title(filename)
plt.ylabel(r"$E_{pot} [\frac{eV}{Volume}]$")
plt.xlabel(r"Unit cell volume $[\AA ^3]$")

if "average" in sys.argv:
    n=Y.shape[0]
    win=n/50
    for i in range(n-win):
        Y[i,:] = np.mean(Y[i:i+win,:],axis=0)

ax1.plot(X,Y)

plt.savefig(filename+'.png')

if "show" in sys.argv:
    plt.show()
