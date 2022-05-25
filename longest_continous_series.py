"""
    Write a Python code to find the longest continuous series of small alphabetic letters in a text. 

    e.g. input:"This is just an example123 of an ExtrEmely long string". 
         output: "example"

"""


def longestContinousSeries(input_data):
    longest = ""
    output = ""
    for i in input_data:
        if i.isalpha() and i.islower():         #if letter is a lowercase alphabet, adding it to output 
            output += i             
            if len(output) > len(longest):      #comparing output string with the longest string 
                longest = output                #if output is longer than longest, then updating longest string
        elif i == "":                     #if space is found, then start again      
            output = ""
            continue
        else:                             #if digit or uppercase letter found, then start again  
            output = ""
            continue
    return longest        #returning longest string of continous small alphabetic letters

    

ans = longestContinousSeries("This is just an 1example123 of an ExtrEmely long strings")
print(ans)