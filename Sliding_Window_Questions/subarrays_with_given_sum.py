#Given an array of positive integers, find the subarrays that add up to a given number
#sliding window quesiton 3

#Requirements:
#subarrays are contiguous by definition
#input length not limited
#sum provided
#all integers are positive, no negatives or zero

#Analysis:
#return ALL subarrays with given sum, this could be a long list. We may be able to use a generator expression to return each element instead of storing all of them

array = [1, 7, 4, 3, 1, 2, 1, 5, 1]
target = 7

def subarrays_with_given_sum(numbers, target_sum):
    start = 0
    end = 1
    results = []

    if not numbers:
        return None
    elif len(numbers) == 1:
        if numbers[0] != target_sum:
            return None
        else:
            return numbers
    else:
        while end < len(numbers):
            cur = array[start:end+1]
            cur_sum = sum(cur)
            if cur_sum == target_sum:
                results.append(cur)
                start += 1
                end += 1
            elif cur_sum < target_sum:
                end += 1
            elif cur_sum > target_sum:
                start += 1
    return results

print(subarrays_with_given_sum(array, target))