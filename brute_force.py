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
cont = 0
temp = ""

for length in range(1, len(target_password)+1):
    flag = False
    for guess in itertools.product(chars, repeat=length):
        
        commonPrefix = ''.join(guess)  
        if target_password.startswith(commonPrefix):
            temp = commonPrefix
            print(f"Trying: {commonPrefix} (Attempts: {attempts})")
            flag = True
            
            #break
        else:
            attempts += 1   
            print(f"Trying: {temp+commonPrefix} (Attempts: {attempts})")
           
            #breakcd 

        #cont += 1
        time.sleep(0.01)  # Simulate time taken to check password
        if temp+commonPrefix == target_password:
            end_time = time.time()
            total_time = end_time - start_time
            print(f"Password found: {temp+commonPrefix}")
            print(f"Total attempts: {attempts}")
            print(f"Time taken: {total_time:.2f} seconds")
            found = True
            break
    if found:
        break
#if not found:
#    print("Password not found within the given constraints.")