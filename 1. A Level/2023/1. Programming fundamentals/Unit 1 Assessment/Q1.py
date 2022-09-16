character = input('Enter a lowercase character')
code = ord(character)


if 97 <= code <= 122:
   print("uppercase equivalent =", chr(code - 32))
else:
   print('Error: not a lower case character')
