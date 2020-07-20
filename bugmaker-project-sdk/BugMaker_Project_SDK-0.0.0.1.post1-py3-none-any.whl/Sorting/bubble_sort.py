def bubble_sort(list_):
    running = True
    while running:
        have_change = False
        for i in range(len(list_)-1):
            if list_[i]>list_[i+1]:
                list_[i],list_[i+1] = list_[i+1],list_[i]
                have_change = True
        if not have_change:
            break
    return list_