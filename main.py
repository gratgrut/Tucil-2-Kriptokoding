import vigenere_extended as ve
import rc4

text = input()
key = "hehe"

text_ve = ve.encryptExtOrd(text, key)
a = rc4.encryptRC4ORD(text_ve, key)
#text_rc4 = rc4.encryptRC4ORD(text, key)

print(a)

b = rc4.decryptRC4ORD(a, key)
y = ve.decryptExtOrd(b, key)

print(y)
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

