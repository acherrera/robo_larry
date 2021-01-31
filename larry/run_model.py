import numpy as np
from PIL import ImageGrab
import cv2
import time
from directkeys import (
    straight,
    straight_left,
    straight_right,
    left,
    right,
    slow,
    slow_left,
    slow_right,
    cruise,
)
from alexnet import alexnet
from grabscreen import grab_screen

############ Fixing and error when running ###################
from tensorflow.compat.v1 import ConfigProto
from tensorflow.compat.v1 import InteractiveSession

config = ConfigProto()
config.gpu_options.allow_growth = True
session = InteractiveSession(config=config)

###############################################################

WIDTH = 80
HEIGHT = 60
LR = 1e-3
EPOCHS = 8
MODEL_NAME = "ats-{}-{}-{}-epochs.model".format(LR, "alexnetv2", EPOCHS)

model = alexnet(WIDTH, HEIGHT, LR)

control_mapping = {
    0: straight,
    1: straight_left,
    2: straight_right,
    3: left,
    4: right,
    5: slow,
    6: slow_left,
    7: slow_right,
}


def main():
    last_time = time.time()

    for i in list(range(4))[::-1]:
        print(i + 1)
        time.sleep(1)

    while True:
        # 800x600 windowed mode
        window_size = (0, 40, 1024, 748)
        screen = grab_screen(region=window_size)
        # print('loop took {} seconds'.format(time.time()-last_time))
        last_time = time.time()
        screen = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
        screen = cv2.resize(screen, (80, 60))
        cv2.imshow("", screen)
        moves = list(np.around(model.predict([screen.reshape(80, 60, 1)])[0]))
        print(moves)

        # if any(moves):
        #     control_mapping[np.argmax(moves)]()
        # else:
        #     cruise()

        if cv2.waitKey(25) & 0xFF == ord("q"):
            cv2.destroyAllWindows()
            break


if __name__ == "__main__":
    main()
