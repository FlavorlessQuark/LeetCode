int hammingWeight(uint32_t n)
{
    int i;
    int count;

    count = 0;
    i = 0;
    while ( i < 32)
    {
        count += (n & 1);
        n >>= 1;
        i++;
    }
    return count;
}
