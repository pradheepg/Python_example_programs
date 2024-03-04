def floyds_triangle(rows):
    num = 1
    for i in range(1, rows + 1):
        for j in range(1, i + 1):
            print(num, end=" ")
            num += 1
        print()


rows = int(input("Enter the number of rows for Floyd's Triangle: "))
print("Floyd's Triangle:")
floyds_triangle(rows)
