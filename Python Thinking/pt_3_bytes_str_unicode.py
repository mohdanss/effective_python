'''
Python 3:
    There are two types that represent sequences of characters: 
    - bytes, Instances of bytes contain raw 8-bit values. 
    - str, Instances of str contain Unicode characters.

Python 2:
    There are two types that represent sequences of characters: 
    - str, instances of str contain raw 8-bit values. 
    - unicode, instances of unicode contain Unicode characters.

There are many ways to represent Unicode characters as binary data (raw 8-bit values).
The most common encoding is UTF-8. 
- Importantly, str instances in Python 3 and unicode instances in Python 2 do not 
    have an associated binary encoding. 
- To convert Unicode characters to binary data, you must use the encode method. 
- To convert binary data to Unicode characters, you must use the decode method.

When you’re writing Python programs, it’s important to do encoding and decoding of
Unicode at the furthest boundary of your interfaces. The core of your program should use
Unicode character types (str in Python 3, unicode in Python 2) and should not assume
anything about character encodings. This approach allows you to be very accepting of
alternative text encodings (such as Latin-1, Shift JIS, and Big5) while being strict about
your output text encoding (ideally, UTF-8).
The split between character types leads to two common situations in Python code:
You want to operate on raw 8-bit values that are UTF-8-encoded characters (or some
other encoding).
You want to operate on Unicode characters that have no specific encoding.
You’ll often need two helper functions to convert between these two cases and to ensure
that the type of input values matches your code’s expectations.
In Python 3, you’ll need one method that takes a str or bytes and always returns a str.
'''

def to_str(bytes_or_str):
    '''
        This function takes a bytes or str and always returns a str.
        Way to declare a bytes literal in Python 3:
            string = b'Hello world'
    '''
    if isinstance(bytes_or_str, bytes):
        value = bytes_or_str.decode('utf-8')
    else:
        value = bytes_or_str
    return value

def to_bytes(bytes_or_str):
    '''
        This function takes a bytes or str and always returns a bytes.
    '''
    if isinstance(bytes_or_str, str):
        value = bytes_or_str.encode('utf-8')
    else:
        value = bytes_or_str
    return value




