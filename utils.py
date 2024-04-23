def compare(prev_sub, curr_pred, two_current=False):
    c = 0
    
    if two_current:
        for q, w in zip(prev_sub[test_indices], curr_pred[test_indices]):
            if q.item() != w.item():
                c += 1
        return c
    
    for q, w in zip(prev_sub, curr_pred[test_indices]):
        if q != w.item():
            c += 1
    return c