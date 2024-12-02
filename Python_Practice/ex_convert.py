'''How to convert upper string to lower string and vice verssa?'''
# 1. converting to Lowercase
text = "Hello, WORLD!"
print(text.lower())


# 2. Converting to Uppercase
print(text.upper())

# 3. Swtiching Case
print(text.swapcase())

# 4. Capitalizing the First Letter
text2 = "hello, world"
print(text2.capitalize())

# 5. Converting Each Word to Title Case
text3 = "hello, world! python programming."
print(text3.title())

# 6. Converting Based on Conditions
if text.islower():
    print(text.upper())
else:
    print(text.lower())

# 7. Applying Conversion to Lists of Strings
text_list = ["HELLO", "world", "Python"]
lowercase_list = [text.lower() for text in text_list]
uppercase_list = [text.upper() for text in text_list]

print(lowercase_list)
print(uppercase_list)

# Practical Examples
user_input = input("Enter YES or NO: ").lower()
if user_input == "yes":
    print("You said YES!")
elif user_input == "no":
    print("You said NO!")
else:
    print("Invalid input")

sentence = "Python is Fun!"
print(sentence.swapcase())