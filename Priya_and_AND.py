"""

Priya loves bitwise AND, but she hates programming. Help her solve this problem.

Given an array A of size N, let Bij denote the bitwise AND of A[i] and A[j]. You have to find the number of pairs (i,j), such that i<j and Bij=A[i]

"""

# cook your dish here
for _ in range(int(input())):
    size = int(input())
    arr = list(map(int, input().split()))
    
    count = 0
    
    for i in range(size):
        for j in range(i+1, size):
            if arr[i] & arr[j] == arr[i]:
                count += 1 
    
    print(count)
