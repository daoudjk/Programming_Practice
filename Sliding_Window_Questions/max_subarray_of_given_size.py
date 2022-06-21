#Given an array of integers, find maximum sum subarray of required size
#sliding window problem 2

#Requirements:
#Subarrays are contiguous by definition, so the elements should be adjacent
#Input size could be very large

#Analysis:
#Input size is unlimited, so memory can blow up if we are not careful of what we are storing
#Recursion should not be used because we could overflow the stack with large inputs
#which data structure should we use? simple question, so simple data structure: Array

array = [-1, 2, 3]
subarray_size = 2

def max_sum_subarray(numbers, length):
    start = 0
    end = length - 1
    if len(numbers) < length:
        return None
    elif len(numbers) == length:
        return numbers
    else:
        result = array[start:end+1]
        max_sum = sum(array[start:end+1])
        start += 1
        end += 1
        while end < len(array):
            print(start, end)
            print(array[start:end+1])
            if sum(array[start:end+1]) > max_sum:
                result = array[start:end+1]
            start += 1
            end += 1
    return result

print(max_sum_subarray(array, subarray_size))