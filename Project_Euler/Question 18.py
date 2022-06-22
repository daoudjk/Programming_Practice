mystring = """75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23"""

#setup triangle
mystring = mystring.split("\n")
for i in range(len(mystring)):
    mystring[i] = mystring[i].split(' ')

#max possible value at any given point in the triangle
max_values = {}
max_values[(0, 0)] = int(mystring[0][0])

#max value seen so far
total_max = max_values[(0, 0)]

for row in range(1, len(mystring)):
    for item in range(len(mystring[row])):
        #left side of triangle, only one path option
        if item == 0:
            max_values[(
                row,
                item)] = max_values[(row - 1, item)] + int(mystring[row][item])
        #right side of triangle, only one path option
        if item == len(mystring[row]) - 1:
            max_values[(row, item)] = max_values[(row - 1, item - 1)] + int(
                mystring[row][item])
        #middle of triangle, 2 path options per item. We take the max of the two options
        if item != len(mystring[row]) - 1 and item != 0:
            max_values[(row,
                        item)] = max(max_values[(row - 1, item)], max_values[
                            (row - 1, item - 1)]) + int(mystring[row][item])
        #once the best option has been identified, compare with the total maximum seen so far
        if max_values[row, item] > total_max:
            total_max = max_values[row, item]

print(total_max)