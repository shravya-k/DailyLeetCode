class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp=[1]*len(nums)
        if len(nums)==1 or len(nums)==0:
            return len(nums)
        for i in range(1,len(nums)):
            res=1
            for j in range(i):
                if nums[i]>nums[j]:
                    res=max(res,(dp[j])+1)
            dp[i]=res 
        return max(dp)            
        
