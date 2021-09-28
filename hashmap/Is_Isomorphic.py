
# class Solution:
#     def isIsomorphic(self, s: str, t: str) -> bool:
#         #its mentioned in constraints that len(s)==len(t)
        
#         """
#         method 2: check encoding of s and t
#         create a method to generate encoding for a string
#         """
#         def encode(s):
#             encoding=[]
#             dicti=dict()
#             count=0
#             for ch in s:
#                 if ch in dicti:
#                     encoding.append(dicti[ch])
#                 else:
#                     encoding.append(count)
#                     dicti[ch]=count
#                     count+=1
#             return encoding
        
#         return encode(s)==encode(t)
                    
        
        
#         """
#           method 1: character mapping: we need to check two way mapping. if two way mapping i.e from s->t and t->s of all char pair s,t is possible, then s and t are isomorphic
#         """
#         s_t=defaultdict(str)
#         t_s=defaultdict(str)
        
#         for c1,c2 in zip(s,t):
#             if c1 not in s_t and c2 not in t_s:
#                 s_t[c1]=c2
#                 t_s[c2]=c1
                
#             elif s_t[c1]!=c2 or t_s[c2]!=c1:
#                 return False
#         return True
            
        

#follow up question:  GROUP ISOMORPHIC STRINGS

strings=['aab', 'xxy', 'xyz', 'abc', 'def', 'xyx']
# op:
# [['xyx'], ['xyz', 'abc', 'def'], ['aab', 'xxy']]

def encode(s):
    encoding=[]
    dicti=dict()
    count=0
    for ch in s:
        if ch in dicti:
            encoding.append(dicti[ch])
        else:
            encoding.append(count)
            dicti[ch]=count
            count+=1
    return tuple(encoding)             #convert to tuple as u cant have list as a key of dicti
    							       #error: unhashable type: 'list'


dicti=dict()
for s in strings:
	enc=encode(s)
	if enc in dicti: 
		dicti[enc].append(s)
	else: 
		dicti[enc]=[s]
res=[dicti[key] for key in dicti.keys()]
print(res)
	


