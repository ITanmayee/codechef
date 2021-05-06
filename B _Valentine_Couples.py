"""
There are two groups, one of N boys and the other of N girls numbered from 1 to N.

You are given two arrays A and B containing N numbers each, denoting the height of boys and girls in the group. 
You have to form N couples, where each couple will consist of 1 boy and 1 girl.

Each couple has a LIKENESS VALUE, where

LIKENESS VALUE = height of girl in the couple + height of boy in that couple.
You have to form N couples in such a way that the maximum of LIKENESS VALUE of all the couples is minimum.

Note:- No boy or girl can form more than one couple.

"""

for _ in range(int(input())):
    no_of_pairs = int(input())
    boys_height = list(map(int, input().split()))
    girls_height = list(map(int, input().split()))
    
    boys_height.sort()
    girls_height.sort(reverse = True)
    
    pair_height = [boys_height[i] + girls_height[i] for i in range(no_of_pairs)]
    
    print(max(pair_height))
