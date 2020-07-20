def bucket_sort(list_):
    bucket = [[],[],[],[],[]]
    max_ = list_[0]
    for item in list_[1:]:
        if item > max_:
            max_ = item
    gap = max_/5
    for item in list_:
        bucket[int((item-1)/gap)].append(item)
    for i in range(len(bucket)):
        bucket[i] = select(bucket[i])
    list_ = []
    for item in bucket:
        list_ += item
    return list_