import numpy as np
import cv2
import time
import logging
import threading
import mss
from larry.getkeys.getkeys import key_check, getKeys
from larry.controls.controls import cont_right, cont_left, cont_straight, cont_slow, stop_all
from larry.utils.alexnet import alexnet

logger = logging.getLogger(__name__)

WIDTH = 80
HEIGHT = 60
LR = 1e-3
EPOCHS = 8
MODEL_NAME = './ats-{}-{}-{}-epochs.model'.format(LR, 'alexnetv2',EPOCHS)

model = alexnet(WIDTH, HEIGHT, LR)
model.load(MODEL_NAME)

def main():

    # th = threading.Thread(target=getKeys)
    # th.start()

    fps_list = list()
    last_print = time.time()
    last_time = time.time()
    target_fps = 60

    for i in list(range(4))[::-1]:
        print(i+1)
        time.sleep(1)

    paused = False
    while(True):

        if not paused:
            with mss.mss() as sct:
                last_frame = time.time()
                # screen =  np.array(ImageGrab.grab(bbox=(0,40,800,640)))
                monitor = {"top": 40, "left": 0, "width": 1024, "height": 748}
                screen = np.array(sct.grab(monitor))
                screen = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
                screen = cv2.resize(screen, (80,60))
                cv2.imshow('',screen)
                moves = list(np.around(model.predict([screen.reshape(80,60,1)])[0]))
                print(moves)

                stop_all()

                if moves == [1,0,0,0]:
                    cont_straight()
                elif moves == [0,1,0,0]:
                    cont_straight()
                    cont_left()
                elif moves == [0,0,1,0]:
                    cont_slow()
                elif moves == [0,0,0,1]:
                    cont_straight()
                    cont_right()
                else:
                    cont_straight()


                if cv2.waitKey(25) & 0xFF == ord('q'):
                    cv2.destroyAllWindows()
                    break

                fps_list.append(1 / (time.time() - last_time))
                last_time = time.time()

                if time.time() - last_print > 2:
                    logger.info(f'fps: {int(np.average(fps_list))}')
                    last_print = time.time()
                    fps_list = []
                    line_count_list = []
                    turnval_list = list()

                while (time.time() - last_frame) < 1/target_fps:
                    pass

            # keys = key_check()
            # if keys and 'T' in keys:
            #     if paused:
            #         paused = False
            #         time.sleep(1)
            #     else:
            #         paused = True
            #         stop_all()
            #         time.sleep(1)

if __name__ == "__main__":
    main()
