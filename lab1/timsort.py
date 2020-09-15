from lab1.helper import generate_vector, make_plot, get_parameters, timeit
import bisect


def get_min_run(n):
    """
    We need to choose min_run so that N/min_run would be between 32 and 64
    """
    r = 0
    while n >= 64:
        r |= n & 1
        n >>= 1
    return n + r


def insertionSort(array, left, right):
    for i in range(left + 1, right + 1):
        temp = array[i]
        j = i - 1

        while array[j] > temp and j >= left:
            array[j + 1] = array[j]
            j -= 1

        array[j + 1] = temp


def merge(array, left, middle, right):
    """ Merges two sorted arrays """

    len1 = middle - left + 1
    len2 = right - middle

    left_side = array[left: left + len1]
    right_side = array[middle + 1: middle + len2 + 1]

    i = j = 0
    k = left

    while i < len1 and j < len2:
        if left_side[i] <= right_side[j]:
            array[k] = left_side[i]
            i += 1
        else:
            array[k] = right_side[j]
            j += 1

        k += 1

    while i < len1:
        array[k] = left_side[i]
        i += 1
        k += 1

    while j < len2:
        array[k] = right_side[j]
        j += 1
        k += 1


@timeit
def timsort(array, length):
    min_run = get_min_run(length)
    for i in range(0, length, min_run):
        insertionSort(array, i, min(i + 31, length - 1))

    size = min_run

    while size < length:
        left = 0

        while left < length:
            mid = min(left + size - 1, length - 1)
            right = min(left + 2 * size - 1, length - 1)

            merge(array, left, mid, right)

            left += size * 2

        size *= 2

@timeit
def builtin_timsort(array):
    sorted(array)


if __name__ == "__main__":
    max_value, step = get_parameters()
    x = [i for i in range(1, max_value, step)]
    time = []
    for vector_len in [i for i in range(1, max_value, step)]:
        vector = generate_vector(vector_len)
        time.append(timsort(vector, vector_len))
    make_plot(x, time, 'Timsort', 2)

    time = []
    for vector_len in [i for i in range(1, max_value, step)]:
        vector = generate_vector(vector_len)
        time.append(builtin_timsort(vector))
    make_plot(x, time, 'Builtin_Timsort', 2)

