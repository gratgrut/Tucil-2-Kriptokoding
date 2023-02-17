from vigenere_extended import *
from rc4 import *

text = "halo halo bandung askdjfhlkasjh2864^%$^%"
key = "abcd"

text_rc4 = encryptRC4ORD(text, key)

print(text_rc4)

# decrypt = decryptExt(str(hasil), key)
# print(decrypt)
dec = text_rc4.decode('unicode_escape')
hasildec = decryptRC4ORD(dec, key)
print(hasildec)

