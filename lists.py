#!/usr/bin/python3.6

# This should be introduced in the interactive python shell. Where the arguments to print should just be passed to the shell.

letters = ['a','b','c']
print(letters)

# Indexing:
print(letters[0])
print(letters[1])
print(letters[2])

# At this point we will introduce an error by trying to access an index that has not been defined yet.
# i.e. letters[3]
# Explain the output caused by the error and how it can be useful to debug a program.

print(letters[-1])
print(letters[-2])

# Slicing:
print(letters[1:3])
print(letters[-3:])

letters.append('d')
print(letters)

numbers = [1, 2, 3, 4, 5, 6]
print(numbers)

print(len(numbers))
print(len(letters))

lists = [numbers, letters]
print(lists)
print(len(lists))

mix = numbers + letters
print(mix)
print(len(mix))
