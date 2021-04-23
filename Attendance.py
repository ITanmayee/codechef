"""
Chef is teaching a cooking course. There are N students attending the course, numbered 1 through N.

Before each lesson, Chef has to take attendance, i.e. call out the names of students one by one and mark which students are present. Each student has a first name and a last name. In order to save time, Chef wants to call out only the first names of students. However, whenever there are multiple students with the same first name, Chef has to call out the full names (both first and last names) of all these students. For each student that does not share the first name with any other student, Chef may still call out only this student's first name.

Help Chef decide, for each student, whether he will call out this student's full name or only the first name.

"""

# cook your dish here
test_cases = int(input())

def get_first_name(name) :
    return name.split()[0]

for i in range(test_cases) :
    no_of_std = int(input())
    names = [input() for i in range(no_of_std)]
    first_names = [get_first_name(i) for i in names]
    for i in range(no_of_std) :
        if first_names.count(first_names[i]) > 1 :
            print(names[i])
        else :
            print(first_names[i])
        
