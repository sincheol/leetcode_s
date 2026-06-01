class Solution:
    '''
    pointer를 사용해서 하나씩
    t가 다 포함되면 그 다음부터는 
    '''
    def minWindow(self, s: str, t: str) -> str:
        from collections import defaultdict
        target = defaultdict(int)
        count = 0
        ans = float('inf'), 0, 0

        for word in t:
            target[word] += 1

        window = defaultdict(int)
        
        leftidx = 0
        for rightidx in range(len(s)):
            word = s[rightidx]
            window[word] += 1

            if (word in target) and target[word] == window[word]:
                count+=1
            while count == len(target) and leftidx<=rightidx:
                if rightidx-leftidx+1<ans[0]:
                    ans = rightidx-leftidx+1, leftidx, rightidx
                leftword = s[leftidx]
                window[leftword] -=1
                leftidx+=1
                if leftword in target and window[leftword]<target[leftword]:
                    count-=1

        if ans[0] == float('inf'):
            return ''

        return s[ans[1]:ans[2]+1]
                

        