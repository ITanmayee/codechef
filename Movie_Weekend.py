"""

Little Egor is a huge movie fan. He likes watching different kinds of movies: from drama movies to comedy movies, from teen movies to horror movies. 
He is planning to visit cinema this weekend, but he's not sure which movie he should watch.

There are n movies to watch during this weekend. Each movie can be characterized by two integers Li and Ri, denoting the length and the rating of the corresponding movie. 
Egor wants to watch exactly one movie with the maximal value of Li × Ri. If there are several such movies, he would pick a one with the maximal Ri among them. 
If there is still a tie, he would pick the one with the minimal index among them.

Your task is to help Egor to pick a movie to watch during this weekend.

"""


for _ in range(int(input())):
    no_of_movies = int(input())
    length = list(map(int, input().split()))
    rate = list(map(int, input().split()))
    
    lr_rate_indx = [(length[i] * rate[i], rate[i], i+1) for i in range(no_of_movies)]
    arrange_lr = sorted(lr_rate_indx, key = lambda lr_r_i: lr_r_i[0], reverse = True)
    #print(arrange_lr)
    
    arrange_rate = sorted([i for i in arrange_lr if i[0] == arrange_lr[0][0]], key = lambda lr_r_i: lr_r_i[1], reverse = True)
    
    #print(arrange_rate)
    
    arrange_indx = sorted([i for i in arrange_rate if i[1] == arrange_rate[0][1]], key = lambda lr_r_i: lr_r_i[2])
    
    print(arrange_indx[0][2])
    
