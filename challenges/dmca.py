"""
  dmca.py

    Created on: Mar 28, 2025
        Author: Peter "Magnus" Balling
        License: MIT
  
    Description:
        This is a library for encrypting strings using the 
        infamous cryptographic algorithm only known as DMCA.
"""

import math as Math

HASH_TABLE_SIZE = 256


def BuildHashTable(password: str):
  charTable = [ i for i in range(HASH_TABLE_SIZE) ]
  hashTable = [ 0 for _ in range(HASH_TABLE_SIZE) ]
  for i in range(HASH_TABLE_SIZE):
      unit = (ord(password[i % len(password)]) * (Math.floor(i / len(password)) + 1)) % len(charTable)
      hashTable[i] = charTable[unit]
      del charTable[unit]
  return hashTable


def Encrypt(text: bytes, hashTable: list):
  secretText = bytearray()
  for i in range(len(text)):
      secretText.append(hashTable[text[i]])
  return secretText


def Decrypt(text: bytes, hashTable: list):
  secretText = text
  plainText = bytearray()
  for i in range(len(secretText)):
      plainText.append(hashTable.index(secretText[i]))
  return plainText


def test():
  hashTable = BuildHashTable("sup3r s3cr3t p4ssw0rd")
  secretText = "Hello World!"
  obfuscatedText = Encrypt(secretText.encode(), hashTable)
  plainText = Decrypt(obfuscatedText, hashTable).decode()

  print("Obfuscated Text:", obfuscatedText)
  print("Plain Text:", plainText)
  print("Valid result:", secretText == plainText)

  for idx, char in enumerate(secretText):
    if char != plainText[idx]:
      print(f"{idx}: {char} != {plainText[idx]}")
      break
  print("Test Passed")
