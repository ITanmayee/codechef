#In Ciel's restaurant, a waiter is training. Since the waiter isn't good at arithmetic, sometimes he gives guests wrong change. Ciel gives him a simple problem. What is A-B (A minus B) ?

# Surprisingly, his answer is wrong. To be more precise, his answer has exactly one wrong digit. Can you imagine this? Can you make the same mistake in this problem? 

inp = input()
x = inp.split()
A = int(x[0])
B = int(x[1])

def make_mistake(A , B) :
    if (A - B) % 10 == 9 :
        return(A - B - 1)
    else :
        return(A - B + 1)

