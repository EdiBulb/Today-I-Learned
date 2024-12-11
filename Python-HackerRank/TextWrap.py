import textwrap

# def wrap(string, max_width):
#     # how to divide string into max_width? list usage - for loop
#     #1. make it list
#     #2. make sublist with integer
#     #3. print sublist
    
#     #1.
#     list_string = list(string)
#     sublist = []
#     #2. 
#     repeat_num =0
    
#     ind = len(string)%max_width
#     if(ind ==0):
#         repeat_num = int(len(string)/max_width)
#     else:
#         repeat_num = int(len(string)/max_width +1)
    
#     # how to divide sublist?
#     for i in range(repeat_num): # repeat 
#         for j in range(max_width):
#             sublist.append(list_string[i])

#     print(sublist)
    
#     return
'''usage textwrap.fill()'''
# def wrap(string, max_width):
#     return textwrap.fill(string, max_width)

'''Alternative way'''
def wrap(string, max_width):
    wrapped = ""
    for i in range(0, len(string), max_width): # step에 익숙하지 않았구나.
        wrapped +=string[i:i+max_width] + "\n" # string 에 더할 수도 있구나
    return wrapped.rstrip()

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)