def calculate_moving_average ( data, window_size):
    if window_size <= 0 or window_size > len(data):
        return []
    
    averages = []

    for i in range(len(data) - window_size + 1):
        window = data[i:i + window_size]
        avg = sum(window) / window_size
        averages.append (avg)


    return averages

print(calculate_moving_average([1, 2, 3, 4, 5], 2))
print(calculate_moving_average([10, 20, 30, 40, 50], 3))
print(calculate_moving_average([5, 10, 15], 5))
print(calculate_moving_average([8, 12], 1))
