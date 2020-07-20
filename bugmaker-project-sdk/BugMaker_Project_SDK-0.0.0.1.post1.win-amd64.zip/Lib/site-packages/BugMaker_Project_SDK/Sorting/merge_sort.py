def merge_sort(list_):
    if len(list_)<=1:
        return list_
    if len(list_)==2:
        return list_ if list_[0]<=list_[1] else list_[::-1]
    len_ = len(list_)
    left = merge_sort(list_[:int(len_/2)])
    right = merge_sort(list_[int(len_/2):])
    tmp = []
    left_idx,right_idx = 0,0
    while len(tmp)<len(list_):
        if left[left_idx]<=right[right_idx]:
            tmp.append(left[left_idx])
            left_idx+=1
            if left_idx==len(left):
                tmp += right[right_idx:]
                break
        else:
            tmp.append(right[right_idx])
            right_idx+=1
            if right_idx==len(right):
                tmp += left[left_idx:]
                break
    return tmp
