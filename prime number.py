def prime(n):
    if n <= 1:
        return False
    for x in range(2, int(n/2)+1):
        if n % x == 0:
            return False
    return True
        
num = int(input("Enter the number: "))
isit = prime(num)
if isit:
    print("The number is prime")
else:
    print("The number is not prime")
