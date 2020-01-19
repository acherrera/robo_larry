import os
import numpy as np



def combine_data(input_dir: str, output_dir: str):
    """
        Opens the files, combines into one "master" set and save to the outpu_dir
    """

    files_in = [i for i in os.listdir(input_dir) if i.endswith('.npy')]

    all_arrays = [np.load(input_dir+i, allow_pickle=True) for i in files_in]
    final_array = np.concatenate(all_arrays)
    np.save(output_dir+'output_vals.npy', final_array)

    print(len(final_array))


if __name__ == "__main__":
    input_dir = './training_data/'
    output_dir = './training_data/good_data/'

    combine_data(input_dir, output_dir)
