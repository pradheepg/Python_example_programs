def find_max_min(lst):
    if not lst:
        return None, None  
    else:
        return max(lst), min(lst)

input_list = [int(x) for x in input("Enter a list of integers separated by commas: ").split(',')]
max_element, min_element = find_max_min(input_list)
if max_element is None or min_element is None:
    print("The list is empty.")
else:
    print("Maximum element in the list:", max_element)
    print("Minimum element in the list:", min_element)
