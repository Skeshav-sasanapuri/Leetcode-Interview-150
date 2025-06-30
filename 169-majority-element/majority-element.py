class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        maj_ele = nums[0]
        count = 1
        for i in range(1, len(nums)):
            if nums[i] == maj_ele:
                count += 1
            else:
                if count > 0:
                    count -= 1
                else:
                    maj_ele = nums[i]
                    count = 1
        return maj_ele
