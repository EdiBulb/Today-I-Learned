'''Apply what i learned from Algorithm'''

# f-string apply
def print_full_name(first, last):
    print(f"Hello {first} {last}! Welcome to Algorithm world")

# change string apply - utilizing LIST
def change_title(title, position, character):
    l = list(title)
    l[position] = character
    new_title = ''.join(l)
    return new_title

def count_substring(string, sub_string):
    count = 0
    for i in range(len(string) - len(sub_string) +1):
        if string[i:i+len(sub_string)] == sub_string:
            count+=1 
    return count
    
if __name__ == '__main__':
    print("Pls put your name")
    first_name = input("given name:")
    last_name = input("surname:")
    print_full_name(first_name, last_name)
    

    existing_title = input("Previous name: ")
    index = input("what is index: ")
    new_title = input("new name:")
    new_name=change_title(existing_title, int(index), new_title)
    print(new_name)
    
    # coffee order
    order = "We will order one americano coffee, latte coffee"
    number_of_coffee= count_substring(order, "coffee")
    print(number_of_coffee)