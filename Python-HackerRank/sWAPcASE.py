def swap_case(s):
    swaped_s = s.swapcase()
    return swaped_s

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)