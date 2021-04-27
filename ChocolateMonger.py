"""

There are n chocolates, and you are given an array of n numbers where the i-th number Ai is the flavour type of the i-th chocolate. Sebrina wants to eat as many different types of chocolates as possible, but she also has to save at least x number of chocolates for her little brother.

Find the maximum possible number of distinct flavour types Sebrina can have.


"""

# cook your dish here
for _ in range(int(input())):
    no_of_chocos, bro_chocos = map(int, input().split())
    chocos = list(map(int, input().split()))
    distinct = len(set(chocos))
    extra = no_of_chocos - distinct
    
    print(min(distinct, distinct - (bro_chocos - extra)))
    
