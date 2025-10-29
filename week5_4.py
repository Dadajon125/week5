def find_longest_run(data):
    if not data:
        return 0
    
    longest = 1
    current = 1

    for i in range(1, len(data)):
        if data[i] == data[i - 1]:
           current += 1
    else:
        longest =max(longest, current)
        current = 1

    longest = max(longest, current)

    return longest


print(find_longest_run([1, 2, 2, 3, 3, 3, 2, 2]))
print(find_longest_run(['A', 'A', 'A', 'B', 'C', 'C']))
print(find_longest_run([5, 5, 5, 5, 5]))
print(find_longest_run([1, 2, 3, 4, 5]))
print(find_longest_run([]))
