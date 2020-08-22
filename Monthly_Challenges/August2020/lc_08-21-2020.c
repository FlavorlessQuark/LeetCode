/* Sort Array By Parity */
#include <stdlib.h>
#include <stdio.h>

int *sortArrayByParity(int *A, int Asize, int *returnSize)
{
	int i = 0, n = Asize - 1, l = 0;
	int *res;

	returnSize = Asize;
	res = malloc(sizeof(int) * Asize);
	while ( i < Asize)
	{
		if (A[i] % 2 == 0)
		{
			res[l++] = A[i];
		}
		else
			res[n--] = A[i];
		i++;
	}
	return res;
}

int main()
{
	int A[] = {3,1,2,4};
	int *res;
	int i = 0;
	res = sortArrayByParity(A, 4, res);
	printf("Input : ");

	while (i < 4)
	{
		printf("%d ", A[i]);
		i++;
	}
	printf("OUTPUT : ");
	i = 0;
	while (i < 4)
	{
		printf("%d ", res[i]);
		i++;
	}
	printf("\n");
	return 0;
}
