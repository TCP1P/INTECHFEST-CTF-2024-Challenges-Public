#!/usr/bin/env python3
from Crypto.Util.number import *

FLAG = open("flag.txt", "rb").read()


def intechprimes(nbit, z=8):
    hbit = nbit // 2
    big = getStrongPrime(nbit)
    small = sum(pow(2, e) for e in range(hbit - z, hbit))

    while True:
        small += 1
        p = big % (small - z)
        q = big % (small + z)
        n = p * q
        if isPrime(p) and isPrime(q) and n.bit_length() == nbit:
            return [n, (small << hbit) + (big >> hbit)]


m = bytes_to_long(FLAG)
e = 65537
n, h = intechprimes(1024)
c = pow(m, e, n)

print(f"e = {hex(e)}")
print(f"n = {hex(n)}")
print(f"h = {hex(h)}")
print(f"c = {hex(c)}")
