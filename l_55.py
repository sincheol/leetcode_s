class Solution:
    def canJump(self, nums: List[int]) -> bool:
        idx = 0
        nidx = 0
        for i in range(len(nums)):
            idx = i
            if nidx >= len(nums)-1:
                return True
            if nums[nidx] == 0 and idx == nidx:
                return False
            idx = idx+nums[idx]
            if idx>nidx:
                nidx = idx
        return False

'''
idx 0 -> n jump
1~n-1 -> jump if n안에 있으면 무시 else n을 치환
n이 len-1넘으면 True else False

if 0 stay
'''