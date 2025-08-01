def numbers(n):
    for i in range(1, n + 1):
        print(i)

numbers(10)


def greet(name):
    print("Hello " + name)

greet("Ixvis Tolma")


def gamravleba(x, y):
    result = x * y
    print(result)

gamravleba(5, 7)

def shebruneba(list):
    for i in range(len(list) - 1, -1, -1):
     print(list[i], end=' ')
    print()
  
shebruneba([1, 2, 3, 4, 5])


def metia10ze(list):
    axali_sia = []
    for num in list:
        if num > 10:
            axali_sia.append(num)
    return axali_sia

og_sia = [6, 18, 6, 65, 8, 73]
result = metia10ze(og_sia)
print(result)




def remove(list):
    return list[1:-1]

elementebi = ['ki', 'ara', 'tu', 'diax', 'eee']
list_axali = remove(elementebi)
print(list_axali) 


def list_gamravleba(list1, list2):
    jami = 0
    jami1 = 0

    for num in list1:
        jami += num

    for num in list2:
        jami1 += num

    result = jami * jami1
    return result

a = [3, 9, 8]
b = [46, 11, 93, 0]
print(list_gamravleba(a, b))           


def gaormagebit_list(num):
    double = []
    i = 0
    while i < len(num):
        double.append(num[i] * 2)
        i += 1
    return double

list = [12, 33, 9]
print(gaormagebit_list(list))

def luwebi(numbers):
    luwi_ricx = []
    for num in numbers:
        if num % 2 == 0:
            luwi_ricx.append(num)
    return luwi_ricx

nums = [1, 2, 3, 4, 5, 6]
print(luwebi(nums))



def Saxelebi_Nze(names):
    namebi = []
    for name in names:
        if name.startswith("N"):
            namebi.append(name)
    return namebi

names_list = ["Nino", "Giorgi", "Natia", "Luka", "Nuca"]
print(Saxelebi_Nze(names_list))


def ricxvi(a, b):
    return a ** b

print(ricxvi(2, 3))

def sigrdze(winadadeba):
    words = winadadeba.split()
    for word in words:
        print(f" '{word}' {len(word)}")
        
sigrdze("sityvebit winadadeba")