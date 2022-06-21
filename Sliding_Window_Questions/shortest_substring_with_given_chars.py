#Given a string and n characters, find the shortest substring that contains all the desired characters.
#Sliding Window Question 5

#Requirements
#desired characters may be in any order
#String length is not limited
#desired characters may be longer than the given string
#case sensitive? assume yes

#Analysis
#window can never be shorter than the length of the desired characters
#Can not store all substrings because it would require too much memory, must track the minimum
#recursion could overflow the stack

given_string = "fa4chba4c"
desired_characters = "abcc"

def shortest_substring(the_string, letters):
    start = 0
    end = len(given_string)-1
    #this will track the number of occurances of a letter in letters once initialized. 
    #Comparing against the string decrements the counter such that a substring is only valid if all the values in counter are less than or equal to zero
    #Meaning that the substring has at least as many occurances of the letter as the letters string has
    counter = {}
    blocking = 0

    if len(letters) > len(the_string):
        return None
    
    if not the_string:
        return None

    if not letters:
        return ""

    for i in letters:
        if i not in counter:
            counter.setdefault(i, 1)
        else:
            counter[i] += 1

    for i in the_string:
        if i in letters:
            counter[i] -= 1

    for i in counter:
        if counter[i] > 0:
            return None

    while blocking < 2 or start == end:
        front = the_string[start]
        back = the_string[end]

        if front in letters:
            if counter[front] < 0:
                start += 1
                counter[front] += 1
            else:
                blocking += 1
        else:
            start += 1
        
        if back in letters:
            if counter[back] < 0:
                end -= 1
                counter[back] += 1
            else:
                blocking += 1
        else:
            end -= 1

    return the_string[start:end+1]
print(shortest_substring(given_string, desired_characters))