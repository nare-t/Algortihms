def partition(arr, left, right):
    pivot = arr[(left + right) // 2]
    i = left
    j = right

    while i <= j:
        while arr[i] < pivot:
            i += 1

        while arr[j] > pivot:
            j -= 1

        if i >= j:
            break

        arr[i], arr[j] = arr[j], arr[i]
        i += 1
        j -= 1

    return j


def quick_sort(arr):
    def _sort(left, right):
        if left < right:
            pi = partition(arr, left, right)
            _sort(left, pi)
            _sort(pi + 1, right)
    _sort(0, len(arr) - 1)
    return arr


tveri_zangvac = [4, 56, 89, 3, 0, -3, 45, -21, 2, 678]
print(quick_sort(tveri_zangvac))