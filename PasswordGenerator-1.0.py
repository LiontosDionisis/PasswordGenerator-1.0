import random
nums = [2,3,4,5,6,7,8,9,0]
symbols = ['/','_','-','.',',']
letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
           'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
yesnum = False
yessymbol = False
def numcheck():
    global yesnum
    nums = [2,3,4,5,6,7,8,9,0]
    numbers = input("Do you want numbers in your password? type 'y' or 'n':")
    if 'y' in numbers:
        yesnum = True
        return yesnum
    else:
        yesnum = False
        return yesnum
    
def symbolcheck():
    global yessymbol
    symbols = ['/','_','-','.',',']
    symbolcheckity = input("Do you want symbols in your password? type 'y' or 'n': ")
    if 'y' in symbolcheckity:
        yessymbol = True
        return   yessymbol
        
    else:
        yessymbol = False
        return  yessymbol

def passgen():
    passlen = int(input("Type a number for your password length: "))
    numcheck()
    symbolcheck()
    if yesnum == True and yessymbol == False:
        res = nums + letters
        random.shuffle(res)
        print(*res[0:passlen], sep ='')
    if yesnum == True and yessymbol == True:
        res = nums + letters + symbols
        random.shuffle(res)
        print(*res[0:passlen], sep = '')
    if yesnum == False and yessymbol == True:
        res = letters + symbols
        random.shuffle(res)
        print(*res[0:passlen], sep = '')
    if yesnum == False and yessymbol == False:
        random.shuffle(letters)
        print(*letters[0:passlen],sep = '')
    
        
passgen()
        
