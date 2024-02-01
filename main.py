import pyautogui
import argparse
import time

# Initialize parser
parser = argparse.ArgumentParser()

# Adding optional argument
parser.add_argument("-t", "--time", help = "Set minutes to sleep before moving the cursor again")

args = parser.parse_args()

sleep = 120
direction = 'up'

if args.time:
    sleep = int(args.time) * 60

print(f"Setting sleep time to: {sleep} seconds")
print(f"Moving pointer to start position...")

width, height = pyautogui.size();

pyautogui.moveTo(width, height, duration = 1)

while True:
    if direction == 'up':
        print(f"Moving pointer up...");
        pyautogui.moveTo(width, 0, duration = 1)
        direction = 'down'
    elif direction == 'down':
        print(f"Moving pointer down...");
        pyautogui.moveTo(width, height, duration = 1)
        direction = 'up'
    else:
        print(f"Error reading direction: {direction}")
        break;
    
    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)
    print(f"Movement made at {current_time}. Next direction is: {direction}")
    time.sleep(sleep)

