if __name__ == '__main__':
    N = int(input())

    list = []    
    for i in range(N):
        command = input().split()
                
        # insert
        if (command[0] =="insert"):
            list.insert(command[2], command[1])
        # print
        elif(command[0] =="print"):
            
            print(list(map(int, list)))
        # remove
        elif(command[0] == "remove"):
            list.remove(command[1])
        # append
        elif(command[0] == "append"):
            list.append(command[1])
        # sort
        elif(command[0] == "sort"):
            list.sort()
        # pop
        elif(command[0] == "pop"):
            list.pop(command[1])
        # reverse
        elif(command[0] == "reverse"):
            list.reverse()
        else:
            print("error")