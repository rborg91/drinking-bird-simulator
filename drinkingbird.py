import argparse
import animations
import os
import random
import time

from pynput.keyboard import Controller

parser = argparse.ArgumentParser(description="Drinking Bird Simulator")
parser.add_argument("-k", "--key", 
                    type=str, 
                    default="y",
                    metavar="",
                    help="key to be pressed (string) (default: y)")
parser.add_argument("-r", "--rounds", 
                    type=int, 
                    default=1000,
                    metavar="",
                    help="number of times the drinking bird presses the key (integer) (default: 1000)")
args = parser.parse_args()

keyboard = Controller()
rounds = args.rounds
key_input = args.key

quotes = [
    "I think I'll order a TAB",
    "Where's the 'any' key?",
    "All I see is esc, ctrl and pig up"
]

os.system("cls")
print("""Change to your desired window - 10 seconds to start
Keep this terminal in view to see the drinking bird in action""")
time.sleep(10)
print("")
print(random.choice(quotes))
time.sleep(2)

counter=0
while counter<rounds:
    os.system("cls")
    animations.frame_1()
    time.sleep(0.5)
    os.system("cls")
    animations.frame_2()
    time.sleep(0.5)
    os.system("cls")
    animations.frame_3()
    keyboard.press(key_input)
    time.sleep(0.5)
    os.system("cls")
    animations.frame_2()
    time.sleep(0.5)
    counter+=1
