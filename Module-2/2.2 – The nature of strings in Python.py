# Example 1

word = 'by'
print(len(word))


# Example 2

empty = ''
print(len(empty))


# Example 3

i_am = 'I\'m'
print(len(i_am))

multiline = '''Line #1
Line #2'''

print(len(multiline))

#Operations on strings

str1 = 'a'
str2 = 'b'

print(str1 + str2)
print(str2 + str1)
print(5 * 'a')
print('b' * 4)

# Demonstrating the ord() function.
#show the ASCII/UNICODE code point value

char_1 = 'a'
char_2 = ' '  # space

print(ord(char_1))
print(ord(char_2))

# Demonstrating the chr() function. show the character

print(chr(97))
print(chr(945))

# Indexing strings.

the_string = 'silly walks'

for i in range(len(the_string)):
    print(the_string[i], end=' ')

print()

# Iterating through a string.

the_string = 'silly walks'

for character in the_string:
    print(character, end=' ')

print()

# Slices [start:stop:step]

alpha = "abdefg"

print(alpha[1:3])
print(alpha[3:])
print(alpha[:3])
print(alpha[3:-2])
print(alpha[-3:4])
print(alpha[::2])
print(alpha[1::2])

# The in and not in operators
# Check if its left argument can be found or not

alphabet = "abcdefghijklmnopqrstuvwxyz"

print("f" in alphabet)
print("F" in alphabet)
print("1" in alphabet)
print("ghi" in alphabet)
print("Xyz" in alphabet)

print("f" not in alphabet)
print("F" not in alphabet)
print("1" not in alphabet)
print("ghi" not in alphabet)
print("Xyz" not in alphabet)

#Python strings are immutable and cannot use del append insert

alphabet = "bcdefghijklmnopqrstuvwxy"

alphabet = "a" + alphabet
alphabet = alphabet + "z"

print(alphabet)

# Demonstrating min() - Example 1:
print(min("aAbByYzZ"))


# Demonstrating min() - Examples 2 & 3:
t = 'The Knights Who Say "Ni!"'
print('[' + min(t) + ']')

t = [0, 1, 2]
print(min(t))

# Demonstrating max() - Example 1:
print(max("aAbByYzZ"))


# Demonstrating max() - Examples 2 & 3:
t = 'The Knights Who Say "Ni!"'
print('[' + max(t) + ']')

t = [0, 1, 2]
print(max(t))

# Demonstrating the index() method:
print("aAbByYzZaA".index("b"))
print("aAbByYzZaA".index("Z"))
print("aAbByYzZaA".index("A"))

# Demonstrating the list() function:
print(list("abcabc"))

# Demonstrating the count() method:
print("abcabc".count("b"))
print('abcabc'.count("d"))