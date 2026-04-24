class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        sp=0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[sp] = nums[i]
                sp+=1
        return sp