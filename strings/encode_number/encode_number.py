def encode(num):
    
    if num == 0:
        return ''
    
    div_int = (num - 1) // 2
    rem = (num - 1) % 2
    
    return encode(div_int) + str(rem)