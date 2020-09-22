import numpy as np
import random
from scipy.optimize import minimize, least_squares, curve_fit, newton
from lab3.first_and_second_methods import gradient_descent, linear, rational, newtons_method, conjugate_gradient_descent, \
    Levenberg_Marquardt, loss
from matplotlib import pyplot as plt

eps = 1e-5
alpha = random.randint(0, 1000) / 1000
beta = random.randint(0, 1000) / 1000
s = list(np.random.normal(size=100))
X = np.array([_ / 100 for _ in range(100)])
Y = [alpha * k / 100 + beta + s[k] for k in range(100)]
# for linear just replace all rational calls to linear

popt, pcov = curve_fit(rational, X, Y)
print('Gradient descent:')
gd_res = gradient_descent(X,Y)
print('Conjugate gradient descent')
cgd_res = conjugate_gradient_descent(popt, X, Y) # 300 calls of linear,
print('Newton method:')
newton_res = newtons_method(popt, X, Y)
print('Levenberg_Marquardt:')
res_lm = Levenberg_Marquardt(popt,X,Y)
fig, ax = plt.subplots()


ax.scatter(X, Y, color='r', label='Generated data')
ax.plot(X, [rational(x, *popt) for x in X], label='Linear')
ax.plot(X, [rational(x, *cgd_res) for x in X], label='Conjugate gradient descent')
ax.plot(X, [rational(x, *gd_res.x) for x in X], label='gradient descent')
ax.plot(X, [rational(x, *res_lm.x) for x in X], label = 'Levenberg_Marquardt')
ax.plot(X, [rational(x, *newton_res.x) for x in X], label = 'Newton')


ax.figure.set_size_inches(24, 12)
ax.legend()
plt.savefig(f'/Users/rokatyy/Desktop/masters/ALGORITHMS/labs_algorithms/lab3/Linear.svg', format='svg')
