stroka=[56,91,11,2]
print(stroka)

def stroka_more():
    str_s = [str(x) for x in stroka]
    number = int("".join(sorted(str_s, key=lambda x: x[0], reverse = True)))
    return number


print(stroka_more())