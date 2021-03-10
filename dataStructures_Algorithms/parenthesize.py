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

def parenthesize(exp):


postfix = "a+b*c"
infix=parenthesize(postfix.strip())
