from vigenere_extended import *
from rc4 import *

text = "halo halo bandung askdjfhlkasjh2864^%$^%"
key = "hehe"

text_rc4 = encryptRC4ORD(text, key)

print(text_rc4)

# decrypt = decryptExt(str(hasil), key)
# print(decrypt)
# dec = text_rc4.decode('unicode_escape')
# print(dec)
# dec = '\x1b\x9f\xf7\xf2\xac'
# print(type(dec))
# x = input()
# print(type(x))
hasildec = decryptRC4ORD(text_rc4, key)
print(str(hasildec))

# hasildec2 = decryptRC4ORD(x, key)
# print(str(hasildec2))

