# Caesar Cipher

#import pyperclip

# The string to be encrypted/decrypted
meesage = "This is my secret message"
# The encryption/decryption key
key = 13

#Wheather the program encrypts or deceypts
mode = 'encrypt'

# Every possible symbol that can be encrypted
# Python constant

SYMOBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'

# Store the encrypted/decrypted from of the message
translated = ''

for symbol in meesage:
    # NOTE: only symobls in the symbols string can be encrypted/decrypted.
    if symbol in SYMOBOLS:
        symbolIndex = SYMOBOLS.find(symbol)

        # Preform encrypted/decrypted
        if mode == 'encrypt':
            translatedIndex = symbolIndex + key
        elif mode == 'decrypt':
            translatedIndex = symbolIndex - key

        # Handel wraparound if needed:
        if translatedIndex >= len(SYMOBOLS):
            translatedIndex = translatedIndex - len(SYMOBOLS)
        elif translatedIndex < 0:
            translatedIndex = translatedIndex + len(SYMOBOLS)

        translated = translated + SYMOBOLS[translatedIndex]
    else: 
        #Append the symbol without encrypted/decrypted
        translated = translated + symbol

# Output the translated string
print(translated)
#pyperclip.copy(translated)