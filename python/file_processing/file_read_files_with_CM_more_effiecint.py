"""
- Some time you more conrol over exactly what you're reading from the file
- f.read() can be used as it allows to specify the amount of data we want to read.
- so f.read(100): it will read first 100 characters of a file instead of printing the whole thing all at once.
"""
try:
    with open('test.txt', 'r') as f:
        f_contents = f.read(50)
        print(f_contents)
except FileNotFoundError:
    print("Error:File Name or Provided Path is Incorrect !")

"""
out:
1] This is a test file with
2] multiple lines of d
"""
print()
"""
Since we don't know how large the file going to be 
We can use above technique with some modification
"""
with open('test.txt', 'r') as f:
    size_to_read = 10

    f_contents = f.read(size_to_read)

    while len(f_contents) > 0:
        print(f_contents, end='')
        f_contents = f.read(size_to_read)

"""
Understad the concepts
"""
with open('test.txt', 'r') as f:
    size_to_read = 10

    f_contents = f.read(size_to_read)

    while len(f_contents) > 0:
        print(f_contents, end='*')
        f_contents = f.read(size_to_read)

"""
out
1] This is* a test fi*le with
2]* multiple *lines of d*ata.
3] Th*rid Line
4*] Fourth L*ine
5] Fif*th Line
*
we can see the current position advances everytime we read from file
we can actually see current position using f.tell()
"""
print()
with open('test.txt', 'r') as f:
    size_to_read = 10

    f_contents = f.read(size_to_read)
    print(f.tell())

    # while len(f_contents) > 0:
    #     print(f_contents, end='*')
    #     f_contents = f.read(size_to_read)

"""
f.seek(index): we can provide the position from where we want to seek the read
f.seek(0): back to initial read 
"""
print()
with open('test.txt', 'r') as f:
    size_to_read = 10

    f_contents = f.read(size_to_read)
    print(f_contents)
    f.seek(1)
    f_contents = f.read(size_to_read)
    print(f_contents)
"""
out:
1] This is
] This is 

"""