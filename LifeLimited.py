"""

Recently the company Life Ltd created a new logo for themselves. You are asked to test the design of the logo.

The logo is a 3 * 3 square grid with 9 cells. Each cell contains some lower case english letter. This logo will be considered good if there exist three cells in the shape of an L that contain the letter 'l' (lower case 'L') in each of them. That is, there should be a cell with 'l', its cell directly beneath it should also have 'l' and the cell to the right of the second cell should also have 'l'.

Your task is to tell whether the logo is good or not.

"""

test_cases = int(input())

for i in range(test_cases) :# cook your dish here
    logo = [input() for i in range(3)]
    
    if logo[0][0] + logo[1][:2] == "lll" or logo[0][1] + logo[1][1:] == "lll" or logo[1][0] + logo[2][:2] == "lll" or logo[1][1] + logo[2][1:] == "lll" :
        print("yes")
    else :
        print("no")
