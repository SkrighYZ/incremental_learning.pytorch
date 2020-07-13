import numpy as np
import matplotlib.pyplot as plt
import sys
import os

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

results_folder = 'results'
icarl = np.load(os.path.join(results_folder, 'Rmatrix_icarl.npy'))
bic_fc = np.load(os.path.join(results_folder, 'Rmatrix_bic_fc.npy'))
ucir_cosine = np.load(os.path.join(results_folder, 'Rmatrix_ucir_cosine.npy'))
itaml = np.load(os.path.join(results_folder, 'Rmatrix_itaml.npy'))

if sys.argv[1] == 'seen':
	acc_icarl = acc_seen(icarl)
	acc_bic_fc = acc_seen(bic_fc)
	acc_ucir_cosine = acc_seen(ucir_cosine)
	acc_itaml = acc_seen(itaml)
	title = 'Accuracy on all seen tasks'
else:
	acc_icarl = acc_current(icarl)
	acc_bic_fc = acc_current(bic_fc)
	acc_ucir_cosine = acc_current(ucir_cosine)
	acc_itaml = acc_current(itaml)
	title = 'Accuracy on current task'

plt.plot(acc_icarl, label='icarl')
plt.plot(acc_bic_fc, label='bic')
plt.plot(acc_ucir_cosine, label='ucir')
plt.plot(acc_itaml, label='itaml')
plt.plot([9], [0.926], marker='o', markersize=10, label='oracle')
plt.title(title)
plt.legend()
plt.xticks(range(10))
plt.show()

