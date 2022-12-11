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
    :param user_pairs:pairs represent preferences of one user
    :param ref_rank:a list
    :param phi:a float parameter
    :return: a rank
    '''
    rank = []

    #initial rank
    rank.append(ref_rank[0])

    #turn pairs to a list
    u_pair = [tuple(pair) for pair in user_pairs]

    #every loop insert a item
    for i in range(1,len(ref_rank)):
        L_i = []
        H_i = []
        sigma_i = ref_rank[i]
        #i' that less than i
        for j in range(i-1,-1,-1):
            r_j = rank[j]
            if (r_j, sigma_i) in u_pair:
                L_i.append(j)
            if (sigma_i,r_j) in u_pair:
                H_i.append(j)
        # print("L_i is:", L_i)
        # print("H_i is:", H_i)
        l_i = 0 if len(L_i)==0 else max(L_i)+1
        h_i = i if len(H_i)==0 else min(H_i)
        #print("l_i and h_i:",l_i,h_i)

        positions = [idx for idx in range(l_i, h_i + 1)]

        #print("candidate positions:", positions)
        probs = [np.power(phi, i - j) for j in positions]
        probs = np.divide(probs, sum(probs))
        in_idx = np.random.choice(positions, p=probs)
        rank.insert(in_idx, sigma_i)

    return rank




