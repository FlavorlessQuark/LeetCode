class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        properties.sort(key= lambda x : (x[0], -x[1]), reverse=True)
        
        defense = 0
        weak = 0
        for x in properties:
            if (x[1] < defense):
                weak += 1
            else :
                defense = x[1]
        return weak
