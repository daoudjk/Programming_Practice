#Given an array of 0's and 1's, find the maximum sequence of continuous 1's that can be formed by flipping at most k 0's to 1's
#Sliding Window Question 4

#Requirements:
#Array only contains 0's and 1's
#We can convert at most K 0's into 1's

#Analysis:
#we can track the number of flips in the current subarray, and then treat the entire subarray as 1's until we run out of available flips
#keep track of the longest array so far, making sure to increment our flips available as we pop 0's from our sliding window

array = [0, 1, 0, 1, 0, 0, 0, 1, 1]
max_flips = 2

def max_subarray_with_flips(numbers, num_flips):
    result = []
    cur_flips = 0
    start = 0
    end = 1

    if len(numbers) == 0:
        return None
    
    elif len(numbers) == 1:
        if numbers[0] == 1:
            return numbers
        elif numbers[0] == 0 and num_flips > 0:
            return numbers
        else:
            return None
    else:
        if numbers[start] == 0 and cur_flips < num_flips:
            cur_flips += 1
        elif numbers[start] == 0 and cur_flips >= num_flips:
            start += 1
        while end < len(numbers):
            if numbers[end] == 0:
                cur_flips += 1
            if cur_flips > num_flips:
                while cur_flips > num_flips:
                    if numbers[start] == 0:
                        cur_flips -= 1
                    start += 1
                    if start > end:
                        end = start
            cur = numbers[start:end+1]
            if len(cur) > len(result):
                result = cur
            end += 1
    return result

print(max_subarray_with_flips(array, max_flips))