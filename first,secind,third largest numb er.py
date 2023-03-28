def ranking(arr, n):
    largest = arr[0]
    second_largest = arr[0]
    third_largest = arr[0]
    for i in range(1, n):

            if largest  < arr[i]:
                third_largest = second_largest
                second_largest = largest
                largest = arr[i]
            elif largest > arr[i]:
                third_largest = second_largest
                second_largest = arr[i]
            elif arr[i] > third_largest:
                third_largest = arr[i]


    print(f"The largest number is {largest},second largest is {second_largest},third larget is {third_largest}")


arr = []
n = int(input("Enter the number of terms in the array: "))
for x in range(n):
    arr.append(int(input(f"Enter the number at position {x}: ")))

ranking(arr, n)


