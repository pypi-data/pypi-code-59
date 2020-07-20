def quick_sort(list_):
    if len(list_)<=1:
        return list_
    if len(list_)==2:
        return list_ if list_[0]<=list_[1] else list_[::-1]
    base_idx = int(len(list_)/2)
    base = list_[base_idx]
    left = []
    right = []
    for i in range(len(list_)):
        if i != base_idx:
            if list_[i] <= base:
                left.append(list_[i])
            else:
                right.append(list_[i])
    return quick(left)+[base]+quick(right)