#print(ord('c')-ord('a'))
# letters wrap out:  if target =='z' and letters=['a','b','c'] ==> return 'a'
def findnextgreatestletter(letters,key):
	if key>letters[-1]:
		return -1
	l=0
	r=len(letters)-1
	while l<=r:
		mid=l+(r-l)//2
		if letters[mid]==key:
			return mid
		if key<letters[mid]:
			r=mid-1 
		else:
			l=mid+1
	# ceil=letters[l]
	return letters[l%len(letters)]    #or write if l==len(letters) return letters[0]

letters=["c","f","j"]
target='a'
print(findnextgreatestletter(letters,target))