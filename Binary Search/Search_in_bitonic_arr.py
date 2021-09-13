def find_peak(arr):
    l=0
    r=len(arr)-1
    #if l==r, loop breaks and if we get index of peak
    while l<r:
        mid=l+(r-l)//2
        if arr[mid]>arr[mid+1]: # we are in desc part
            r=mid #to make sure that mid is our peak
        elif arr[mid]<arr[mid+1]: #we are in asc part
            l=mid+1 #potential peak can be found towards right subarr
    return l

def bs(arr,start,end):
    l=start
    r=end-1
    asc=arr[l]<arr[r]
    asc=True
    res=-1
    while l<=r:
        mid=l+(r-l)//2
        if arr[mid]==target:
            return mid
        
        if target<arr[mid]:
            if asc:
                r=mid-1
            else:
                l=mid+1
                
        elif target>arr[mid]:
            if asc:
                l=mid+1
            else:
                r=mid-1
    return res
                        
def search(arr,peak):
    if arr[peak]==target:
        return peak
    search_in_asc=bs(arr,0,peak)
    if search_in_asc!=-1:
        return search_in_asc
    search_in_dsc=bs(arr,peak+1,len(arr))
    return search_in_dsc

arr=[4,5,6,7,0,1,2]
target=1
peak=find_peak(arr)
print(search(arr,peak))