#include <stdlib.h>
#include <stdio.h>

/* Given an array of integer, return indices of the two  numbers so that they add up to a specific target*/

int *TwoSum(int *nums, int numsSize, int target, int *returnSize)
{
	int i = 0, n;
	int *ret;

	*returnSize = 2;
	ret = malloc(sizeof(int) * 2);
	while (i < numsSize)
	{
		n = 0;
		while (n < numsSize)
		{
			if (nums[i] + nums[n] == target)
				break ;
			n++;
		}
		i++;
	}
	ret[0] = n;
	ret[1] = i;
	return ret;
}


int main()
{
	int A[] = {2,5,5,11};
	int *res;
	int s;
	int i = 0;

	res = TwoSum(A, 4, 10, &s);
	printf("Input : ");

	while (i < 4)
	{
		printf("%d ", A[i]);
		i++;
	}
	printf("OUTPUT : ");
	i = 0;
	while (i < s)
	{
		printf("%d ", res[i]);
		i++;
	}
	printf("\n");
	return 0;
}
