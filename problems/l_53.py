class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = nums[0]
        total = 0
        for i in range(len(nums)):
            total+=nums[i]
            if total>res:
                res = total
            if total<0:
                total = 0
        return res



'''
음수가 있으니 0을 기준으로 생각..
어차피 음수면 1개의 음수 중 가장 큰 수가 res임
0보다 클때를 기준으로 저장하다가 0보다 작아지면 무시..
누적은 많아질수록 유리!
곱셈이나 덧셈이나.
'''