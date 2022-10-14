"""
    Consider that vowels in the alphabet are a, e, i, o, u and y.
    Function score_words takes a list of lowercase words as an argument and returns a score as follows:
    The score of a single word is 2 if the word contains an even number of vowels. Otherwise, the score of this word is 1. The score for the whole list of words is the sum of scores of all words in the list.
    Debug the given function score_words such that it returns a correct score.
"""

vowels = ['a', 'e', 'i', 'o', 'u', 'y']

input_string = input("enter string:")
input_words = input_string.split()

sum = 0

for i in input_words:
    count_num = 0
    for j in i:
        if j in vowels:
            count_num = count_num + 1
        
    if count_num % 2 == 0:
        sum = sum + 2
    else:
        sum = sum + 1


print(sum)            