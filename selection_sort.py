def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr


tveri_zangvac = [43, 56, 766, 5, 0, 75, 1234]
print(selection_sort(tveri_zangvac))