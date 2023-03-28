def largest(arr, n):
    largestt = arr[0]
    for x in range(1, n):
        if arr[x] > largestt:
            largestt = arr[x]
    
    return largestt

arr = []
n = int(input("\nEnter the number of elements in array: "))
for x in range(n):
    arr.append(int(input(f"\nEnter the element at index {x}: ")))
large = largest(arr, n)
print(f"The largest element in the array is {large}")