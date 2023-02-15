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

def encryptExt(text, key):
    key = autoKey(text, key)
    listofText = []
    a = b''
    for i in range(len(text)):
        x = ((text[i]) + (ord(key[i]))) % 256
        listofText.append(x)
        a += x.to_bytes(1, 'big')
    return a

def decryptExt(text, key):
    key = autoKey(text, key)
    listofText = []
    a = b''
    for i in range(len(text)):
        x = ((text[i]) - (ord(key[i]))) % 256
        listofText.append(x)
        a += x.to_bytes(1, 'big')
    return a