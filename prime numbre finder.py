num = int(input("Enter the number: "))
 #check if the number is prime
is_prime = True

for i in range(2,num):
    if num % i ==0:
        is_prime = False
        break

#print the result
if is_prime:
    print(num," is a prime number.")
if not is_prime:
    print(num," is not a prime number")