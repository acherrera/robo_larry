import numpy as np
import pandas as pd
from collections import Counter
from random import shuffle


def balance_data(filepath, outpath):
    train_data = np.load(filepath, allow_pickle=True)
    df = pd.DataFrame(train_data)

    print(df.head())
    print(Counter(df[1].apply(str)))

    lefts = []
    rights = []
    forwards = []
    backs = []

    shuffle(train_data)

    for data in train_data:
        img = data[0]
        choice = data[1]

        if choice == [1,0,0,0]:
            forwards.append([img,choice])
        elif choice == [0,1,0,0]:
            lefts.append([img,choice])
        elif choice == [0,0,1,0]:
            backs.append([img,choice])
        elif choice == [0,0,0,1]:
            rights.append([img,choice])
        else:
            pass

    print(f'Forwards: {len(forwards)}')
    print(f'Backwards: {len(backs)}')
    print(f'Left: {len(lefts)}')
    print(f'Right: {len(rights)}')

    forwards = forwards[:len(lefts)][:len(rights)][:len(backs)]
    lefts = lefts[:len(forwards)]
    rights = rights[:len(forwards)]
    backs = backs[:len(forwards)]

    final_data = forwards + lefts + rights + backs
    shuffle(final_data)

    np.save(outpath, final_data)


if __name__ == "__main__":
    import sys

    if len(sys.argv) < 3:
        print("Arg1: input data")
        print("Arg2: Output file location")
        sys.exit(1)

    filepath = sys.argv[1]
    outpath = sys.argv[2]
    balance_data(filepath, outpath)
