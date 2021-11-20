def distinctSubKOdds(arr, n, k):
    ans=0
    n=len(arr)
    s=set()
    for i in range(n):
        temp=0
        for j in range(i,n):
            if arr[j]%2!=0:
                temp+=1
            if temp>k:
                break
            if temp<=k:
                #print(arr[i:j+1])
                string="".join(str(arr[i:j+1]))
                if string not in s:
                    ans+=1
                s.add(string)
    return ans