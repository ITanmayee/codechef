
"""

Chef usually likes to play cricket, but now, he is bored of playing it too much, so he is trying new games with strings. Chef's friend Dustin gave him binary strings S and R, each with length N, and told him to make them identical. However, unlike Dustin, Chef does not have any superpower and Dustin lets Chef perform only operations of one type: choose any pair of integers (i,j) such that 1≤i,j≤N and swap the i-th and j-th character of S. He may perform any number of operations (including zero).

For Chef, this is much harder than cricket and he is asking for your help. Tell him whether it is possible to change the string S to the target string R only using operations of the given type.

"""

# cook your dish here
def canMakeIdentical(str1, str2):
    if (str1.count('0') == str2.count('0')) and (str1.count('1') == str2.count('1')):
        return "YES"
    return "NO"
    
for _ in range(int(input())):
    size = int(input())
    word1 = input()
    word2 = input()
    
    print(canMakeIdentical(word1, word2))
