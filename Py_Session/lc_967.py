class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        solutions = []
        def recurse(num, prevDigit, length):
            if (length >= n):
                solutions.append(num)
                return
            num *= 10
            for x in range(0, 10):
                if (abs(x - prevDigit) == k):
                    recurse(num + x, x, length + 1)

        for x in range(1, 10):
            recurse(x, x, 1)
        # recurse(1, 1, 1)
        # print(solutions)
        return solutions
