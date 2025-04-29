"""
  validator.py

    Created on: Apr 06, 2025
        Author: Peter "Magnus" Balling
        License: MIT
  
  This script is used to validate challenges in the 100 series.
  Useage:
    Run in console and select challenge to run validation on.
"""

import os
import json
from hashgen import genHash


def loadJson(file: str) -> dict:
  if not os.path.exists(file) or os.path.getsize(file) == 0:
    return {}
  with open(file, 'r') as f:
    return json.load(f)


def validate(challenge: str):
  os.system('clear')
  print(f'Validating challenge {challenge}...')
  hash = genHash(challenge)
  challenges = loadJson('challenges.json')
  if challenges[challenge] == hash:
    print('The solution is valid. Good job!')
  else:
    print('Invalid solution.')
    print('Please fix the code and try again.')


def main():
  os.system('clear')
  while True:
    try:
      challenge = input('Enter challenge number: ')
      if challenge == 'exit' or challenge == 'e' or challenge == 'quit' or challenge == 'q':
        print('Exiting...')
        exit()
      if not challenge.isnumeric():
        print('Invalid challenge number.')
        continue
      if int(challenge) < 100 or int(challenge) > 199:
        print('Invalid challenge number.')
        continue
      if not os.path.isfile(f'{challenge}/{challenge}.py'):
        print('Challenge does not exist.')
        continue
      validate(challenge)
    except ValueError:
      print('Invalid challenge number.')
    except KeyboardInterrupt:
      print('\nExiting...')
      exit()
  

if __name__ == '__main__':
  main()
