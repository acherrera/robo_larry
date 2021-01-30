import numpy as np
from datetime import datetime
from larry.utils.alexnet import alexnet

def main(training_data):

    WIDTH = 80
    HEIGHT = 60
    LR = 1e-3
    EPOCHS = 8
    MODEL_NAME = 'ats-{}-{}-{}-epochs.model'.format(LR, 'alexnetv2',EPOCHS)

    model = alexnet(WIDTH, HEIGHT, LR)

    # Setup the training data:

    train_data = np.load(training_data, allow_pickle=True)

    train = train_data[:-500]
    test = train_data[-500:]

    X = np.array([i[0] for i in train]).reshape(-1,WIDTH,HEIGHT,1)
    Y = [i[1] for i in train]

    test_x = np.array([i[0] for i in test]).reshape(-1,WIDTH,HEIGHT,1)
    test_y = [i[1] for i in test]

    # Now we can actually train the model with:

    model.fit({'input': X}, {'targets': Y}, n_epoch=EPOCHS, validation_set=({'input': test_x}, {'targets': test_y}),
        snapshot_step=500, show_metric=True, run_id=MODEL_NAME)

    # tensorboard --logdir=foo:C:/Users/H/Desktop/ai-gaming/log

    model.save(MODEL_NAME)

if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        print("Arg1: Location of training data")
        sys.exit(1)

    training_data = sys.argv[1]
    main(training_data)
