import random

def median_of_medians(arr, k):
    def partition(arr, pivot):
        left = [x for x in arr if x < pivot]
        right = [x for x in arr if x > pivot]
        return left, right

    def select(arr, k):
        if len(arr) <= 5:
            return sorted(arr)[k]
        
        # Divide arr into groups of 5 and find the medians
        medians = [sorted(arr[i:i+5])[len(arr[i:i+5])//2] for i in range(0, len(arr), 5)]
        
        # Recursively find the median of medians
        pivot = select(medians, len(medians)//2)
        
        left, right = partition(arr, pivot)
        if len(left) > k:
            return select(left, k)
        elif len(left) < k:
            return select(right, k - len(left) - 1)
        else:
            return pivot

    return select(arr, k)

def randomized_quickselect(arr, k):
    def partition(arr, pivot):
        left = [x for x in arr if x < pivot]
        right = [x for x in arr if x > pivot]
        return left, right

    def select(arr, k):
        if len(arr) == 1:
            return arr[0]
        
        pivot = random.choice(arr)
        left, right = partition(arr, pivot)
        
        if len(left) > k:
            return select(left, k)
        elif len(left) < k:
            return select(right, k - len(left) - 1)
        else:
            return pivot

    return select(arr, k)
