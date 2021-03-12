def my_f(t):
    a = t.isascii()
    b = t.islower()
    if a and b is True:
        return t.title()
    else:
        print('Программа принимает только маленькие латинские буквы')


print(my_f('wonderful world'))
