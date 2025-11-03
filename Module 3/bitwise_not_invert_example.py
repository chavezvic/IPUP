flag_register = 0b10101010  # Binary: 10101010 ----- 10101011
inverted = ~flag_register                           #01010100
print(bin(inverted))        # Binary: -1101011 (negative due to two's complement)
#~x = -(x + 1)
#~170 = -(170 + 1) = -171
#~170 = -84
