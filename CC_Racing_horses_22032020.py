# There are N horses in the stable. The skill of the horse i is represented by an integer S[i]. The Chef needs to pick 2 horses for the race such that the difference in their skills is minimum. This way, he would be able to host a very interesting race. Your task is to help him do this and report the minimum difference that is possible between 2 horses in the race.

Input:

test_cases = int(input()) 

for i in range(test_cases) :
    n = int(input())
    arr = list(map(int , input().split(" "))) 
    arr.sort()
    diff = []
    for i in range(1 , n) :
        diff.append(arr[i] - arr[i-1])
    print(min(diff))

# input :
# 1
# 5
# 4 9 1 32 13
