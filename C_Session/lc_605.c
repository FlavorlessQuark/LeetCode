bool canPlaceFlowers(int* flowerbed, int flowerbedSize, int n){
    int i;
    int count;

    i = 0;
    count = 0;

    if (n == 0)
        return true;
    while(i < flowerbedSize)
    {
        if (flowerbed[i] == 0 && (((i - 1 < 0) || flowerbed[i - 1] == 0) &&
                                  (i + 1 >= flowerbedSize || flowerbed[i + 1] == 0)))
        {
            flowerbed[i]++;
             if (++count >= n)
                return true;
       }
        i++;
    }
    return false;
}
