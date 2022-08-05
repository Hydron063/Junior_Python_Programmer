def merge_sort(array):
    if len(array) < 2:
        return array
    left = merge_sort(array[:len(array) // 2])
    right = merge_sort(array[len(array) // 2:])
    n = m = k = 0
    while n < len(left) and m < len(right):
        if left[n] <= right[m]:
            array[k] = left[n]
            n += 1
        else:
            array[k] = right[m]
            m += 1
        k += 1
    while n < len(left):
        array[k] = left[n]
        n += 1
        k += 1
    while m < len(right):
        array[k] = right[m]
        m += 1
        k += 1
    return array


def qsort(array):
    less, greater = [], []
    if len(array) > 1:
        ind = len(array) // 2
        pivot = array[ind]
        for i, x in enumerate(array):
            if x < pivot:
                less.append(x)
            elif x >= pivot and ind != i:
                greater.append(x)
        greater.append(pivot) if less else less.append(pivot)
        return qsort(less) + qsort(greater)
    else:
        return array
