# import time

# def wait_for_bus():
#     while True:
#         print("Still waiting for the bus...")
#         time.sleep(10)  # Wait for 10 seconds

#         response = input("Has the bus arrived? (yes/no): ").lower()

#         if response == "yes":
#             print("Hooray! The bus has arrived. Have a safe journey!")
#             break
#         elif response == "no":
#             print("Okay, continue waiting for the bus...")
#         else:
#             print("Invalid input. Please enter 'yes' or 'no'.")

# if __name__ == "__main__":
#     wait_for_bus()



import time

def wait_for_bus():
    print("Welcome! You are now waiting for the bus.")
    
    while True:
        print("Still waiting for the bus...")
        time.sleep(10)  # Wait for 10 seconds
        
        user_input = input("Has the bus arrived? (yes/no): ").lower()
        
        if user_input == "yes":
            print("Hooray! The bus has arrived. Have a safe journey!")
            break
        elif user_input == "no":
            print("Continuing to wait for the bus...")
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

# Run the program
wait_for_bus()
