def hanoi(n,a,c,b):
    if n==0:
        return
    hanoi(n-1, a, b, c)
    print("Shift disk",n,"From",a,"To",c)
    hanoi(n-1, b, c, a)

n=int(input("Enter the number of disk: "))
print("Ideration needed: ",(pow(2, n)-1))
hanoi(n,"A", "C", "B")
