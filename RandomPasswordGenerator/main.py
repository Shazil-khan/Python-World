import string
import random

def getRandomPassword(len):
    mystring = string.ascii_letters
    digits = string.digits
    special ="!@#$%^&*()_+>?<|}[],~`"
    passwordlist = list(mystring + digits + special)
    print(passwordlist)
    random.shuffle(passwordlist)
    orignalPassword=[]
    for i in range(len):
        orignalPassword.append(random.choice(passwordlist))
    
    return "".join(orignalPassword)

print(getRandomPassword(7))