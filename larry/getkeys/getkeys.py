"""
    Script showing how to get keypresses for every key pressed
"""
from pynput.keyboard import Key, Listener
from collections import Counter
import os

def on_press(key):
    key = str(key)
    if 'Key' not in key:
        key = key.replace("'", '')
    with open('/tmp/pyplays-keypress.txt', 'a') as f:
        f.write(key + '\n')

def getKeys():
    print("Get Keys started up")
    with Listener(on_press=on_press) as listener:
        print(listener.join())

def reset_files(file_path: str, remake=False):
    """
        Removes the file and creates a blank one in its place
        Args:
            file_path: location of file
    """
    if os.path.exists(file_path):
        os.remove (file_path)

    if remake:
        os.mknod(file_path)


def key_check():
    file_path = '/tmp/pyplays-keypress.txt'
    if os.path.exists(file_path):
        with open('/tmp/pyplays-keypress.txt', 'r') as f:
            keys_pressed = f.read().splitlines()
            keys_pressed = [i.upper() for i in keys_pressed]
            reset_files(file_path)

            value_counts = Counter(keys_pressed)
            # print(f"Keys Pressed:")
            # for i in value_counts.keys():
            #     print(f"{i} : {value_counts[i]}")
            return value_counts



def keys_to_output(top_keys: Counter):
    '''
    Convert keys to a multi-hot array with
    [W,A,S,D] boolean values.

    Args:
        top_keys: Counter object of keys
    '''
    output = [0,0,0,0] # WASD

    if top_keys:
        keys_pressed = top_keys.keys()
        if 'A' in keys_pressed:
            output[1] = 1
        elif 'D' in keys_pressed:
            output[3] = 1
        elif 'S' in keys_pressed:
            output[2] = 1
        elif 'W' in keys_pressed:
            output[0] = 1

    return output


if __name__ == "__main__":
    import time
    import threading

    th = threading.Thread(target=getKeys)
    th.start()

    last_read = time.time()
    file_path = '/tmp/pyplays-keypress.txt'

    reset_files(file_path)

    while True:
        if time.time() - last_read > 0.25:
            keyvals = key_check()
            outarray = keys_to_output(keyvals)
            print(outarray)
            last_read = time.time()
