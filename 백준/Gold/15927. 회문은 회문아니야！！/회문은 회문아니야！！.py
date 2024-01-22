
def palin(search) :
    for i in range(len(search)//2) :
        if search[i] != search[-(i+1)] :
            return False 
    return True 

def same(search) :
    for i in range(1,len(search)) :
        if search[i] != search[0] : return False 
    return True 

if __name__=="__main__" :
    char = input()
    if palin(char) :
        print(-1 if same(char) else len(char)-1)
    else :
        print(len(char))