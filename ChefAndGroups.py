"""

There are N seats in a row. You are given a string S with length N; for each valid i, the i-th character of S is '0' if the i-th seat is empty or '1' if there is someone sitting in that seat.

Two people are friends if they are sitting next to each other. Two friends are always part of the same group of friends. Can you find the total number of groups?

"""

def findGroups(seats):
    groups = 0
    for i in range(len(seats) - 1):
        if seats[i] == '1':
            if seats[i+1] == '0':
                groups += 1
                
    if seats[-1] == '1':
            groups += 1
            
    return groups

for _ in range(int(input())):
    print(findGroups(list(input())))
