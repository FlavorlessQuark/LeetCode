class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i1 = 0
        i2 = 0

        if not nums2:
            return

        tmp = list(nums1[:m])

        while True:

            if i2 >= n:
                for x in tmp[i1:]:
                    nums1[i1 + i2] = x
                    i1 += 1
                break
            if i1 >= m:
                for x in nums2[i2:]:
                    nums1[i1 + i2] = x
                    i2 += 1
                break
            print(nums1, tmp[i1:], nums2[i2:])
            if tmp[i1] < nums2[i2]:
                nums1[i1 + i2] = tmp[i1]
                i1 += 1
            else:
                nums1[i1 + i2] = nums2[i2]
                i2 += 1
