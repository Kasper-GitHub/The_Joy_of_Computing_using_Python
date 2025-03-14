def threesquares(m):
    if m < 0:
        return False
    val = int(m**0.5)+1
    for p in range(val+1):
        for q in range(val+1):
            for r in range(val+1):
                if p**2 + q**2 + r**2 == m:
                    return True
    return False
num = int(input())
print(threesquares(num))

# Legendre's Three-Square Theorem:
# A positive integer m can be expressed as the sum of three squares
# (i.e., m = p^2 + q^2 + r^2 for some integers p, q, r)
# if and only if m is not of the form:
#
# m = 4^a * (8b + 7)
#
# where a and b are non-negative integers.
#
# Explanation of the modulo 8 condition:
# - Any perfect square is congruent to 0, 1, or 4 modulo 8.
# - Therefore, the sum of three squares can only be 0, 1, 2, 3, 4, 5, or 6 modulo 8.
# - It is impossible for three squares to sum to 7 modulo 8.
#
# Steps to apply the theorem:
# 1. Remove all factors of 4 by repeatedly dividing m by 4 (this doesn't affect whether m can be written as a sum of squares).
# 2. If the resulting value is congruent to 7 modulo 8 (i.e., m % 8 == 7),
#    m cannot be expressed as the sum of three squares — return False.
#
# This allows us to quickly eliminate impossible cases without looping through all square combinations.
