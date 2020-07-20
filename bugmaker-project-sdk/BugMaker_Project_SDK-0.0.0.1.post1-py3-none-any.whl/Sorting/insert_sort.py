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