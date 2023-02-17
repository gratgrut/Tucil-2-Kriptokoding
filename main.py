import vigenere_extended as ve
import rc4

#text = "FileAwal.pdf"

key = "abcd"

#text_ve = ve.encryptExtFile(text, key)
#a = rc4.encryptRCFile(text_ve, key)
#text_rc4 = rc4.encryptRC4ORD(text, key)
with open('FotoEnkripsi.png', 'rb') as f:
    text = f.read()

b = rc4.decryptRC4File(text, key)
y = ve.decryptExtFile(b, key)

with open('FotoDekripsi.png', 'wb') as f:
    f.write(y)

# decrypt = decryptExt(str(hasil), key)
# print(decrypt)
# dec = text_rc4.decode('unicode_escape')
# print(dec)
# dec = '\x1b\x9f\xf7\xf2\xac'
# print(type(dec))
# x = input()
# print(type(x))
#hasildec = rc4.decryptRC4ORD(text_rc4, key)
#print(str(hasildec))

# hasildec2 = decryptRC4ORD(x, key)
# print(str(hasildec2))

