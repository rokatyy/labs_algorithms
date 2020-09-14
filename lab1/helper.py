import random
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import time


def timeit(method):
    def timed(*args, **kw):
        ts = time.time()
        result = method(*args, **kw)
        te = time.time()
        return (te - ts) * 1000

    return timed


def get_parameters():
    max_value = 2000
    step = 1
    return max_value, step


def generate_vector(n, max_value=10000):
    return [random.randint(0, max_value) for _ in range(n)]


def get_approximation(x, y, d=1):
    fp, residuals, rank, sv, rcond = np.polyfit(x, y, d, full=True)
    f = np.poly1d(fp)
    return f


def make_plot(x, y, label, d=1):
    f = get_approximation(x, y, d)
    print(f)
    fig, ax = plt.subplots()
    ax.plot(x, y, label='Experiment results')
    ax.plot(x, f(x), label='Approximation')
    ax.figure.set_size_inches(24, 12)
    ax.set_xlabel('Vector length')
    ax.set_ylabel('Time, ms')
    ax.legend()
    plt.savefig(f'lab1/results/{label}.svg', format='svg')
