def max_Num(a,b,c):
    if a>b and a>c:
        print(f"{a} is Maximum among others")
    elif b>a and b>c:
        print(f"{b} is Maximum among others")
    elif c>a and c>b:
        print(f"{c} is Maximum among others")
    else:
        print(f"{a}, {b} & {c} are may be Equal")

num1=int(input("Number 1 : "))
num2=int(input("Number 2 : "))
num3=int(input("Number 3 : "))
max_Num(num1,num2,num3)