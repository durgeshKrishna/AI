from itertools import permutations

def solve_cryptarithm(words, result):
    unique_chars = set(''.join(words) + result)
    if len(unique_chars) > 10:
        return False  # More than 10 unique characters is not possible with digits 0-9
    
    # Generate all possible digit assignments (permutations of digits 0-9)
    for perm in permutations(range(10), len(unique_chars)):
        char_to_digit = dict(zip(unique_chars, perm))
        if is_valid_assignment(words, result, char_to_digit):
            print("Mapping found:")
            for char, digit in char_to_digit.items():
                print(f"{char} -> {digit}")
            return True
    return False

def is_valid_assignment(words, result, char_to_digit):
    # Ensure no leading zeroes for multi-digit words
    for word in words + [result]:
        if char_to_digit[word[0]] == 0:
            return False
    
    def word_to_number(word):
        return int(''.join(str(char_to_digit[char]) for char in word))
    
    words_sum = sum(word_to_number(word) for word in words)
    result_value = word_to_number(result)
    
    return words_sum == result_value

# Example usage
words = ["SEND", "MORE"]
result = "MONEY"
if solve_cryptarithm(words, result):
    print("Yes")
else:
    print("No")
