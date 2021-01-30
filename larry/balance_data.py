"""
Balances the data. Shuffles, creates a list of value and bundle it with the
input data
"""

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
    
    # Need to convert this to a one-hot array that can deal with all the
    # possible outcomes
    # [f, fl, fr, l, r, b, bl, br, null] 

    f_ =  [1,0,0,0,0,0,0,0]
    f_l = [0,1,0,0,0,0,0,0]
    f_r = [0,0,1,0,0,0,0,0] 
    l_ =  [0,0,0,1,0,0,0,0]
    r_ =  [0,0,0,0,1,0,0,0]
    b_ =  [0,0,0,0,0,1,0,0]
    b_l = [0,0,0,0,0,0,1,0]
    b_r = [0,0,0,0,0,0,0,1]
    _ =   [0,0,0,0,0,0,0,0]



    shuffle(train_data)

    for data in train_data:
        img = data[0]
        choice = list(data[1])

        if choice == [1,0,0,0]:
            choice = f_
            forwards.append([img,choice])
        elif choice == [0,1,0,0]:
            choice = l_
            lefts.append([img,choice])
        elif choice == [0,0,0,1]:
            choice = r_
            rights.append([img,choice])
        elif choice == [1,1,0,0]:
            choice = f_l
            front_left.append([img,choice])
        elif choice == [1,0,0,1]:
            choice = f_r
            front_right.append([img,choice])
        elif choice == [0,0,0,1]:
            choice = r_
            rights.append([img,choice])
        elif choice == [0,0,1,0]:
            choice = b_
            back.append([img,choice])
        elif choice == [0,1,1,0]:
            choice = b_l
            back_left.append([img,choice])
        elif choice == [0,0,1,1]:
            choice = b_r
            back_right.append([img,choice])
        elif choice == [0,0,0,0]:
            choice = _
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

    # if len(sys.argv) < 3:
    #     print("Arg1: input data")
    #     print("Arg2: Output file location")
    #     sys.exit(1)


    filepath = './training_data/good_data/output_vals.npy'
    outpath = './training_data_balanced.npy'

    balance_data(filepath, outpath)
