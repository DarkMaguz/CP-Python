"""
  hashgen.py

    Created on: Apr 06, 2025
        Author: Peter "Magnus" Balling
        License: MIT
"""

import os
import json


def saveJson(file: str, data: dict):
  with open(file, 'w') as f:
    json.dump(data, f, indent=2)


def genHash(target: str) -> str:
  path = f'{target}/{target}.solved.py'
  if not os.path.isfile(path):
    raise FileNotFoundError(f'{path} was not found.')
  cmd = f'python3 {path} | sha256sum'
  hash = os.popen(cmd).read().split(' ')[0]
  # print(f'Hash for {target} is {hash}')
  return hash


def main():
  challenges = {}
  for dir in os.walk('.'):
    target = dir[0].split('/')[-1]
    if not target.isdigit():
      continue
    hash = genHash(target)
    challenges[target] = hash

  saveJson('challenges.json', challenges)
  print(f'Hashed {len(challenges)} challenges.')


if __name__ == '__main__':
  main()
