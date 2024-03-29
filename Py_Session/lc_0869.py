def countNumbers(n):
    count = 1
    while n >= 10 :
        n //= 10
        count += 1
    return count

def makePowers():
    powers = {}

    # print(countNumbers(n))
    # 10^9 = 1000000000
    i = 1
    powers[1] = [['1']]
    while (i <= 1000000000):
        i <<= 1
        lst = sorted(list(str(i)))
        count = len(lst)
        if (count not in powers):
            powers[count] = []
        powers[count].append(lst)


    print(powers)


class Solution(object):
    def reorderedPowerOf2(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # makePowers()
        powers = {1: [['1'], ['2'], ['4'], ['8']], 2: [['1', '6'], ['2', '3'], ['4', '6']], 3: [['1', '2', '8'], ['2', '5', '6'], ['1', '2', '5']], 4: [['0', '1', '2', '4'], ['0', '2', '4', '8'], ['0', '4', '6', '9'], ['1', '2', '8', '9']], 5: [['1', '3', '4', '6', '8'], ['2', '3', '6', '7', '8'], ['3', '5', '5', '6', '6']], 6: [['0', '1', '1', '2', '3', '7'], ['1', '2', '2', '4', '4', '6'], ['2', '2', '4', '5', '8', '8']], 7: [['0', '1', '4', '5', '6', '7', '8'], ['0', '1', '2', '2', '5', '7', '9'], ['0', '1', '3', '4', '4', '4', '9'], ['0', '3', '6', '8', '8', '8', '8']], 8: [['1', '1', '2', '6', '6', '7', '7', '7'], ['2', '3', '3', '3', '4', '4', '5', '5'], ['0', '1', '4', '6', '6', '7', '8', '8']], 9: [['1', '1', '2', '2', '3', '4', '7', '7', '8'], ['2', '3', '4', '4', '5', '5', '6', '6', '8'], ['0', '1', '2', '3', '5', '6', '7', '8', '9']], 10: [['0', '1', '1', '2', '3', '4', '4', '7', '7', '8']]}

        number = sorted(list(str(n)))
        count = len(number)
        for x in powers[count]:
            # print(x, number)
            if all([x[i] == number[i] for i, _  in enumerate(number)]):
                return True
        return False
