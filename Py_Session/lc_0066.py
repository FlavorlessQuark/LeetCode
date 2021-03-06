class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        for i in range(len(digits) -1, -1 , -1):
            if digits[i] >= 9:
                digits[i] = 0
                if i != 0:
                    digits[i - 1] += 1
                    if digits[i - 1] <= 9:
                        return digits
                else:
                    return [1] + digits
            else:
                digits[i] += 1
                return digits
        return digits
