from lab1.timer import timeit
from lab1.helper import generate_vector, make_plot


@timeit
def bubble_sort(array):
    n = len(array)
    swapped = True
    x = -1
    while swapped:
        swapped = False
        x = x + 1
        for i in range(1, n - x):
            if array[i - 1] > array[i]:
                array[i - 1], array[i] = array[i], array[i - 1]
                swapped = True


if __name__ == "__main__":
    max_value = 1900
    k = max_value / 10
    step = 1
    x = [i for i in range(0, max_value, step)]
    time = []
    for vector_len in [i for i in range(0, max_value, step)]:
        vector = generate_vector(vector_len)
        time.append(bubble_sort(vector))
    make_plot(x, time, 'Bubble', 2)
