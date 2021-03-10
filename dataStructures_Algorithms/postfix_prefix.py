def isOperand(x):
    return ((x >='a' and x<='z') or
           ( x >='A' and x <='Z'))

def getPreceedence(ch):
    if ch=='+' or ch=='-':
        return 1
    elif ch=='*' or ch=='/':
        return 2
    elif ch=='^':
        return 3
    else:
        return 0

def getInfix(exp):
    s=[]
    for i in exp:
        if (isOperand(i)):
            s.insert(0,i)
        else:
            op1=s.pop(0)
            op2=s.pop(0)
            s.insert(0,"("+op2 + i + op1 +")")
    return(s[0])

def getpostfix(exp):
    s=[]
    res=[]
    for i in range(len(exp)):
        if isOperand(exp[i]):
            res.append(exp[i])
        elif exp[i]=="(" or exp[i]==")":
            continue
        else:
            prec = getPreceedence(exp[i])
            if len(s)>0:
                while len(s)>0 and getPreceedence(s[0])>prec :
                    res.append(s.pop(0))
            s.insert(0,exp[i])
    while s:
        res.append(s.pop())
    print("".join(res))

def getprefix(exp):
    s = []
    res = []
    prec_stack = 0
    for i in range(len(exp)-1,-1,-1):
        if isOperand(exp[i]):
            res.append(exp[i])
        elif exp[i] == "(" or exp[i] == ")":
            continue
        else:
            prec = getPreceedence(exp[i])
            if len(s) > 0:
                while len(s)>0 and getPreceedence(s[0])>prec:
                    res.append(s.pop())
            s.insert(0, exp[i])

    while s:
        res.append(s.pop(0))
    res = res[::-1]
    print("".join(res))


postfix = "ab*c+"
infix=getInfix(postfix.strip())
print(infix)
getpostfix(infix)
getprefix(infix)
