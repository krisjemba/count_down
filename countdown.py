import time
from datetime import datetime

#print("Welcome to the first useless but most useful programme of the cosmos")
def countdown_to_newyear():
    while True:
        now = datetime.now()
        new_year = datetime(now.year + 1, 1, 1)
        delta = new_year - now
        print("Welcome to the first useless but most useful programme of the cosmos")
        print(f"\n{' Welcome to Jemba\'s first project for the year ':=^50}")
        print(f"\nMonths: {delta.days // 30}")
        print(f"Weeks: {delta.days // 7}")
        print(f"Days: {delta.days}")
        print(f"Hours: {delta.seconds // 3600}")
        print(f"Minutes: {(delta.seconds % 3600) // 60}")
        print(f"Seconds: {delta.seconds % 60}")
        print(f"Microseconds: {delta.microseconds}")
        
        time.sleep(1)
        print("\033[H\033[J")  # Clear terminal

if __name__ == "__main__":
    countdown_to_newyear()
