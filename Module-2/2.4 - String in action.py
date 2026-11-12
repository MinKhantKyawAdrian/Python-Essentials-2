# Comparing the first characters
print('10' == '010')
print('10' > '010')
print('10' > '8')
print('20' < '8')
print('20' < '80')

# Demonstrating the sorted() function:
first_greek = ['omega', 'alpha', 'pi', 'gamma']
first_greek_2 = sorted(first_greek)

print(first_greek)
print(first_greek_2)

# Demonstrating the sort() method:
second_greek = ['omega', 'alpha', 'pi', 'gamma']
print(second_greek)

second_greek.sort()
print(second_greek)

#Numbers to strings
itg = 13
flt = 1.3
si = str(itg)
sf = str(flt)

print(si + ' ' + sf)

#Strings to numbers
si = '13'
sf = '1.3'
itg = int(si)
flt = float(sf)

print(itg + flt)

#Excepted output
s1 = 'Where are the snows of yesteryear?'
s2 = s1.split()
s3 = sorted(s2)
print(s3[1])

s1 = '12.8'
i = int(s1)
s2 = str(i)
f = float(s2)
print(s1 == s2)