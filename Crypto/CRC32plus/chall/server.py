#!/usr/bin/env python3
from Crypto.Cipher import Salsa20
from Crypto.Util.number import long_to_bytes
import random
import signal
import string
import os

CHARSET = string.digits + string.ascii_lowercase + "_"
FLAG = os.getenv("GZCTF_FLAG", "INTECHFEST{redacted}")


class crc32plus:
    def __init__(self, p):
        self.m = 0xFFFFFFFF
        self.p = p & self.m
        self.t = []
        for i in range(256):
            v = i
            for _ in range(8):
                v = (self.p ^ (v >> 1)) if (v & 1) == 1 else (v >> 1)
            self.t.append(v)

    def _update(self, buf):
        v = self.m
        for c in buf:
            v = self.t[(v ^ c) & 0xFF] ^ (v >> 8)
        return v ^ self.m

    def calc(self, buf):
        v = self.m
        buf = b"\x88" + buf + b"\x88"
        for i in range(len(buf) - 1):
            v = self._update(long_to_bytes(v, 4) + buf[i : i + 2])
        return long_to_bytes(v ^ self.m, 4)

    def __repr__(self):
        return f"crc32plus(poly={hex(self.p)})"


def gen_rand_str():
    return "crc32plus_" + "".join(random.choices(CHARSET[:-1], k=6))


def user_input(s):
    try:
        inp = input(s).strip()
        assert len(inp) < 256 and all(c in CHARSET for c in inp)
        return inp.encode()
    except:
        exit()


def main():
    poly = random.getrandbits(32)
    c32p = crc32plus(poly)

    print(f"Prove that you can find collision on {c32p}")
    m1 = user_input("Message #1: ")
    m2 = user_input("Message #2: ")
    if m1 == m2 or c32p.calc(m1) != c32p.calc(m2):
        print("Nope")
        return

    key = gen_rand_str().encode()
    ptx = gen_rand_str().encode()
    cipher = Salsa20.new(key)
    ctx = cipher.nonce + cipher.encrypt(ptx)
    hsh = c32p.calc(key)

    print(f"Prove that you can reverse this crc32plus: {hsh.hex() + ctx.hex()}")
    m3 = user_input("Plaintext: ")
    if m3 != ptx:
        print("Nope")
        return

    print(FLAG)


if __name__ == "__main__":
    signal.alarm(90)
    main()
