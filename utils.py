import numpy as np
import sys
sys.path.append("..")
num_users, num_items = 0, 0

#user,item id start from 0

def load_data(path='sushi3-2016'):
    num_users, num_items = 0, 0
    print('loading pair-wise data from flie %s...' % path)
    user_input, item_i_input, item_j_input = [], [], []
    init_rank = []
    if path == 'sushi3-2016':
        # file_user = '../dataset/' + path + '/sushi3.udata'
        num_users, num_items = 5000, 10
        file = '../dataset/' + path + '/sushi3a.5000.10.order'
        uid = 0
        with open(file,'r') as f:
            for line in f:
                arr = line.replace('\n','').split(' ')[2:]
                arr = list(map(int,arr))
                if len(arr) <= 0:
                    continue
                for i in range(len(arr)):
                    for j in range(i + 1, len(arr)):
                        user_input.append(uid)
                        item_i_input.append(arr[i])
                        item_j_input.append(arr[j])
                init_rank = [i for i in arr]
                uid += 1

    return num_users, num_items, user_input, item_i_input, item_j_input, init_rank

