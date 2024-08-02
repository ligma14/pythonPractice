def filter_matrix(matrix):
    # Initialize an empty list to store the filtered numbers
    filtered_numbers = []
    
    # Iterate through each row in the matrix
    for row in matrix:
        # Iterate through each number in the row
        for number in row:
            # Check if the number is greater than 10 and even
            if number > 10 and number % 2 == 0:
                filtered_numbers.append(number)
   
    return filtered_numbers

# Input matrix
matrix = [
    [5, 12, 18],
    [7, 11, 14],
    [3, 22, 9]
]

result = filter_matrix(matrix)
print('Результат фильтрации матрицы:', result)  # Output will be: [12, 18, 14, 22]