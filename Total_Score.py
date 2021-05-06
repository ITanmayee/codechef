"""

There are K problems in a contest with N participants. All the problems don't necessarily have the same points assigned to them - you are given an array A of integers, where Ai denotes the points assigned to the ith problem. 
If a participant solves the ith problem, they will get Ai points added to their total score. Note that there are no partial points - they can get only 0 or Ai points on the ith problem. 
For each participant i, you are also given their final verdict in each problem in the form of a binary string Si - a 1 denotes that they solved that problem, and a 0 denotes that they did not.

Your job is to find the total score of each participant.

"""


for _ in range(int(input())):
    no_of_paricipants, no_of_tests = map(int, input().split())
    points = list(map(int, input().split()))
    
    for _ in range(no_of_paricipants):
        solved = input()
        print(sum([points[i] for i in range(no_of_tests) if solved[i] == '1']))
