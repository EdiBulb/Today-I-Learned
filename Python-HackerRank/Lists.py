if __name__ == '__main__':
    N = int(input())

    my_list = []    
    for i in range(N):
        command = input().split()
                
        # insert
        if (command[0] =="insert"):
            my_list.insert(int(command[1]), int(command[2]))
        # print
        elif(command[0] =="print"):
            
            print(my_list)
        # remove
        elif(command[0] == "remove"):
            my_list.remove(int(command[1]))
        # append
        elif(command[0] == "append"):
            my_list.append(int(command[1]))
        # sort
        elif(command[0] == "sort"):
            my_list.sort()
        # pop
        elif(command[0] == "pop"):
            if len(command) > 1:  # pop with index
                my_list.pop(int(command[1]))
            else:  # pop last element
                my_list.pop()
        # reverse
        elif(command[0] == "reverse"):
            my_list.reverse()
        else:
            print("error")