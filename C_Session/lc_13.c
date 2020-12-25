int count(char *s, char *find, int i, int *len)
{
    int count;

    count = 0;
    *len = ((i + 1)  % 2 == 0) ? (2) : (1);
    // printf("len %d %d\n",*len, i);
    if (s[0] != find[0])
        return 0;
    while(s = strstr(s, find))
    {
       count++;
       s += *len;
        if (s[0] != find[0])
            return count;
    }
    return count;
}

int romanToInt(char * s)
{
    int vals[13] = {1000, 900, 500, 400, 100,90, 50, 40, 10, 9, 5, 4, 1};
    char *romans[13] = {"M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"};
    int i;
    int spn;
    int len;

    i = 0;
    int num;
    num = 0;
    while (i < 13 && s[0] != '\0')
    {
        spn = count(s, romans[i], i, &len);

        num += (vals[i] * spn);
        s += len * spn;
        i++;
    }
    return num;
}
