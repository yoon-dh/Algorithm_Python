from itertools import combinations
from collections import Counter

def solution(orders, course):
    ans = []
    
    for i in course:
        temp = []
        for j in orders:
            temp.extend(list(combinations(sorted(j), i)))
        
        C = Counter(temp)
        print(C.values())
        
        if C:
            if sorted(C.values())[-1] > 1:
                for k, v in C.items():
                    if v == sorted(C.values())[-1]: 
                        ans.append("".join(k))
                
    return sorted(ans)
    
    
    
    
    
    
    