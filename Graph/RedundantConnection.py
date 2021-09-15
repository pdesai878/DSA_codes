
# if we can reach v from u, then this means that u,v is an redundant edge and we can remove it to eliminate a loop/cycle
def dfs(u,v):
    if u==v:
        return True
    
    visited.add(u)
    for neighbor in adjlist[u]:
        if neighbor not in visited:
            cycle_mila=dfs(neighbor,v)
            if cycle_mila:
                return True
    return False

adjlist=defaultdict(list)
for u,v in edges:
    visited=set()
    if dfs(u,v):        #dfs call will give productive res onlf if u in adj and v in adj. Therefore this will deinitely suffice for whats mentioned in the ques. return the most later added edge causing trouble
        return [u,v]
    adjlist[u].append(v)
    adjlist[v].append(u)