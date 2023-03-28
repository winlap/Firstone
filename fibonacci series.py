a = 0
b = 1
n = int(input("Enter the nth term: "))
print(f"The fibonacci series upto {n}th term is {a}\n{b}")
for i in range(2,n):
    c = a + b
    print(f"{c}")
    a = b
    b = c