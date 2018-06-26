n = int(input("Enter number of terms:"))

n1=0
n2=1
n3=0
if n<1:
    print("Enter a positive number")
elif n==1:
    print(n1,",",n2,end=",")
else:
    print(n1, ",", n2, end=",")
    while(n>2):
       n3=n2
       n2=n1+n2
       n1=n3
       print(n2, end=",")
       n=n-1