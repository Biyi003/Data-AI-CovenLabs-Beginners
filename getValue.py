def getValue(a):
    s = a.split(',')
    e = s[0]
    n = s[1]
    i = s[2]
    l = s[3]
    a = s[4]
    m = s[5]
    
    netValue = 0
    if (e == 'Depressed'):
        netValue += 5
    elif (e == 'Happy'):
        netValue += 15
    elif (e == 'Confused'):
        netValue += 5
    elif (e == 'Bored'):
        netValue += 10

    if (n == '1'):
        netValue += 10
    elif (n == '2'):
        netValue += 15
    elif (n == '3'):
        netValue += 20

    if (i == 'Personal'):
        netValue += 5
    elif (i == 'Business'):
        netValue += 10
    elif (i == 'Project'):
        netValue += 15
    
    if (l == '1'):
        netValue += 20
    elif (l == '2'):
        netValue += 15
    elif (l == '3'):
        netValue += 10
    elif (l == '4'):
        netValue += 5

    if (a == '1'):
        netValue += 10
    elif (a == '2'):
        netValue += 15
    elif (a == '3'):
        netValue += 5

    if (m == '1'):
        netValue += 10
    elif (m == '2'):
        netValue += 15
    elif (m == '3'):
        netValue += 5

    return str(netValue)


# getValue(e,n,i,l,a,m)

# print (getValue('Happy,3,Project,1,2,2'))

file=open("output.txt","w+");

with open("input.txt") as task:
    for j in range(1,101):
        k=str(task.readline());
        file.write(getValue(str(k))+"\n");

file.close();
