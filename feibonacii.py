
n=int(input("需要第几项\n"))
a=0
b=1
i=2
if n==1:
    print(a)
elif n==2:
    print(b)
else:
    while(i<n):
        result=a+b
        a=b
        b=result
        i+=1
    print(result)
    
