# if __name__ == '__main__':
#     n = int(input())
#     arr = map(int, input().split())
    
        
#     # finding maximum
#     max = max(arr)
    
#     # remove the max score
#     while max in list_score:
#         list_score.remove(max)
#     runner_up = max(list_score)
#     print(list_score)
    
#     # fingding runner up
#     runup = 0
#     for i in range(n):
#         if(list_score[i]>=runup and list_score[i]<max):
#             runup = list_score[i]
#             # print(runup)
#     print(runup)

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
        
    # finding maximum
    first = max(arr)
    
    # remove the max score
    while first in arr:
        arr.remove(first)
        
    # finding maximum again
    runner_up = max(arr)
    print(runner_up)
    
# what i learned : 
# 1.i can take the maximu out from the list. 
# 2. i can remove the items in the list.
