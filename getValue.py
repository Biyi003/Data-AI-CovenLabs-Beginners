

def getValue(e,n,i,l):
    netValue = 0
    if (e == 'depressed'):
        netValue += 15
    elif (e == 'happy'):
        netValue += 25
    elif (e == 'confused'):
        netValue += 10
    elif (e == 'bored'):
        netValue += 20

    if (n == 1):
        netValue += 15
    elif (n == 2):
        netValue += 20
    elif (n == 3):
        netValue += 25

    if (i == 'personal'):
        netValue += 15
    elif (i == 'business'):
        netValue += 20
    elif (i == 'project'):
        netValue += 25
    
    if (l == 1):
        netValue += 25
    elif (l == 2):
        netValue += 20
    elif (l == 3):
        netValue += 15
    elif (l == 4):
        netValue += 10

    return netValue

print (getValue('depressed',1,'business',2))

