import numpy as np
import cv2
import time
import os
from getkeys import key_check
from datetime import datetime
from grabscreen import grab_screen

def keys_to_output(keys):
    """
    Convert keys to a multi-hot array. Allowing for combinations of values
    being pressed at the same time

    [W, A, S, D] boolean values.
    """

    options = ['W', 'A', 'S', 'D']
    output = [0,0,0,0]

    for i in range(len(options)):
        if options[i] in keys:
            output[i] = 1

    return output

def initialize_data(file_name):
    """
        Just loads the data if it exists
    """
    if os.path.isfile(file_name):
        print('File exists, loading previous data!')
        starting_data = list(np.load(file_name, allow_pickle=True))
    else:
        print('File does not exist, starting fresh!')
        starting_data = []
    return starting_data


        
def main(debug=False):
    """
    Actually captures the training data.
    Args:
        debug: print out extra data or not
    """
    now = datetime.now()
    prefix = now.strftime("%Y-%m-%d-%H%M%S")
    file_name = f'./training_data/{prefix}-training_data.npy'
    training_data = initialize_data(file_name)
    fps_list = []
    last_print = time.time()

    for i in list(range(4))[::-1]:
        print(i+1)
        time.sleep(1)

    while(True):
        window_size = (0, 40, 1024, 748)
        screen = grab_screen(region=window_size)
        last_time = time.time()
        screen = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
        # resize to something a bit more acceptable for a CNN
        screen = cv2.resize(screen, (80,60))
        keys = key_check()
        output = keys_to_output(keys)
        if debug:
            print(f"Keys: {output}")
            cv2.imshow('window',cv2.cvtColor(screen, cv2.COLOR_BGR2RGB))

        training_data.append([screen,output])
        
        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break

        if len(training_data) % 500 == 0:
            print(len(training_data))
            np.save(file_name,training_data)

if __name__ == "__main__":
    main()
