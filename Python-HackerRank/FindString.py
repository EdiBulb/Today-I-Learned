def count_substring(string, sub_string):
    count = 0
    for i in range(len(string) - len(sub_string) + 1): # how many rotate in string?
        if string[i:i+len(sub_string)] == sub_string: # check if that part of string is same with sub_string
            count +=1 # if it is same, +1
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)