import numpy as np
from scipy.optimize import minimize, curve_fit, leastsq, dual_annealing, differential_evolution, basinhopping, least_squares
from matplotlib import pyplot as plt

f = lambda x: 1 / (x * x - 3 * x + 2)
Function = lambda x, a, b, c=1, d=1: (a * x + b) / (x * x + c * x + d)


def generate_data(k=10 ** 3):
    X = [3 * _ / k for _ in range(k)]
    s = list(np.random.normal(size=k))
    Y = []
    for i in range(k):
        f_val = f(X[i])
        if f_val < -100:
            Y.append(-100 + s[i])
        elif f_val > 100:
            Y.append(100 + s[i])
        else:
            Y.append(f_val + s[i])
    return X, Y


X, Y = generate_data()


def loss(params):
    summary = 0
    for x_i, y_i in zip(X, Y):
        summary += (Function(x_i, *params) - y_i) ** 2
    return summary


def fitfunc(p):
    """This is the equation"""
    return loss(p)


def errfunc(p, y):
    return y - fitfunc(p)


popt, pcov = curve_fit(Function, X, Y, maxfev=1000)

nm_res = minimize(loss, popt, method='nelder-mead', options={'disp': True})
print('nm', nm_res)
#res_lm = least_squares(errfunc, popt, args=([Y]), method='lm')
#print('lm', res_lm)
res_lm_1 = leastsq(errfunc, popt, args=(Y))
print('lm1', res_lm_1)
#res_bh = basinhopping(loss, popt)
#print('bh', res_bh)
bounds = [(-2,2), (-2, 2), (-2, 2), (-2, 2)]
res_de = differential_evolution(loss,bounds, tol=0.0001)
print('de', res_de)
res_da = dual_annealing(loss, bounds)
print('da', res_da)
fig, ax = plt.subplots()

ax.scatter(X, Y, color='r', label='Generated data')
ax.plot(X, [Function(x, *nm_res.x) for x in X], label='Nelder-Mead')
ax.plot(X, [Function(x, *res_lm_1[0]) for x in X], label='Levenberg Marquardt')
#ax.plot(X, [Function(x, *res_bh.x) for x in X], label='Basinhopping')
ax.plot(X, [Function(x, *res_de.x) for x in X], label='Differential Evolution')
ax.plot(X, [Function(x, *res_da.x) for x in X], label='Annealing')

ax.figure.set_size_inches(24, 12)
ax.legend()
plt.savefig(f'/Users/rokatyy/Desktop/masters/ALGORITHMS/labs_algorithms/lab4/plotr.svg', format='svg')
