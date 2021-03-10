def palindrome(number):
    currentDigit=0
    copyNumber,reverseNumber=0,0
    copyNumber=number
    while copyNumber!=0:
        currentDigit=copyNumber%10
        reverseNumber=(reverseNumber*10)+currentDigit
        copyNumber=copyNumber//10

    if reverseNumber==number:
        return "yes"
    else:
        return "No"
def strng_palindrome(strng):
    l=len(strng)
    for i in range(l):
        if strng[i]!=strng[l-1-i]:
            print("No")
    else:
        print ("yes")


number=(input("enter the number"))
#x=palindrome(number)
x=strng_palindrome(number)
#print(x)

