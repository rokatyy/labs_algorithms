import numpy as np

from sklearn.linear_model import SGDClassifier
import random
from scipy.optimize import minimize, least_squares, curve_fit, newton
from lab3.first_and_second_methods import gradient_descent, linear, rational, newtons_method
from matplotlib import pyplot as plt

eps = 1e-5
alpha = random.randint(0, 1000) / 1000
beta = random.randint(0, 1000) / 1000
s = list(np.random.normal(size=100))
X = np.array([_ / 100 for _ in range(100)])
Y = [alpha * k / 100 + beta + s[k] for k in range(100)]

popt, pcov = curve_fit(linear, X, Y)
res = newtons_method(linear, popt, X, Y)
# print(clf.coef_, clf.intercept_)
