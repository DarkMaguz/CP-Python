#!/usr/bin/python3.6

print("Hello!\nIm a friendly computer program.\nMy name is I/O, byt my frinds call me Io, just like the moon of Saturn.")

name = input("What's your name?: ")
print("Hello " + name + "!")

age = int(input("How old are you?: "))
print("Wow! %d that is awesome!" % age)

feeling = input("How do you feel to day?: ")
print("I don't know how that feels like, but somtimes I wish I could feel %s too." % feeling)

print("It was nice talking with you %s who is %d years old and is feeling %s" % (name, age, feeling))