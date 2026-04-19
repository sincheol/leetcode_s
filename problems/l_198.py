class Solution:
    '''
    인접하지 않은 것 (퐁당으로 훔)

    length가 100까지 dp일수도
    
    idx 기준 / max(idx를 털거면 idx-1은 털면 안됨, idx를 안털거면 idx-1은 털었어도 됐고 안털었어도 됐음)
    결국 idx -> 최적은 max(idx값 + idx-2, idx-1)
    '''
    def rob(self, nums: List[int]) -> int:
        if len(nums)<=2:
            return max(nums)
        idx = 0
        dp = nums
        dp[1] = max(nums[0:2])

        for i in range(2,len(nums)):
            dp[i] = max(dp[i-2]+dp[i], dp[i-1])
        
        return dp[len(nums)-1]