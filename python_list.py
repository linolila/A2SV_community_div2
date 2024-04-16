if __name__ == '__main__':
    N = int(input())

    list1 = []
    for i in range(N) :
        cmd = input().split()
        if cmd[0] == "insert":
           list1.insert(int(cmd[1]),int(cmd[2]) )
        if cmd[0] == "print" :
            print(list1)
            
        if cmd[0] == "pop" :
            list1.pop()
            
        if cmd[0] == "append" :
           
            list1.append(int(cmd[1]))
        
        if cmd[0] == "sort" :
            list1.sort()
            
        if cmd[0] == "reverse" :
            list1.reverse()
        if cmd[0] == "remove" :
           
            list1.remove(int(cmd[1]))
    
