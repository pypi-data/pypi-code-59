def select_sort(list_):
    for i in range(len(list_)-1):
        min_idx = i
        for j in range(i,len(list_)):
            if list_[min_idx]>list_[j]:
                min_idx = j
        list_[i],list_[min_idx] = list_[min_idx],list_[i]
    return list_