import copy
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        temp = copy.deepcopy(nums)
        for i in range(len(temp)):
            if temp[i] == val:
                nums.remove(val)
        return len(nums)