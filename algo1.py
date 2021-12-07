# array = [3, 5, -4, 8, 11, 1, -1, 6]


def twoNumberSum(array, targetSum):
	for i in range(len(array) -1 ):
		num1 = array[i]
		for j in range(i +1, len(array)):
			num2 = array[j]
			if num1 + num2 == targetSum:
				return[num1, num2]
	return []

print(twoNumberSum([3, 5, -4, 8, 11, 1, -1, 6], 10))