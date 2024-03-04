print("Choose a shape to calculate the area:")
print("1. Rectangle")
print("2. Circle")
print("3. Triangle")
print("4. Square")
choice = int(input("Enter your choice (1/2/3/4): "))

if choice == 1:
    length = float(input("Enter the length of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))
    area = length * width
    print("Area of the rectangle:", area)
elif choice == 2:
    radius = float(input("Enter the radius of the circle: "))
    area = 3.14 * radius ** 2
    print("Area of the circle:", area)
elif choice == 3:
    base = float(input("Enter the base length of the triangle: "))
    height = float(input("Enter the height of the triangle: "))
    area = 0.5 * base * height
    print("Area of the triangle:", area)
elif choice == 4:
    side = float(input("Enter the side length of the square: "))
    area = side ** 2
    print("Area of the square:", area)
else:
    print("Invalid choice!")    
