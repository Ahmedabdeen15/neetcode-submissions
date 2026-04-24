class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        flag = 0
        res = 0
        for i in range(len(nums)):
            if(nums[i]==1):
                flag+=1
            else:
                if(res < flag):
                    res = flag
                flag=0
        if(res < flag):
            res = flag
        return res
            