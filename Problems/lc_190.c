uint32_t reverseBits(uint32_t n)
{
    uint32_t result;
    int i;

    i = 0;
    while (i < 32)
    {
        result <<= 1;
        if (n & 1)
            result |= 1;
        n >>= 1;
        i++;
    }
    return result;
}
