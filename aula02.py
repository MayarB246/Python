# break line:   \r\n -> CRLF   |   \n -> LF

print("1", 2, 1+2, sep="_", end='\r\n \r\n')
print("4", 5, 2+4, sep='-', end="##\n")
print("7", 8, 3+6, sep=' ', end='\r\n##')