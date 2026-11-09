from random import randrange, randint 

print(randrange(1), end=' ')
print(randrange(0, 1), end=' ')
print(randrange(0, 1, 1), end=' ') # 1 to 3 arguments eg. start, stop, step excluding stop inti
print(randint(0, 1)) # only two arguments start and stop including stop inti

for i in range(10):
    print(randint(1, 10), end=',')

from random import choice, sample

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(choice(my_list))
print(sample(my_list, 5))
print(sample(my_list, 10))

from platform import platform

print(platform())
print(platform(1))
print(platform(0, 1))

from platform import machine

print(machine())

from platform import processor

print(processor())

from platform import system

print(system())

from platform import version

print(version())

from platform import python_implementation, python_version_tuple

print(python_implementation())

for atr in python_version_tuple():
    print(atr)