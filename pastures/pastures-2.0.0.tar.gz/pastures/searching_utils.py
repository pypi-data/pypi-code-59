import random

# Linear Search

def linear_search(data, value):
    
    output = []
    cases = 0
    indexes = []

    for i in range(len(data)):
        e = data[i]
        if e == value:
            cases += 1
            indexes.append(i)

    if cases == 0:
        cases = None
        indexes = None

    output.append(cases)
    output.append(indexes)

    return output

# Binary Search

def binary_search(data, value):
    
    low = 0
    high = len(data) - 1
    mid = 0

    while low <= high:
        mid = (high + low) // 2
    
        if data[mid] < value:
            low = mid + 1
        elif data[mid] > value:
            high = mid - 1
        else:
            return mid
            break

    return None

data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
print(binary_search(data, 19))
