

def split_and_join(line):
    # write your code here
    split_list = line.split(" ")
    split_list = "-".join(split_list)
    return split_list

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)