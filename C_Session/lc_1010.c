long long factorial(int n)
{
    return n * (n - 1) / 2;
}

int numPairsDivisibleBy60(int* time, int timeSize){
    int count;
    int mods[60] = {0};
    count = 0;

    for(int i = 0; i < timeSize; i++)
    {
        mods[time[i] % 60]++;
        count += mods[i] * mods[60 - i];
    }
    return count;
}
