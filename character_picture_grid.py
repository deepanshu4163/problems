"""

Copy the previous grid value, and write code that uses it to print the image.


..OO.OO..
.OOOOOOO.
.OOOOOOO.
..OOOOO..
...OOO...
....O....

"""




grid = [['.','.','.','.','.','.'],
['.','O','O','.','.','.'],
['O','O','O','O','.','.'],
['O','O','O','O','O','.'],
['.','O','O','O','O','O'],
['O','O','O','O','O','.'],
['O','O','O','O','.','.'],
['.','O','O','.','.','.'],
['.','.','.','.','.','.']]


for x in range(len(grid[0])):       #get the number of coloumns
    for i in range(len(grid)):      #get the number of rows    
        print(grid[i][x], end="")   #end is used to print nothing instead of new-line character in the end of the row

    print()            #to print new-line after printing every coloumn


