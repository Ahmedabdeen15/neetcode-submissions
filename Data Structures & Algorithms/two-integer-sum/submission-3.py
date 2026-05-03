class Solution:
    def twoSum(self, nums: [int], target: int) -> [int]:
        length = len(nums)
        if length == 0 : 
            return [0,0]
        for i in range(length):
            for j in range(i+1,length,1):
                if nums[i] + nums[j] == target:
                    return [i,j]
        return [0,0]