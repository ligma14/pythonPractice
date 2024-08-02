def filter_and_get_lengths(strings):
    # Get the lengths
    len_array = [len(s) for s in strings]
    
    # Filter out lengths < 5
    filtered_lengths = [length for length in len_array if length > 5]

    # Sort from A to Z (big to small)
    filtered_lengths.sort(reverse=True)
    
    return filtered_lengths

# Let's filter fruits[]
# 5, 6, 6, 9, 4, 9
strings = ['apple', 'banana', 'cherry', 'blueberry', 'kiwi', 'pineapple']

# Ожидаемый результат: [9, 9, 6, 6]

result = filter_and_get_lengths(strings)
print('Result:', result) 
