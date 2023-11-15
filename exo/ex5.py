def factorielle(n):
    if type(n) is not int or n < 0:
        return "La fonction factorielle n'est définie que pour les entiers naturels."
    elif n == 0:
        return 1
    elif n == 1:
        return n
    return n * factorielle(n - 1)


print(factorielle(0))
print(factorielle(1))
print(factorielle(2))
print(factorielle(3))
print(factorielle(4))
print(factorielle(5))
print(factorielle(-1))
print(factorielle(5.5))
