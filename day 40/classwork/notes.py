# not da in gamoiyeneba if tan not aris chveulebrivi uaryobidi funqcia romelic abrunebs true da falses
# in kide agnishnavs funqciit mocemul winadadebashi aris tu ara raime elementi

def manual_capitalize(s):
    if not s:
        return s 
    first = s[0].upper()
    rest = s[1:].lower()
    return first + rest

def manual_capitalize(i):
    sen = i.split(' ')
    capitalized_words = []

    for word in sen:
        if word:
            first = word[0].upper()
            rest = word[1:].lower()
            capitalized_words.append(first + rest)
        else:
            capitalized_words.append('')

    return ' '.join(capitalized_words)