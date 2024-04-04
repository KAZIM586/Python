def count_vowels_and_consonants(input_string):
    vowels = "aeiouAEIOU"
    consonants_count = 0
    vowels_count = 0

    for char in input_string:
        if char.isalpha():
            if char.lower() in vowels:
                vowels_count += 1
            else:
                consonants_count += 1

    print("Number of vowels:", vowels_count)
    print("Number of consonants:", consonants_count)

# Example usage:
input_string = input("Enter a string: ")
count_vowels_and_consonants(input_string)
