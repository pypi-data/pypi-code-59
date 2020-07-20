def insert_sort(list_):
    for i in range(1,len(list_)):
        idx = i
        for j in range(i):
            if list_[j]>list_[idx]:
                idx = j
                break
        if idx != i:
            tmp = list_[i]
            list_[idx+1:i+1] = list_[idx:i]
            list_[idx] = tmp
    return list_
def shell_sort(list_,gap=None):
    len_ = len(list_)
    gap = int(len_/2) if not gap else gap
    while gap >= 1:
        for i in range(gap):
            list_[i:len_:gap] = insert_sort(list_[i:len_:gap])
        gap = int(gap/2)
    return list_