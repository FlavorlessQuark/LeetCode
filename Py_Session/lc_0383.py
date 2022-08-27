class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        ransomNote = sorted(str(ransomNote))
        magazine = sorted(str(magazine))

        cr = Counter(ransomNote)
        cm = Counter(magazine)
        cm.subtract(cr)
        # print([cm[x] >= 0 for x in cm])
        if (all([cm[x] >= 0 for x in cm])):
            return True
        return False
