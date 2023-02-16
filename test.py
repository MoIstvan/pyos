def roundbytes(lbytes:int,block:int):
    def roundnum(number, multiple, direction='nearest'):
        from math import ceil, floor
        if direction == 'nearest':
            return multiple * round(number / multiple)
        elif direction == 'up':
            return multiple * ceil(number / multiple)
        elif direction == 'down':
            return multiple * floor(number / multiple)
        else:
            return multiple * round(number / multiple)


    if lbytes < 0:
        raise ValueError(f"Invalid value: {lbytes}. Must be at least 0")
    elif lbytes > 2147483647 and lbytes < 9223372036854775808:
        print(f"{roundnum(lbytes,block,'up')} bytes; {(roundnum(lbytes,block,'up')) // block} blocks\nWARNING: Can cause trouble on 32-bit systems!")
    elif lbytes > 9223372036854775808:
        raise ValueError(f"Invalid value: {lbytes}. Cannot be bigger than 9223372036854775807")
    else:
        print(f"{roundnum(lbytes,block,'up')} bytes; {(roundnum(lbytes,block,'up')) // block} blocks")

print(roundbytes(2147483648,1))