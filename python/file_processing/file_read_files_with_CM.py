try:
    with open('test.txt', 'r') as f:
        contents = f.read()
except FileNotFoundError:
    print("Wrong File or File Path!")
else:
    print(contents)
    print(type(contents))
"""
out:
1] This is a test file with
2] multiple lines of data.
3] Thrid Line
4] Fourth Line
5] Fifth Line
"""
"""
- Above piece of code is fine when we have small content in file
- When we have more content in file and we don't want  to load all the contents into the 
  memory, then we can use couple of other methods in that case.
  
  1. f.readlines(): gives the list of all the lines in the file
  2. f.readline(): give the single line
"""

try:
    with open('test.txt', 'r') as f:
        contents = f.readlines()
        print(contents)
except FileNotFoundError:
    print("Wrong File name or Path!")
"""
output: ['1] This is a test file with\n', '2] multiple lines of data.\n', '3] Thrid Line\n', '4] Fourth Line\n', '5] Fifth Line\n']
"""

"""
f.readline(): grap one line at a time
"""
try:
    with open('test.txt', 'r') as f:
        content = f.readline()
        print(content,end='')

        content = f.readline()
        print(content)
except FileNotFoundError:
    print("Wrong File name or Path!")
"""
out:
1] This is a test file with
2] multiple lines of data.
"""
"""
Note: 
  - So till now we still havn't solve the problem of how we could read all of the content from
    an extremely large file.
  - If we read entire fle at once then we could run out of memory and we also don't
    wanna run f.readline() thousand times. 
    
  - so instead f using readlines() or readine() we ca simple iterate over all the lines in the file
    as shown below.
     - this won;t create any memory issue.
"""

try:
    with open('test.txt', 'r') as f:
        for line in f:
            print(line, end='')
except FileNotFoundError:
    print("Wrong File Name or Path")
