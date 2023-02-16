from vigenere_extended import *
from rc4 import *

text = "halo halo bandung askdjfhlkasjh2864^%$^%"
key = "abcd"

text_rc4 = encryptRC4(text, key)
hasil = encryptExt(text_rc4, key)

print(hasil)