# Calculating root using Newton's method
# Formulae for newton's method
# square_root = 0.5 * (assumed_Value+(actual_value/assumed_value))
def root(num, tol):
    assumedValue = num
    while True:
        s_root = 0.5 * (assumedValue+(num/assumedValue))
        z = abs(s_root - assumedValue)
        if(z < tol):
            break
        assumedValue = s_root
    return s_root
print(root(9, 0.000000000001))