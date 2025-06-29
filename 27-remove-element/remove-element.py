class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        k = len(nums)
        while i < len(nums):
            if nums[i] == val:
                nums.pop(i)
                k -= 1
            else:
                i += 1
        return k
