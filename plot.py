import numpy as np
import matplotlib.pyplot as plt

def acc_curve(r_mat):
	acc_seen = np.zeros(r_mat.shape[0])
	for i in range(r_mat.shape[0]):
		for j in range(i+1):
			acc_seen[i] += r_mat[i, j]
		acc_seen[i] /= i+1
	return acc_seen

plt.style.use('seaborn')

icarl = np.load('Rmatrix_icarl.npy')
bic = np.load('Rmatrix_bic.npy')

acc_icarl = acc_curve(icarl)
acc_bic = acc_curve(bic)

plt.plot(acc_icarl, label='icarl')
plt.plot(acc_bic, label='bic')
plt.legend()
plt.xticks(range(10))
plt.show()

