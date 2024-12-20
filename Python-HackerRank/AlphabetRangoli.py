def print_rangoli(size):
    # generate the alphabet
    alphabet = [chr(96+i) for i in range(1, size + 1)]
    print(alphabet)
    
    # calculate the with of the rangoli
    width = 4*size -3
    
    # build each row of the rangoli
    rows = []
    for i in range(size):
        left_part = alphabet[size - i -1:size]
        full_row = "-".join(left_part[::-1]+left_part[1:])
        rows.append(full_row.center(width, '-'))
    
    # combine the rows (top + bottom)
    rangoli = "\n".join(rows + rows[-2::-1])
    print(rangoli)
    


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
    