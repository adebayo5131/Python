#O(n) Time || O(n) space
def maxSubsetSumNoAdjacent(array):
	if not len(array):
		return 0
	elif len(array) == 1:
		return array[0]
        
	maxSum = array[:]
	maxSum[1] = max(array[0], array[1])
	
	for i in range(2,len(array)):
		maxSum[i] = max ( maxSum[i-1],maxSum[i-2]+ array[i] )
	return maxSum[-1]
		
	# second  = array[0]
	# first =  max(array[0], array[1])
	# for nums in range(2,len(array)):
	# 	currentSum = max(first, second + array[nums])
	# 	second = first
	# 	first = currentSum
	# return first

print(maxSubsetSumNoAdjacent([75,105,120,75,90,135]))