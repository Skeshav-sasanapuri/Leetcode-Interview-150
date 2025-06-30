class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 2
        for i in range(2, len(nums)):
            if not(nums[i] == nums[k-1] and nums[i] == nums[k-2]):
                nums[k] = nums[i]
                k+=1                
        return k