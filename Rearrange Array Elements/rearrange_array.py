import statistics
def rearrangeArray(nums):
    n = len(nums)
    median = statistics.median(nums)
    nums.sort()
    odd_indices = 1
    even_indices = 0
    ret_arr = [0] * len(nums)
    i = 0
    while (i < n):
        print(i)
        if nums[i] < median and odd_indices < n:
            ret_arr[odd_indices] = nums[i]
            odd_indices += 2
            i += 1
        elif nums[i] >= median and even_indices < n:
            ret_arr[even_indices] = nums[i]
            even_indices += 2
            i += 1
        else:
            i += 1
            
    
    return ret_arr

