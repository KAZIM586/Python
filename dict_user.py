# Initial dictionary of friends' names and phone numbers
friends_dict = {
    'Ranjit': '123-456-7890',
    'Kazim': '234-567-8901',
    'Samay': '345-678-9012',
    'Sachin': '456-789-0123',
    'Manish': '567-890-1234'
}

# Print the dictionary in sorted order
sorted_friends_dict = dict(sorted(friends_dict.items()))
print("Sorted Friends Dictionary:", sorted_friends_dict)

# Prompt the user to enter a name
user_input_name = input("Enter a friend's name: ")

# Check if the name is present in the dictionary
if user_input_name in sorted_friends_dict:
    print(f"The phone number for {user_input_name} is {sorted_friends_dict[user_input_name]}")
else:
    # If the name is not present, prompt the user to enter details
    user_input_phone = input("Enter the phone number: ")
    sorted_friends_dict[user_input_name] = user_input_phone
    print(f"Details added for {user_input_name}. Updated dictionary:", sorted_friends_dict)
