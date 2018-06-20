#QUESTION 1

radius=float(input("enter radius"))
def area(rad):
    area=3.14*rad*rad
    return area
ar=area(radius)
print(ar)


#QUESTION 2
def perfect(n):
    sum=0
    for i in range(1,n):
        if(n%i==0):
            sum=sum+i
    if sum==n:
        return True
    else:
        return False
for i in range(1,1001):
    if(perfect(i))==True:
        print(i)

#QUESTION 3
n=12
def multi_table(n):
    j=n*i
    return j
for i in range(1,11):
    print(n,"x",i,"=",multi_table(n))


#QUESTION 4
def power(a,b):
    if b==1:
        return a
    if b!=1:
        return(a*power(a,b-1))
a=int(input("enter any number"))
b=int(input("enter any number"))
print(a,"^", b, "=", power(a,b))


#QUESTION 5
d={}
n=int(input("enter any number"))
def factorial(n):
    if(n==1 or n==0):
        return 1
    else:
        return n*factorial(n-1)
d[n]=factorial(n)
print(d)


