import textwrap

def wrap(string, max_width):
    # how to divide string into max_width? list usage - for loop
    #1. make it list
    #2. make sublist with integer
    #3. print sublist
    
    #1.
    list_string = list(string)
    sublist = []
    #2. 
    repeat_num =0
    
    ind = len(string)%max_width
    if(ind ==0):
        repeat_num = int(len(string)/max_width)
    else:
        repeat_num = int(len(string)/max_width +1)
    
    # how to divide sublist?
    for i in range(repeat_num): # repeat 
        for j in range(max_width):
            sublist.append(list_string[i])

    print(sublist)
    
    return

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)