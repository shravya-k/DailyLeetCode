class Solution:
    def rob(self, nums: List[int]) -> int:
        nums = [0] + nums
        for i in range(2, len(nums)):
            nums[i] = max(nums[i-1], nums[i-2] + nums[i])
        return nums[-1]
