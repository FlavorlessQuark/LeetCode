/* Valid mountain array */

/**
 * Recall that arr is a mountain array if and only if:
 * arr.length >= 3
 * There exists some i with 0 < i < arr.length - 1 such that:
 * arr[0] < arr[1] < ... < arr[i - 1] < A[i]
 * arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
**/


bool validMountainArray(int* arr, int arrSize){
    int i;
    int max;

    if (arrSize < 3 || arr[0] >= arr[1])
        return false;
    i = 1;
    while (i < arrSize)
    {
        if (arr[i] <= arr[i - 1])
            break ;
        i++;
    }
    if (i == arrSize)
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
