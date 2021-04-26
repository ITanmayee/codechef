"""

Chef wants to order food from a food delivery app. He wishes to order once today, and buy three items costing A1,A2 and A3 rupees, respectively. He'll also order once tomorrow, when he'll buy three items costing B1,B2 and B3 rupees, respectively. There is an additional delivery charge of rupees D for each order.

He notices that there is a coupon on sale, which costs rupees C. If he buys that coupon, the delivery charges on any day, on an order of rupees 150 or more shall be waived (that is, the D rupees will not be added, if the sum of the costs of the items is ≥150).

Note that Chef is ordering the three items together on each day, so the delivery charge is charged only once each day. Also, note that it's only needed to buy the coupon once to avail the delivery fee waiver on both days.

Should Chef buy the coupon? Note that Chef shall buy the coupon only if it costs him strictly less than what it costs him without the coupon, in total.

"""

def useCoupon(day1_bill, day2_bill, delivery_cost, coupon_cost):
    
    if (day1_bill + day2_bill) < 150:
        return "NO"

    without_coupon = day1_bill + day2_bill + (2 * delivery_cost)
    with_coupon = day1_bill + day2_bill

    if day1_bill >= 150 and day2_bill >= 150:
        with_coupon += coupon_cost
    elif day1_bill >= 150 or day2_bill >= 150:
        with_coupon += coupon_cost + delivery_cost
    else:
        with_coupon += delivery_cost + delivery_cost
    
    if with_coupon >= without_coupon :
        return "NO"
    return "YES"     

for _ in range(int(input())):
    delivery_cost, coupon_cost = map(int, input().split())
    c = 0
    day1_bill = sum(map(int, input().split()))
    day2_bill = sum(map(int, input().split()))
    
    print(useCoupon(day1_bill, day2_bill, delivery_cost, coupon_cost))
