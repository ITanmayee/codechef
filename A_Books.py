"""

You are given a sorted list A of size N.You have to make a new list B such that B[i] is equal to the number of elements strictly greater than A[i] in the list A.

Print the new list.

"""

def strictlyGreater(size, arr):
    no_of_elems = []
    indx = 0
    while indx < size:
        no_of_elems += [str(size - arr.count(arr[indx]) - indx)] * arr.count(arr[indx])
        indx += arr.count(arr[indx])

    return ' '.join(no_of_elems)


for _ in range(int(input())):

    size = int(input())
    arr = list(map(int, input().split()))

    print(strictlyGreater(size, arr))
