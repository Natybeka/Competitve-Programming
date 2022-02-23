def find_original_array(changed):
	if len(changed) % 2 != 0:
		return []	
	ret_arr = []
	changed.sort()
	
	counts = dict()
	for nums in changed:
		if nums in counts.keys():
			counts[nums] += 1
		else:
			counts[nums] = 1 

	index = len(changed) - 1

	while index > 0: 
		
		num = changed[index]
		if counts[num] == 0:
			index -= 1
		elif num % 2 != 0:
			return []
		else:
			counts[num] -= 1
			if num // 2 in counts.keys():
				counts[num // 2] -= 1
			else:
				return []
			index -= 1
			ret_arr.append(num // 2)
	if len(ret_arr) == len(changed) // 2:
		return ret_arr

	return []

print(find_original_array([1,3,4,2,6,8]))

