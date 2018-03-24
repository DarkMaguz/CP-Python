#!/usr/bin/python3.6

# This should be introduced in the interactive python shell. Where the arguments to print should just be passed to the shell. 

firstStr = "This is a string of text."

print(firstStr)

secondStr = "This is another string."

print(firstStr + secondStr)

print(firstStr + " " + secondStr)

thirdStr = firstStr + " " + secondStr
print(thirdStr)

strLength = len(thirdStr)

print("thirdStr has %d characters." % strLength)


