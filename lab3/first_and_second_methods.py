import numpy as np
from scipy import optimize, special
from sklearn.linear_model import SGDClassifier
from sklearn import preprocessing
import neupy
from neupy import algorithms
from autograd import grad, jacobian, hessian
from lmfit import minimize, Parameters, Parameter, report_fit
from scipy.integrate import ode

linear_c = 0
eps = 0.001

linear = lambda x, a, b: a * x + b
rational = lambda x, a, b: a / (1 + b * x)


def gradient_descent(X, Y):
    return optimize.minimize(loss, [0, 0], args=(X, Y), tol=eps, method='BFGS', options={'disp': True})


def conjugate_gradient_descent(x0, X, Y):
    res = optimize.fmin_cg(loss, (0, 0), args=(X, Y), disp=True)
    return res


def Levenberg_Marquardt(x0, X, Y):
    res = optimize.least_squares(loss, x0, method='lm', args=(X, Y),jac=jacobian(loss) )
    param = Parameters()
    param.add('a', value=float(x0[0]), min=-100, max=100)
    param.add('b', value=float(x0[1]), min=-100, max=100)
    res = minimize(special_loss, param, args=(X, Y), method='leastsq')

    return res


def newtons_method( x0, X, Y, eps=0.001):
    return optimize.minimize(loss, x0, args=(X, Y), tol=eps, method='Newton-CG',
                             jac=jacobian(loss), options={'disp': True})


def loss(x0, X, Y):
    summary = 0
    for x_i, y_i in zip(X, Y):
        summary += (rational(x_i, x0[0], x0[1]) - y_i) ** 2
    return summary



def special_loss(params, X,Y):
    a = params['a'].value
    b = params['b'].value
    summary = 0
    for x_i, y_i in zip(X, Y):
        summary += (rational(x_i, a, b) - y_i) ** 2
    return summary
