import numpy as np
import matplotlib.pyplot as plt
import sys

def acc_seen(r_mat):
	acc_seen = np.zeros(r_mat.shape[0])
	for i in range(r_mat.shape[0]):
		for j in range(i+1):
			acc_seen[i] += r_mat[i, j]
		acc_seen[i] /= i+1
	return acc_seen

def acc_current(r_mat):
	acc_current = [r_mat[i, i] for i in range(r_mat.shape[0])]
	return acc_current

plt.style.use('seaborn')

icarl = np.load('Rmatrix_icarl.npy')
bic_fc = np.load('Rmatrix_bic_fc.npy')
ucir_cosine = np.load('Rmatrix_ucir_cosine.npy')

if sys.argv[1] == 'seen':
	acc_icarl = acc_seen(icarl)
	acc_bic_fc = acc_seen(bic_fc)
	acc_ucir_cosine = acc_seen(ucir_cosine)
	title = 'Accuracy on all seen tasks'
else:
	acc_icarl = acc_current(icarl)
	acc_bic_fc = acc_current(bic_fc)
	acc_ucir_cosine = acc_current(ucir_cosine)
	title = 'Accuracy on current task'

plt.plot(acc_icarl, label='icarl')
plt.plot(acc_bic_fc, label='bic_fc')
plt.plot(acc_ucir_cosine, label='ucir_cosine')
plt.plot([9], [0.926], marker='o', markersize=10, label='oracle')
plt.title(title)
plt.legend()
plt.xticks(range(10))
plt.show()

