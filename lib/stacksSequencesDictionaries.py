def is_balanced(expression):
    opening_brackets = ['(', '{', '[']
    closing_brackets = [')', '}', ']']
    bracket_stack = []

    for char in expression:
        if char in opening_brackets:
            bracket_stack.append(char)
        elif char in closing_brackets:
            if len(bracket_stack) == 0:
                return False
            elif opening_brackets.index(bracket_stack.pop()) != closing_brackets.index(char):
                return False

    if len(bracket_stack) == 0:
        return True
    else:
        return False

# expression1 = "([]{})"
# expression2 = "([)]"

# print(is_balanced(expression1))  
# print(is_balanced(expression2)) 
    

def remove_duplicates(sequence):
    seen = set()
    result = []

    for item in sequence:
        if item not in seen:
            result.append(item)
            seen.add(item)

    return result

# input_sequence = [2, 3, 2, 4, 5, 3, 6, 7, 5]
# result = remove_duplicates(input_sequence)
# print(result)  # Output: [2, 3, 4, 5, 6, 7]

import re

def word_frequency(sentence):
    words = re.findall(r'\b\w+\b', sentence.lower())
    frequency = {}

    for word in words:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1

    return frequency

# sentence = "This is a test sentence. This sentence is a test."
# result = word_frequency(sentence)
# print(result)