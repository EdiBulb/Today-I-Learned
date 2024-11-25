# def is_leap(year):
#     leap = False
#     # Write your logic here
    
#     if(year%4==0 & year%400==0):
#         leap = True
#     elif(year%4==0 & year%100==0):
#         leap = False
#     else:
#         leap = False

#     return leap

# year = int(input())
# print(is_leap(year))

# better solution
def is_leap(year):
    
    if(year%4 ==0 and (year % 100 !=0 or year % 400 ==0)):
        return True
    else:
        return False

year = int(input("Enter a year"))
print(is_leap(year))