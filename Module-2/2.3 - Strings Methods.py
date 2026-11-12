# Demonstrating the capitalize() method:
# Making the first character of the string capital

print("Alpha".capitalize())
print('ALPHA'.capitalize())
print(' Alpha'.capitalize())
print('123'.capitalize())
print("αβγδ".capitalize())

# Demonstrating the center() method:
# adding some spaces before and after the string
print('[' + 'alpha'.center(10)+ ']')
print('[' + 'Beta'.center(2) + ']') #the string itself has already 4 so it will output orginal string
print('[' + 'Beta'.center(4) + ']') #string = 4 and space = 4, output orginal string
print('[' + 'Beta'.center(6) + ']') # 6 - 4 = 2, 1 space each for left and right

print('[' + 'gamma'.center(20, '*') + ']') # two parameter variant

# Demonstrating the endswith() method:
if "epsilon".endswith("on"):
    print("yes")
else:
    print("no")

t = "zeta"
print(t.endswith("a"))
print(t.endswith("A"))
print(t.endswith("et"))
print(t.endswith("eta"))

# Demonstrating the find() method:
#The find() method is similar to index()
#it doesn't generate an error for a non-existent substring (it returns -1 then)
print("Eta".find("ta"))
print("Eta".find("mma"))

#work with strings only
t = 'theta'
print(t.find('eta'))
print(t.find('et'))
print(t.find('the'))
print(t.find('ha'))

the_text = """A variation of the ordinary lorem ipsum
text has been used in typesetting since the 1960s 
or earlier, when it was popularized by advertisements 
for Letraset transfer sheets. It was introduced to 
the Information Age in the mid-1980s by the Aldus Corporation, 
which employed it in graphics and word-processing templates
for its desktop publishing program PageMaker (from Wikipedia)"""

fnd = the_text.find('the')
while fnd != -1:
    print(fnd)
    fnd = the_text.find('the', fnd + 1)


# Demonstrating the isalnum() method:
#check the string contains alphabet or digits
print('lambda30'.isalnum())
print('lambda'.isalnum())
print('30'.isalnum())
print('@'.isalnum())
print('lambda_30'.isalnum())
print(''.isalnum())

# Demonstrating the isapha() method: letter only
print("Moooo".isalpha())
print('Mu40'.isalpha())

# Demonstrating the isdigit() method: digit only
print('2018'.isdigit())
print("Year2019".isdigit())

#Demonstrating the islower() method: lower-case letters only
print("Moooo".islower())
print('moooo'.islower())

# Demonstrating the isspace() method: identifies whitespaces only
print(' \n '.isspace())
print(" ".isspace())
print("mooo mooo mooo".isspace())

# Demonstrating the isupper() method: upper-case letters only
print("Moooo".isupper())
print('moooo'.isupper())
print('MOOOO'.isupper())

# Demonstrating the join() method:
print(",".join(["omicron", "pi", "rho"]))

# Demonstrating the lower() method:
print("SiGmA=60".lower())
print("MIN KHANT KYAW".lower())

# Demonstrating the lstrip() method: remove whitespaces
print("[" + " tau ".lstrip() + "]")
print("     min khant kyaw      ".lstrip())

# Demonstrating the replace() method:
print("www.netacad.com".replace("netacad.com", "pythoninstitute.org"))
print("This is it!".replace("is", "are"))
print("Apple juice".replace("juice", ""))

# three paramter replace, limit the number of replacements
print("This is it!".replace("is", "are", 1))
print("This is it!".replace("is", "are", 2))  
print("This is it! This is it!".replace("is", "are", 3))
print("This is it! This is it!".replace("is", "are", 4))

# Demonstrating the rfind() method: return the highest(last)index
# find() method return the lowest(first)index
print("tau tau tau".rfind("ta"))
print("tau tau tau".rfind("ta", 9))
print("tau tau tau".rfind("ta", 3, 9))

# Demonstrating the rstrip() method:
print("[" + " upsilon ".rstrip() + "]")
print("cisco.com".rstrip(".com"))

# Demonstrating the split() method:
print("phi       chi\npsi".split())

# Demonstrating the startswith() and endswith() method: 
# check the start and end specified substrings
print("omega".startswith("meg"))
print("omega".startswith("om"))
print()
print("adrian".endswith("ian"))
print("adrian".endswith("adr"))

# Demonstrating the strip() method: combines lstrip() and rstrip()
print("[" + "   aleph   ".strip() + "]")
print("[" + "   aleph   ".lstrip() + "]")
print("[" + "   aleph   ".rstrip() + "]")

# Demonstrating the swapcase() method: swaping lowercase and uppercase
print("I know that I know nothing.".swapcase())

# Demonstrating the title() method:
print("I know that I know nothing. Part 1.".title())

# Demonstrating the upper() method:
print("I know that I know nothing. Part 2.".upper())

#What is the expected output quizzes?
for ch in "abc123XYX":
    if ch.isupper():
        print(ch.lower(), end='')
    elif ch.islower():
        print(ch.upper(), end='')
    else:
        print(ch, end='')

s1 = 'Where are the snows of yesteryear?'
s2 = s1.split()
print(s2[-2])

the_list = ['Where', 'are', 'the', 'snows?']
s = '*'.join(the_list)
print(s)
s = ' '.join(the_list)
print(s)

s = 'It is either easy or impossible'
s = s.replace('easy', 'hard').replace('im', '')
print(s)