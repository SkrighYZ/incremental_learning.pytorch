import numpy as np
import sys
import matplotlib.pyplot as plt


def fwt_gem(Rmatrix):
	T = Rmatrix.shape[0]
	fwt = sum([Rmatrix[i, i+1]-0.01 for i in range(T-1)]) / (T-1)
	return fwt

def intransigence_rwalk(Rmatrix):
	return 0.926 - Rmatrix[-1, -1]

def fwt_nipsw(Rmatrix):
	T = Rmatrix.shape[0]
	fwt = 0
	for i in range(T):
		fwt += sum([Rmatrix[j, i] for j in range(i)])
	fwt /= T*(T-1)/2
	return fwt


Rmat = np.load(sys.argv[1])

print('FWT-GEM: {}'.format(fwt_gem(Rmat)))
print('Intransigence: {}'.format(intransigence_rwalk(Rmat)))
print('FWT-NIPSW: {}'.format(fwt_nipsw(Rmat)))

fig, ax = plt.subplots()
min_val, max_val = 0, 9
matrix = Rmat.T

ax.matshow(matrix, cmap=plt.cm.Reds)

for i in range(10):
    for j in range(10):
        c = matrix[j,i]
        ax.text(i, j, str(c), va='center', ha='center')

plt.show()

