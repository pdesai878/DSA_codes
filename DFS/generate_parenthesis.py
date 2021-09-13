#iterative solution      method: ip-op

n=3
res=[]
stack=[["",n,n]]
while stack:
    op,o,c=stack.pop()
    if o==0 and c==0:
        res.append(op)
    else:
        if o:
            stack.append([op+'(',o-1,c])
        if o<c:
            stack.append([op+')',o,c-1])
print(res)
