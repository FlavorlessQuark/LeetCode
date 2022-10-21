class Solution:
    def longestSubsequence(self, arr: List[int], diff: int) -> int:
        dic = {}
        
        for x in arr:
            if x - diff in dic:
                dic[x] = dic[x - diff] + 1
            else :
                dic[x] = 1
        return (max(dic.items(), key = lambda x : x[1]))[1]
        
        
        
