/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* sortArrayByParity(int* A, int ASize, int* returnSize){

    int i = 0, n = 0, l = ASize - 1;
    int *ptr;

    *returnSize = ASize;
    ptr = malloc(sizeof(int) * ASize);

    while (i < ASize)
    {
        if (A[i] % 2 == 0)
            ptr[n++] = A[i];
        else
            ptr[l--] = A[i];
        i++;
    }
    return ptr;
}
