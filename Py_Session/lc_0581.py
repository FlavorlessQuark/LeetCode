class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        arr = sorted(nums)
        if (arr == nums):
            return 0
        i = 0
        n = len(nums) - 1
        while (arr[i] == nums[i]):
            i +=1
        while(arr[n] == nums[n]):
            n  -=1
        return (n - i) + 1
