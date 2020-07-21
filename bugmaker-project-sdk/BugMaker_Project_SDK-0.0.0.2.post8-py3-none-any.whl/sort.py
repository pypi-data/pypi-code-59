'''
Created by Begonia ,June 21st 2020, in SH
It's the Package for sorting functions
'''
import typing
__author__="Begonia"
def bubble_sort(list_:typing.List[int or float])->typing.List[int or float]:
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
def bucket_sort(list_:typing.List[int or float])->typing.List[int or float]:
    min_num = min(list_)
    max_num = max(list_)
    bucket_range = (max_num-min_num) / len(list_)
    count_list = [ [] for i in range(len(list_) + 1)]
    for i in list_:
        count_list[int((i-min_num)//bucket_range)].append(i)
    list_.clear()
    for i in count_list:
        for j in sorted(i):
            list_.append(j)
def count_sort(list_:typing.List[int or float])->typing.List[int or float]:
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
def insert_sort(list_:typing.List[int or float])->typing.List[int or float]:
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
def merge_sort(list_:typing.List[int or float])->typing.List[int or float]:
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
def quick_sort(list_:typing.List[int or float])->typing.List[int or float]:
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
    return quick_sort(left)+[base]+quick_sort(right)
def radix_sort(list_:typing.List[int or float])->typing.List[int or float]:
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
def select_sort(list_:typing.List[int or float])->typing.List[int or float]:
    for i in range(len(list_)-1):
        min_idx = i
        for j in range(i,len(list_)):
            if list_[min_idx]>list_[j]:
                min_idx = j
        list_[i],list_[min_idx] = list_[min_idx],list_[i]
    return list_
def insert_sort(list_:typing.List[int or float])->typing.List[int or float]:
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
def shell_sort(list_:typing.List[int or float],gap:int=None)->typing.List[int or float]:
    len_ = len(list_)
    gap = int(len_/2) if not gap else gap
    while gap >= 1:
        for i in range(gap):
            list_[i:len_:gap] = insert_sort(list_[i:len_:gap])
        gap = int(gap/2)
    return list_
def quick_sort(list_:typing.List[int or float])->typing.List[int or float]:
    length = len(list_)
    if length <= 1:
        return list_
    else:
        pivot = list_.pop()
        greater, lesser = [], []
        for element in list_:
            if element > pivot:
                greater.append(element)
            else:
                lesser.append(element)
        return quick_sort(lesser) + [pivot] + quick_sort(greater)
def pancake_sort(list_:typing.List[int or float])->typing.List[int or float]:
    cur = len(list_)
    while cur > 1:
        mi = list_.index(max(list_[0:cur]))
        list_ = list_[mi::-1] + list_[mi + 1 : len(list_)]
        list_ = list_[cur - 1 :: -1] + list_[cur : len(list_)]
        cur -= 1
    return list_