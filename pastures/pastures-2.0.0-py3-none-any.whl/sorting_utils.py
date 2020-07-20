import  random

# Bubble Sort (I used the pseudocode from: https://www.tutorialspoint.com/data_structures_algorithms/bubble_sort_algorithm.htm)

def is_sorted(data):
    return all(data[i] <= data[i+1] for i in range(len(data)-1))

def bubble_sort(data):
    for j in range(len(data)):
        for i in range(len(data) - 1):
            if data[i]> data[i+1]:
            
                # Courtosey of https://stackoverflow.com/questions/14836228/is-there-a-standardized-method-to-swap-two-variables-in-python
                data[i], data[i+1] = data[i+1], data[i]

    return data

# Merge Sort (Pseudocode: https://en.wikipedia.org/wiki/Merge_sort)

def merge_sort(data):
   if len(data) > 1:
        mid = len(data) // 2
        left = data[:mid]
        right = data[mid:]

        merge_sort(left)
        merge_sort(right)

        i = 0
        j = 0
        
        k = 0
        
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
              data[k] = left[i]
              i += 1
            else:
                data[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            data[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            data[k]=right[j]
            j += 1
            k += 1
    
        return data
 
data = [1, 2, 3, 4, 5, 6, 6, 8]
random.shuffle(data)
print(merge_sort(data))
