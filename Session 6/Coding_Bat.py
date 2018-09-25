def diff21 (n):
    if n > 21:
        return abs(n - 21) * 2
    else:
        return abs(n-21)

# print(diff21(19))
# print(diff21(11))
# print(diff21(21))
# print(diff21(40))

def cigar_party(cigars, is_weekend):
    if is_weekend:
        return True
    else:
        if 40<=cigars<=60:
            return True
        else:
            return False

print(cigar_party(30, False))
print(cigar_party(50, False))
print(cigar_party(70, True))