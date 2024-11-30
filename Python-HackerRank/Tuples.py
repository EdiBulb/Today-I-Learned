if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    
    # how to move all element from the integer_list to tuple_t?
    tuple_t = tuple(integer_list)
    
    print(hash(tuple_t))
    