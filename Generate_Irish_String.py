import random
#GENERATE A STRING CONTAINING A USER SPECIFIED NUMBER OF CAPITALS, LETTERS ,DIGITS AND IRISH-LETTERS
def GenerateIrishString(Caps, Letters, Digits, IrishLetters):
#Data dictionaries containing data used for string and user input
    data ={'charsCaps':"ABCXYZ", 'chars':"qwertyuiopasdfghjklzxcvbnm",'irishChars':"áéúíó",'digits':"0123456789" }
    data2 ={'charsCaps':Caps, 'chars':Letters,'irishChars':IrishLetters,'digits':Digits }
    finalString =""
    arr =['charsCaps', 'chars', 'digits','irishChars',]
    for x in range (0,4):
        item = data[str(arr[x])]
        item2 = data2[str(arr[x])]
        for y in range (0,item2):#get random item from each dataset and add to final string
            rand = random.randint(0,len(item)-1)
            finalString+=data[str(arr[x])][rand]
    finalString = ''.join(random.sample(finalString, len(finalString)))#Shuffle the content
    return finalString
print(GenerateIrishString(2,2,2,2))
