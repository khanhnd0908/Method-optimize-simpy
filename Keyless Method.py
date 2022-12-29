def gcd_extended(num1, num2):
    if num1 == 0:
        return num2, 0, 1
    else:
        div, x, y = gcd_extended(num2 % num1, num1)
    return div, y - (num2 // num1) * x, x


a, r, s = gcd_extended(973169, 550351)
print(f'e1∙r + e2∙s = ±1\n\tr = {r}\n\ts = {s}\n')
print(a)

