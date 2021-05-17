"""

Chef got into a fight with the evil Dr Doof. Dr Doof has decided to destroy all even numbers from the universe using his Evil-Destroy-inator. Chef has N integers with him. To stop Doof, Chef has to find an odd number which is an integer multiple of all N numbers that he has with him. Find if it is possible for Chef to prevent Dr Doof from destroying the even numbers.

Formally, given N positive integers, find if there exists an odd number which is an integer multiple of all the given N numbers. If yes, print "YES", otherwise "NO". You can print any letter in any case.

"""

def canFindMultiple(numbers):
    for i in numbers:
        if i % 2 == 0:
            return "NO"
    return "YES"
    
for _ in range(int(input())):
    no_of_numbers = int(input())
    numbers = list(map(int, input().split()))
    print(canFindMultiple(numbers))
