char * convert(char * s, int rows)
{
    char    *convert;
    int     i;
    int     n;
    int     offset;
    int     diagonal;
    int     len;

    n = 0;
    offset = 0;
    len = strlen(s);

    if (len <= rows || rows <= 1)
        return s;
    convert = malloc(len);
    diagonal = rows * 2 - 2;

    while (offset < diagonal / 2)
    {
        i = 0;
        while (i < len && n < len)
        {
            if (offset == 0)
                convert[n++] = s[i];
            else
            {
                if (i + offset < len)
                    convert[n++] = s[i + offset];
                if (i + diagonal - offset < len)
                    convert[n++] = s[i + diagonal - offset];
            }
            i += diagonal;
        }
        offset++;
    }
    i = 0;
    while (i + offset < len)
    {
        convert[n] = s[i + offset];
        n++;
        i += diagonal;
    }
    memcpy(s, convert, len);
    return s;
}  
