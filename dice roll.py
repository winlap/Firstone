c = input("Enter a number: ")
if c <= 1:
    flag = 0
for i in range(2,c,1):
    if c % i == 0 :
        flag = 0
    else:
        flag = 1

if flag == 0:
    print("The number " + str(c) + " is not a prime number")
else:
    print("The number " + str(c) + " is a prime number")
        