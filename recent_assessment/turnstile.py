from collections import deque
time=[0,0,1,5]
dirn=[0,1,1,0]
res=[0]*len(time)

entry,exit=deque(),deque()
for ind,d in enumerate(dirn):
    if d==0:
        entry.append((time[ind],ind))
    else:
        exit.append((time[ind],ind))
timecounter=0
last=-1
while entry or exit:
    #exit
    if exit and exit[0][0]<=timecounter and (last==-1 or last==1 or not entry or (last==0 and entry[0][0]>timecounter)):
        res[exit[0][1]]=timecounter
        exit.popleft()
        last=1
    #entry
    elif entry and entry[0][0]<=timecounter:
        res[entry[0][1]]=timecounter
        entry.popleft()
        last=0
    else:
        last=-1

    timecounter+=1
print(res)





