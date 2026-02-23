def biggest (a,b,c):
    if a > b and a> c:
        return a
    elif b > a and b > c:
        return b
    elif c > a and c > b:
        return c

def smallest (a,b,c):
    if a < b and a < c:
        return a
    elif b < a and b < c:
        return b
    elif c < a and c < b:
        return c
a = 1
b = 2
c = 3
biggest(a,b,c)
smallest(a,b,c)
print (f'biggest {biggest(a,b,c)}')
print (f'smallest {smallest(a,b,c)}')