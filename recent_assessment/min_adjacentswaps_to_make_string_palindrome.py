# Given a string, what is the minimum number of adjacent swaps required to convert a string into a palindrome. If not possible, return -1.
from collections import Counter
s="aabb"
s=list(s)
#we keep two pointers
l=0
r=len(s)-1
#edge case to check:  a string can be a valid palindrome iff it contains only 1 char having odd freq.
d=Counter(s)
# cnt=0
# for ch,freq in d.items():
#     if freq%2!=0:
#         cnt+=1
#         if cnt>1:
#             return False
swaps=0
while l<r:
    if s[l]!=s[r]:
        #have another pointer k and decreement its value untill ch at l==ch at r
        k=r 
        while s[l]!=s[k] and l<k:
            k-=1

        #if l==k:  it means that ch at index l is the one which should be at the middle, 
        #swap(l,l+1)

        if l==k:
            s[l],s[l+1]=s[l+1],s[l]
            swaps+=1
            continue

        if l<k and s[l]==s[k]:  #if this cond is true, keep swapping (k,k+1) untill k<r
            while k<r:
                s[k],s[k+1]=s[k+1],s[k]
                swaps+=1
                k+=1

            #eventually after the above loop ends, ch at l will be equal to ch at r. Therefore shrink window
            l+=1
            r-=1
    else:
        l+=1
        r-=1

print(swaps)






