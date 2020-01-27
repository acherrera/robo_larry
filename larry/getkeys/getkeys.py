"""
    Script showing how to get keypresses for every key pressed
"""

import keyboard
from collections import Counter
import os
import json
import time


def getKeys():
    desired_fps = 120
    delay_time = 1 / desired_fps
    read_time = time.time()
    while True:
        if time.time() - read_time > delay_time:
            read_time = time.time()
            keyvals = [
                keyboard.is_pressed("w"),
                keyboard.is_pressed("a"),
                keyboard.is_pressed("s"),
                keyboard.is_pressed("d"),
            ]
            keyvals = [1 if i else 0 for i in keyvals]
            keyvals = json.dumps(keyvals)
            with open("/tmp/pyplays-keypress.txt", "a") as f:
                f.write(keyvals + "\n")


def reset_files(file_path: str, remake=False):
    """
        Removes the file and creates a blank one in its place
        Args:
            file_path: location of file
    """
    if os.path.exists(file_path):
        os.remove(file_path)

    if remake:
        os.mknod(file_path)


def key_check():
    file_path = "/tmp/pyplays-keypress.txt"
    if os.path.exists(file_path):
        with open("/tmp/pyplays-keypress.txt", "r") as f:
            keys_pressed = f.read().splitlines()
            reset_files(file_path)
            value_counts = Counter(keys_pressed)
            value_counts = json.loads(value_counts.most_common(1)[0][0])
            # print(value_counts)
            return value_counts


def keys_to_output(top_keys: Counter):
    """
    Convert keys to a multi-hot array with
    [W,A,S,D] boolean values.

    Args:
        top_keys: Counter object of keys
    """
    output = [0, 0, 0, 0]  # WASD

    if top_keys:
        keys_pressed = top_keys.keys()
        if "A" in keys_pressed:
            output[1] = 1
        elif "D" in keys_pressed:
            output[3] = 1
        elif "S" in keys_pressed:
            output[2] = 1
        elif "W" in keys_pressed:
            output[0] = 1

    return output


if __name__ == "__main__":
    import time
    import threading

    file_path = "/tmp/pyplays-keypress.txt"
    reset_files(file_path)
    print("Firing off key logger")
    getKeys()
