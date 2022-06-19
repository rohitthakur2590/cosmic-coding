"""
- We can use read and write on multiple files at same time
- so we are going to use this to make a copy of our test.txt file

"""
try:
    with open('test.txt', 'r') as rf:
        with open('test_copy.txt', 'w') as wf:
            for line in rf:
                wf.write(line)
except FileNotFoundError:
    print("Error: Wrong File or path name")
except Exception as err:
    print("Error! ", repr(err))

"""
Lets try to copty an image file withh above program
"""

try:
    with open('shoes.jpg') as rf:
        with open('shoes_to_buy.jpg', 'w') as wf:
            for line in rf:
                wf.write(line)
except FileNotFoundError:
    print("Error: Wrong File name or Path!")
except Exception as err:
    print("Error: ", repr(err))
else:
    print("Go Buy New Shoes!")
"""
out:
Error:  UnicodeDecodeError('utf-8', ...... 

so in order to copy an image we need tobe reading orwrting bytes instead of working with text.
to use in binary mode we can append a 'b' to ou read 'r' makes 'rb' operation an 'w' makes 'wb'
"""

with open('shoes.jpg', 'rb') as rf:
    with open('shoes_to_buy.jpg', 'wb') as wf:
        for line in rf:
            wf.write(line)


"""
How do we perform these operations in chunk sizes
"""
with open('shoes.jpg', 'rb') as rf:
    with open('shoes_to_order.jpg', 'wb') as wf:
        chunk_size = 4096
        rf_chunk = rf.read(chunk_size)
        while len(rf_chunk) > 0:
            wf.write(rf_chunk)
            rf_chunk = rf.read(chunk_size)