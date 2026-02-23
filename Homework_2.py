basic = []

def basic_math (a = 10, b = 2):
    if b == 0:
        print (b, "is invalid")
        return 0
    basic.append (a + b)
    basic.append (a - b)
    basic.append (a / b)
    basic.append (a * b)

basic_math ()
print (basic)

# #option 2:
#  a = int(input("Enter a number: "))
#  b = int(input("Enter another number: "))
#
# basic = []
#
# def basic_math (a = 10, b = 2):
#     if b == 0:
#         print (b, "is invalid")
#         return 0
#     basic.append (a + b)
#     basic.append (a - b)
#     basic.append (a / b)
#     basic.append (a * b)

basic_math (a,b)
print (basic)