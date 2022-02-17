def insertionSort1(n, arr):
    # Write your code here
    num = arr[n - 1]
    index = n - 2
    while (arr[index] > num):
        arr[index + 1] = arr[index]
        print(*arr)
        index -= 1
        if index == -1:
            break

    arr[index + 1] = num
    print(*arr)


insertionSort1(10, [2, 3, 4, 5, 6, 7, 8, 9, 10, 1])
