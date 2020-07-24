def find_lst_ipair_when_fstltsnd(arr):
    lngth = len(arr)
    for snd in range(lngth-1,0,-1):
        fst = snd - 1
        if(arr[fst]<arr[snd]):
            return((fst,snd))
        else:
            pass
    return(None)

def find_lst_vpair_when_fstltsnd(arr):
    lngth = len(arr)
    for snd in range(lngth-1,0,-1):
        fst = snd - 1
        if(arr[fst]<arr[snd]):
            return((arr[fst],arr[snd]))
        else:
            pass
    return(None)


def find_lst_ipair_when_fstgtsnd(arr):
    lngth = len(arr)
    for snd in range(lngth-1,0,-1):
        fst = snd - 1
        if(arr[fst]>arr[snd]):
            return((fst,snd))
        else:
            pass
    return(None)

def find_lst_vpair_when_fstgtsnd(arr):
    lngth = len(arr)
    for snd in range(lngth-1,0,-1):
        fst = snd - 1
        if(arr[fst]>arr[snd]):
            return((arr[fst],arr[snd]))
        else:
            pass
    return(None)
