def max_sum_subseq_fast(items):
    iter_items = iter(items)
    try:
        temp_sum = next(iter_items)
    except StopIteration:
        temp_sum = 0
    max_sum = temp_sum
    for item in iter_items:
        temp_sum += item
        if item > temp_sum:
            temp_sum = item
        if temp_sum > max_sum:
            max_sum = temp_sum
    return max_sum if max_sum > 0 else 0
nums = [4,1,-9,2,19,4,-2]
ob1 = max_sum_subseq_fast(nums)
print(ob1)