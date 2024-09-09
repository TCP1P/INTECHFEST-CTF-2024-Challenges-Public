import os
import ed25519 # pip install ed25519

vks = bytes.fromhex(input('vk: '))
assert 0 not in vks and 255 not in vks
vk = ed25519.VerifyingKey(vks)

for _ in range(50):
    suffix = os.urandom(8)
    print(suffix.hex())
    sig = bytes.fromhex(input('sig: '))

    prefix = os.urandom(8)
    print(prefix.hex())
    msg = bytes.fromhex(input('msg: '))

    vk.verify(sig+suffix, prefix+msg)

print(open('flag.txt', 'r').read())