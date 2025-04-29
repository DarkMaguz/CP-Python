"""
  103.py

    Created on: Apr 07, 2025
        Author: Peter "Magnus" Balling
        License: MIT
  In this challenge, you must generate a list of all the numbers from 1 to 100.
  Use a for loop and the `range` function to generate the list.
  Then, use the `append` method to add each number to the list.
"""

numbers = []

for i in range(1, 101):
    numbers.append(i)

print(numbers)
