#Kadane's Algo.
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        s=0
        ans=0
        for i in range(len(nums)):
            s+=nums[i]
            if s<0:
                s=0
            else:
                ans=max(ans,s)
        return max(nums) if len(nums)>=1 and ans==0 else ans
        
        
        
                
        
        
