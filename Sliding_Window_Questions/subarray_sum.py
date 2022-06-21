#find the subarrays that add up to 9
#sliding window problem 1

array = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def find_subarrays_with_sum(numbers, target):
    start = 0
    end = 0
    results = []
    while end < len(numbers):
        result = sum(numbers[start:end])
        if result == target:
            results.append(numbers[start:end])
            start += 1
            end += 1
        elif result > target:
            start += 1
        elif result < target:
            end += 1
    return results

print(find_subarrays_with_sum(array, 9))
