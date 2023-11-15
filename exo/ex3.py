# def addition(a, b):
#     return int(a) + int(b)
#
#
# def soustraction(a, b):
#     return int(a) - int(b)
#
#
# def multiplication(a, b):
#     return int(int(a) * int(b))
#
#
# def division(a, b):
#     res = int(a) / int(b)
#     if ".0" in str(res):
#         return int(res)
#     else:
#         return res
#
#
# def calcul(string):
#     res = 0
#     for c in string:
#         if c == 'x' or c == '/':
#             operator = c
#             operator_index = string.index(c)
#             left_string = string[0:operator_index]
#             right_string = string[operator_index:-1]
#             for c in string:
#             a = string[string.index('+') - 1]
#             b = string[string.index('+') + 1]
#             res = multiplication(a, b)
#             string_to_replace = a + '+' + b
#             string = string.replace(string_to_replace, str(res))
#         elif c == '/':
#             a = string[string.index('-') - 1]
#             b = string[string.index('-') + 1]
#             res = soustraction(a, b)
#             string_to_replace = a + '-' + b
#             string = string.replace(string_to_replace, str(res))
#     return string
#
#
# inputStr = input("Faites un calcul de base (+, -, x, /) : ")
# print(calcul(inputStr))
