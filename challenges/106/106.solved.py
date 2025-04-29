"""
  106.py

    Created on: Apr 07, 2025
        Author: Peter "Magnus" Balling
        License: MIT
    Print a row of numbers from 1 to 10 separated by one space.
    We can use the `strip` method to remove any trailing whitespace of a string.
"""

row = ""

for i in range(1, 11):
  row += str(i) + " "

print(row.strip())
