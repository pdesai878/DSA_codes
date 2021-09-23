#euclid algo for finding gcd of two numbers. This algo is based on long division method
#divisor becomes dividend and remainder becomes divisor, when remainder==0 return divisor 
def gcd(a,b): 
    if b%a==0:
        return a 
    return gcd(b%a,a)

print("gcd",gcd(12,18))


#product(a*b)=gcd(a,b)*lcm(a*b)
# ==> lcm=product//gcd
import math
print("lcm",(12*18)//math.gcd(12,18)) #use of inbuilt gcd function from math lib

#TC for finding gcd=O(logn)
