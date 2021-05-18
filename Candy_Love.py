"""

Sammy and Simmy love candies and frequently visit the local candy shop. Sammy and Simmy have bought N candy packs. Packet i contains Ai candies. Sammy being the elder one is happy only if she has strictly more candies than Simmy. However Simmy, the more sensible one, is happy only if the difference between their number of candies is not more than 1.

The shopkeeper, being a generous lady, agrees to help Sammy and Simmy by distributing the candies among them in a way that makes both of them happy. The shopkeeper can open the packs and distribute the candies even within a single pack to different people.

"""

# cook your dish here
def canDivide(candies):
    if sum(candies) % 2 == 0:
        return "NO"
    return "YES"
    
for _ in range(int(input())):
    no_of_packs = int(input())
    candies = list(map(int, input().split()))
    
    print(canDivide(candies))
