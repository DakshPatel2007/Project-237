import time

def thirty_timer(current_hour, current_minute):
    while True:
        current_minute += 30
    
        if current_minute > 60:
            current_hour += 1
            current_minute = current_minute % 60
            time.sleep(1800)
            print("Drink Water")
    
        
current_hour = input("Enter hours: ")
current_minute = input("Enter minutes: ")

thirty_timer(int(current_hour),int(current_minute))