ans=0
def rev(n):
    global ans
    if not n:
        return 
    r=n%10
    ans=ans*10+r
    rev(n//10)
    
 

rev(123)
print(ans)


*******************method 2*************************
def rev(n,c):
    if not n:
        return 0
    r=n%10 
    c-=1
    return rev(n//10,c)+ r*pow(10,c)

print(rev(123,3))


******************** iterative method ***************
n=123
ans=0
while n:
    r=n%10
    ans=ans*10+r
    n//=10

print(ans)
