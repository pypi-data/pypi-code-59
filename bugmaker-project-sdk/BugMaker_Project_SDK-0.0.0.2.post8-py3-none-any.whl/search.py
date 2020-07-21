import typing as t
def simple_search(list_:list,item:t.Any)->bool:
    for char in list_:
        if char==item:
            return True
        else:
            continue
    return False

