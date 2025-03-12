def delit(a,b):
    return a/b

def minus(a,b):
    return a-b

def mySumm(a,b,func=""):
    return a+b

def mult(a,b):
    return a*b

userInput = input("mida sa tahad teha?")

if userInput == "1":
    tegevus = mySumm
elif userInput == "2":
    tegevus = minus
elif userInput == "3":
    tegevus = delit
else:
    tegevus = mult
    
print(tegevus(5,5))