BAGS = 10
ITEMS = 20
COMMON = 4
import random
from typing import List,Tuple,Set

# generate bags
item = list(range(ITEMS))
bs = [random.sample(item,random.randrange(6,ITEMS)) for _ in range(BAGS)]
# print(bs)

# dicts of occurences
d = {}
for i in range(ITEMS):
    d[i]={j for j,b in enumerate(bs) if i in b}
# let us sort by their frequency
od = sorted(d.items(), key = lambda x: len(x[1]), reverse=True)
# print(od)

b = len(od[0][1]&od[1][1]&od[2][1])  # initial best length
j = 0                                # index
l:List[Tuple[int,Set[int]]] = []     # stack of part-solution  
sol:List[int] = []
sols: List[List[int]] = []     
sols_l = 0                           # actually best length
while True:
    if j<0 or j>=ITEMS and l==[]:    # we have checked everything
        break
    elif j>=ITEMS:                   # no more options at this level
        j,_ = l.pop()
    elif len(l)==0 and len(od[j][1])>=b:  # maybe there exists here a solution here
        l=[(j,od[j][1])]
    elif len(l)==0:                  # do not try a hopeless variant
        pass
    else:
        s = od[j][1]&l[-1][1]
        if len(s)>=b:                # lets calculate 
            if len(l)<COMMON-1:      # not a solution yet, store the subresult
                l.append((j,od[j][1]&l[-1][1]))
            elif len(l)==COMMON-1:   # a new solution 
                b = len(od[j][1]&l[-1][1])
                sol = [i[0] for i in l]
                sol.append(j)
                if sols and sols_l<b: # a better solution
                    sols=[]
                    sols_l=b
                sols.append(sol)
    j+=1
out=[]
for sol in sols:
    out.append(sorted([od[j][0] for j in sol]))
print(out)