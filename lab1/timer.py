import time


def timeit(method):
    def timed(*args, **kwargs):
        ts = time.time()
        method(*args, **kwargs)
        te = time.time()
        return (te - ts) * 1000

    return timed
