"""
  level104.py

    Created on: Mar 07, 2025
        Author: Peter "Magnus" Balling
        License: MIT

  Description: In this file, we will be learning about the use of loops in Python.
  Create a new Python file for this assignment.
  Go through the following examples one by one.

"""

def example1():
  """
  This function will print out the numbers 1 to 10.
  """
  for i in range(1, 11):
    print(i)

def example2():
  """
  This function will print out the numbers 1 to 10 in reverse order.
  """
  for i in range(10, 0, -1):
    print(i)

def example3():
  """
  This function will print out the numbers 1 to 10 in steps of 2.
  """
  for i in range(1, 11, 2):
    print(i)

def example4():
  """
  This function will print out a matrix of numbers.
  """
  for i in range(1, 4):
    for j in range(1, 4):
      print(i * j, end=" ")
    print()

example4()
