class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        arr = [nums[0]]
        l = 0
        for num in nums:
            if num > arr[-1]:
                l+=1
                arr.append(num)
            elif num < arr[-1]:
                for x in range (l + 1):
                    if ((x == 0 or arr[x -1] < num) and arr[x] > num):
                        arr[x] = num
                        break
        # print(arr, num)
        return (len(arr))
            
