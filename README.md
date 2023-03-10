# Huffman Coding Algorithm

```
DESCRIPTION
—   These script receives a text and prints it out coded with Huffman coding algorithm
USAGE
—   The following ways to launch the scripts can be used:
    —   python3 encode_huffman.py t <TEXT> — encodes TEXT
    —   python3 encode_huffman.py f <FILE> — encodes the text, stored in FILE 
NOTES
—   Text passed as an argument must not contain any special symbols (commas, braces, etc.)
    to avoid any bash conflicts
```

## Sample

```
$ python3 encode_huffman.py t This is a test text
```
```
TEXT
This is a test text
USED FOLLOWING CODES
{' ': '111', 's': '110', 'x': '1011', 'a': '1010', 'h': '1001', 'T': '1000', 'e': '011', 'i': '010', 't': '00'}
CODED TEXT
100010010101101110101101111010111000111100011100011101100
```

###### Copyright 2023, Sergey Lagov