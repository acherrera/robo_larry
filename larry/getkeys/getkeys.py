"""
    Script showing how to get keypresses for every key pressed
"""
from pynput.keyboard import Key, Listener

def on_press(key):
    key = str(key)
    if 'Key' not in key:
        key = key.replace("'", '')
    with open('/tmp/pyplays-keypress.txt', 'a') as f:
        f.write(key + '\n')

def getkeys():
    with Listener(on_press=on_press) as listener:
        print(listener.join())


def key_check():
    # TODO
    pass

if __name__ == "__main__":
    import os
    file_path = '/tmp/pyplays-keypress.txt'
    if os.path.exists(file_path):
        os.remove (file_path)
    while True:
        getkeys()
