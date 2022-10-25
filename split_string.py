"""
    INPUT- 
        ABCDEFGHIJKLIMNOQRSTUVWXYZ
        4
    OUTPUT-
        ABCD
        EFGH
        IJKL
        IMNO
        QRST
        UVWX
        YZ    
"""

def wrap(string, max_width):
    list_str = []
    for i in range(0, len(string), max_width):
        list_str.append(string[i : i + max_width])
    return list_str
    
    #OR
    #import textwrap
    # wrapped = textwrap.wrap(string, width=max_width)
    # return "\n".join(wrapped)

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)

    