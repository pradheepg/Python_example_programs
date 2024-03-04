n = int(input("Enter a number to generate Fibonacci series up to that number: "))
a, b = 0, 1
print("Fibonacci series up to", n, ":", end=" ")
for i in range(0,n):
    print(a, end=" ")
    a, b = b, a + b
