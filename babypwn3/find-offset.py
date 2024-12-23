from pwn import *

# Start the process
p = process('main3')

# Generate a cyclic pattern so that pwntools can automatically find the offset
pattern = cyclic(2000)  # 300 is just an example, adjust it to be larger than the buffer

# Send the pattern to the program
p.sendlineafter("Which operation do you want to use?\n", pattern)


# Wait for the program to crash
p.wait()

# Get the core dump
core = Coredump('./core')  # The path to the core file

# Now find the offset
offset = cyclic_find(core.read(core.rsp, 4))  # Adjust the register if needed

print(f"The offset is: {offset}")

# Close the process
p.close()
