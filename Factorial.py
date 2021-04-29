# For any positive integer N, Z(N) is the number of zeros at the end of the decimal form of number N!. 
# For every number N, output a single line containing the single non-negative integer Z(N).


test_cases = int(input())
N = []
for i in range(test_cases) :
    x = int(input())
    N.append(x)

def findTrailingZeros(number):
    exp = 0
    base = 5
    while (number / base>= 1):
        exp += int(number / base)
        base *= 5
    return exp

result = [findTrailingZeros(i) for i in N ]

for i in result :
    print(i)


# sample test_case :
# 6
# 3
# 60
# 100
# 1024
# 23456
# 8735373

