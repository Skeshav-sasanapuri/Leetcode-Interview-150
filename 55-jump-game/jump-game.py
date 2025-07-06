class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_reachable = 0
        l = len(nums)
        for i in range(l):
            if i > max_reachable:
                return False
            max_r = i+ nums[i]
            if max_reachable < max_r:
                max_reachable = max_r
            # max_reachable = max(i + nums[i], max_reachable)
        
        return True
