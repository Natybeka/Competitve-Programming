def kthLargestNumber(k, nums):
    nums.sort(key= lambda num: int(num))
    print(nums)
    if k > len(nums):
        return nums[0]
    return nums[len(nums) - k]
print(kthLargestNumber(3, ["2", "21", "12", "1"]))