def pathInput(input):
    with open(input, 'rb') as file:
        text = file.read()
    return text

def autoKey(text, key):
    key = list(key.upper())
    if len(text) == len(key):
        return key
    else:
        for i in range(len(text) - len(key)):
            key.append(key[i % len(key)])
    return ''.join(key)

def encryptExtOrd(text, key):
    key = autoKey(text, key)
    listofText = []
    for i in range(len(text)):
        x = ((ord(text[i])) + (ord(key[i]))) % 256
        listofText.append(chr(x))
    return "".join(listofText)

def decryptExtOrd(text, key):
    key = autoKey(text, key)
    listofText = []
    a = b''
    for i in range(len(text)):
        x = ((ord(text[i])) - (ord(key[i]))) % 256
        listofText.append(chr(x))
    return "".join(listofText)

def encryptExtFile(text, key):
    key = autoKey(text, key)
    listofText = []
    a = b''
    for i in range(len(text)):
        x = ((text[i]) + (ord(key[i]))) % 256
        listofText.append(x)
        a += x.to_bytes(1, 'big')
    return a

def decryptExtFile(text, key):
    key = autoKey(text, key)
    listofText = []
    a = b''
    for i in range(len(text)):
        x = ((text[i]) - (ord(key[i]))) % 256
        listofText.append(x)
        a += x.to_bytes(1, 'big')
    return a