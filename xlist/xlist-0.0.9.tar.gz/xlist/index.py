
def uniform_index(index,lngth):
    if(index<0):
        rl = lngth+index
        if(rl<0):
            index = 0
        else:
            index = rl
    elif(index>=lngth):
        index = lngth
    else:
        index = index
    return(index)



def index_fst(ol,value):
    return(ol.index(value))


def index_fst_not(ol,value):
    lngth = ol.__len__()
    for i in range(0,lngth):
        if(value == ol[i]):
            pass
        else:
            return(i)
    return(None)


def index_lst(ol,value):
    length = ol.__len__()
    for i in range(length-1,-1,-1):
        if(value == ol[i]):
            return(i)
        else:
            pass
    return(None)



def index_lst_not(ol,value):
    length = ol.__len__()
    for i in range(length-1,-1,-1):
        if(value == ol[i]):
            pass
        else:
            return(i)
    return(None)


def index_which(ol,value,which):
    length = ol.__len__()
    seq = -1
    for i in range(0,length):
        if(value == ol[i]):
            seq = seq + 1
            if(seq == which):
                return(i)
            else:
                pass
        else:
            pass
    return(None)


def index_which_not(ol,value,which):
    length = ol.__len__()
    seq = -1
    for i in range(0,length):
        if(value == ol[i]):
            pass
        else:
            seq = seq + 1
            if(seq == which):
                return(i)
            else:
                pass
    return(None)


def indexes_all(ol,value):
    length = ol.__len__()
    indexes =[]
    for i in range(0,length):
        if(value == ol[i]):
            indexes.append(i)
        else:
            pass
    return(indexes)



def indexes_all_not(ol,value):
    length = ol.__len__()
    indexes =[]
    for i in range(0,length):
        if(value == ol[i]):
            pass
        else:
            indexes.append(i)
    return(indexes)

def indexes_some(ol,value,*seqs):
    seqs = list(seqs)
    length = ol.__len__()
    indexes =[]
    seq = -1
    for i in range(0,length):
        if(value == ol[i]):
            seq = seq + 1
            if(seq in seqs):
                indexes.append(i)
            else:
                pass
        else:
            pass
    return(indexes)



def indexes_some_not(ol,value,*seqs):
    seqs = list(seqs)
    length = ol.__len__()
    indexes =[]
    seq = -1
    for i in range(0,length):
        if(value == ol[i]):
            pass
        else:
            seq = seq + 1
            if(seq in seqs):
                indexes.append(i)
            else:
                pass
    return(indexes)



def indexes_fst_slice(ol,value):
    length = ol.__len__()
    begin = None
    slice = []
    for i in range(0,length):
        if(ol[i]==value):
            begin = i
            break
        else:
            pass
    if(begin == None):
        return(None)
    else:
        slice.append(begin)
        for i in range(begin+1,length):
            if(ol[i]==value):
                slice.append(i)
            else:
                break
    return(slice)



def indexes_fst_not_slice(ol,value):
    length = ol.__len__()
    begin = None
    slice = []
    for i in range(0,length):
        if(not(ol[i]==value)):
            begin = i
            break
        else:
            pass
    if(begin == None):
        return(None)
    else:
        slice.append(begin)
        for i in range(begin+1,length):
            if(not(ol[i]==value)):
                slice.append(i)
            else:
                break
    return(slice)


def indexes_lst_slice(ol,value):
    length = ol.__len__()
    end = None
    slice = []
    for i in range(length-1,-1,-1):
        if(ol[i]==value):
            end = i
            break
        else:
            pass
    if(end == None):
        return(None)
    else:
        slice.append(end)
        for i in range(end-1,-1,-1):
            if(ol[i]==value):
                slice.append(i)
            else:
                break
    slice.reverse()
    return(slice)



def indexes_lst_not_slice(ol,value):
    length = ol.__len__()
    end = None
    slice = []
    for i in range(length-1,-1,-1):
        if(not(ol[i]==value)):
            end = i
            break
        else:
            pass
    if(end == None):
        return(None)
    else:
        slice.append(end)
        for i in range(end-1,-1,-1):
            if(not(ol[i]==value)):
                slice.append(i)
            else:
                break
    slice.reverse()
    return(slice)


def indexes_which_slice(ol,value):
    length = ol.__len__()
    seq = -1
    cursor = 0
    begin = None
    slice = []
    while(cursor < length):
        cond1 = (ol[cursor] == value)
        cond2 = (begin == None)
        if(cond1 & cond2):
            begin = cursor
            slice.append(cursor)
            cursor = cursor + 1
        elif(cond1 & (not(cond2))):
            slice.append(cursor)
            cursor = cursor + 1
        elif((not(cond1)) & (not(cond2))):
            seq = seq + 1
            if(seq == which):
                return(slice)
            else:
                cursor = cursor + 1
                begin = None
                slice = []
        else:
            cursor = cursor + 1
    if(slice):
        seq = seq + 1
    else:
        pass
    if(seq == which):
        return(slice)
    else:
        return([])


def indexes_which_not_slice(ol,value):
    length = ol.__len__()
    seq = -1
    cursor = 0
    begin = None
    slice = []
    while(cursor < length):
        cond1 = not(ol[cursor] == value)
        cond2 = (begin == None)
        if(cond1 & cond2):
            begin = cursor
            slice.append(cursor)
            cursor = cursor + 1
        elif(cond1 & (not(cond2))):
            slice.append(cursor)
            cursor = cursor + 1
        elif((not(cond1)) & (not(cond2))):
            seq = seq + 1
            if(seq == which):
                return(slice)
            else:
                cursor = cursor + 1
                begin = None
                slice = []
        else:
            cursor = cursor + 1
    if(slice):
        seq = seq + 1
    else:
        pass
    if(seq == which):
        return(slice)
    else:
        return([])


def indexes_some_slices(ol,value,*seqs):
    seqs = list(seqs)
    rslt = []
    length = ol.__len__()
    seq = -1
    cursor = 0
    begin = None
    slice = []
    while(cursor < length):
        cond1 = (ol[cursor] == value)
        cond2 = (begin == None)
        if(cond1 & cond2):
            begin = cursor
            slice.append(cursor)
        elif(cond1 & (not(cond2))):
            slice.append(cursor)
        elif((not(cond1)) & (not(cond2))):
            seq = seq + 1
            if(seq in seqs):
                rslt.append(slice)
            else:
                pass
            begin = None
            slice = []
        else:
            pass
        cursor = cursor + 1
    if(slice):
        seq = seq + 1
        if(seq in seqs):
            rslt.append(slice)
        else:
            pass
    else:
        pass
    return(rslt)


def indexes_some_not_slices(ol,value,*seqs):
    seqs = list(seqs)
    rslt = []
    length = ol.__len__()
    seq = -1
    cursor = 0
    begin = None
    slice = []
    while(cursor < length):
        cond1 = not(ol[cursor] == value)
        cond2 = (begin == None)
        if(cond1 & cond2):
            begin = cursor
            slice.append(cursor)
        elif(cond1 & (not(cond2))):
            slice.append(cursor)
        elif((not(cond1)) & (not(cond2))):
            seq = seq + 1
            if(seq in seqs):
                rslt.append(slice)
            else:
                pass
            begin = None
            slice = []
        else:
            pass
        cursor = cursor + 1
    if(slice):
        seq = seq + 1
        if(seq in seqs):
            rslt.append(slice)
        else:
            pass
    else:
        pass
    return(rslt)


def indexes_all_slices(ol,value):
    rslt = []
    length = ol.__len__()
    cursor = 0
    begin = None
    slice = []
    while(cursor < length):
        cond1 = (ol[cursor] == value)
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


def indexes_all_not_slices(ol,value):
    rslt = []
    length = ol.__len__()
    cursor = 0
    begin = None
    slice = []
    while(cursor < length):
        cond1 = not(ol[cursor] == value)
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






