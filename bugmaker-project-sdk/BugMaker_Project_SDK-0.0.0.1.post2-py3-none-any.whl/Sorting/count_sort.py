def count_sort(list_):
    min_,max_ = list_[0],list_[0]
    for i in range(1,len(list_)):
        if list_[i]<min_:
            min_ = list_[i]
        if list_[i]>max_:
            max_ = list_[i]
    count_list = [0]*(max_-min_+1)
    for item in list_:
        count_list[item-min_] += 1

    list_ = []
    for i in range(len(count_list)):
        for j in range(count_list[i]):
            list_.append(i+min_)
    return list_