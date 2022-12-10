import numpy as np
import random
from utils import load_data
from functions import local_kemeny

if __name__ == '__main__':
    path = 'sushi3-2016'
    num_u, num_i, uids, iid1, iid2, init_rank = load_data(path)
    random.shuffle(init_rank)
    print(init_rank)

    pairs = np.array([[i, j] for u, i, j in zip(uids, iid1, iid2)])
    ref_rank = local_kemeny(pairs, init_rank)
    print(ref_rank)
