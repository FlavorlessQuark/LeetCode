#include <string.h>
#include <limits.h>

int myAtoi(char * s)
{
    int i;
    int l;
    long n;
    int sign;

    n = 0;
    s += strspn(s," \t");
    sign = 1;
    if (s[0] == '-')
    {
        s++;
        sign = -1;
    }
    else if (s[0] == '+')
        s++;
    s += strspn(s,"0");
    l = strspn(s, "0123456789");
    if (l > 10)
    {
        if (sign == -1)
            return INT_MIN;
        return INT_MAX;
    }
    i = 0;
    while (s[i] && isdigit(s[i]))
    {
        n *= 10;
        n += s[i] - 48;
        i++;

    }
    n *= sign;
    if (n > INT_MAX)
        return INT_MAX;
    if (n < INT_MIN)
        return INT_MIN;
    return n;
}
