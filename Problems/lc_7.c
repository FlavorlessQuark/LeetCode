#include <limits.h>

int reverse(int x)
{
    long n;
    long neg;

    n = 0;
    neg = 1;
    if (x > INT_MAX || x <= INT_MIN)
        return 0;
    if (x < 0)
    {
        neg = -1;
        x *= -1;
    }
    while (x > 0)
    {
        n *= 10;
        n += x % 10;
        x /= 10;
    }
     if (n > INT_MAX || n < INT_MIN)
        return 0;

    return n * neg;
}
