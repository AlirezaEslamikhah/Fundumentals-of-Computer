def q1_get_max(a,b,c):
    bigger=a
    if b>bigger:
        bigger = b
    if c > bigger:
        bigger =c
    return bigger

def q2_is_right_angled(a,b,c):
    if a**2 == b**2 + c**2 or b**2 == a**2 + c**2 or c**2 == b**2 + a**2:
        return True
    else:
        return False

def q3_array_fsum(a,b,c):
    sum=0
    for i in range(len(a)):
        sum = sum + (a[i]*b[i] + c[i])
    return sum


def q4_string_shuffle(strr):
    z = []
    for i in strr:
        z.append(i+1)
        z.append(i)
    return z
