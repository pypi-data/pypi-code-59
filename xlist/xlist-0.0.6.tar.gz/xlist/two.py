def comprise(list1,list2,**kwargs):
    if('mode' in kwargs):
        mode = kwargs['mode']
    else:
        mode = "loose"
    len_1 = list1.__len__()
    len_2 = list2.__len__()
    if(len_2>len_1):
        return(False)
    else:
        if(mode=="strict"):
            if(list2 == list1[:len_2]):
                return(True)
            else:
                return(False)
        else:
            end = len_1 - len_2
            for i in range(0,end+1):
                if(list2 == list1[i:(i+len_2)]):
                    return(True)
                else:
                    pass
    return(False)




def diff_indexes(l1,l2):
    '''
        from elist.elist import *
        l1 = [1,2,3,5]
        l2 = [0,2,3,4]
        diff_indexes(l1,l2)
    '''
    rslt = []
    for i in range(0,l1.__len__()):
        if(l1[i]!=l2[i]):
            rslt.append(i)
    return(rslt)

def diff_values(l1,l2):
    '''
        from elist.elist import *
        l1 = [1,2,3,5]
        l2 = [0,2,3,4]
        diff_values(l1,l2)
    '''
    rslt = []
    for i in range(0,l1.__len__()):
        if(l1[i]!=l2[i]):
            rslt.append(l1[i])
    return(rslt)


def same_indexes(l1,l2):
    '''
        from elist.elist import *
        l1 = [1,2,3,5]
        l2 = [0,2,3,4]
        same_indexes(l1,l2)
    '''
    rslt = []
    for i in range(0,l1.__len__()):
        if(l1[i]==l2[i]):
            rslt.append(i)
    return(rslt)

def same_values(l1,l2):
    '''
        from elist.elist import *
        l1 = [1,2,3,5]
        l2 = [0,2,3,4]
        same_values(l1,l2)
    '''
    rslt = []
    for i in range(0,l1.__len__()):
        if(l1[i]==l2[i]):
            rslt.append(l1[i])
    return(rslt)

def intersection(ol1,ol2):
    nl = list(set(ol1).intersection(set(ol2)))
    return(nl)

def shorter(ol1,ol2):
    lngth1 = len(ol1)
    lngth2 = len(ol2)
    if(lngth1 < lngth2):
        return(ol1)
    else:
        return(ol2)

def longer(ol1,ol2):
    lngth1 = len(ol1)
    lngth2 = len(ol2)
    if(lngth1 > lngth2):
        return(ol1)
    else:
        return(ol2)



def ordered_intersection(ol1,ol2):
    nl = []
    ol = shorter(ol1,ol2)
    for i in range(len(ol)):
        cond = (ol1[i] == ol2[i])
        if(cond):
            nl.append(ol1[i])
        else:
            pass
    return(nl)


def fullinfo_intersection(ol1,ol2,**kwargs):
    if("detailed" in kwargs):
        detailed = kwargs['detailed']
    else:
        detailed = False
    len1  = ol1
    len2  = ol2
    lngth = min(len1,len2)
    rslt = []
    for i in range(lngth):
        if(ol1[i] == ol2[i]):
            if(detailed):
                rslt.append({
                    "index":i,
                    "value":ol1[i]
                })
            else:
                rslt.append(ol1[i])
        else:
            pass
    return(rslt)


def union(ol1,ol2):
    nl = list(set(ol1).union(set(ol2)))
    return(nl)

def difference(ol1,ol2):
    nl = list(set(ol1).difference(set(ol2)))
    return(nl)

def fst_cmmn_val_index(l0,l1,**kwargs):
    reverse =  kwargs['reverse'] if("reverse" in kwargs) else False
    lngth = min(len(l0),len(l1))
    if(reverse):
        cursor = None
        for i in range(-1,-1-lngth,-1):
            if(l0[i] == l1[i]):
                cursor = i
            else:
                break
        if(cursor == None):
            # the fst from end is-not-eq
            return(None)
        else:
            rslt = (uniform_index(cursor,len(l0)),uniform_index(cursor,len(l1)))
            return(rslt)
    else:
        for i in range(lngth):
            if(l0[i] == l1[i]):
                return((i,i))
            else:
                pass
        return(None)


def fst_cmmn_val(l0,l1,**kwargs):
    rslt = fst_cmmn_val_index(l0,l1,**kwargs)
    rslt = None if(rslt==None) else l0[rslt[0]]
    return(rslt)


