def solution(record):
    
    record_list = [i.split(' ') for i in record]
    
    user_dict = dict()
    
    result = []
    for i in record_list:
        if i[0] == "Enter":
            user_dict[i[1]] = i[2]
            result.append([i[1],"님이 들어왔습니다."])
        elif i[0] == "Leave":
            result.append([i[1],"님이 나갔습니다."])
        else:
            user_dict[i[1]] = i[2]
    
    ans = []
    for i in result:
        i[0] = user_dict[i[0]]
        ans.append(''.join(i))
        
    
    # print(ans)
    return ans

# result에 userid로 들어왔다 나갔다를 적어두고 
# 모든 과정 완료 후 딕셔너리에서 꺼내서 싹 넣어주면 될 것 같음