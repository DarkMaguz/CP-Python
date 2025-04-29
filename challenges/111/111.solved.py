"""
  111.py

    Created on: Apr 06, 2025
        Author: Peter "Magnus" Balling
        License: MIT
  Use the base64 module to decode the message.
"""

import base64

encodedMessage = b'WW91IGFyZSBkb2luZyBncmVhdCB3b3JrIQ=='

encodedMessage = base64.b64decode(encodedMessage)

print(encodedMessage.decode())
