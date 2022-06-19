"""
Read and write File operations
"""
f = open('test.txt') # not recomended this way
print(f)  # out: <_io.TextIOWrapper name='./test.txt' mode='r' encoding='UTF-8'>

"""
- we also need to specific the mode for the open operations whether
- we are opening this to read or write , append or  for both by default it is read.
- read = r
- write = w
- append = a
- read and write = r+
"""

f = open('test.txt', 'r')

# print name of the file through file object
print(f.name)  # test.txt

# print the mode in which file is open
print(f.mode)  # r

"""
Note:
  If we open a file this way then we need to explicitely close the file when not needed anymore
  and to do that we can use f.close()
"""
f.close()
