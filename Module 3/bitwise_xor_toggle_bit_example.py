flag_register = 0b10101010  # Binary: 10101010
the_mask = 0b00000100       # Binary: 00000100 (Toggling the 3rd bit)
flag_register ^= the_mask
print(bin(flag_register))   # Binary: 10101110
#Same bit = 0, Different bit = 1
