arr=[5, 3, 0, 7, 4]
arr.sort()
# a=""
# b=""
# for i in range(0,len(arr),2):
#     a+=str(arr[i])
#     if i+1<len(arr):
#         b+=str(arr[i+1])

# print(a,b)      
# print(int(a)+int(b))

a=0
b=0
for i in range(0,len(arr),2):
    a=a*10+arr[i]
    if i+1<len(arr):
        b=b*10+arr[i+1]
print(a,b)
print(a+b)


# num=53074
# digits=0
# p=num
# arr=[]
# while p:
#     digits+=1
#     arr.append(p%10)
#     p//=10





