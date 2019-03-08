# This is a simple Caesar cipher that I use when I teach programming.
# It's best for students at an intermediary level.

charList = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','æ','ø','å',' ','.',',',':',';','?','!','=']
maxLen = len(charList)

def getKey():
	while True:
		keyNumber = int(input("Enter your secret key number: "))
		if keyNumber > 1 and keyNumber < maxLen:
			return keyNumber

def encrypt(text, key):
	eText = ""
	for char in text:
		charIndex = charList.index(char)
		charIndex += key
		while charIndex > maxLen:
			charIndex -= maxLen
		eText += charList[charIndex]
	return eText

def decrypt(text, key):
	dText = ""
	for char in text:
		charIndex = charList.index(char)
		charIndex -= key
		while charIndex > maxLen:
			charIndex += maxLen
		dText += charList[charIndex]
	return dText

key = getKey()
text = input("Enter text to encrypt: ")
print("Text to be encrypted: " + text)

encText = encrypt(text, key)
print("Encrypted text: " + encText)

decText = decrypt(encText, key)
print("Decrypted text: " + decText)
