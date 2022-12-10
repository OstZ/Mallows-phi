import numpy as np
def local_kemeny(pairs,init_rank):
    '''
    input (u,i,j) pairs and init_rank([3,1,0,9,6...])
    return reference rank
    '''
    #count pairs
    pair_count = dict()
    for pair in pairs:
        tuple_p = tuple(pair)
        if pair_count.get(tuple_p):
            pair_count[tuple_p] += 1
        else:
            pair_count[tuple_p] = 1

    for i in range(1,len(init_rank)):
        for j in range(i-1,-1,-1):
            pi_i = init_rank[i]
            pi_j = init_rank[j]
            if pair_count.get(tuple([pi_i, pi_j])) > pair_count.get(tuple([pi_j, pi_i])):
                tmp = pi_i
                init_rank[i] = pi_j
                init_rank[j] = tmp
            if pair_count.get(tuple([pi_i, pi_j])) < pair_count.get(tuple([pi_j, pi_i])):
                break
    return init_rank

def AMP(user_pairs, ref_rank,phi):
    '''
    return rank sampled from specific phi
    :param user_pairs:a nx2 np.array
    :param ref_rank:a list
    :param phi:a float parameter
    :return:
    '''
    rank = []
    #initial rank
    rank.append(ref_rank[0])
    u_pair = [tuple(pair) for pair in user_pairs]
    #every loop insert a item
    for i in range(1,len(ref_rank)):
        #i' that less than i
        for j in range(i-1,-1,-1):
            if



