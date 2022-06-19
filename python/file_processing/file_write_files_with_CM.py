"""
What happens we try to write on to files in read mode
"""
try:
    with open('test2.txt', 'r') as f:
        f.write("Hello there!")
except FileNotFoundError:
    print("Error: Wrong File name or Path")
except Exception as err:
    print("Error: ", repr(err))

"""
out:
f.write("Hello there!")
io.UnsupportedOperation: not writable
"""

"""
Can we create file without writin to it ? YES
"""
with open('test2.txt', 'w') as f:
    pass

"""
write content to file
"""
with open('test2.txt', 'w') as f:
    f.write('1) This is a multiline file')
    f.seek(0)
    f.write('2) This is test2 file')
