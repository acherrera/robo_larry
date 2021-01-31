"""
Play back the data in the training file along with the image recorded
"""
import numpy as np
from collections import Counter
from random import shuffle
import cv2


def replay_data(file_name):
    train_data = np.load(file_name, allow_pickle=True)

    for data in train_data:
        img = data[0]
        choice = data[1]
        cv2.imshow("Verify Data", img)
        print(choice)

        if cv2.waitKey(25) & 0xFF == ord("q"):
            cv2.destroyAllWindows()
            break


if __name__ == "__main__":
    import sys

    file_name = sys.argv[1]
    replay_data(file_name)
