# function input nums array and number of operation allowed
# output is the max frequency allowed

def maxFrequency(nums, k):
	nums.sort()
	left = 0
	total = 0
	result = 0
	for right in range(len(nums)):
		total += nums[right]
		# shrink the window until no of operation can reach right pointer
		while nums[right] * (right - left + 1) > total + k:
			total -= nums[left]
			left += 1
		result = max(result, right - left + 1)

		
	return result
	
print(maxFrequency([1,2,3,4,5], 5))