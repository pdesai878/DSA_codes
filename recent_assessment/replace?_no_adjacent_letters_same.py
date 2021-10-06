"""
Replace ‘?’ in a string such that no two adjacent characters are same
"""

string="b?aa?"
string=list(string)
n=len(string)
if string[0]=="?":
    string[0]='a'
    if string[0]==string[1]:
        string[0]=chr(ord(string[1])+1)

for i in range(1,n-1):
    if string[i]=="?":
        string[i]='a'
        if string[i]==string[i-1]:             # aab
            string[i]=chr(ord(string[i-1])+1)
        if string[i]==string[i+1]:
            string[i]=chr(ord(string[i+1])+1)
        if string[i]==string[i-1]:              # cbb and i is at index1
            string[i]=chr(ord(string[i-1])+1)

if string[n-1]=="?":
    string[n-1]='a'
    if string[n-1]==string[n-2]:
        string[n-1]=chr(ord(string[n-2])+1)

print("".join(string))






   
