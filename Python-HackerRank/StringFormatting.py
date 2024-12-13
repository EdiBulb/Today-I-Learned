def print_formatted(number):
    
    # your code goes here
    width = len(bin(number)[2:])
    
    for i in range(1, number+1):
        number = i
        octal = oct(number)[2:]
        hexadecimal = hex(number)[2:].upper()
        binary = bin(number)[2:]
        # :> 을 새로 배움
        print(f"{number:>{width}} {octal:>{width}} {hexadecimal:>{width}} {binary:>{width}}")
        
        
if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
    
# 숫자를 입력받으면 그 입력 받은 수만큼 반복은 기본
# 그 숫자의 decimal, octal, hexadecimal, binary를 출력하기
# 즉, 어떻게 decimal을 변환하는지만 알면됨

