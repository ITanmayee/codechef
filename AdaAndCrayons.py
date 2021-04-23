"""

Ada has an array of N crayons, some crayons are pointing upwards and some downwards. Ada thinks that an array of crayons is beautiful if all the crayons are pointing in the same direction.

In one step you can flip any segment of consecutive crayons. After flipping a segment, all crayons pointing downwards will point upwards and visceversa

What is the minimum number of steps to make the array of crayons beautiful?

"""

# cook your dish here

test_cases = int(input())

def caryonSet(l) :
    cry = list(l)
    search = cry[0]
    for i in range(1 , len(cry)) :
        if cry[i] == search :
            cry[i] = ""
        else :
            search = cry[i]
    return ''.join(cry)

for i in range(test_cases) :
    crayons = input()
    print(min(caryonSet(crayons).count('U') , caryonSet(crayons).count('D')))

            
