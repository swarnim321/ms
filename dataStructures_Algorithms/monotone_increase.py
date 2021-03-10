def monotoneIncreasingDigits( N):
        s = list(str(N))
        i =1
        l=len(s)
        while i <= l and int(s[i-1]) <= int(s[i]):
            i+=1
        s[i:]='9'*(l-i-1)
        s[i-1] = str(int(s[i-1])-1)
        print(l-i-1)
        while 0<i<l:
           while int(s[i-1])>= int(s[i]):
                s[i-1] = str(int(s[i-1])-1)
           i-=1
        #s[i+1:] ='9' *(l -i-1)
        print(int("".join(s)))


monotoneIncreasingDigits("574")
