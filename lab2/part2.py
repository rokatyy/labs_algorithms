import numpy as np
from scipy.optimize import minimize, least_squares, curve_fit
from sklearn import linear_model
import random
from matplotlib import pyplot as plt
from lab2.direct_methods import loss, exhaustive_search_multi

linear = lambda x, a, b: a * x + b
rational = lambda x, a, b: a / (1 + b * x)

eps = 1e-5
alpha = random.randint(0, 1000) / 1000
beta = random.randint(0, 1000) / 1000
s = list(np.random.normal(size=100))
X = [_ / 100 for _ in range(100)]
Y = [alpha * k / 100 + beta + s[k] for k in range(100)]
reg = linear_model.LinearRegression()

for method, name in zip([linear, rational], ['linear', 'rational']):
    popt, pcov = curve_fit(method, X, Y)
    popt_exh = exhaustive_search_multi(method, X, Y)
    res = minimize(loss, popt, method='nelder-mead', args=(X, Y, method),options={ 'xatol':eps, 'disp':True})
    print('{}'.format(res.x))
    nelder_a, nelder_b = res.x

    Y_nelder = [method(x, res.x[0], res.x[1]) for x in X]

    Y_r = [1 / y for y in Y]
    if name is 'rational':
        reg = linear_model.LinearRegression()
        reg.fit(np.array(X).reshape(-1, 1), Y_r)
        a = 1 / reg.intercept_
        popt_gaussf = 1 / reg.intercept_, reg.coef_ / reg.intercept_
    else:

        reg.fit(np.array(X).reshape(-1, 1), Y)
        popt_gaussf = reg.coef_, reg.intercept_
    print(
        f'Results:\n\t exhastive search: {popt_exh[0]}, {popt_exh[1]}\n\t Linear: {popt[0]},{popt[1]}\n\t Nelder-Mead:  {nelder_a},{nelder_b}\n\tGauss: {popt_gaussf[0]},{popt_gaussf[1]}\n\t')

    fig, ax = plt.subplots()

    ax.scatter(X, Y, color='g', label='Generated data')
    ax.plot(X, [method(x, *popt) for x in X], label=name)
    ax.plot(X, [method(x, *popt_exh) for x in X], label='Exhaustive approximation')
    ax.plot(X, [method(x, *popt_gaussf) for x in X], label='Gauss')
    ax.plot(X, Y_nelder, label='Nelder-mead')

    ax.figure.set_size_inches(24, 12)
    ax.legend()
    plt.savefig(f'/Users/rokatyy/Desktop/masters/ALGORITHMS/labs_algorithms/lab2/{name}.svg', format='svg')
