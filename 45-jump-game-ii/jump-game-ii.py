class Solution:
    def jump(self, nums: List[int]) -> int:
        farthest = 0
        current_max = 0
        jumps = 0
        length = len(nums)
        for i in range(length-1):
            farthest = max(farthest, i + nums[i])

            if i == current_max:
                jumps += 1
                current_max = farthest
        return jumps