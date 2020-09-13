from lab1.helper import generate_vector, make_plot, get_parameters, timeit


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
    max_value, step = get_parameters()
    x = [i for i in range(0, max_value, step)]
    time = []
    for vector_len in [i for i in range(0, max_value, step)]:
        vector = generate_vector(vector_len)
        time.append(bubble_sort(vector))
    make_plot(x, time, 'Bubble', 2)
