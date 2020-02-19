def power(value, exponent):
    if exponent == 1:
        return(value)

    if exponent < 0:
        exponent *= -1
        value = 1/value

    if exponent == 0:
        return(1)
    
    
    return(value * power(value, exponent - 1))

print(power(5,5))