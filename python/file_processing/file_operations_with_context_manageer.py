
"""
Why to Use context Manager:
 - If we open the file like we did in previous example then we have to remember
   to explicitly close the file
 - If we don't close the file then we can end up wth leaks that cause you to run
   over the maximum allowed file descriptors on your system and youu application could through an error
 - So its always important to make sure you close the file that you open.
 - In order to you a context manager then its kind of similar ad we can use `with` keyword for this.
"""

"""
Advantages of Context Manager
- They allow us to work with files from within this block and after we exit that bloack of code
  it will automatically close the file for us.
- This will also close the file if there are any exaceptions that are thrown or anything like that. 
"""

with open('test.txt', 'r')  as f:
    pass

"""
- We actually have access to the f manager even after we exit the context manager but file will be just closed.
- so f.mode, f.close will work but f.read() won't
"""
print(f.mode)  # r
print(f.closed)  # True

print(f.read())
"""print(f.read())
ValueError: I/O operation on closed file."""


