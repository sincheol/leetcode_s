class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        for _ in range(32):
            s = n&1
            res+= s
            n>>=1
        
        return res