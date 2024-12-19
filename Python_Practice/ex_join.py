# seperator.join(iterable)
words = ['Hello', 'World', 'Python']
result = ' '.join(words)
print(result)


letters = ['a', 'b', 'c', 'd']
result = '-'.join(letters)
print(result)

# joining a Tuple
fruits = ('apple', 'banana', 'cherry')
result = ', '.join(fruits)
print(result)

# Joining Characters of a String
word = "Python"
result = '-'.join(word)
print(result)

numbers = ["1", "2", "3"]
# numbers = [1, 2, 3]
print(','.join(numbers))

numbers = [1, 2, 3]
print(','.join(map(str, numbers))) # convert integer to strings



# Using [ : : ] 
numbers = [0, 1, 2, 3, 4, 5]
print(numbers[1:4])

numbers = [0, 1, 2, 3, 4, 5]
print(numbers[::2])

# reversing a sequence
numbers = [0, 1, 2, 3, 4, 5]
print(numbers[::-1])

numbers = [0, 1, 2, 3, 4, 5]
print(numbers[:3])

print(numbers[3:])

# Slice Strings
text = "Python"
print(text[1:4])

print(text[::-1])
reversed_text = ''.join(text[::-1])
print(reversed_text)

text = "abcdefghij"
print(text[::2])

numbers = [0, 1, 2, 3, 4, 5]
print(numbers[1:5][::-1])

numbers = [0, 1, 2, 3, 4, 5]
print(numbers[-3:])

print(numbers[:-3])
