class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        solution = []
        def twoSum(i):
            result = []
            dp = {}
            found = set()
            for x in range(i + 1, len(nums)):
                if (nums[x] in dp and nums[x] not in found):
                    result.append([nums[i], nums[x], dp[nums[x]]])
                    found.add(nums[x])
                else :
                    dp[0 - nums[x] - nums[i]] = nums[x]
            return result

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            solution.extend(twoSum(i))
        return solution
