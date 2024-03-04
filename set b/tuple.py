def tuple_elementwise_sum(tuple1, tuple2):
    if len(tuple1) != len(tuple2):
        raise ValueError("Input tuples must have the same length")
    result = tuple(tuple1[i] + tuple2[i] for i in range(len(tuple1)))
    return result
tuple1 = (7, 8, 1)
tuple2 = (6, 4, 9)
result_tuple = tuple_elementwise_sum(tuple1, tuple2)
print("Result:", result_tuple)
