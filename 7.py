# Program 7: Functional Data Filtering & Matrix Transformation Suite

# Input matrix
matrix = [
    [5, 2, 8],
    [7, 4, 1],
    [9, 6, 3]
]

print("Original Matrix:")
for row in matrix:
    print(row)


# 1. Matrix Transformation
# Multiply every element by 2
transformed_matrix = [
    list(map(lambda x: x * 2, row))
    for row in matrix
]

print("\nTransformed Matrix (Elements × 2):")
for row in transformed_matrix:
    print(row)


# 2. Filtering Even Numbers
even_numbers = [
    list(filter(lambda x: x % 2 == 0, row))
    for row in matrix
]

print("\nEven Numbers:")
for row in even_numbers:
    print(row)


# 3. Flatten the matrix
data = [x for row in matrix for x in row]

# 4. Sort the elements
sorted_data = sorted(data)

print("\nSorted Data:")
print(sorted_data)


# 5. Sort in descending order
descending_data = sorted(data, reverse=True)

print("\nSorted Data (Descending):")
print(descending_data)
