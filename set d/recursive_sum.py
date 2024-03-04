def recursive_sum(lst):
    if len(lst) == 0:
        return 0
    else:
        return lst[0] + recursive_sum(lst[1:])

numbers = [1, 2, 3, 4, 5]
result = recursive_sum(numbers)
print("Sum of the list:", result)
