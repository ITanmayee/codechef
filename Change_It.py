"""

You are given a sequence A1,A2,…,AN. You want all the elements of the sequence to be equal. In order to achieve that, you may perform zero or more moves. In each move, you must choose an index i (1≤i≤N), then choose j=i−1 or j=i+1 (it is not allowed to choose j=0 or j=N+1) and change the value of Ai to Aj — in other words, you should replace the value of one element of the sequence by one of its adjacent elements.

What is the minimum number of moves you need to make in order to make all the elements of the sequence equal?

"""

def min_steps(arr):
    counts = [arr.count(i) for i in set(arr)]
    return len(arr) - max(counts)
    
for _ in range(int(input())):
    size = int(input())
    arr = list(map(int, input().split()))
    
    print(min_steps(arr))
