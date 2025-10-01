class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = dict()
        res = []
        for i_str in strs:
            tmp = sorted(i_str)  
            if "".join(tmp) in d.keys():
                res[d["".join(tmp)]].append(i_str)
            else:
                res.append([i_str])
                d["".join(tmp)] = len(res)-1
        
        return res