"""

Chef Ada is preparing N dishes (numbered 1 through N). For each valid i, it takes Ci minutes to prepare the i-th dish. The dishes can be prepared in any order.

Ada has a kitchen with two identical burners. For each valid i, to prepare the i-th dish, she puts it on one of the burners and after Ci minutes, removes it from this burner; the dish may not be removed from the burner before those Ci minutes pass, because otherwise it cools down and gets spoiled. Any two dishes may be prepared simultaneously, however, no two dishes may be on the same burner at the same time. Ada may remove a dish from a burner and put another dish on the same burner at the same time.

What is the minimum time needed to prepare all dishes, i.e. reach the state where all dishes are prepared?


"""

testcases = int(input())

for i in range(testcases):

    no_of_dishes = int(input())
    time_taken = list(map(int, input().split()))
    
    if no_of_dishes == 1:
        print(sum(time_taken))
    
    else:
        arranged_time = sorted(time_taken)[::-1]
        burner1, burner2 = [arranged_time[0]], [arranged_time[1]]
    
        for i in arranged_time[2:]:
            if sum(burner1) + i <= sum(burner2) + i:
                burner1.append(i)
            else:
                burner2.append(i)
        
        print(max(sum(burner1), sum(burner2)))
