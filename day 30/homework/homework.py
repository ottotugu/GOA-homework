def mdzimeebi(sentence):
    words = sentence.split()
    return ", ".join(words)

print(mdzimeebi("mashalah ma brada"))


def grdzeli(sityva):
    wordo = sityva.split()
    for word in wordo:
        print(f"{word}: {len(word)}")
        
grdzeli("ara tu ki game ari bneli")

def remove(winadadeb):
    words = winadadeb.split()  
    return " ".join(words)

print(remove("chemo     netarebav   da lamazoo   "))


def no_space(kideee):
    words = kideee.split()
    return "-".join(words)

print(no_space("erti ori da sami she"))


def ukugma(sentence):
    words = sentence.split()
    ukugma = words[::-1]
    return " ".join(ukugma)

print(ukugma("yo da yos"))

