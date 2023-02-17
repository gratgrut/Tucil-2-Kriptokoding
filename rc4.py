# key scheduling algorithm
def ksa(K):
    S = []
    for i in range(256):
        S.append(i)

    j = 0
    for i in range(256):
        j = (j + S[i] + K[i % len(K)]) % 256
        x = S[i]
        S[i] = S[j]
        S[j] = x

    return S

# pseudo-random generation algorithm
def prga(S):
    i = 0
    j = 0
    # convert to unsigned int

    while True:
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        x = S[i]
        S[i] = S[j]
        S[j] = x
        t = (S[i] + S[j]) % 256
        u = S[t]

        yield u

def encryptRCFile(text, key):
    a = b''
    listofKey = []
    for i in range(len(key)):
        x = ord(key[i])
        listofKey.append(x)

    listofText = []
    for j in range(len(text)):
        y = (text[j])
        listofText.append(y)

    hasil_ksa = ksa(listofKey)
    hasil_prga = prga(hasil_ksa)

    listofCipher = []
    for x in listofText:
        en = (x ^ next(hasil_prga))
        listofCipher.append(chr(en))
        a += en.to_bytes(1, 'big')
    return a

def decryptRC4File(text, key):
    a = b''
    listofKey = []
    for i in range(len(key)):
        x = ord(key[i])
        listofKey.append(x)

    listofText = []
    for j in range(len(text)):
        y = (text[j])
        listofText.append(y)

    hasil_ksa = ksa(listofKey)
    hasil_prga = prga(hasil_ksa)

    listofPlainText = []
    for x in listofText:
        de = (x ^ next(hasil_prga))
        listofPlainText.append(chr(de))
        a += de.to_bytes(1, 'big')
    return a  

def encryptRC4ORD(text, key):
    a = b''
    listofKey = []
    for i in range(len(key)):
        x = ord(key[i])
        listofKey.append(x)

    listofText = []
    for j in range(len(text)):
        y = ord(text[j])
        listofText.append(y)

    hasil_ksa = ksa(listofKey)
    hasil_prga = prga(hasil_ksa)

    listofCipher = []
    for x in listofText:
        en = (x ^ next(hasil_prga))
        listofCipher.append(chr(en))
        a += en.to_bytes(1, 'big')
    return a

def decryptRC4ORD(text, key):
    a = b''
    listofKey = []
    for i in range(len(key)):
        x = ord(key[i])
        listofKey.append(x)

    listofText = []
    for j in range(len(text)):
        y = ord(text[j])
        listofText.append(y)

    hasil_ksa = ksa(listofKey)
    hasil_prga = prga(hasil_ksa)

    listofPlainText = []
    for x in listofText:
        de = (x ^ next(hasil_prga))
        listofPlainText.append(chr(de))
        a += de.to_bytes(1, 'big')
    return a    