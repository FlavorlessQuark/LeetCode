class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        c = Counter(words)
        
        
        c = c.most_common()
        c = sorted(c, key = lambda x: (-x[1], x[0]))
        return [x[0] for x in c[:k] ]
