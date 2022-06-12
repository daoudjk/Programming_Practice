# max = 0
# for val1 in range(100, 1000):
#     for val2 in range(100, 1000):
#         prod = val1 * val2
#         # print(str(val1) + " " + str(val2) + " " + str(prod))
#         if "".join(reversed(str(prod))) == str(prod) and prod > max:
#             max = prod
#             # print("******************************************")
# print(max)

def c():
	max = maxI = maxJ = 0
	i = 999
	j = 990
	while (i > 100):
		j = 990
		while (j > 100):
			product = i * j
			if (product > max):
				productString = str(product)
				if (productString == productString[::-1]):
					max = product
					maxI = i
					maxJ = j
			j -= 11
		i -= 1
	return max, maxI, maxJ

print(c())