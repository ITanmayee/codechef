"""

Chef decided to find the connections with all of his friends in an unnamed social network. He calls a user of the social network his friend if there is a common substring of the string "chef" and the nickname of that user with length ≥ 2.

Given a list of users of the social network, compute the number of Chef's friends.

"""

def isFriend(name) :
    if len(name) >= 2 :
        if "ch" in name or "he" in name or "ef" in name :
            return True
    return False
    

no_of_names = int(input())
names = [input() for i in range(no_of_names)]
print(len([i for i in names if isFriend(i)]))
