from .map import mapv


def _dflt_vgroup_cond_func(v,*o):
    return((v == o[0]))


def group_indexes_via_value(ol,*args,**kwargs):
    cond_func = _dflt_vgroup_cond_func if(not("cond_func" in kwargs)) else kwargs["cond_func"]
    rslt = []
    length = ol.__len__()
    cursor = 0
    begin = None
    slice = []
    while(cursor < length):
        cond1 = cond_func(ol[cursor],*args)
        cond2 = (begin == None)
        if(cond1 & cond2):
            begin = cursor
            slice.append(cursor)
        elif(cond1 & (not(cond2))):
            slice.append(cursor)
        elif((not(cond1)) & (not(cond2))):
            rslt.append(slice)
            begin = None
            slice = []
        else:
            pass
        cursor = cursor + 1
    if(slice):
        rslt.append(slice)
    else:
        pass
    return(rslt)


def get_vgroupi_brkseqs(ol,*args,**kwargs):
    '''
        >>> vgroupi_brkseqs([0, 0, 0, 1, 2, 0, 2],0)
        [3, 6]
    '''
    slc = group_indexes_via_value(ol,*args,**kwargs)
    brkseqs = list(map(lambda ele:ele[-1]+1,slc))
    return(brkseqs)




def refl_brkseqs(refl):
    '''
        >>> refl_brkseqs([0, 0, 0, 1, 2, 2, 2])
        [3, 4]
    '''
    brks = []
    prev_value = refl[0]
    for i in range(1,len(refl)):
        curr_value = refl[i]
        if(curr_value == prev_value):
            pass
        else:
            brks.append(i)
            prev_value = curr_value
    return(brks)



def refl_vgroupv(refl):
    '''
        >>> refl_vgroupv([0, 0, 0, 1, 2, 2, 2])
        [[0, 0, 0], [1], [2, 2, 2]]
    '''
    rslts = []
    prev_value = refl[0]
    prev_index = 0
    for i in range(1,len(refl)):
        curr_value = refl[i]
        if(curr_value == prev_value):
            pass
        else:
            slc = refl[prev_index:i]
            rslts.append(slc)
            prev_value = curr_value
            prev_index = i
    slc = refl[prev_index:]
    rslts.append(slc)
    return(rslts)



def refl_vgroupi(refl):
    '''
        >>> refl_vgroupi([0, 0, 0, 1, 2, 2, 2])
        [[0, 1, 2], [3], [4, 5, 6]]
    '''
    rslts = []
    prev_value = refl[0]
    prev_index = 0
    lngth = len(refl)
    for i in range(1,lngth):
        curr_value = refl[i]
        if(curr_value == prev_value):
            pass
        else:
            slc = list(range(prev_index,i))
            rslts.append(slc)
            prev_value = curr_value
            prev_index = i
    slc = list(range(prev_index,lngth))
    rslts.append(slc)
    return(rslts)



def group_by_refl(ol,refl):
    '''

    '''
    rslts = []
    prev_value = refl[0]
    prev_index = 0
    for i in range(1,len(refl)):
        curr_value = refl[i]
        if(curr_value == prev_value):
            pass
        else:
            slc = ol[prev_index:i]
            rslts.append(slc)
            prev_value = curr_value
            prev_index = i
    slc = ol[prev_index:]
    rslts.append(slc)
    return(rslts)


def group_by_lngth(l):
    st = set({})
    rslt = {}
    for i in range(len(l)):
        lngth = len(l[i])
        if(lngth in st):
            rslt[lngth].append(l[i])
        else:
            st.add(lngth)
            rslt[lngth] = [l[i]]
    return(rslt)



def group_by_attr_lngth(l,attrname):
    st = set({})
    rslt = {}
    for i in range(len(l)):
        a = l[i].__getattribute__(attrname)
        lngth = len(a)
        if(lngth in st):
            rslt[lngth].append(l[i])
        else:
            st.add(lngth)
            rslt[lngth] = [l[i]]
    return(rslt)




def group_by_value_lngth(l,keyname):
    st = set({})
    rslt = {}
    for i in range(len(l)):
        v = l[i].__getitem__(keyname)
        lngth = len(v)
        if(lngth in st):
            rslt[lngth].append(l[i])
        else:
            st.add(lngth)
            rslt[lngth] = [l[i]]
    return(rslt)



def group_by_head_str(arr,n):
    ndict = {}
    for i in range(len(arr)):
        s = arr[i]
        s = s[0:n]
        cond = (s in ndict)
        if(cond):
            ndict[s].append(arr[i])
        else:
            ndict[s] = [arr[i]]
    return(ndict)


def group_values_using_continuous_same(l):
    '''
        l = [1,"a","a",2,2,"a",1,"a","b","a",5,"b","b","b"]
        >>> groupv_via_same(l)
        [[1], ['a', 'a'], [2, 2], ['a'], [1], ['a'], ['b'], ['a'], [5], ['b', 'b', 'b']]
        >>>
    '''
    rslt = []
    lngth = len(l)
    if(lngth ==0):
        return([])
    else:
        cursor = 0
        value = l[0]
        cache = []
        while(cursor < lngth):
            cond = (l[cursor] == value)
            if(cond):
                cache.append(value)
            else:
                rslt.append(cache)
                value = l[cursor]
                cache = [value]
            cursor = cursor + 1
        if(len(cache)>0):
            rslt.append(cache)
    return(rslt)



def group_indexes_using_continuous_same(l):
    '''
        l = [1,"a","a",2,2,"a",1,"a","b","a",5,"b","b","b"]
        >>> groupi_via_same(l)
        [[0], [1, 2], [3, 4], [5], [6], [7], [8], [9], [10], [11, 12, 13]]
        >>>
    '''
    rslt = []
    lngth = len(l)
    if(lngth ==0):
        return([])
    else:
        cursor = 0
        value = l[0]
        cache = []
        while(cursor < lngth):
            cond = (l[cursor] == value)
            if(cond):
                cache.append(cursor)
            else:
                rslt.append(cache)
                value = l[cursor]
                cache = [cursor]
            cursor = cursor + 1
        if(len(cache)>0):
            rslt.append(cache)
    return(rslt)


def group_ranges_via_continuous_same(l):
    '''
        l = [1,"a","a",2,2,"a",1,"a","b","a",5,"b","b","b"]
        >>> group_range_via_same(l)
        [[0, 1], [1, 3], [3, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 14]]
        >>>
    '''
    def map_func(ele):
        if(len(ele)==1):
            ele = [ele[0],ele[0]+1]
        else:
            ele = [ele[0],ele[-1]+1]
        return(ele)
    arr = group_indexes_using_continuous_same(l)
    rngs = mapv(arr,map_func)
    return(rngs)

