class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        three = 0
        five = 0
        end = []
        for i in range(1, n + 1):
            s = ""
            three += 1
            five += 1
            if three == 3:
                s += "Fizz"
                three = 0
            if five == 5:
                s += "Buzz"
                five = 0
            end.append(s if s else str(i))
        return end
