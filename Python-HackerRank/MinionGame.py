def minion_game(string):
    # your code goes here
    kevin_score = 0 # Kevin's substrings : A, E, I, O, U
    stuart_score = 0 # Stuart's substrings : non-vowels
    
    # Set of vowels
    vowels = {'A', 'E', 'I','O', 'U'}
    n = len(string)
    
    # Calculate scores
    for i in range(n):
        if string[i] in vowels:
            kevin_score += n-i # Substirngs starting with this vowel
        else:
            stuart_score += n-i # Substrings starting with this consonant ex) if i = 0, B, BA, BAN, BANA, BANAN, BANANA => 6
    
    # Determine the winner
    if kevin_score > stuart_score:
        print(f"Kevin {kevin_score}")
    elif stuart_score > kevin_score:
        print(f"Stuart {stuart_score}")
    else:
        print("Draw")


if __name__ == '__main__':
    s = input()
    minion_game(s)
