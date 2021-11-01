# arr=[10,12,15]
arr=[9, 2, 8, 4, 5, 7, 6, 0]
s=0
arr.sort()
print(arr)
n=len(arr)
=> rearrange the circular arr such that sum of diff of two consecutive arr el is max
# for i in range(n):
#     s+=abs(arr[n-i-1]-arr[i])
# print(s)

=>rearrange arr to minmize sum of product of consecutive pair elements
for i in range(n//2):
    s+=(arr[i]*arr[n-i-1])
    print(arr[i],arr[n-i-1])
print(s)