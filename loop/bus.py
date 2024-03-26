
# param1='no'
import time

# def wait_for_bus():
while True:
       
        # print("Still waiting for the bus...")
        time.sleep(10)  # Wait for 10 seconds

        # param1 = input("Has the bus arrived? (yes/no): ").lower()
        param1 ='no'.lower()
        
        if param1 == "yes":
            print("Hooray! The bus has arrived. Have a safe journey!")
            break
        elif param1 == "no":
            print("Okay, continue waiting for the bus...")
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

# if __name__ == "__main__":
#     wait_for_bus()
