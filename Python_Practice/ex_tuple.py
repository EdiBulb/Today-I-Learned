empty_tuple=()

single_element_tuple = (42,)
numbers = (1, 2, 3, 4)

names = "Alice", "Bob", "Charlie"

print(empty_tuple)
print(single_element_tuple)
print(numbers)
print(names)

print(numbers[0])
print(numbers[1])


numbers2 = (10, 20, 30, 40)
print(numbers2[1:3])
print(numbers2[:3])
print(numbers2[-1])

# Tuple Operation
a = (1, 2, 3)
b = (4, 5)
c = a+b
print(c)

# Repetition
repeat = (1, 2, 3)
repeat2 = repeat*2
print(repeat2)

# Membership Test
party_member = ("Harry", "Goun", "Nikki", "Gajesh")
print("Nikki" in party_member)


# Unpacking Tuples
point = (3, 4)
x, y = point
print(x)
print(y)

couple = ("YJ", "NB")
man, women = couple

print(man)
print(women)