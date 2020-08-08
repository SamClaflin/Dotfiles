#!/usr/bin/python3

import subprocess 
import sys
import os


def adjust_brightness(value):
    os.system(f"xrandr --output eDP-1 --brightness {value}")


def main():
    # Validate command line arguments 
    arguments = sys.argv
    if len(arguments) < 2:
        print("Error: requires argument '--up' or '--down'")
        return

    # Use xrandr to get the current brightness 
    proc = subprocess.run(["xrandr", "--verbose"], capture_output=True)
    out_string = str(proc.stdout)
    search_string = "Brightness: "
    start_index = out_string.find(search_string)
    end_index = start_index + len(search_string)
    curr_brightness = float(out_string[end_index : end_index + 3])
 
    # Adjust brightness
    increment = 0.1
    argument = arguments[1]
    if argument == "--up":
        new_brightness = curr_brightness + increment
        if new_brightness > 1.0:
            return

        adjust_brightness(new_brightness) 

    elif argument == "--down":
        new_brightness = curr_brightness - increment
        if new_brightness < 0.0:
            return

        adjust_brightness(new_brightness)

    else:
        print(f"Invalid argument: {argument}")


if __name__ == "__main__":
    main()

