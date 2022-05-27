"""
    Write a function that takes a string and does the same thing as the strip()
    string method. If no other arguments are passed other than the string to
    strip, then whitespace characters will be removed from the beginning and
    end of the string. Otherwise, the characters specified in the second argu-
    ment to the function will be removed from the string.

"""

import re

test_str = """
    Write a function that takes a string and does the same thing as the strip()
    string method. If no other arguments are passed other than the string to
    strip, then whitespace characters will be removed from the beginning and
    end of the string. Otherwise, the characters specified in the second argu-
    ment to the function will be removed from the string.
    """

test_str2 = "           hello       world           "

test_str3 = """
        Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut 
        labore et dolore magna aliqua. Ipsum dolor sit amet consectetur adipiscing elit. Amet est 
        placerat in egestas erat. Tristique senectus et netus et malesuada fames ac. Sed sed risus 
        pretium quam vulputate. Rhoncus urna neque viverra justo.
        """


def regexStrip(input_str, split_var=""):
    if split_var == "":
        regexS = re.sub("^\s+|\s+$", "", input_str)         #regex to substitute whitespaces at start and end of the string with empty string
        return regexS
    regexS = re.sub(r'{}'.format(split_var), "", input_str, flags=re.I) #regex to substitute word in the string with empty string
    return regexS                                                       #re.escape(split_var) can also be used instead of format method    
                                                                        #flags=re.I is used to IGNORECASE        

ans = regexStrip(test_str3, "sed")       #calling our regexStrip method
print(ans)