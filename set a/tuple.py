input_val = input("Enter a tuple of values separated by space : ")
val = tuple(map(int, input_val.split()))
sum_tup = sum(val)
tup_len = len(val)
avg     = sum_tup/tup_len
print("Average of Tuple : ",avg)