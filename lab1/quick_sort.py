from lab1.timer import timeit
from lab1.helper import generate_vector, make_plot


@timeit
def quicksort(array):
    def quick_sort(array):
        if len(array) < 2:
            return array
        pivot = array[-1]
        left = []
        right = []
        for i in array[:-1]:
            left.append(i) if i > pivot else right.append(i)
        if len(left) > 1:
            left = quick_sort(left)
        if len(right) > 1:
            right = quick_sort(right)
        return right + [pivot] + left

    quick_sort(array)


if __name__ == "__main__":
    max_value = 1900
    k = max_value / 10
    step = 1
    x = [i for i in range(1, max_value, step)]
    time = []
    for vector_len in [i for i in range(1, max_value, step)]:
        vector = generate_vector(vector_len)
        time.append(quicksort(vector))
    make_plot(x, time, 'Quick sort', 2)
