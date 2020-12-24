from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        for x in strs:
            print(x)
            s = "".join(sorted(x))
            d[s].append(x)
        return d.values()
