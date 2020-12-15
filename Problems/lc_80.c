int removeDuplicates(int *nums,int numsSize)
{
    int i;
    int n;

    if (numsSize==0)
        return 0;

    i = 1;
    n = 1;
    while (i < numsSize)
    {
        if (i == 1 || nums[n - 2] != nums[i] ||  nums[i] != nums[i - 1])
        {
            nums[n] = nums[i];
            n++;
        }
        i++;
    }

  return n;
}
