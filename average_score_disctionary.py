"""
    The provided code stub will read in a dictionary containing key/value pairs of 
    name:[marks] for a list of students. Print the average of the marks array for the student name 
    provided, showing 2 places after the decimal.

    Input- 
        3
        Krishna 67 68 69
        Arjun 70 98 63
        Malika 52 56 60
        Malika

    Output-
        56.00    
"""

#code stub provided
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    #getting list of the input student
    score_list = student_marks[query_name]
    sum = 0

    #finding sum of scores
    for i in score_list:
        sum += i

    #calculating average
    average_score = sum / len(score_list)

    #printing average score upto 2 decimal places
    # print(round(average_score, 2))
    print("%.2f"%average_score)