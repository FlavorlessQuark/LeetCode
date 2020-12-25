bool isPalindrome(int x)
{
    long i;
    int n;
    int tmp;

    if (x < 0)
        return false;
    if (x < 10)
        return true;
    tmp = x;
    i = 0;
    while(tmp > 0)
    {

        i *= 10;
        i += tmp % 10;
        tmp /= 10;
    }
    if (x != i)
        return false;

    return true;
}
