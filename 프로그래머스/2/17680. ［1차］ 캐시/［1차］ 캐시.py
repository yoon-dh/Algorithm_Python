from collections import deque

def solution(cacheSize, cities):
    now_set = set()
    cache = deque()
    Q = deque(cities)
    ans = 0

    if cacheSize == 0:
        return len(cities) * 5


    while Q:
        city = Q.popleft().lower()

        if city not in now_set:
            if len(cache) < cacheSize:
                now_set.add(city)
                cache.append(city)
                ans += 5
            else:
                LRU = cache.popleft()
                now_set.discard(LRU)
                now_set.add(city)
                cache.append(city)
                ans += 5
        else:
            cache.remove(city)
            cache.append(city)
            ans += 1
    
    return ans