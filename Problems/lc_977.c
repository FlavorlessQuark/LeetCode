/**
 * Note: The returned array must be malloced, assume caller calls free().
 */

int smaller(void *a, void *b)
{
    return *(int *)a > *(int *)b;
}

int* sortedSquares(int* nums, int n, int* returnSize)
{
    int i;

    i = 0;
    *returnSize = n;
    while (i < n)
    {
        nums[i] *= nums[i];
        i++;
    }
    qsort(nums, n, sizeof(n), smaller);
    return nums;
}
