def sort(arr, n):
    for x in range(n):
        for i in range(x + 1, n):
            if arr[x] > arr[i]:
                temp = arr[x]
                arr[x] = arr[i]
                arr[i] = temp
    return arr

n = int(input("Enter the number of elements in the array: "))
arr = []
for x in range(n):
    arr.append(int(input(f"Enter the element at index {x}: ")))
sorted_arr = sort(arr, n)
print(f"The sorted array is: {sorted_arr}")
