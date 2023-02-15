# key scheduling algorithm
def ksa(K):
    S = []
    for i in range(256):
        S[i] = i

    j = 0
    for i in range(256):
        j = (j + S[i] + K[i % len(K)]) % 256
        x = S[i]
        S[i] = S[j]
        S[j] = x

    return S

# pseudo-random generation algorithm
def prga(S, P):
    i = 0
    j = 0

    # convert to unsigned int

    for idx in range(len(P) - 1):
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        x = S[i]
        S[i] = S[j]
        S[j] = x
        t = (S[i] + S[j]) % 256
        u = S[t]
        c = u ^ P[idx]
    
    return c
