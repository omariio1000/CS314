
def encrypt(phrase: str) -> str:
    if not (all(c.isalpha() or c.isspace() for c in phrase) and phrase.islower):
        print("\nPassword must be all lowercase letters or spaces, no numbers!")
        raise ValueError

    keyword = getKeyWord()
    encrypted = ""

    counter = 0;
    for i in range(len(phrase)):
        shift = keyword[counter % len(keyword)] - 97
        temp = phrase[i]
        
        if (temp == ' '):
            temp = ' '
        else: 
            counter += 1
            temp = chr(ord(temp) + shift % 26)
            if (ord(temp) > 122):
                temp = chr(ord(temp) - 26)
        
        encrypted = encrypted + temp

    
    return encrypted

def decrypt(phrase: str) -> str:
    keyword = getKeyWord()
    decrypted = ""

    counter = 0
    for i in range(len(phrase)):
        shift = keyword[counter % len(keyword)] - 97
        temp = phrase[i]

        if (temp == ' '):
            temp = ' '
        else: 
            counter += 1
            temp = chr(ord(temp) - shift % 26)
            if (ord(temp) < 97):
                temp = chr(ord(temp) + 26)

        decrypted = decrypted + temp

    return decrypted

def getKeyWord():
    keyWord = "chocan"
    temp = []

    for i in range(len(keyWord)):
        temp.append(ord(keyWord[i]))
    
    return temp