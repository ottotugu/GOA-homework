
# "string"
# 2025
# 2.15
# ნებისმიერი ინტეგერი შეგვიძლია გადავაქციოთ სტრინგად str() დახმაებით

print(type(str(2025)))

# სტრინგი შეგვიძლია გადავაქციოთ ინტეგერად int() დახმაებით თუ მაშსი არის რიცხვები
name = "23049"
print(type(int(name)))


#ჩვენ შეგვიძლია გადავაქციოთ სტრინგი float ად თუ მასში რიცხვები ან ათწილადები წერია და შეგვიძლია
#ნებისმიერი ინტეგერი ფლოატად
number = 23
print(type(float(number)))
print(float(number))

# > < >= <= == !=
#boolean = True False
# True False

print(5 > 2)
print(5 == 2)
print(5 != 2)
print("hello" == "hello")
print("hello" != "hello")

l = 2
i = 5
print(l < i)

# True = 1
# False = 0
print(False < True)

# and or - და, ან
print(True and False) 
#False თუ წერია სადმე გამოვა False
print(True or False)
#True თუ წერის სადმე გამოვა True
print(5>2 and 8<2)

