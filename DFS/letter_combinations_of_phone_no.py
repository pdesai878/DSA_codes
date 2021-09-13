# def get_combinations(op,ip):        
#     if not ip:
#        res.append(op)
#        return
            
#     for el in dicti[ip[0]]:
#         dfs(op+el,ip[1:])


def get_combinations(op,index):
	if len(op)==len(digits):
		res.append("".join([*op]))
		return

	dig=digits[index]
	for el in dicti[dig]:
		op.append(el)
		get_combinations(op,index+1)
		op.pop()

digits="234"      
dicti={'2':'abc',
      '3':'def',
      '4':'ghi',
      '5':'jkl',
      '6':'mno',
      '7':'pqrs',
      '8':'tuv',
      '9':'xyz'}

res=[]
comb=[]
get_combinations(comb,0)
print(res)