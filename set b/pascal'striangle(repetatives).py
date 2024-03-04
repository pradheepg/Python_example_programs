num_rows = int(input("Enter the number of rows for Pascal's triangle: "))

triangle = []
for row_num in range(num_rows):
    row = [1]
    if triangle:
        prev_row = triangle[-1]
        row.extend(prev_row[i] + prev_row[i + 1] for i in range(len(prev_row) - 1))
        row.append(1)
    triangle.append(row)

max_width = len(' '.join(map(str, triangle[-1])))
for row in triangle:
    print(' '.join(map(str, row)).center(max_width))

