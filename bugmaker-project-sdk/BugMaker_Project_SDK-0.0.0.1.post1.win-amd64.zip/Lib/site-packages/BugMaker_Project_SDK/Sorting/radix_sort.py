def radix_sort(list_):
    max_ = list_[0]
    for item in list_[1:]:
        if item > max_:
            max_ = item
    max_radix = len(str(max_))
    radix_list = [[],[],[],[],[],[],[],[],[],[]]
    cur_radix = 0
    while cur_radix<max_radix:
        base = 10**cur_radix
        for item in list_:
            radix_list[int(item/base)%10].append(item)
        list_ = []
        for item in radix_list:
            list_ += item

        radix_list = [[],[],[],[],[],[],[],[],[]]
        cur_radix += 1
    return list_