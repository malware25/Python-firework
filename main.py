# main.py
import os
import random
import time

# ANSI escape sequences for colors
COLORS = [
    "\033[91m",  # Red
    "\033[92m",  # Green
    "\033[93m",  # Yellow
    "\033[94m",  # Blue
    "\033[95m",  # Magenta
    "\033[96m",  # Cyan
    "\033[97m",  # White
]

RESET = "\033[0m"

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def firework():
    x = random.randint(10, 40)   # horizontal position
    y = random.randint(5, 15)    # vertical position
    color = random.choice(COLORS)

    # move cursor down y times
    print("\n" * y, end="")
    # print explosion
    for row in [
        "   *   ",
        "  ***  ",
        " ***** ",
        "  ***  ",
        "   *   ",
    ]:
        print(" " * x + color + row + RESET)

if __name__ == "__main__":
    try:
        while True:
            clear()
            for _ in range(random.randint(1, 3)):
                firework()
            time.sleep(0.8)
    except KeyboardInterrupt:
        clear()
        print("🎆 Fireworks show ended. Bye!")
