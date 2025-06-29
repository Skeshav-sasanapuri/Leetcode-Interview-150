class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        l = len(nums) - 1
        while i < l:
            if nums[i] == nums[i+1]:
                nums.pop(i)
                l -= 1
            else:
                i+=1
        return len(nums) 