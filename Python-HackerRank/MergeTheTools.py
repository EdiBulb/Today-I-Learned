def merge_the_tools(string, k):
    # your code goes here

    # 문자열을 K 크기로 나누기            
    for i in range(0, len(string), k): # for 문에서도 건너 뛰면서 반복할 수 있다는 것을 잊지말 것
        substring = string[i:i+k]
        
        # 중복제거하기기
        unique = ""
        for char in substring:
            if char not in unique:
                unique += char
        print(unique)
        
    
if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)