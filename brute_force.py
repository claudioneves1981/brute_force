import itertools
import string
import time
from datetime import datetime

chars = string.ascii_letters + string.digits
target_password = input("Enter the target password(max 8 characters ): ")
if len(target_password) > 8:
    print("Password must be 8 characters or less.")
    exit()

start_time = time.time()
attempts = 0
found = False
commonPrefix = ""
temp = ""

for length in range(1, len(target_password)+1):
    for guess in itertools.product(chars, repeat=length):
        
        commonPrefix = ''.join(guess)  
        if guess[-1] == target_password[len(commonPrefix)-1]:
            temp += commonPrefix[-1]
            print(f"Trying: {temp} (Attempts: {attempts})")
            if temp == target_password:                
               end_time = time.time()
               total_time = end_time - start_time
               print(f"Password found: {temp}")
               print(f"Total attempts: {attempts}")
               print(f"Time taken: {total_time:.2f} seconds")
               found = True
               break
            break
        
        
        print(f"Trying: {temp+commonPrefix[-1]} (Attempts: {attempts})")
        attempts += 1  
     
        
        time.sleep(0.01)  # Simulate time taken to check password
        
    if found:
        break
