def string_lengths(t):
    return tuple(len(s) for s in t)

input_tuple = ("apple", "banana", "orange", "kiwi")
output_tuple = string_lengths(input_tuple)
print("Lengths of strings in the input tuple:", output_tuple)
