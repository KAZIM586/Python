def remove_vowels(input_string):
    vowels = "aeiouAEIOU"
    result = ''.join(char for char in input_string if char not in vowels)
    return result

# Get input from the user
user_input = input("Enter a string: ")

# Remove vowels and display the result
result_string = remove_vowels(user_input)
print("String after removing vowels:", result_string)
