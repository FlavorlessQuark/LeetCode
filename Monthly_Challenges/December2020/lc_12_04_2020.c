/* The kth Factor of n */

int kthFactor(int n, int k)
{
	int i;
	int x;

	i = 0;
	x = 1;
	while (x <= n)
	{
		if (n % x == 0)
			i++;
		if (i == k)
			return x;
		x++;
	}
	return -1;
}
