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
bic_fc = np.load('Rmatrix_bic_fc.npy')
ucir_cosine = np.load('Rmatrix_ucir_cosine.npy')

acc_icarl = acc_curve(icarl)
acc_bic_fc = acc_curve(bic_fc)
acc_ucir_cosine = acc_curve(ucir_cosine)

plt.plot(acc_icarl, label='icarl')
plt.plot(acc_bic_fc, label='bic_fc')
plt.plot(acc_ucir_cosine, label='ucir_cosine')
plt.plot()
plt.legend()
plt.xticks(range(10))
plt.show()

