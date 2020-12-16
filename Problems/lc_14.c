

char * longestCommonPrefix(char ** strs, int size)
{
    int i;
    int n;
    char c;
    bool found;

    if (size == 1)
        return strs[0];
    if (size == 0)
        return "";
    i = 0;
    while (42)
    {
        n = 0;
        if (strs[0][i] == '\0')
            break ;
        c = strs[0][i];
        found = false;
        while (n < size)
        {
            if (strs[n][i] == '\0' || strs[n][i] != c)
            {
                found = true;
                break ;
            }
            n++;
        }
        if (found == true)
            break ;
        i++;
    }
    printf("%d\n", i);
    strs[0][i] = '\0';
    return  strs[0];
}
