"""

Recently, Chef's College Examination has concluded. He was enrolled in 3 courses and he scored A,B,C in them, respectively. 
To pass the semester, he must score at least Amin,Bmin,Cmin marks in the respective subjects along with a cumulative score of at least Tmin, i.e, A+B+C≥Tmin.

Given seven integers Amin,Bmin,Cmin,Tmin,A,B,C, tell whether Chef passes the semester or not.

"""

# cook your dish here

def canPass(a_min, b_min, c_min, total_min, a, b, c):
    if a >= a_min:
        if b >= b_min:
            if c >= c_min:
                if (a+b+c) >= total_min:
                    return "YES"
    return "NO"
    
for _ in range(int(input())):
    a_min, b_min, c_min, total_min, a, b, c = map(int, input().split())
    
                    
    print(canPass(a_min, b_min, c_min, total_min, a, b, c))
