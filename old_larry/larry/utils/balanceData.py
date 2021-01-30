import sys
import numpy as np
import pandas as pd
from collections import Counter
from random import shuffle


def balance_data(filepath, outpath):

    print('Loading data...')

    train_data = np.load(filepath, allow_pickle=True)
    df = pd.DataFrame(train_data)

    print(df.head())
    print(Counter(df[1].apply(str)))

    forwards = []
    front_left = []
    front_right = []
    lefts = []
    rights = []
    back = []
    back_left = []
    back_right = []
    empty = []

    shuffle(train_data)

    for data in train_data:
        img = data[0]
        choice = list(data[1])

        if choice == [1,0,0,0]:
            forwards.append([img,choice])
        elif choice == [0,1,0,0]:
            lefts.append([img,choice])
        elif choice == [0,0,0,1]:
            rights.append([img,choice])
        elif choice == [1,1,0,0]:
            front_left.append([img,choice])
        elif choice == [1,0,0,1]:
            front_right.append([img,choice])
        elif choice == [0,0,0,1]:
            rights.append([img,choice])
        elif choice == [0,0,1,0]:
            back.append([img,choice])
        elif choice == [0,1,1,0]:
            back_left.append([img,choice])
        elif choice == [0,0,1,1]:
            back_right.append([img,choice])
        elif choice == [0,0,0,0]:
            empty.append([img, choice])


    print(f'Forwards: {len(forwards)}')
    print(f'Front Left: {len(front_left)}')
    print(f'Front Right: {len(front_right)}')
    print(f'Left: {len(lefts)}')
    print(f'Right: {len(rights)}')
    print(f'Backwards: {len(back)}')
    print(f'Back Left: {len(back_left)}')
    print(f'back Right: {len(back_right)}')
    print(f'Empty: {len(empty)}')


    # What data do you want to keep?
    master_list = [
            forwards,
            lefts,
            rights,
            front_left,
            front_right,
            back,
            # back_left,
            # back_right,
            empty,
            ]

    lengths = [len(i) for i in master_list]
    min_len = min(lengths)
    total = sum(lengths)

    print(f'Minimum length: {min_len}')
    print(f'Total Values: {total}')

    forwards = forwards[:len(lefts)][:len(rights)][:len(back)]
    lefts = lefts[:len(forwards)]
    rights = rights[:len(forwards)]
    back = back[:len(forwards)]
    empty = empty[:len(forwards)]

    decision = input("Should we save the data? (Not saving empty) [y/n]")
    print(f'You chose {decision}')

    if decision.upper() != 'Y':
        print("Exiting...")
        sys.exit(1)

    print(f'Saving data to {outpath}')

    # To we want to add empty?
    final_data = list()
    for i in master_list:
        final_data += i
    shuffle(final_data)

    np.save(outpath, final_data)


if __name__ == "__main__":

    if len(sys.argv) < 3:
        print("Arg1: input data")
        print("Arg2: Output file location")
        sys.exit(1)

    filepath = sys.argv[1]
    outpath = sys.argv[2]
    balance_data(filepath, outpath)
