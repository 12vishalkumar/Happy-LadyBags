from collections import Counter
from itertools import groupby

def happyLadybugs(S):
    c = Counter(S)
    if('_' in c):
      for i, j in c.items():
        if(j<2 and i!='_'):
            return 'NO'
    else:
        for i, j in groupby(S):
            if(len(list(j))<2):
                return 'NO'
    return 'YES'            
T = int(input())
for i in range(T):
    n = int(input())
    print(happyLadybugs(input()))