"""
Say you have a list value like this:

    spam = ['apples', 'bananas', 'tofu', 'cats']
    
Write a function that takes a list value as an argument and returns
a string with all the items separated by a comma and a space, with and
inserted before the last item. For example, passing the previous spam list to
the function would return 'apples, bananas, tofu, and cats' . But your func-
tion should be able to work with any list value passed to it.
"""




spam = ['apples', 'bananas', 'tofu', 'cats', 'mangoes']


def print_list(spam):
    spam_list = ""
    for i in range(len(spam)):

        if spam[-1] == spam[i]:
            spam_list = spam_list + " and " + spam[i]
            break

        spam_list = spam_list + spam[i] + ", "

    print(spam_list)

print_list(spam)