# 1. Matrix Diagonal Difference
# Problem: Write a function diagonalDifference(matrix) that calculates the difference between the sums of the diagonals in a square matrix (2D array).
# Example:
# diagonalDifference([
#   [1, 2, 3],
#   [4, 5, 6],
#   [7, 8, 9]
# ]) 
# // Left diagonal: 1 + 5 + 9 = 15
# // Right diagonal: 3 + 5 + 7 = 15
# // Output: 0

def diagonalDifference(matrix):
    left_diagonal_sum = 0
    right_diagonal_sum = 0
    n = len(matrix)  # Assuming matrix is square

    for i in range(n):
        left_diagonal_sum += matrix[i][i]  # Sum for left diagonal
        right_diagonal_sum += matrix[i][n - 1 - i]  # Sum for right diagonal

    return abs(left_diagonal_sum - right_diagonal_sum)  # Return the absolute difference

# Example call to the function
result = diagonalDifference([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])
print(result)  # Output the result

# 2. Vowel and Consonant Counter
# Problem: Write a function countVowelsAndConsonants(str) that takes a string and returns an object with the count of vowels and consonants. Ignore numbers, spaces, and special characters.
# Example:
# countVowelsAndConsonants("Hello World!") 
# // Output: { vowels: 3, consonants: 7 }

def countVowelsAndConsonants(s):
    vowels = "aeiouAEIOU"
    count = {"vowels": 0, "consonants": 0}

    for char in s:
        if char.isalpha():  # Check if the character is a letter
            if char in vowels:
                count["vowels"] += 1  # Increment vowel count
            else:
                count["consonants"] += 1  # Increment consonant count

    return count  # Return the counts

# Example call to the function
result = countVowelsAndConsonants("Hello World!")
print(result)  # Output the result

# 3. Mumbling Pattern
# Problem: Write a function mumblingPattern(str) that repeats each character in a string a number of times corresponding to its index, with each repetition capitalized and separated by hyphens.
# Example:
# mumblingPattern("abcd") 
# // "A-Bb-Ccc-Dddd"

def mumblingPattern(s):
    result = []  # Initialize an empty list to store the parts of the pattern

    for i, char in enumerate(s):
        part = char.upper() + char.lower() * i  # Capitalize the first character and repeat it
        result.append(part)  # Add the part to the result list

    return '-'.join(result)  # Join the parts with hyphens and return the final string

# Example call to the function
result = mumblingPattern("abcd")
print(result)  # Output: "A-Bb-Ccc-Dddd"