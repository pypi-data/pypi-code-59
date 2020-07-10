# -*- coding: utf-8 -*-

def int_list_to_bytes(intlist):
    from .strutils import ints2bytes
    return ints2bytes(intlist)

def pad(thelist, size, padding):
    if len(thelist) < size:
        for _ in range(size - len(thelist)):
            thelist.append(padding)
    return thelist

def chunk(thelist, size, with_padding=False, padding=None):
    data = []
    start = 0
    while True:
        if len(thelist) < size:
            if with_padding:
                pad(thelist, size, padding)
            data.append(thelist)
            break
        data.append(thelist[start:start+size])
        thelist = thelist[start+size:]
        if not thelist:
            break
    return data

def clean_none(thelist):
    """Remove None or empty element in thelist.
    """
    return [element for element in thelist if element]

ignore_none_element = clean_none


def unique(thelist):
    """Remove duplicated elements from the list.
    """
    result = []
    for element in thelist:
        if not element in result:
            result.append(element)
    return result

def replace(thelist, map, inplace=True):
    """Replace element in thelist, the map is collection of {old_value: new_value}.
    
    inplace == True, will effect the original list.
    inplace == False, will create a new list to return.
    """
    thelist = list(thelist)
    if inplace:
        for index in range(len(thelist)):
            value = thelist[index]
            if value in map:
                thelist[index] = map[value]
        return thelist
    else:
        newlist = []
        for index in range(len(thelist)):
            value = thelist[index]
            if value in map:
                newlist.append(map[value])
            else:
                newlist.append(value)
        return newlist

def append_new(thelist, value):
    """Append new value and only new value to the list.
    """
    if not value in thelist:
        thelist.append(value)
    return value

def group(thelist):
    """Count every element in thelist. e.g. ["a", "b", "c", "a", "b", "b"] => {"a": 2, "b": 3, "c": 1}.
    """
    info = {}
    for x in thelist:
        if x in info:
            info[x] += 1
        else:
            info[x] = 1
    return info

