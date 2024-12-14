def print_rangoli(size):
    # Generate the alphabet list from 'a' to the required letter
    alphabet = [chr(i) for i in range(97, 97 + size)]

    # Calculate the width of the rangoli
    width = 4 * size - 3

    # Build the rows for the rangoli
    rows = []
    for i in range(size):
        # Get the decreasing sequence of letters for this row
        left_part = alphabet[size - i - 1:size]
        # Build the full row by combining left and right parts
        full_row = "-".join(left_part[::-1] + left_part[1:])
        # Center-align the row
        rows.append(full_row.center(width, '-'))

    # Combine the rows into the final rangoli pattern
    rangoli = "\n".join(rows + rows[-2::-1])
    print(rangoli)

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
