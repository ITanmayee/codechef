"""

Tomya is a girl. She loves Chef Ciel very much.

Tomya like a positive integer p, and now she wants to get a receipt of Ciel's restaurant whose total price is exactly p. The current menus of Ciel's restaurant are shown the following table.

Name of Menu	                                           price
-------------------------------------------------------------------------
eel flavored water                                         	1
deep-fried eel bones                                    	2
clear soup made with eel livers                         	4
grilled eel livers served with grated radish               	8
savory egg custard with eel                             	16
eel fried rice (S)                                      	32
eel fried rice (L)	                                        64
grilled eel wrapped in cooked egg	                        128
eel curry rice	                                            256
grilled eel over rice	                                    512
deluxe grilled eel over rice                            	1024
eel full-course	                                            2048

Note that the i-th menu has the price 2i-1 (1 ≤ i ≤ 12).

Since Tomya is a pretty girl, she cannot eat a lot. So please find the minimum number of menus whose total price is exactly p. Note that if she orders the same menu twice, then it is considered as two menus are ordered. 

"""


prices = [2 ** i for i in range(12)][::-1]

test_cases = int(input())
for i in range(test_cases):
    cost = int(input())
    menu = 0

    for i in prices:
        if cost >= i :
            deduct = cost // i
            menu += deduct
            cost -=  (i * deduct)

    print(menu)
