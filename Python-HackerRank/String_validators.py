if __name__ == '__main__':
    s = input()  # Input string

    # Check each property and print the result
    print(any(char.isalnum() for char in s))  # Alphanumeric characters
    print(any(char.isalpha() for char in s))  # Alphabetical characters
    print(any(char.isdigit() for char in s))  # Digits
    print(any(char.islower() for char in s))  # Lowercase characters
    print(any(char.isupper() for char in s))  # Uppercase characters
