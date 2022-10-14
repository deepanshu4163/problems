"""
    Given the names and grades for each student in a class of  students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

    Note: If there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line.

Example
    records = [["chi", 20.0], ["beta", 50.0], ["alpha", 50.0] ]
    The ordered list of scores is [20, 50], so the second lowest score is 50. There are two students with that score: ["beta", "alpha"]. Ordered alphabetically, the names are printed as:
    -
        alpha
        beta
"""

if __name__ == '__main__':
    name_list = []
    score_list = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
               
        name_list.append(name)
        score_list.append(score)

    #initializing 2d list
    foo = 'foo'    
    student = [[foo for i in range(2)] for j in range(len(name_list))] 

    #inserting names and score in 2d list
    for i in range(len(name_list)):
        for j in range(2):
            if j == 0:
                student[i][j] = name_list[i]
            else:
                student[i][j] = score_list[i]

    #finding lowest score
    lowest_score = min(score_list)
    new_score_list = []
    
    for i in score_list:
        if i != lowest_score:
            new_score_list.append(i)

    #finding second lowest score
    second_lowest = min(new_score_list)
    new_name_list = []

    #finding names of students who have second lowest score
    for i in range(len(name_list)):
        for j in range(2):
            if j == 1:
                if student[i][j] == second_lowest:
                    new_name_list.append(student[i][j-1])

    #printing names alphabetically
    print(sorted(new_name_list))

