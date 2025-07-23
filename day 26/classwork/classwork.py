num = int(input("ent num:"))
def  is_positive(num):
    if num > 0:
        print("True")
    else:
        print("False")

is_positive(num)


def max_of_two(a, b,):
    if a > b:
        print(a)
    else:
        print(b)

print(max_of_two(15, 62))


def max_of_three(a, b, c):
    if a > b:
        print(a)
    elif c > b :
        print(c)
    elif a > c:
        print(a)
    elif c > a :
        print(c)    
    elif b > c:
        print(b)
    elif b > a :
        print(b)
    else:
        print()


print(max_of_three(68, 62, 12))

temp = int(input("ent temp:"))
def is_hot(temp):
    
    if temp > 30:
        print("True")
    elif temp < 30:
        print("false")
    
is_hot(temp)


