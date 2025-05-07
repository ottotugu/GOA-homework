
# <, > მეტია ან ნაკლებია
# <=, >= მეტია ტოლია ან ნაკლები ტოლია
# == ტოლია
# != არ ტოლია

#print(True and False) 
#False თუ წერია სადმე გამოვა False

#print(True or False)
#True თუ წერის სადმე გამოვა True

print(True and 6<7 or "hello" != 5.4 and False or 7-7 < 9+2)
#  True and True არის True
#  "hello != 5.4" არის True 
#  ამიტომაც True or True იქნება True
#  True and False იქნება False
#  True or False იქნება True

# integer-ით და integer-ით გამოიყენება ნებისმიერი შედარების ოპერატორები
# integer-ით და float-ით გამოიყნება ნებისმიერი შედარების ოპერატორები
# integer-ით და string-ით გამოიყენება მხოლოდ != 
# string-ით და string-ით გამოიყენება == და !=

print(False and False)
print(False and True)
print(True and False)
print(True and True)

print(True or False)
print(True or True)
print(False or True)
print(False or False)