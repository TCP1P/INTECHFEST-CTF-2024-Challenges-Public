#!/usr/bin/python3
import ctypes

data = bytearray(('A' * ctypes.sizeof(ctypes.c_long)).encode())

def write(offset, value):
    try:
        byte_ptr = ctypes.cast(id(data) + offset, ctypes.POINTER(ctypes.c_ubyte))
        byte_ptr.contents.value = value
    except Exception as e:
        print("Error:", e, file=open("/dev/stderr","w"))

def main():
    print("Current data:", data)
    try:
        offset = int(input("offset: "))
        if offset < 0x1deed5 and offset > -0x31337:
            value = int(input("value: "))
            write(offset, value)
        else:
            print("Invalid offset")
    except ValueError:
        print("Invalid input", file=open("/dev/stderr","w"))

if __name__ == "__main__":
    for _ in range(2):
        main()
