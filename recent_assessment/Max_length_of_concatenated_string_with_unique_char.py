def partition_possible(target,n):
    s=0
    part=1
    for el in arr:
        s+=el
        if s>target:
            part+=1
            s=0
    return part

def getsum(arr):
    l=arr[-1]
    r=sum(arr)
    while l<=r:
        mid=l+(r-l)//2
        part=partition_possible(mid,n)
        if part==n:
            return mid
        if part<mid:
            r=mid 
        else:
            l=mid

def getsubsets(op,s,n):
    if s==0:
        res.append([*op])
        return
    if n==0 and s!=0:
        return

    getsubsets(op+[arr[n-1]],s-arr[n-1],n-1)
    getsubsets(op,s,n-1)


n=3
arr=[1,2,3,4,5]
s=getsum(arr)
res=[]
getsubsets([],s,len(arr))
print(res)

