numbers = [int(x) for x in input("Enter a list of integers separated by space: ").split()]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print("Even numbers from the list:", even_numbers)
