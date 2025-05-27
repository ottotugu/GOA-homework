
# while loop ამეორებს სანამ რამე ბრძანება არ გააჩერებს ხოლო for loopს 
# ჭირდება range ბრძანება სადაც წერია რამდენჯერ უნდა განმეორდეს


age = int(input("Ent yo age: "))

if age >= 18:
    print("you are big adult")
if age <= 18:
    print("Lil boy")

i = 1

while i <= 10:
    print(i)
    i = i + 1

i = 10

while i >= 1:
    print(i)
    i = i - 1

i = 0
while i < 1:
    print('cavatanem')
    i = i - 1


