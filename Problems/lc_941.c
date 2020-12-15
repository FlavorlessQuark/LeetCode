bool validMountainArray(int* arr, int arrSize){
    int i;
    int max;

    if (arrSize < 3)
        return false;
    i = 1;
    while (i < arrSize)
    {
        if (arr[i] <= arr[i - 1])
            break ;
        i++;
    }
    if (i == arrSize || i == 1)
        return false;
    max = arr[i - 1];
    while (i < arrSize)
    {
        if (arr[i] >= arr[i - 1] || arr[i] >= max)
            return false;
        i++;
    }
    return true;
}
