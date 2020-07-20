import copy
from operator import itemgetter
from types import MethodType
import functools
import itertools
import random
# 为了避免循环import efuntool 只能单独引入一个函数


def cond_select_all(ol,**kwargs):
    '''
        from elist.elist import *
        from elist.jprint import pobj
        def test_func(ele,x):
            cond = (ele > x)
            return(cond)

        ol = [1,2,3,4,5,6,7]
        rslt = cond_select_all(ol,cond_func = test_func,cond_func_args = [3])
        pobj(rslt)
    '''
    cond_func = kwargs['cond_func']
    if('cond_func_args' in kwargs):
        cond_func_args = kwargs['cond_func_args']
    else:
        cond_func_args = []
    ####
    founded = find_all(ol,cond_func,*cond_func_args)
    rslt = array_map(founded,lambda ele:ele['value'])
    return(rslt)


def cond_select_all2(ol,**kwargs):
    '''
        from elist.elist import *
        from xdict.jprint import pobj
        def test_func(ele,index,x):
            cond1 = (ele > x)
            cond2 = (index %2 == 0)
            cond =(cond1 & cond2)
            return(cond)

        ol = [1,2,3,4,5,6,7]
        rslt = cond_select_all2(ol,cond_func = test_func,cond_func_args = [3])
        pobj(rslt)
    '''
    cond_func = kwargs['cond_func']
    if('cond_func_args' in kwargs):
        cond_func_args = kwargs['cond_func_args']
    else:
        cond_func_args = []
    ####
    founded = find_all2(ol,cond_func,*cond_func_args)
    rslt = array_map(founded,lambda ele:ele['value'])
    return(rslt)


cond_select_values_all = cond_select_all
cond_select_values_all2 = cond_select_all2


def eqlength_select_values_all(ol,lngth):
    return(cond_select_values_all(ol,cond_func=lambda ele:(ele.__len__()==lngth)))

def gelength_select_values_all(ol,lngth):
    return(cond_select_values_all(ol,cond_func=lambda ele:(ele.__len__()>=lngth)))

def gtlength_select_values_all(ol,lngth):
    return(cond_select_values_all(ol,cond_func=lambda ele:(ele.__len__()>lngth)))

def lelength_select_values_all(ol,lngth):
    return(cond_select_values_all(ol,cond_func=lambda ele:(ele.__len__()<=lngth)))

def ltlength_select_values_all(ol,lngth):
    return(cond_select_values_all(ol,cond_func=lambda ele:(ele.__len__()<lngth)))


def cond_select_indexes_all(ol,**kwargs):
    '''
        from elist.elist import *
        from elist.jprint import pobj
        def test_func(ele,x):
            cond = (ele > x)
            return(cond)
        
        ol = [1,2,3,4,5,6,7]
        rslt = cond_select_indexes_all(ol,cond_func = test_func, cond_func_args = [3])
        pobj(rslt)
    '''
    cond_func = kwargs['cond_func']
    if('cond_func_args' in kwargs):
        cond_func_args = kwargs['cond_func_args']
    else:
        cond_func_args = []
    ####
    founded = find_all(ol,cond_func,*cond_func_args)
    rslt = array_map(founded,lambda ele:ele['index'])
    return(rslt)


def cond_select_indexes_all2(ol,**kwargs):
    '''
        from elist.elist import *
        from xdict.jprint import pobj
        def test_func(ele,index,x):
            cond1 = (ele > x)
            cond2 = (index %2 == 0)
            cond =(cond1 & cond2)
            return(cond)

        ol = [1,2,3,4,5,6,7]
        rslt = cond_select_indexes_all2(ol,cond_func = test_func,cond_func_args = [3])
        pobj(rslt)
    '''
    cond_func = kwargs['cond_func']
    if('cond_func_args' in kwargs):
        cond_func_args = kwargs['cond_func_args']
    else:
        cond_func_args = []
    ####
    founded = find_all2(ol,cond_func,*cond_func_args)
    rslt = array_map(founded,lambda ele:ele['index'])
    return(rslt)



#######################################
#swap and reindex
########################################

def iswap(arr,i1,i2,**kwargs):
    if('deepcopy' in kwargs):
        deepcopy = kwargs['deepcopy']
    else:
        deepcopy = True
    if(deepcopy):
        arr = copy.deepcopy(arr)
    else:
        pass
    tmp = arr[i1]
    arr[i1] = arr[i2]
    arr[i2] = tmp
    return(arr)


def vswap(arr,v1,v2,**kwargs):
    i1 = arr.index(v1)
    i2 = arr.index(v2)
    arr = iswap(arr,i1,i2,**kwargs)
    return(arr)


def reindex(arr,*nindexes,**kwargs):
    if('deepcopy' in kwargs):
        deepcopy = kwargs['deepcopy']
    else:
        deepcopy = True
    if(deepcopy):
        arr = copy.deepcopy(arr)
    else:
        pass
    nindexes = list(nindexes)
    if(isinstance(nindexes[0],list)):
        nindexes = nindexes[0]
    else:
        nindexes = nindexes
    tmp = copy.deepcopy(arr)
    for i in range(nindexes.__len__()):
        arr[nindexes[i]] = tmp[i]
    return(arr)







#####################################
#
######################################



def setsome(ol,*args,**kwargs):
    nl = newlist(ol,**kwargs)
    args = list(args)
    if(isinstance(args,list)):
        indexes = args[0]
        values = args[1]
    else:
        indexes = slct_odds(ol)
        values = slct_evens(ol)
    lngth = indexes.__len__()
    for i in range(lngth):
        index = indexes[i]
        value = values[i]
        nl[index] = value
    return(nl)



# class name initial is  uppercased 
# vars 可以动态调用函数
###############################

def str_fuzzy_search(arr,k):
    slcted = cond_select_values_all(arr,cond_func = lambda ele:(k in ele))
    return(slcted)


##############################

#############################

#cond_select_values
##select (values) (via) cond_func(index,value,*cond_func_args)

#cond_select = cond_select_values

#cond_select_some = cond_select_values_via_some
#cond_select_seqs = cond_select_values_via_seqs
#cond_select_many = cond_select_values_via_manay

#cond_select_indexes
##select (values) (via) cond_func(index,value,*cond_func_args)
#cond_select_indexes_some
#cond_select_indexes_seqs
#cond_select_indexes_many

#def icond_select_all(ol,**kwargs):






###################################################

def append(ol,ele,**kwargs):
    '''
        from elist.elist import *
        ol = [1,2,3,4]
        ele = 5
        id(ol)
        append(ol,ele,mode="original")
        ol
        id(ol)
        ####
        ol = [1,2,3,4]
        ele = 5
        id(ol)
        new = append(ol,ele)
        new
        id(new)
    '''
    if('mode' in kwargs):
        mode = kwargs["mode"]
    else:
        mode = "new"
    if(mode == "new"):
        new = copy.deepcopy(ol)
        new.append(ele)
        return(new)
    else:
        ol.append(ele)
        return(ol)

def append_some(ol,*eles,**kwargs):
    '''
        from elist.elist import *
        ol = [1,2,3,4]
        id(ol)
        append_some(ol,5,6,7,8,mode="original")
        ol
        id(ol)
        ####
        ol = [1,2,3,4]
        id(ol)
        new = append_some(ol,5,6,7,8)
        new
        id(new)
    '''
    if('mode' in kwargs):
        mode = kwargs["mode"]
    else:
        mode = "new"
    return(extend(ol,list(eles),mode=mode))


def prepend(ol,ele,**kwargs):
    '''
        from elist.elist import *
        ol = [1,2,3,4]
        ele = 5
        id(ol)
        prepend(ol,ele,mode="original")
        ol
        id(ol)
        ####
        ol = [1,2,3,4]
        ele = 5
        id(ol)
        new = prepend(ol,ele)
        new
        id(new)
    '''
    if('mode' in kwargs):
        mode = kwargs["mode"]
    else:
        mode = "new"
    if(mode == "new"):
        new = [ele]
        cpol = copy.deepcopy(ol)
        new.extend(cpol)
        return(new)
    else:
        length = ol.__len__()
        ol.append(None)
        for i in range(length-1,-1,-1):
            ol[i+1] = ol[i]
        ol[0] = ele
        return(ol)

def prepend_some(ol,*eles,**kwargs):
    '''
        from elist.elist import *
        ol = [1,2,3,4]
        id(ol)
        prepend_some(ol,5,6,7,8,mode="original")
        ol
        id(ol)
        ####
        ol = [1,2,3,4]
        id(ol)
        new = prepend_some(ol,5,6,7,8)
        new
        id(new)
        #####unshift is the same as prepend_some
        >>> unshift(ol,9,10,11,12)
        [9, 10, 11, 12, 1, 2, 3, 4]
    '''
    if('mode' in kwargs):
        mode = kwargs["mode"]
    else:
        mode = "new"
    return(prextend(ol,list(eles),mode=mode))

unshift = prepend_some

def extend(ol,nl,**kwargs):
    '''
        from elist.elist import *
        ol = [1,2,3,4]
        nl = [5,6,7,8]
        id(ol)
        extend(ol,nl,mode="original")
        ol
        id(ol)
        ####
        ol = [1,2,3,4]
        nl = [5,6,7,8]
        id(ol)
        new = extend(ol,nl)
        new
        id(new)
    '''
    if('mode' in kwargs):
        mode = kwargs["mode"]
    else:
        mode = "new"
    if(mode == "new"):
        new = copy.deepcopy(ol)
        cpnl = copy.deepcopy(nl)
        new.extend(cpnl)
        return(new)
    else:
        ol.extend(nl)
        return(ol)

def push(ol,*eles,**kwargs):
    '''
        from elist.elist import *
        ol=[1,2,3,4]
        id(ol)
        new = push(ol,5,6,7)
        new
        id(new)
        ####
        ol=[1,2,3,4]
        id(ol)
        rslt = push(ol,5,6,7,mode="original")
        rslt
        id(rslt)
    '''
    if('mode' in kwargs):
        mode = kwargs['mode']
    else:
        mode = "new"
    eles = list(eles)
    return(extend(ol,eles,mode=mode))

def prextend(ol,nl,**kwargs):
    '''
        from elist.elist import *
        ol = [1,2,3,4]
        nl = [5,6,7,8]
        id(ol)
        id(nl)
        prextend(ol,nl,mode="original")
        ol
        id(ol)
        ####
        ol = [1,2,3,4]
        nl = [5,6,7,8]
        id(ol)
        id(nl)
        new = prextend(ol,nl)
        new
        id(new)
    '''
    if('mode' in kwargs):
        mode = kwargs["mode"]
    else:
        mode = "new"
    if(mode == "new"):
        new = copy.deepcopy(nl)
        cpol = copy.deepcopy(ol)
        new.extend(cpol)
        return(new)
    else:
        length = ol.__len__()
        nl_len = nl.__len__()
        for i in range(0,nl_len):
            ol.append(None)
        for i in range(length-1,-1,-1):
            ol[i+nl_len] = ol[i]
        for i in range(0,nl_len):
            ol[i] = nl[i]
        return(ol)

def concat(*arrays):
    '''
        from elist.elist import *
        l1 = [1,2,3]
        l2 = ["a","b","c"]
        l3 = [100,200]
        id(l1)
        id(l2)
        id(l3)
        arrays = [l1,l2,l3]
        new = concat(arrays)
        new
        id(new)
    '''
    new = []
    length = arrays.__len__()
    for i in range(0,length):
        array = copy.deepcopy(arrays[i])
        new.extend(array)
    return(new)

concat_some = concat

def concat_seqs(arrays):
    '''
        from elist.elist import *
        l1 = [1,2,3]
        l2 = ["a","b","c"]
        l3 = [100,200]
        id(l1)
        id(l2)
        id(l3)
        arrays = [l1,l2,l3]
        new = concat_seqs(arrays)
        new
        id(new)
    '''
    return(concat(*tuple(arrays)))



def cons(head_ele,l,**kwargs):
    '''
        from elist.elist import *
        ol=[1,2,3,4]
        id(ol)
        new = cons(5,ol)
        new
        id(new)
        ####
        ol=[1,2,3,4]
        id(ol)
        rslt = cons(5,ol,mode="original")
        rslt
        id(rslt)
    '''
    if('mode' in kwargs):
        mode = kwargs['mode']
    else:
        mode = "new"
    return(prepend(l,head_ele,mode=mode))


def insert(ol,start_index,ele,**kwargs):
    '''
        from elist.elist import *
        ol = [1,2,3,4]
        ele = 5
        id(ol)
        insert(ol,2,ele,mode="original")
        ol
        id(ol)
        ####
        ol = [1,2,3,4]
        ele = 5
        id(ol)
        new = insert(ol,2,ele)
        new
        id(new)
    '''
    if('mode' in kwargs):
        mode = kwargs["mode"]
    else:
        mode = "new"
    if(mode == "new"):
        length = ol.__len__()
        cpol = copy.deepcopy(ol)
        si = uniform_index(start_index,length)
        new = copy.deepcopy(cpol[0:si])
        new.append(ele)
        new.extend(cpol[si:])
        return(new)
    else:
        ol.insert(start_index,ele)
        return(ol)

def insert_some(ol,*eles,**kwargs):
    '''
        from elist.elist import *
        ol = [1,2,3,4]
        id(ol)
        insert_some(ol,5,6,7,8,index=2,mode="original")
        ol
        id(ol)
        ####
        ol = [1,2,3,4]
        id(ol)
        new = insert_some(ol,5,6,7,8,index=2)
        new
        id(new)
    '''
    start_index = kwargs['index']
    if('mode' in kwargs):
        mode = kwargs["mode"]
    else:
        mode = "new"
    length = ol.__len__()
    cpol = copy.deepcopy(ol)
    if(mode == "new"):
        si = uniform_index(start_index,length)
        new = copy.deepcopy(cpol[0:si])
        new.extend(list(eles))
        new.extend(cpol[si:])
        return(new)
    else:
        si = uniform_index(start_index,length)
        new = cpol[0:si]
        new.extend(list(eles))
        new.extend(cpol[si:])
        ol.clear()
        for i in range(0,new.__len__()):
            ol.append(new[i])
        return(ol)

def insert_many(ol,eles,locs,**kwargs):
    '''
        from elist.elist import *
        ol = [1,2,3,4,5]
        eles = [7,77,777]
        locs = [0,2,4]
        id(ol)
        new = insert_many(ol,eles,locs)
        ol
        new
        id(new)
        ####
        ol = [1,2,3,4,5]
        eles = [7,77,777]
        locs = [0,2,4]
        id(ol)
        rslt = insert_many(ol,eles,locs,mode="original")
        ol
        rslt
        id(rslt)
    '''
    if('mode' in kwargs):
        mode = kwargs["mode"]
    else:
        mode = "new"
    eles = copy.deepcopy(eles)
    locs = copy.deepcopy(locs)
    new = []
    length = ol.__len__()
    cpol = copy.deepcopy(ol)
    for i in range(0,locs.__len__()):
        if(locs[i]>=length):
            pass
        else:
            locs[i] = uniform_index(locs[i],length)
    tmp = sorted_refer_to(eles,locs)
    eles = tmp['list']
    locs = tmp['referer']
    label = eles.__len__()
    si = 0
    ei = 0
    for i in range(0,locs.__len__()):
        if(locs[i]>=length):
            label = i
            break
        else:
            ei = locs[i]
            new.extend(cpol[si:ei])
            new.append(eles[i])
            si = ei
    for i in range(label,locs.__len__()):
        new.append(eles[i])
    new.extend(cpol[ei:])
    if(mode == "new"):
        return(new)
    else:
        ol.clear()
        ol.extend(new)
        return(ol)

def insert_sections_some(ol,*secs,**kwargs):
    '''
        ol = initRange(0,20,1)
        ol
        loc = 6
        rslt = insert_sections_some(ol,['a','a','a'],['c','c','c','c'],index=loc)
        rslt
        ####
    '''
    if('mode' in kwargs):
        mode = kwargs["mode"]
    else:
        mode = "new"
    loc = kwargs['index']
    secs = list(secs)
    secs = [concat(*secs)]
    locs = [loc]
    return(insert_sections_many(ol,secs,locs,mode=mode))


def insert_section(ol,sec,loc,**kwargs):
    '''
        ol = initRange(0,20,1)
        ol
        loc = 6
        sec = ['a','b','c','d']
        rslt = insert_section(ol,sec,loc)
        rslt
        ####
    '''
    if('mode' in kwargs):
        mode = kwargs["mode"]
    else:
        mode = "new"
    secs = [sec]
    locs = [loc]
    return(insert_sections_many(ol,secs,locs,mode=mode))

def insert_sections_many(ol,secs,locs,**kwargs):
    '''
        ol = initRange(0,20,1)
        ol
        locs = [1,6,14,9]
        secs = [
            ['a','a','a'],
            ['b','b'],
            ['c','c','c','c'],
            ['d','d']
        ]
        rslt = insert_sections_many(ol,secs,locs)
        rslt
        ####
        ol
        locs = [0,3,6,9,12,15,16]
        secs = [
            ['a','a','a'],
            ['b','b'],
            ['c','c','c','c'],
            ['d','d']
        ]
        rslt = insert_sections_many(ol,secs,locs)
        rslt
        ####
        ol
        locs = [1,6,14,9]
        secs = [
            ['a','a','a'],
            ['b','b'],
            ['c','c','c','c'],
            ['d','d'],
            ['e'],
            ['f','f','f','f'],
            [777,777,777,777]
        ]
        rslt = insert_sections_many(ol,secs,locs)
        rslt
    '''
    if('mode' in kwargs):
        mode = kwargs["mode"]
    else:
        mode = "new"
    secs = copy.deepcopy(secs)
    locs = copy.deepcopy(locs)
    brked = broken_seqs(ol,locs)
    seclen = secs.__len__()
    brklen = brked.__len__()
    if(locs[0]==0):
        new = secs[0]
        length = seclen -1
        if(length < brklen):
            for i in range(0,length):
                new.extend(brked[i])
                new.extend(secs[i+1])
            for i in range(length,brklen):
                new.extend(brked[i])
        elif(length == brklen):
            for i in range(0,length):
                new.extend(brked[i])
                new.extend(secs[i+1])
        else:
            for i in range(0,brklen):
                new.extend(brked[i])
                new.extend(secs[i+1])
            for i in range(brklen,length):
                new.extend(secs[i])
    else:
        new = brked[0]
        length = brklen -1
        if(length < seclen):
            for i in range(0,length):
                new.extend(secs[i])
                new.extend(brked[i+1])
            for i in range(length,seclen):
                new.extend(secs[i])
        elif(length == seclen):
            for i in range(0,length):
                new.extend(secs[i])
                new.extend(brked[i+1])
        else:
            for i in range(0,seclen):
                new.extend(secs[i])
                new.extend(brked[i+1])
            for i in range(seclen,length):
                new.extend(brked[i])
    if(mode == "new"):
        return(new)
    else:
        ol.clear()
        ol.extend(new)
        return(ol)

####

def reorder_sub(ol,sub):
    '''
        sub = ['query', 'params', 'fragment', 'path']
        ol = ['scheme', 'username', 'password', 'hostname', 'port', 'path', 'params', 'query', 'fragment']
        reorder_sub(ol,sub)
    '''
    def cond_func(ele,ol):
        index = ol.index(ele)
        return(index)
    indexes = array_map(sub,cond_func,ol)
    nsub = sorted_refer_to(sub,indexes)['list']
    return(nsub)



def sort(ol,**kwargs):
    '''
        from elist.elist import *
        ol = [1,3,4,2]
        id(ol)
        new = sort(ol)
        ol
        new
        id(ol)
        id(new)
        ####
        ol = [1,3,4,2]
        id(ol)
        rslt = sort(ol,mode="original")
        ol
        rslt
        id(ol)
        id(rslt)
    '''
    if('mode' in kwargs):
        mode = kwargs["mode"]
    else:
        mode = "new"
    if(mode == "new"):
        new = copy.deepcopy(ol)
        new.sort()
        return(new) 
    else:
        ol.sort()
        return(ol)

def sorted_refer_to(l,referer,reverse=False,**kwargs):
    '''
        from elist.elist import *
        l = ["a","b","c"]
        referer = [7,8,6]
        sorted_refer_to(l,referer)
        {'list': ['c', 'a', 'b'], 'referer': [6, 7, 8]}
        l
        referer
        >>>
    '''
    if("mode" in kwargs):
        mode = kwargs["mode"]
    else:
        mode = "both"
    tl =[]
    length = l.__len__()
    for i in range(0,length):
        ele = (l[i],referer[i])
        tl.append(ele)
    tl = sorted(tl,key=itemgetter(1),reverse=reverse)
    sorted_l =[]
    sorted_r = []
    for i in range(0,length):
        sorted_l.append(tl[i][0])
        sorted_r.append(tl[i][1])
    if(mode == "only-list"):
        return(sorted_l)
    elif(mode == "only-referer"):
        return(referer)
    else:
        return({"list":sorted_l,"referer":sorted_r})

def batsorted(referer,*lists,**kwargs):
    '''
        from elist.elist import *
        referer = [4,2,3,1]
        l1 = ['a','b','c','d']
        l2 = [100,200,300,400]
        l3 = ['A','B','A','B']
        nl1,nl2,nl3 = batsorted(referer,l1,l2,l3)
        nl1
        nl2
        nl3
        nl1,nl2,nl3 = batsorted(referer,l1,l2,l3,reverse=True)
        nl1
        nl2
        nl3
        ####the batsorted will not modify the original lists
        l1
        l2
        l3
    '''
    if('reverse' in kwargs):
        reverse = kwargs['reverse']
    else:
        reverse = False
    length = referer.__len__()
    indexes = list(range(0,length))
    rslt = sorted_refer_to(indexes,referer,reverse=reverse)
    referer = rslt['referer']
    indexes = rslt['list']
    rslt = []
    lists = copy.deepcopy(list(lists))
    for i in range(0,lists.__len__()):
        l = lists[i]
        nl = []
        for j in range(0,length):
            loc = indexes[j]
            nl.append(l[loc])
        rslt.append(nl)
    return(tuple(rslt))

####

def transpose(mat):
    nmat = init(mat[0].__len__(),[])
    nmat = mapv(nmat,lambda ele:init(mat.__len__(),None))
    for i in range(mat.__len__()):
        layer = mat[i]
        for j in range(layer.__len__()):
            nmat[j][i] = layer[j]
    return(nmat)
        


def batexec(map_func,*params_lists):
    params_lists = list(params_lists)
    args_array = transpose(params_lists)
    nl = []
    for i in range(args_array.__len__()):
        args = args_array[i]
        nl.append(map_func(*args))
    return(nl)


####

def sortDictList(dictList,**kwargs):
    '''
        students = [
            {'name':'john','class':'A', 'year':15},
            {'name':'jane','class':'B', 'year':12},
            {'name':'dave','class':'B', 'year':10}
        ]
        
        rslt = sortDictList(students,cond_keys=['name','class','year'])
        pobj(rslt)
        rslt = sortDictList(students,cond_keys=['name','year','class'])
        pobj(rslt)
        rslt = sortDictList(students,cond_keys=['class','name','year'])
        pobj(rslt)
        rslt = sortDictList(students,cond_keys=['class','year','name'])
        pobj(rslt)
        rslt = sortDictList(students,cond_keys=['year','name','class'])
        pobj(rslt)
        rslt = sortDictList(students,cond_keys=['year','name','class'])
        pobj(rslt)
    '''
    def default_eq_func(value1,value2):
        cond = (value1 == value2)
        return(cond)
    def default_gt_func(value1,value2):
        cond = (value1 > value2)
        return(cond)
    def default_lt_func(value1,value2):
        cond = (value1 < value2)
        return(cond)
    if('eq_func' in kwargs):
        eq_func = kwargs['eq_func']
    else:
        eq_func = default_eq_func
    if('gt_func' in kwargs):
        gt_func = kwargs['gt_func']
    else:
        gt_func = default_gt_func
    if('lt_func' in kwargs):
        lt_func = kwargs['lt_func']
    else:
        lt_func = default_lt_func
    if('reverse' in kwargs):
        reverse = kwargs['reverse']
    else:
        reverse = False
    keys = kwargs['cond_keys']
    def cmp_dict(d1,d2):
        '''
        '''
        length = keys.__len__()
        for i in range(0,length):
            key = keys[i]
            cond = eq_func(d1[key],d2[key])
            if(cond):
                pass
            else:
                cond = gt_func(d1[key],d2[key])
                if(cond):
                    return(1)
                else:
                    return(-1)
        return(0)
    ndl = dictList
    ndl = sorted(ndl,key=functools.cmp_to_key(cmp_dict),reverse=reverse)
    return(ndl)


###############

def lcstr(s0,s1):
    len0 = len(s0)
    len1 = len(s1)
    slider_len = len1-1 + len0 + len1-1
    label_s0_end = len1-1 + len0 + 1
    label_s0_start = len1 
    def get_si1_ei1(len1,label_s0_end,cursor):
        si1 = len1-1-cursor 
        si1 = 0 if(si1 <0) else si1
        ei1 = len1 if((cursor+len1)<(label_s0_end)) else (label_s0_end-cursor-1)
        return((si1,ei1))
    def get_si0_ei0(len1,label_s0_start,label_s0_end,cursor):
        si0 = 0 if(cursor <label_s0_start) else (cursor-len1+1)
        ei0 = len0 if((cursor+len1)>=label_s0_end) else ((cursor+1))
        return((si0,ei0))
    def lcstr_for_same_length_array(arr0,arr1,lngth):
        rslt = []
        i = 0
        si = None
        while(i<lngth):
            if(arr0[i] == arr1[i]):
                if(si == None):
                    si = i
                else:
                    pass
            else:
                if(si != None):
                    t = (si,i)
                    rslt.append(t)
                    si = None
                else:
                    pass
            i = i + 1
        return(rslt)
    def get_comm_substr(len0,len1,label_s0_end):
        rslt = []
        si1_begin = 0
        si1_end = len1-1 + len0 + 1
        si0_begin = len1-1
        for cursor in range(si1_begin,si1_end):
            si1,ei1 = get_si1_ei1(len1,label_s0_end,cursor)
            si0,ei0 = get_si0_ei0(len1,label_s0_start,label_s0_end,cursor)
            subs0 = s0[si0:ei0]
            subs1 = s1[si1:ei1]
            lngth = ei0 - si0
            tmp = lcstr_for_same_length_array(subs0,subs1,lngth)
            for each in tmp:
                rsi,rei = each
                cmms = subs0[rsi:rei]
                if(len(cmms)==0):
                    pass
                else:
                    d = {
                        "pos0":(si0+rsi,si0+rei),
                        "pos1":(si1+rsi,si1+rei),
                        "s":cmms,
                        "len":len(cmms)
                    }
                    rslt.append(d)
            rslt = sortDictList(rslt,cond_keys=['len'])
        return(rslt)
    rslt = get_comm_substr(len0,len1,label_s0_end)
    return(rslt)

###############



def sortDictList2(dictList,**kwargs):
    '''
        
    '''
    def default_eq_func(value1,value2):
        cond = (value1 == value2)
        return(cond)
    def default_gt_func(value1,value2):
        cond = (value1 > value2)
        return(cond)
    def default_lt_func(value1,value2):
        cond = (value1 < value2)
        return(cond)
    keys = kwargs['cond_keys']
    length = keys.__len__()
    if('eq_funcs' in kwargs):
        eq_funcs = kwargs['eq_funcs']
    else:
        eq_funcs = [default_eq_func] * length
    if('gt_funcs' in kwargs):
        gt_funcs = kwargs['gt_funcs']
    else:
        gt_funcs = [default_gt_func] * length
    if('lt_funcs' in kwargs):
        lt_funcs = kwargs['lt_funcs']
    else:
        lt_funcs = [default_lt_func] * length
    def cmp_dict(d1,d2):
        '''
        '''
        for i in range(0,length):
            key = keys[i]
            eq_func = eq_funcs[i]
            cond = eq_func(d1[key],d2[key])
            if(cond):
                pass
            else:
                gt_func = gt_funcs[i]
                cond = gt_func(d1[key],d2[key])
                if(cond):
                    return(1)
                else:
                    return(-1)
        return(0)
    ndl = dictList
    ndl = sorted(ndl,key=functools.cmp_to_key(cmp_dict))
    return(ndl)

########

##group

def _dflt_vgroup_cond_func(v,*o):
    return((v == o[0]))

def vgroupi(ol,*args,**kwargs):
    '''
        vgroupi([0, 0, 0, 1, 2, 0, 2],0)
        [[0, 1, 2], [5]]
    '''
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


##

def vgroupi_brkseqs(ol,*args,**kwargs):
    '''
        >>> vgroupi_brkseqs([0, 0, 0, 1, 2, 0, 2],0)
        [3, 6]
    '''
    slc = vgroupi(ol,*args,**kwargs)
    brkseqs = list(map(lambda ele:ele[-1]+1,slc))
    return(brkseqs)
##


##
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



def groupby_refl(ol,refl):
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



########

def groupby_lngth(l):
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



def groupby_attr_lngth(l,attrname):
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


def groupby_value_lngth(l,keyname):
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

#######

def groupby_head_str(arr,n):
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



########
########

def groupv_via_same(l):
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

def groupi_via_same(l):
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


def group_range_via_same(l):
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
    arr = groupi_via_same(l)
    rngs = elel.mapv(arr,map_func)
    return(rngs)


########
########




def shift(ol,**kwargs):
    '''
        from elist.jprint import pobj
        from elist.elist import *
        ol = [1,2,3,4]
        id(ol)
        rslt = shift(ol)
        pobj(rslt)
        ol
        id(ol)
        id(rslt['list'])
        ####
        ol = [1,2,3,4]
        id(ol)
        rslt = shift(ol,mode="original")
        rslt
        ol
        id(ol)
    '''
    if('mode' in kwargs):
        mode = kwargs['mode']
    else:
        mode = "new"
    length = ol.__len__()
    rslt = pop(ol,0,mode=mode)
    return(rslt)

def pop(ol,index,**kwargs):
    '''
        from elist.jprint import pobj
        from elist.elist import *
        ol = [1,2,3,4]
        id(ol)
        rslt = pop(ol,2)
        pobj(rslt)
        ol
        id(ol)
        id(rslt['list'])
        ####
        ol = [1,2,3,4]
        id(ol)
        rslt = pop(ol,2,mode="original")
        rslt
        ol
        id(ol)
    '''
    index = uniform_index(index,ol.__len__())
    if('mode' in kwargs):
        mode = kwargs["mode"]
    else:
        mode = "new"
    if(mode == "new"):
        new = copy.deepcopy(ol)
        popped = new.pop(index)
        return({'popped':popped,'list':new})
    else:
        popped = ol.pop(index)
        return(popped)
#



def cond_pop(ol,index,**kwargs):
    '''
        from elist.jprint import pobj
        from elist.elist import *
        ol = [{'data':0;'type':'number'},{'data':'x';'type':'str'},{'data':'y';'type':'str'},4]
        #cond_func_args is a array
        def cond_func(index,value,cond_func_args):
            
    '''
    cond_func = kwargs['cond_func']
    cond_func_args = kwargs['cond_func_args']
    index = uniform_index(index,ol.__len__())
    if('mode' in kwargs):
        mode = kwargs["mode"]
    else:
        mode = "new"
    value = ol[index]
    cond = cond_func(index,value,*cond_func_args)
    if(mode == "new"):
        new = copy.deepcopy(ol)
        if(cond):
            popped = new.pop(index)
        else:
            popped = new
        return({'popped':popped,'list':new})
    else:
        if(cond):
            popped = ol.pop(index)
        else:
            popped = ol
        return(popped)


#
def pop_range(ol,start_index,end_index,**kwargs):
    '''
        from elist.jprint import pobj
        from elist.elist import *
        ol = [1,2,3,4,5,6]
        id(ol)
        rslt = pop_range(ol,2,4)
        ol
        id(ol)
        id(rslt['list'])
        ####
        ol = [1,2,3,4,5,6]
        id(ol)
        rslt = pop_range(ol,2,4,mode="original")
        rslt
        ol
        id(ol)
    '''
    length = ol.__len__()
    start_index = uniform_index(start_index,length)
    end_index = uniform_index(end_index,length)
    if('mode' in kwargs):
        mode = kwargs["mode"]
    else:
        mode = "new"
    if(mode == "new"):
        cpol = copy.deepcopy(ol)
        new = []
        popped = []
        for i in range(0,start_index):
            new.append(cpol[i])
        for i in range(start_index,end_index):
            popped.append(cpol[i])
        for i in range(end_index,length):
            new.append(cpol[i])
        return({'popped':popped,'list':new})
    else:
        tmp = []
        popped = []
        for i in range(0,start_index):
            tmp.append(ol[i])
        for i in range(start_index,end_index):
            popped.append(ol[i])
        for i in range(end_index,length):
            tmp.append(ol[i])
        ol.clear()
        for i in range(0,tmp.__len__()):
            ol.append(tmp[i])
        return(popped)

def pop_some(ol,*indexes,**kwargs):
    '''
        from elist.jprint import pobj
        from elist.elist import *
        ol = [1,2,3,4,5,6]
        id(ol)
        rslt = pop_some(ol,0,2,5)
        ol
        id(ol)
        id(rslt['list'])
        ####
        ol = [1,2,3,4,5,6]
        id(ol)
        rslt = pop_some(ol,0,2,5,mode="original")
        rslt
        ol
        id(ol)
    '''
    length = ol.__len__()
    indexes = list(map(lambda index:uniform_index(index,length),list(indexes)))
    if('mode' in kwargs):
        mode = kwargs["mode"]
    else:
        mode = "new"
    if(mode == "new"):
        cpol = copy.deepcopy(ol)
        new = []
        popped = []
        for i in range(0,length):
            if(i in indexes):
                popped.append(cpol[i])
            else:
                new.append(cpol[i])
        return({'popped':popped,'list':new})
    else:
        tmp = []
        popped = []
        for i in range(0,length):
            if(i in indexes):
                popped.append(ol[i])
            else:
                tmp.append(ol[i])
        ol.clear()
        for i in range(0,tmp.__len__()):
            ol.append(tmp[i])
        return(popped)

def pop_indexes(ol,indexes,**kwargs):
    '''
        from elist.jprint import pobj
        from elist.elist import *
        ol = [1,2,3,4,5,6]
        id(ol)
        rslt = pop_indexes(ol,{0,-3,5})
        ol
        id(ol)
        id(rslt['list'])
        ####
        ol = [1,2,3,4,5,6]
        id(ol)
        rslt = pop_indexes(ol,{0,-3,5},mode="original")
        rslt
        ol
        id(ol)
    '''
    length = ol.__len__()
    indexes = list(map(lambda index:uniform_index(index,length),list(indexes)))
    if('mode' in kwargs):
        mode = kwargs["mode"]
    else:
        mode = "new"
    if(mode == "new"):
        cpol = copy.deepcopy(ol)
        new = []
        popped = []
        for i in range(0,length):
            if(i in indexes):
                popped.append(cpol[i])
            else:
                new.append(cpol[i])
        return({'popped':popped,'list':new})
    else:
        tmp = []
        popped = []
        for i in range(0,length):
            if(i in indexes):
                popped.append(ol[i])
            else:
                tmp.append(ol[i])
        ol.clear()
        for i in range(0,tmp.__len__()):
            ol.append(tmp[i])
        return(popped)


####
def another_pop_seqs(l,seqs):
    seqs = sorted(seqs)
    count = 0
    for i in range(0,seqs.__len__()):
        seq = seqs[i]
        seq = seq -count
        l.pop(seq)
        count = count + 1
    return(l)
####


def remove_first(ol,value,**kwargs):
    '''
        from elist.jprint import pobj
        from elist.elist import *
        ol = [1,'a',3,'a',5,'a']
        id(ol)
        new = remove_first(ol,'a')
        ol
        new
        id(ol)
        id(new)
        ####
        ol = [1,'a',3,'a',5,'a']
        id(ol)
        rslt = remove_first(ol,'a',mode="original")
        ol
        rslt
        id(ol)
        id(rslt)
        ####array_remove is the same as remove_first
    '''
    if('mode' in kwargs):
        mode = kwargs["mode"]
    else:
        mode = "new"
    if(mode == "new"):
        new = copy.deepcopy(ol)
        new.remove(value)
        return(new)
    else:
        ol.remove(value)
        return(ol)

array_remove = remove_first

def remove_firstnot(ol,value,**kwargs):
    '''
        from elist.jprint import pobj
        from elist.elist import *
        ol = [1,'a',3,'a',5,'a']
        id(ol)
        new = remove_firstnot(ol,'a')
        ol
        new
        id(ol)
        id(new)
        ####
        ol = [1,'a',3,'a',5,'a']
        id(ol)
        rslt = remove_firstnot(ol,'a',mode="original")
        ol
        rslt
        id(ol)
        id(rslt)
        ####array_removenot is the same as remove_firstnot
    '''
    if('mode' in kwargs):
        mode = kwargs["mode"]
    else:
        mode = "new"
    length = ol.__len__()
    if(mode == "new"):
        new = copy.deepcopy(ol)
        for i in range(0,length):
            if(new[i] == value):
                pass
            else:
                new.pop(i)
                return(new)
        return(new)
    else:
        for i in range(0,length):
            if(ol[i] == value):
                pass
            else:
                ol.pop(i)
                return(ol)
        return(ol)

array_removenot = remove_firstnot

def remove_last(ol,value,**kwargs):
    '''
        from elist.elist import *
        ol = [1,'a',3,'a',5,'a']
        id(ol)
        new = remove_last(ol,'a')
        ol
        new
        id(ol)
        id(new)
        ####
        ol = [1,'a',3,'a',5,'a']
        id(ol)
        rslt = remove_last(ol,'a',mode="original")
        ol
        rslt
        id(ol)
        id(rslt)
    '''
    if('mode' in kwargs):
        mode = kwargs["mode"]
    else:
        mode = "new"
    new = copy.deepcopy(ol)
    new.reverse()
    new.remove(value)
    new.reverse()
    if(mode == "new"):
        return(new)
    else:
        ol.clear()
        ol.extend(new)
        return(ol)

def remove_lastnot(ol,value,**kwargs):
    '''
        from elist.jprint import pobj
        from elist.elist import *
        ol = [1,'a',3,'a',5,'a']
        id(ol)
        new = remove_lastnot(ol,'a')
        ol
        new
        id(ol)
        id(new)
        ####
        ol = [1,'a',3,'a',5,'a']
        id(ol)
        rslt = remove_lastnot(ol,'a',mode="original")
        ol
        rslt
        id(ol)
        id(rslt)
    '''
    if('mode' in kwargs):
        mode = kwargs["mode"]
    else:
        mode = "new"
    length = ol.__len__()
    if(mode == "new"):
        new = copy.deepcopy(ol)
        for i in range(length-1,-1,-1):
            if(new[i] == value):
                pass
            else:
                new.pop(i)
                return(new)
        return(new)
    else:
        for i in range(length-1,-1,-1):
            if(ol[i] == value):
                pass
            else:
                ol.pop(i)
                return(ol)
        return(ol)

def remove_which(ol,value,which,**kwargs):
    '''
        from elist.elist import *
        ol = [1,'a',3,'a',5,'a']
        id(ol)
        new = remove_which(ol,'a',1)
        ol
        new
        id(ol)
        id(new)
        ####
        ol = [1,'a',3,'a',5,'a']
        id(ol)
        rslt = remove_which(ol,'a',1,mode="original")
        ol
        rslt
        id(ol)
        id(rslt)
    '''
    if('mode' in kwargs):
        mode = kwargs["mode"]
    else:
        mode = "new"
    new = copy.deepcopy(ol)
    length = ol.__len__()
    if(mode == "new"):
        l = new 
    else:
        l = ol
    seq = -1
    for i in range(0,length):
        if(ol[i]==value):
            seq = seq + 1
            if(seq == which):
                l.pop(i)
                break
            else:
                pass
        else:
            pass
    return(l)

def remove_whichnot(ol,value,which,**kwargs):
    '''
        from elist.elist import *
        ol = [1,'a',3,'a',5,'a']
        id(ol)
        new = remove_whichnot(ol,'a',1)
        ol
        new
        id(ol)
        id(new)
        ####
        ol = [1,'a',3,'a',5,'a']
        id(ol)
        rslt = remove_whichnot(ol,'a',1,mode="original")
        ol
        rslt
        id(ol)
        id(rslt)
    '''
    if('mode' in kwargs):
        mode = kwargs["mode"]
    else:
        mode = "new"
    new = copy.deepcopy(ol)
    length = ol.__len__()
    if(mode == "new"):
        l = new 
    else:
        l = ol
    seq = -1
    for i in range(0,length):
        if(not(ol[i]==value)):
            seq = seq + 1
            if(seq == which):
                l.pop(i)
                break
            else:
                pass
        else:
            pass
    return(l)

def remove_some(ol,value,*seqs,**kwargs):
    '''
        from elist.elist import *
        ol = [1,'a',3,'a',5,'a',6,'a']
        id(ol)
        new = remove_some(ol,'a',1,3)
        ol
        new
        id(ol)
        id(new)
        ####
        ol = [1,'a',3,'a',5,'a',6,'a']
        id(ol)
        rslt = remove_some(ol,'a',1,3,mode="original")
        ol
        rslt
        id(ol)
        id(rslt)
    '''
    if('mode' in kwargs):
        mode = kwargs["mode"]
    else:
        mode = "new"
    seqs = list(seqs)
    new = []
    length = ol.__len__()
    seq = -1
    cpol = copy.deepcopy(ol)
    for i in range(0,length):
        if(cpol[i]==value):
            seq = seq + 1
            if(seq in seqs):
                pass
            else:
                new.append(cpol[i])
        else:
            new.append(cpol[i])
    if(mode == "new"):
        return(new) 
    else:
        ol.clear()
        ol.extend(new)
        return(ol)

def remove_somenot(ol,value,*seqs,**kwargs):
    '''
        from elist.elist import *
        ol = [1,'a',3,'a',5,'a',6,'a']
        id(ol)
        new = remove_somenot(ol,'a',1,3)
        ol
        new
        id(ol)
        id(new)
        ####
        ol = [1,'a',3,'a',5,'a',6,'a']
        id(ol)
        rslt = remove_somenot(ol,'a',1,3,mode="original")
        ol
        rslt
        id(ol)
        id(rslt)
    '''
    if('mode' in kwargs):
        mode = kwargs["mode"]
    else:
        mode = "new"
    seqs = list(seqs)
    new = []
    length = ol.__len__()
    seq = -1
    cpol = copy.deepcopy(ol)
    for i in range(0,length):
        if(not(cpol[i]==value)):
            seq = seq + 1
            if(seq in seqs):
                pass
            else:
                new.append(cpol[i])
        else:
            new.append(cpol[i])
    if(mode == "new"):
        return(new) 
    else:
        ol.clear()
        ol.extend(new)
        return(ol)

def remove_seqs(ol,value,seqs,**kwargs):
    '''
        from elist.elist import *
        ol = [1,'a',3,'a',5,'a',6,'a']
        id(ol)
        new = remove_seqs(ol,'a',{1,3})
        ol
        new
        id(ol)
        id(new)
        ####
        ol = [1,'a',3,'a',5,'a',6,'a']
        id(ol)
        rslt = remove_seqs(ol,'a',{1,3},mode="original")
        ol
        rslt
        id(ol)
        id(rslt)
    '''
    if('mode' in kwargs):
        mode = kwargs["mode"]
    else:
        mode = "new"
    seqs = list(seqs)
    new = []
    length = ol.__len__()
    cpol = copy.deepcopy(ol)
    seq = -1
    for i in range(0,length):
        if(cpol[i]==value):
            seq = seq + 1
            if(seq in seqs):
                pass
            else:
                new.append(cpol[i])
        else:
            new.append(cpol[i])
    if(mode == "new"):
        return(new) 
    else:
        ol.clear()
        ol.extend(new)
        return(ol)

def remove_seqsnot(ol,value,seqs,**kwargs):
    '''
        from elist.elist import *
        ol = [1,'a',3,'a',5,'a',6,'a']
        id(ol)
        new = remove_seqsnot(ol,'a',{1,3})
        ol
        new
        id(ol)
        id(new)
        ####
        ol = [1,'a',3,'a',5,'a',6,'a']
        id(ol)
        rslt = remove_seqsnot(ol,'a',{1,3},mode="original")
        ol
        rslt
        id(ol)
        id(rslt)
    '''
    if('mode' in kwargs):
        mode = kwargs["mode"]
    else:
        mode = "new"
    seqs = list(seqs)
    new = []
    length = ol.__len__()
    cpol = copy.deepcopy(ol)
    seq = -1
    for i in range(0,length):
        if(not(cpol[i]==value)):
            seq = seq + 1
            if(seq in seqs):
                pass
            else:
                new.append(cpol[i])
        else:
            new.append(cpol[i])
    if(mode == "new"):
        return(new) 
    else:
        ol.clear()
        ol.extend(new)
        return(ol)

def remove_all(ol,value,**kwargs):
    '''
        from elist.elist import *
        ol = [1,'a',3,'a',5,'a',6,'a']
        id(ol)
        new = remove_all(ol,'a')
        ol
        new
        id(ol)
        id(new)
        ####
        ol = [1,'a',3,'a',5,'a',6,'a']
        id(ol)
        rslt = remove_all(ol,'a',mode="original")
        ol
        rslt
        id(ol)
        id(rslt)
    '''
    if('mode' in kwargs):
        mode = kwargs["mode"]
    else:
        mode = "new"
    new = []
    length = ol.__len__()
    cpol = copy.deepcopy(ol)
    for i in range(0,length):
        if(cpol[i]==value):
            pass
        else:
            new.append(cpol[i])
    if(mode == "new"):
        return(new) 
    else:
        ol.clear()
        ol.extend(new)
        return(ol)

def remove_allnot(ol,value,**kwargs):
    '''
        from elist.elist import *
        ol = [1,'a',3,'a',5,'a',6,'a']
        id(ol)
        new = remove_allnot(ol,'a')
        ol
        new
        id(ol)
        id(new)
        ####
        ol = [1,'a',3,'a',5,'a',6,'a']
        id(ol)
        rslt = remove_allnot(ol,'a',mode="original")
        ol
        rslt
        id(ol)
        id(rslt)
    '''
    if('mode' in kwargs):
        mode = kwargs["mode"]
    else:
        mode = "new"
    new = []
    length = ol.__len__()
    cpol = copy.deepcopy(ol)
    for i in range(0,length):
        if(cpol[i]==value):
            new.append(cpol[i])
        else:
            pass
    if(mode == "new"):
        return(new) 
    else:
        ol.clear()
        ol.extend(new)
        return(ol)

def remove_many(ol,values,seqs,**kwargs):
    '''
        from elist.elist import *
        ol = [1,'a',3,'b',5,'a',6,'a',7,'b',8,'b',9]
        id(ol)
        new = remove_many(ol,['a','b'],[1,2])
        ol
        new
        id(ol)
        id(new)
        ####
        ol = [1,'a',3,'b',5,'a',6,'a',7,'b',8,'b',9]
        id(ol)
        rslt = remove_many(ol,['a','b'],[1,2],mode="original")
        ol
        rslt
        id(ol)
        id(rslt)
    '''
    if('mode' in kwargs):
        mode = kwargs["mode"]
    else:
        mode = "new"
    values = copy.deepcopy(values)
    seqs = copy.deepcopy(seqs)
    cursors = [-1] * values.__len__()
    new = []
    length = ol.__len__()
    cpol = copy.deepcopy(ol)
    for i in range(0,length):
        label = True
        for j in range(0,cursors.__len__()):
            which = seqs[j]
            value = values[j]
            if(cpol[i] == value):
                cursors[j] = cursors[j] + 1
                if(cursors[j] == which):
                    label = False
                    break
                else:
                    pass
            else:
                pass
        if(label):
            new.append(cpol[i])
        else:
            pass
    if(mode == "new"):
        return(new) 
    else:
        ol.clear()
        ol.extend(new)
        return(ol)

def remove_manynot(ol,values,seqs,**kwargs):
    '''
        from elist.elist import *
        ol = [1,'a',3,'b',5,'a',6,'a',7,'b',8,'b',9]
        id(ol)
        new = remove_manynot(ol,['a','b'],[1,2])
        ol
        new
        id(ol)
        id(new)
        ####
        ol = [1,'a',3,'b',5,'a',6,'a',7,'b',8,'b',9]
        id(ol)
        rslt = remove_manynot(ol,['a','b'],[1,2],mode="original")
        ol
        rslt
        id(ol)
        id(rslt)
    '''
    if('mode' in kwargs):
        mode = kwargs["mode"]
    else:
        mode = "new"
    values = copy.deepcopy(values)
    seqs = copy.deepcopy(seqs)
    cursors = [-1] * values.__len__()
    new = []
    length = ol.__len__()
    cpol = copy.deepcopy(ol)
    for i in range(0,length):
        label = True
        for j in range(0,cursors.__len__()):
            which = seqs[j]
            value = values[j]
            if(not(cpol[i] == value)):
                cursors[j] = cursors[j] + 1
                if(cursors[j] == which):
                    label = False
                    break
                else:
                    pass
            else:
                pass
        if(label):
            new.append(cpol[i])
        else:
            pass
    if(mode == "new"):
        return(new) 
    else:
        ol.clear()
        ol.extend(new)
        return(ol)

#remove_swarm(ol,values,seqs_matrix=[[value1_seqs],[value2_seqs],[value3_seqs]....[valuen_seqs]],**kwargs)
#remove_swarmnot

def cond_remove_all(ol,**kwargs):
    '''
        from elist.elist import *
        ol = [1,'X',3,'b',5,'c',6,'A',7,'b',8,'B',9]
        id(ol)
        def afterCH(ele,ch):
            cond = (ord(str(ele)) > ord(ch))
            return(cond)

        new = cond_remove_all(ol,cond_func=afterCH,cond_func_args=['B'])
        ol
        new
        id(ol)
        id(new)
        ####
        ol = [1,'X',3,'b',5,'c',6,'A',7,'b',8,'B',9]
        id(ol)
        rslt = cond_remove_all(ol,cond_func=afterCH,cond_func_args=['B'],mode='original')
        ol
        rslt
        id(ol)
        id(rslt)

    '''
    cond_func = kwargs['cond_func']
    if('cond_func_args' in kwargs):
        cond_func_args = kwargs['cond_func_args']
    else:
        cond_func_args = []
    if('mode' in kwargs):
        mode = kwargs["mode"]
    else:
        mode = "new"
    new = copy.deepcopy(ol)
    selected = find_all(new,cond_func,*cond_func_args)
    selected_indexes = array_map(selected,lambda ele:ele['index'])
    new = pop_indexes(new,selected_indexes)['list']
    if(mode == "new"):
        return(new)
    else:
        ol.clear()
        ol.extend(new)
        return(ol)


def cond_remove_seqs(ol,seqs,**kwargs):
    '''
        from elist.elist import *
        ol = [1,'X',3,'b',5,'c',6,'A',7,'b',8,'B',9]
        id(ol)
        def afterCH(ele,ch):
            cond = (ord(str(ele)) > ord(ch))
            return(cond)

        new = cond_remove_seqs(ol,[0,2],cond_func=afterCH,cond_func_args=['B'])
        ol
        new
        id(ol)
        id(new)
        ####
        ol = [1,'X',3,'b',5,'c',6,'A',7,'b',8,'B',9]
        id(ol)
        rslt = cond_remove_seqs(ol,[0,2],cond_func=afterCH,cond_func_args=['B'],mode='original')
        ol
        rslt
        id(ol)
        id(rslt)

    '''
    cond_func = kwargs['cond_func']
    if('cond_func_args' in kwargs):
        cond_func_args = kwargs['cond_func_args']
    else:
        cond_func_args = []
    if('mode' in kwargs):
        mode = kwargs["mode"]
    else:
        mode = "new"
    new = copy.deepcopy(ol)
    selected = find_all(new,cond_func,*cond_func_args)
    selected_indexes = array_map(selected,lambda ele:ele['index'])
    selected_indexes = pop_indexes(selected_indexes,seqs)['popped']
    new = pop_indexes(new,selected_indexes)['list']
    if(mode == "new"):
        return(new)
    else:
        ol.clear()
        ol.extend(new)
        return(ol)

def cond_remove_some(ol,*some,**kwargs):
    '''
        from elist.elist import *
        ol = [1,'X',3,'b',5,'c',6,'A',7,'b',8,'B',9]
        id(ol)
        
        def afterCH(ele,ch):
            cond = (ord(str(ele)) > ord(ch))
            return(cond)
        
        new = cond_remove_some(ol,0,2,cond_func=afterCH,cond_func_args=['B'])
        ol
        new
        id(ol)
        id(new)
        ####
        ol = [1,'X',3,'b',5,'c',6,'A',7,'b',8,'B',9]
        id(ol)
        rslt = cond_remove_some(ol,0,2,cond_func=afterCH,cond_func_args=['B'],mode='original')
        ol
        rslt
        id(ol)
        id(rslt)
    '''
    cond_func = kwargs['cond_func']
    if('cond_func_args' in kwargs):
        cond_func_args = kwargs['cond_func_args']
    else:
        cond_func_args = []
    if('mode' in kwargs):
        mode = kwargs["mode"]
    else:
        mode = "new"
    seqs = list(some)
    rslt = cond_remove_seqs(ol,seqs,cond_func=cond_func,cond_func_args=cond_func_args)
    return(rslt)




#cond_remove
#cond_remove_first
#cond_remove_last
#cond_remove_which
#cond_remove_many
#cond_remove_swarm



def copy_within(ol,target, start=None, end=None):
    '''
        from elist.elist import *
        ol = [1, 2, 3, 4, 5]
        id(ol)
        rslt = copyWithin(ol,0,3,4)
        rslt
        id(rslt)
        ####
        ol = [1, 2, 3, 4, 5]
        id(ol)
        rslt = copyWithin(ol,0,3)
        rslt
        id(rslt)
        ####
        ol = [1, 2, 3, 4, 5]
        id(ol)
        rslt = copyWithin(ol,-2)
        rslt
        id(rslt)
        ####copyWithin is the same as copy_within
    '''
    length = ol.__len__()
    if(start==None):
        start = 0
    else:
        pass
    if(end==None):
        end = length
    else:
        pass
    target = uniform_index(target,length)
    start = uniform_index(start,length)
    end = uniform_index(end,length)
    cplen = end - start
    cpend = target+cplen
    if(target+cplen > length):
        cpend = length
    else:
        pass
    shift = start - target
    if(shift>=0):
        for i in range(target,cpend):
            ol[i] = ol[i+shift]
    else:
        for i in range(cpend-1,target-1,-1):
            ol[i] = ol[i+shift]
    return(ol)

copyWithin = copy_within

def reverse(ol,**kwargs):
    '''
        from elist.elist import *
        ol = [1,2,3,4]
        id(ol)
        new = reverse(ol)
        ol
        new
        id(ol)
        id(new)
        ####
        ol = [1,2,3,4]
        id(ol)
        rslt = reverse(ol,mode="original")
        ol
        rslt
        id(ol)
        id(rslt)
    '''
    if('mode' in kwargs):
        mode = kwargs["mode"]
    else:
        mode = "new"
    if(mode == "new"):
        new = copy.deepcopy(ol)
        new.reverse()
        return(new) 
    else:
        ol.reverse()
        return(ol)


    'reverse',
    'sort'

def comprise(list1,list2,**kwargs):
    '''
        from elist.elist import *
        comprise([1,2,3,4,5],[2,3,4],mode="loose")
        comprise([1,2,3,4,5],[2,3,4])
        comprise([1,2,3,4,5],[2,3,4],mode="strict")
        comprise([1,2,3,4,5],[1,2,3,4],mode="strict")
        #not recursive ,only one level
        #please refer to ListTree.search for recursive support
    '''
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

def entries(ol):
    '''
        from elist.elist import *
        ol = ['a','b','c']
        rslt = entries(ol)
        rslt
    '''
    rslt = []
    length = ol.__len__()
    for i in range(0,length):
        entry = [i,ol[i]]
        rslt.append(entry)
    return(rslt)

def includes(ol,value):
    '''
        from elist.elist import *
        ol = [1,2,3,4]
        includes(ol,3)
        includes(ol,5)
    '''
    return((value in ol))

def toString(ol):
    '''
        from elist.elist import *
        ol = [1,2,3,4]
        toString(ol)
    '''
    return(ol.__str__())

def toSource(ol):
    '''
        from elist.elist import *
        ol = [1,2,3,4]
        toSource(ol)
    '''
    return(ol.__repr__())

def splice(ol,start,deleteCount,*eles,**kwargs):
    '''
        from elist.elist import *
        ol = ["angel", "clown", "mandarin", "surgeon"]
        id(ol)
        new = splice(ol,2,0,"drum")
        new
        id(new)
        ####
        ol = ["angel", "clown", "mandarin", "surgeon"]
        id(ol)
        new = splice(ol,2,1,"drum",mode="original")
        new
        id(new)
        ####
        ol = [1,2,3,4,5,6]
        id(ol)
        new = splice(ol,2,2,77,777)
        new
        id(new)
    '''
    if('mode' in kwargs):
        mode = kwargs['mode']
    else:
        mode = "new"
    length = ol.__len__()
    new = copy.deepcopy(ol)
    if(start >= length):
        eles = list(eles)
        new.extend(eles)
    else:
        start = uniform_index(start,length)
        end = start + deleteCount
        tmp = pop_range(new,start,end,mode="new")['list']
        new = insert_some(tmp,*eles,index=start,mode="new")
    if(mode == "new"):
        return(new)
    else:
        ol.clear()
        ol.extend(new)
        return(ol)

def slice(ol,start,end=None,**kwargs):
    '''
        from elist.elist import *
        ol = [1,2,3,4,5]
        id(ol)
        new = slice(ol,2,4)
        new
        id(new)
        ####
        id(ol)
        rslt = slice(ol,1,-2,mode="original")
        rslt
        id(rslt)
    '''
    if('mode' in kwargs):
        mode = kwargs['mode']
    else:
        mode = "new"
    length = ol.__len__()
    new = copy.deepcopy(ol)
    if(end == None):
        end = length
    else:
        end = uniform_index(end,length)
    start = uniform_index(start,length)
    if(mode == "new"):
        return(new[start:end])
    else:
        ol.clear()
        ol.extend(new[start:end])
        return(ol)

def join(ol,separator=","):
    '''
        from elist.elist import *
        ol = [1,2,3,4]
        join(ol,separator="-")
    '''
    if(ol.__len__() == 0):
        return("")
    else:
        pass
    cond = (type(ol[0])==type(b''))
    if(cond):
        rslt = b''
    else:
        rslt =""
    length = ol.__len__()
    for i in range(0,length-1):
        ele = ol[i]
        if(cond):
            pass
        else:
            ele = str(ele)
        rslt = rslt + ele + separator
    if(cond):
        rslt = rslt + ol[length - 1]
    else:
        rslt = rslt + str(ol[length - 1])
    return(rslt)

def join2(ol,*sps):
    '''
        from elist.elist import *
        ol = [1,2,3,4]
        join2(ol,"-","+","*")
    '''
    rslt =""
    length = ol.__len__()
    for i in range(0,length-1):
        rslt = rslt + str(ol[i]) + sps[i]
    rslt = rslt + str(ol[length - 1])
    return(rslt)

def htmljoin(ol,sp,**kwargs):
    '''
        ol = [1,2,3,4]
        htmljoin(ol,"option",outer="select")
        
    '''
    if('outer' in kwargs):
        outer = kwargs['outer']
    else:
        outer = ""
    if(outer):
        head = "<" + outer + ">"
        tail = "</" + outer + ">"
    else:
        head = ""
        tail = ""
    rslt = head
    length = ol.__len__()
    begin = "<" + sp + ">"
    end = "</" + sp + ">"
    for i in range(0,length):
        rslt = rslt + begin + str(ol[i]) + end
    rslt = rslt + tail
    return(rslt)

def uniqualize(l,**kwargs):
    '''
        from elist.elist import *
        l = [1, 2, 2]
        new = uniqualize(l)
        new
        id(l)
        id(new)
        ####
        l = [1, 2, 2]
        rslt = uniqualize(l,mode="original")
        rslt
        id(l)
        id(rslt)
    '''
    if('mode' in kwargs):
        mode = kwargs['mode']
    else:
        mode = 'new'
    pt = copy.deepcopy(l)
    seqs =[]
    freq = {}
    for i in range(0,pt.__len__()):
        v = pt[i]
        if(v in freq):
            freq[v] = freq[v] + 1
        else:
            freq[v] = 0
            seqs.append(i)
    #####下面是影响速度的关键,append特别耗时
    npt = select_seqs(pt,seqs)
    ########################
    pt = npt
    if(mode == 'new'):
        return(npt)
    else:
        l.clear()
        l.extend(npt)
        return(l)

#uniqulize_many

def cond_uniqualize(l,**kwargs):
    '''
        from elist.elist import *
        l = [('BIGipServer', 'rd100'), ('TS013d8ed5', '00A0'), ('BIGipServer', 'rd200'), ('TS013d8ed5', '00B0'), ('SID', '1'), ('SID', '2')]
        
        def cond_func(ele,*args):
            cond = ele[0]
            return(cond)
        
        uniqualized = cond_uniqualize(l,cond_func=cond_func)
        pobj(uniqualized)
        
        l = [('BIGipServer', 'rd100'), ('TS013d8ed5', '00A0'), ('BIGipServer', 'rd200'), ('TS013d8ed5', '00B0'), ('SID', '1'), ('SID', '2')]
        
        reserved_mapping = {'BIGipServer':0,'TS013d8ed5':1,'SID':1}
        uniqualized = cond_uniqualize(l,cond_func=cond_func,reserved_mapping=reserved_mapping)
        pobj(uniqualized)
        
    '''
    cond_func = kwargs['cond_func']
    if('cond_func_args' in kwargs):
        cond_func_args = kwargs['cond_func_args']
    else:
        cond_func_args = []
    if('reserved_mapping' in kwargs):
        reserved_mapping = kwargs['reserved_mapping']
    else:
        reserved_mapping = None
    if('mode' in kwargs):
        mode = kwargs['mode']
    else:
        mode = 'new'
    desc = cond_value_indexes_mapping(l,cond_func=cond_func,cond_func_args=cond_func_args,with_none=True)
    keys = list(desc.keys())
    if(None in keys):
        keys.remove(None)
    else:
        pass
    rmapping = {}
    for key in keys:
        rmapping[key] = 0
    if(reserved_mapping == None):
        pass
    else:
        for key in reserved_mapping:
            rmapping[key] = reserved_mapping[key]
    reserved_indexes = []
    for key in keys:
        indexes = desc[key]
        index = indexes[rmapping[key]]
        reserved_indexes.append(index)
    newcopy = copy.deepcopy(l)
    new = select_seqs(newcopy,reserved_indexes)
    ####
    if(None in desc):
        for index in desc[None]:
            new.append(newcopy[index])
    else:
        pass
    ####
    if(mode == "new"):
        return(new)
    else:
        ol.clear()
        ol.extend(new)
        return(ol)

     





def interleave(*arrays,**kwargs):
    '''
        arr1 = [1,2,3,4]
        arr2 = ['a','b','c','d']
        arr3 = ['@','#','%','*']
        interleave(arr1,arr2,arr3)
    '''
    anum = arrays.__len__()
    rslt = []
    length = arrays[0].__len__()
    for j in range(0,length):
        for i in range(0,anum):
            array = arrays[i]
            rslt.append(array[j])
    return(rslt)


def deinterleave(ol,gnum):
    '''
        ol = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        deinterleave(ol,3)
        
    '''
    def test_func(ele,index,interval,which):
        cond= (index % interval == which)
        return(cond)
    rslt = []
    for i in range(0,gnum):
        arr = cond_select_all2(ol,cond_func = test_func,cond_func_args = [gnum,i])
        rslt.append(arr)
    return(rslt)


#@@@@@@@@@@@@@@@@@@


def every(ol,test_func,*args):
    '''
        from elist.elist import *
        def test_func(ele,x):
            cond = (ele > x)
            return(cond)
        
        ol = [1,2,3,4]
        every(ol,test_func,3)
        
        ol = [10,20,30,40]
        every(ol,test_func,3)
        
    '''
    rslt = (True,None)
    length = ol.__len__()
    for i in range(0,length):
        cond = test_func(ol[i],*args)
        if(cond):
            pass
        else:
            return((False,i))
    return(rslt)


def every2(ol,test_func,*args):
    '''
        from elist.elist import *
        def test_func(ele,index,x):
            cond1 = (ele > x)
            cond2 = (index %2 ==0)
            cond = cond1 & cond2
            return(cond)

        ol = [1,2,3,4]
        every2(ol,test_func,3)

        ol = [10,20,30,40]
        every2(ol,test_func,3)

    '''
    rslt = (True,None)
    length = ol.__len__()
    for i in range(0,length):
        cond = test_func(ol[i],i,*args)
        if(cond):
            pass
        else:
            return((False,i))
    return(rslt)


###
def loose_in(pl,k):
    '''
        pl = ['bcd','xabcxx','x','y']
        loose_in(pl,'abc')
        
    '''
    cond = some(pl,lambda ele:(k in ele))['cond']
    return(cond)


def select_loose_in(pl,k):
    '''
        pl = ['bcd','xabcxx','x','y']
        select_loose_in(pl,'abc')
    '''
    def cond_func(ele,index,k):
        if(type(ele) == type([])):
            cond = loose_in(ele,k)
        else:
            cond = (k in ele)
        return(cond)
    arr = cond_select_values_all2(pl,cond_func=cond_func, cond_func_args =[k])
    return(arr)


def select_strict_in(pl,k):
    '''
        pl = ['bcd','xabcxx','x','y']
        select_strict_in(pl,'abc')
    '''
    def cond_func(ele,index,k):
        if(type(ele) == type([])):
            cond = (k in ele)
        else:
            cond = (k == ele)
        return(cond)
    arr = cond_select_values_all2(pl,cond_func=cond_func, cond_func_args =[k])
    return(arr)



def regex_in(pl,regex):
    '''
        regex = re.compile("^[a-z]+$")
        pl = ['b1c3d','xab15cxx','1x','y2']
        regex_in(pl,regex)
        
        regex = re.compile("^[0-9a-z]+$")
        pl = ['b1c3d','xab15cxx','1x','y2']
        regex_in(pl,regex)
        
    '''
    def cond_func(ele,regex):
        m = regex.search(ele)
        if(m == None):
            return(False)
        else:
            return(True)
    cond = some(pl,cond_func,regex)['cond']
    return(cond)


def select_regex_in(pl,regex):
    '''
        regex = re.compile("^x.*x$")
        pl = ['bcd','xabcxx','xx','y']
        select_regex_in(pl,'abc')
    '''
    def cond_func(ele,index,regex):
        if(type(ele)==type([])):
            cond = regex_in(ele,regex)
        else:
            m = regex.search(ele)
            if(m == None):
                cond = False
            else:
                cond = True
        return(cond)
    arr = cond_select_values_all2(pl,cond_func=cond_func, cond_func_args =[regex])
    return(arr)




###





def some(ol,test_func,*args):
    '''
        from elist.elist import *
        def test_func(ele,x):
            cond = (ele > x)
            return(cond)
        
        ol = [1,2,3,4]
        some(ol,test_func,3)
        
        ol = [1,2,1,3]
        some(ol,test_func,3)
    '''
    rslt = {'cond':False,'index':None}
    length = ol.__len__()
    for i in range(0,length):
        cond = test_func(ol[i],*args)
        if(cond):
            return({'cond':True,'index':i})
        else:
            pass
    return(rslt)




def reduce_left(ol,callback,initialValue):
    '''
        from elist.elist import *
        def callback(accumulator,currentValue):
            accumulator.append(currentValue[0])
            accumulator.append(currentValue[1])
            return(accumulator)
        
        ol = [(1,2),("a","b"),("x","y")]
        reduce_left(ol,callback,[])
        #array_reduce, reduceLeft ,reduce_left  are the same
    '''
    length = ol.__len__()
    accumulator = initialValue
    for i in range(0,length):
        accumulator = callback(accumulator,ol[i])
    return(accumulator)

array_reduce = reduce_left
reduceLeft = reduce_left

def reduce_right(ol,callback,initialValue):
    '''
        from elist.elist import *
        def callback(accumulator,currentValue):
            accumulator.append(currentValue[0])
            accumulator.append(currentValue[1])
            return(accumulator)
        
        ol = [(1,2),("a","b"),("x","y")]
        reduce_right(ol,callback,[])
        #reduceRight,reduce_right are the same 
    '''
    length = ol.__len__()
    accumulator = initialValue
    for i in range(length-1,-1,-1):
        accumulator = callback(accumulator,ol[i])
    return(accumulator)

reduceRight = reduce_right

#

def cond_value_indexes_mapping(l,**kwargs):
    '''
        from elist.elist import *
        l = [('BIGipServer', 'rd19'), ('TS013d8ed5', '0105b6b0'), ('BIGipServer', 'rd19'), ('TS013d8ed5', '0105b6b0'), ('SID', '1'), ('SID', '2')]

        def cond_func(ele,*args):
            cond = ele[0]
            return(cond)

        desc = cond_value_indexes_mapping(l,cond_func=cond_func)
        pobj(desc)

    '''
    cond_func = kwargs['cond_func']
    if('cond_func_args' in kwargs):
        cond_func_args = kwargs['cond_func_args']
    else:
        cond_func_args = []
    if('with_none' in kwargs):
        with_none = kwargs['with_none']
    else:
        with_none = False
    desc = {}
    for i in range(0,l.__len__()):
        ele = l[i]
        cond = cond_func(ele,*cond_func_args)
        if((cond == None)&(not(with_none))):
            pass
        else:
            if(cond in desc):
                desc[cond].append(i)
            else:
                desc[cond] = [i]
    return(desc)




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



def cond_value_indexes_mapping(l,**kwargs):
    '''
        from elist.elist import *
        l = [('BIGipServer', 'rd19'), ('TS013d8ed5', '0105b6b0'), ('BIGipServer', 'rd19'), ('TS013d8ed5', '0105b6b0'), ('SID', '1'), ('SID', '2')]
        
        def cond_func(ele,*args):
            cond = ele[0]
            return(cond)
        
        desc = cond_value_indexes_mapping(l,cond_func=cond_func)
        pobj(desc)
    
    '''
    cond_func = kwargs['cond_func']
    if('cond_func_args' in kwargs):
        cond_func_args = kwargs['cond_func_args']
    else:
        cond_func_args = []
    if('with_none' in kwargs):
        with_none = kwargs['with_none']
    else:
        with_none = False
    desc = {}
    for i in range(0,l.__len__()):
        ele = l[i]
        cond = cond_func(ele,*cond_func_args)
        if((cond == None)&(not(with_none))):
            pass
        else:
            if(cond in desc):
                desc[cond].append(i)
            else:
                desc[cond] = [i]
    return(desc)




def getitem_via_pathlist(ol,pathlist):
    '''
        from elist.elist import *
        y = ['a',['b',["bb"]],'c']
        y[1][1]
        getitem_via_pathlist(y,[1,1])
    '''
    this = ol
    for i in range(0,pathlist.__len__()):
        key = pathlist[i]
        this = this.__getitem__(key)
    return(this)

def getitem_via_pathlist2(pathlist,ol):
    '''
        from elist.elist import *
        y = ['a',['b',["bb"]],'c']
        y[1][1]
        getitem_via_pathlist2([1,1],y)
    '''
    this = ol
    for i in range(0,pathlist.__len__()):
        key = pathlist[i]
        this = this.__getitem__(key)
    return(this)

def getitem_via_sibseqs(ol,*sibseqs):
    '''
        from elist.elist import *
        y = ['a',['b',["bb"]],'c']
        y[1][1]
        getitem_via_sibseqs(y,1,1)
    '''
    pathlist = list(sibseqs)
    this = ol
    for i in range(0,pathlist.__len__()):
        key = pathlist[i]
        this = this.__getitem__(key)
    return(this)



#get_seqs
#get_some




def set_seqs(ol,indexes,values):
    for i in range(indexes.__len__()):
        ol[i] = values[i]
    return(ol)

def set_some(ol,*iv_tuples):
    iv_tuples = list(iv_tuples)
    for t in iv_tuples:
        ol[t[0]] = t[1]
    return(ol)




def setitem_via_pathlist(ol,value,pathlist):
    '''
        from elist.elist import *
        y = ['a',['b',["bb"]],'c']
        y[1][1]
        setitem_via_pathlist(y,"500",[1,1])
        y
    '''
    this = ol
    for i in range(0,pathlist.__len__()-1):
        key = pathlist[i]
        this = this.__getitem__(key)
    this.__setitem__(pathlist[-1],value)
    return(ol)

def setitem_via_sibseqs(ol,value,*sibseqs):
    '''
        from elist.elist import *
        y = ['a',['b',["bb"]],'c']
        y[1][1]
        setitem_via_sibseqs(y,"500",1,1)
        y
    '''
    this = ol
    pathlist = list(sibseqs)
    for i in range(0,pathlist.__len__()-1):
        key = pathlist[i]
        this = this.__getitem__(key)
    this.__setitem__(pathlist[-1],value)
    return(ol)

def delitem_via_pathlist(ol,pathlist):
    '''
        from elist.elist import *
        y = ['a',['b',["bb"]],'c']
        y[1][1]
        delitem_via_pathlist(y,[1,1])
        y
    '''
    this = ol
    for i in range(0,pathlist.__len__()-1):
        key = pathlist[i]
        this = this.__getitem__(key)
    this.__delitem__(pathlist[-1])
    return(ol)

def delitem_via_sibseqs(ol,*sibseqs):
    '''
        from elist.elist import *
        y = ['a',['b',["bb"]],'c']
        y[1][1]
        delitem_via_sibseqs(y,1,1)
        y
    '''
    pathlist = list(sibseqs)
    this = ol
    for i in range(0,pathlist.__len__()-1):
        key = pathlist[i]
        this = this.__getitem__(key)
    this.__delitem__(pathlist[-1])
    return(ol)

##

#replace
#replacenot
#replace_first
#replace_firstnot
#replace_last
#replace_lastnot
#replace_all
#replace_allnot

def replace_seqs(ol,value,indexes,**kwargs):
    '''
        from elist.elist import *
        ol = [1,'a',3,'a',5,'a',6,'a']
        id(ol)
        new = replace_seqs(ol,'AAA',[1,3,7])
        ol
        new
        id(ol)
        id(new)
        ####
        ol = [1,'a',3,'a',5,'a',6,'a']
        id(ol)
        rslt = replace_seqs(ol,'AAA',[1,3,7],mode="original")
        ol
        rslt
        id(ol)
        id(rslt)
        #replace_indexes = replace_seqs
    '''
    if('mode' in kwargs):
        mode = kwargs["mode"]
    else:
        mode = "new"
    indexes = list(indexes)
    new = []
    length = ol.__len__()
    cpol = copy.deepcopy(ol)
    for i in range(0,length):
        if(i in indexes):
            new.append(value)
        else:
            new.append(cpol[i])
    if(mode == "new"):
        return(new)
    else:
        ol.clear()
        ol.extend(new)
        return(ol)

replace_indexes = replace_seqs

def replace_some(ol,value,*indexes,**kwargs):
    '''
        from elist.elist import *
        ol = [1,'a',3,'a',5,'a',6,'a']
        id(ol)
        new = replace_some(ol,'AAA',1,3,7)
        ol
        new
        id(ol)
        id(new)
        ####
        ol = [1,'a',3,'a',5,'a',6,'a']
        id(ol)
        rslt = replace_some(ol,'AAA',1,3,7,mode="original")
        ol
        rslt
        id(ol)
        id(rslt)
    '''
    if('mode' in kwargs):
        mode = kwargs["mode"]
    else:
        mode = "new"
    indexes = list(indexes)
    return(replace_seqs(ol,value,indexes,mode=mode))
    

#replace_value
#replace_value_first
#replace_value_last
#replace_value_which
#replace_value_many
#replace_value_all
    
def replace_value_seqs(ol,src_value,dst_value,seqs,**kwargs):
    '''
        from elist.elist import *
        ol = [1,'a',3,'a',5,'a',6,'a']
        id(ol)
        new = replace_value_seqs(ol,'a','AAA',[0,1])
        ol
        new
        id(ol)
        id(new)
        ####
        ol = [1,'a',3,'a',5,'a',6,'a']
        id(ol)
        rslt = replace_value_seqs(ol,'a','AAA',[0,1],mode="original")
        ol
        rslt
        id(ol)
        id(rslt)
    '''
    if('mode' in kwargs):
        mode = kwargs["mode"]
    else:
        mode = "new"
    indexes = indexes_some(ol,src_value,*list(seqs))
    return(replace_indexes(ol,dst_value,indexes,mode=mode))
      
def replace_value_some(ol,src_value,dst_value,*seqs,**kwargs):
    '''
        from elist.elist import *
        ol = [1,'a',3,'a',5,'a',6,'a']
        id(ol)
        new = replace_value_some(ol,'a','AAA',0,1)
        ol
        new
        id(ol)
        id(new)
        ####
        ol = [1,'a',3,'a',5,'a',6,'a']
        id(ol)
        rslt = replace_value_some(ol,'a','AAA',0,1,mode="original")
        ol
        rslt
        id(ol)
        id(rslt)
    '''
    if('mode' in kwargs):
        mode = kwargs["mode"]
    else:
        mode = "new"
    return(replace_value_seqs(ol,src_value,dst_value,list(seqs),mode=mode))

#
def cond_replace_value_all(ol,dst_value,**kwargs):
    '''
        from elist.elist import *
        ol = [1,'X',3,'b',5,'c',6,'A',7,'b',8,'B',9]
        id(ol)
        def afterCH(ele,ch):
            cond = (ord(str(ele)) > ord(ch))
            return(cond)

        new = cond_replace_value_all(ol,"REPLACED",cond_func=afterCH,cond_func_args=['B'])
        ol
        new
        id(ol)
        id(new)
        ####
        ol = [1,'X',3,'b',5,'c',6,'A',7,'b',8,'B',9]
        id(ol)
        rslt = cond_replace_value_all(ol,"REPLACED",cond_func=afterCH,cond_func_args=['B'],mode="original")
        ol
        rslt
        id(ol)
        id(rslt)

    ''' 
    cond_func = kwargs['cond_func']
    if('cond_func_args' in kwargs):
        cond_func_args = kwargs['cond_func_args']
    else:
        cond_func_args = []
    if('mode' in kwargs):
        mode = kwargs["mode"]
    else:
        mode = "new"
    new = copy.deepcopy(ol)
    selected = find_all(new,cond_func,*cond_func_args)
    selected_indexes = array_map(selected,lambda ele:ele['index'])
    new = replace_seqs(new,dst_value,selected_indexes)
    if(mode == "new"):
        return(new)
    else:
        ol.clear()
        ol.extend(new)
        return(ol)


def cond_replace_value_seqs(ol,dst_value,seqs,**kwargs):
    '''
        from elist.elist import *
        ol = [1,'X',3,'b',5,'c',6,'A',7,'b',8,'B',9]
        id(ol)
        def afterCH(ele,ch):
            cond = (ord(str(ele)) > ord(ch))
            return(cond)
        
        new = cond_replace_value_seqs(ol,"REPLACED",[0,2],cond_func=afterCH,cond_func_args=['B'])
        ol
        new
        id(ol)
        id(new)
        ####
        ol = [1,'X',3,'b',5,'c',6,'A',7,'b',8,'B',9]
        id(ol)
        rslt = cond_replace_value_seqs(ol,"REPLACED",[0,2],cond_func=afterCH,cond_func_args=['B'],mode="original")
        ol
        rslt
        id(ol)
        id(rslt)
    '''
    cond_func = kwargs['cond_func']
    if('cond_func_args' in kwargs):
        cond_func_args = kwargs['cond_func_args']
    else:
        cond_func_args = []
    if('mode' in kwargs):
        mode = kwargs["mode"]
    else:
        mode = "new"
    new = copy.deepcopy(ol)
    selected = find_all(new,cond_func,*cond_func_args)
    selected_indexes = array_map(selected,lambda ele:ele['index'])
    selected_indexes = select_seqs(selected_indexes,seqs)
    new = replace_seqs(new,dst_value,selected_indexes)
    if(mode == "new"):
        return(new)
    else:
        ol.clear()
        ol.extend(new)
        return(ol)


def cond_replace_value_some(ol,dst_value,*some,**kwargs):
    '''
        from elist.elist import *
        ol = [1,'X',3,'b',5,'c',6,'A',7,'b',8,'B',9]
        id(ol)
        def afterCH(ele,ch):
            cond = (ord(str(ele)) > ord(ch))
            return(cond)
        
        new = cond_replace_value_some(ol,"REPLACED",0,2,cond_func=afterCH,cond_func_args=['B'])
        ol
        new
        id(ol)
        id(new)
        ####
        ol = [1,'X',3,'b',5,'c',6,'A',7,'b',8,'B',9]
        id(ol)
        rslt = cond_replace_value_some(ol,"REPLACED",0,2,cond_func=afterCH,cond_func_args=['B'],mode="original")
        ol
        rslt
        id(ol)
        id(rslt)
    '''
    cond_func = kwargs['cond_func']
    if('cond_func_args' in kwargs):
        cond_func_args = kwargs['cond_func_args']
    else:
        cond_func_args = []
    if('mode' in kwargs):
        mode = kwargs["mode"]
    else:
        mode = "new"
    seqs = list(some)
    new = copy.deepcopy(ol)
    selected = find_all(new,cond_func,*cond_func_args)
    selected_indexes = array_map(selected,lambda ele:ele['index'])
    selected_indexes = select_seqs(selected_indexes,seqs)
    new = replace_seqs(new,dst_value,selected_indexes)
    if(mode == "new"):
        return(new)
    else:
        ol.clear()
        ol.extend(new)
        return(ol)


#cond_replace_value
#cond_replace_value_first
#cond_replace_value_last
#cond_replace_value_which
#cond_replace_value_many
#cond_replace_value_swarm





def rangize(break_points,length):
    '''
        break_points = [1,3,9,12,-2]
        length = 15
        secs = rangize(break_points,length)
        forEach(secs,print)
    '''
    bps = array_map(break_points,uniform_index,length)
    bps.sort()
    bps = prepend(bps,0)
    bps = append(bps,length)
    bps = uniqualize(bps)
    bpslen = bps.__len__()
    secs=[(0,bps[0])]
    for i in range(0,bpslen-1):
        r = (bps[i],bps[i+1])
        secs.append(r)
    secs.append((bps[bpslen-1],length))
    if(secs[0][0] == secs[0][1]):
        secs.pop(0)
    else:
        pass
    if(secs[-1][0] == secs[-1][1]):
        secs.pop(-1)
    else:
        pass
    return(secs)


def rangize_fullfill(spans,lngth):
    brkpnts = []
    for i in range(0,spans.__len__()):
        span = spans[i]
        brkpnts.append(span[0])
        brkpnts.append(span[1])
    return(rangize(brkpnts,lngth))


def rangize_supplement(spans,lngth):
    '''
        spans = [(0, 3), (4, 7), (8, 10), (11, 12), (13, 16), (17, 20)]
        rangize_supplement(spans,24)
        
    '''
    rslt = []
    si = 0
    ei = spans[0][0]
    if(si == ei):
        pass
    else:
        rslt.append((si,ei))
    prev_ei = spans[0][1]
    for i in range(1,spans.__len__()):
        si = prev_ei
        ei = spans[i][0]
        rslt.append((si,ei))
        prev_ei = spans[i][1]
    if(prev_ei < lngth):
        rslt.append((prev_ei,lngth))
    else:
        rslt.append((prev_ei,lngth+1))
    return(rslt)


def rangize_supp(spans,lngth):
    '''
        spans = [(0, 3), (4, 7), (8, 10), (11, 12), (13, 16), (17, 20)]
        rangize_supplement(spans,24)

    '''
    rslt = []
    si = 0
    ei = spans[0][0]
    if(si == ei):
        pass
    else:
        rslt.append((si,ei))
    prev_ei = spans[0][1]
    for i in range(1,spans.__len__()):
        si = prev_ei
        ei = spans[i][0]
        rslt.append((si,ei))
        prev_ei = spans[i][1]
    if(prev_ei < lngth):
        rslt.append((prev_ei,lngth))
    else:
        pass
    return(rslt)


def range_compress(ol):
    '''
        #only support sorted-ints or sorted-ascii
        l = [1,5,6,7,8,13,14,18,30,31,32,33,34]
        range_compress(l)
        l = [1,5,6,7,8,13,14,18,30,31,32,33,34,40]
        range_compress(l)
        l = ['a','b','c','d','j','k','l','m','n','u','y','z']
        range_compress(l)
    '''
    T = (type(ol[0]) == type(0))
    if(T):
        l = ol
    else:
        l = array_map(ol,ord)
    length = l.__len__()
    secs = []
    si = 0
    ei = 0
    prev = l[0]
    for i in range(1,length):
        curr = l[i]
        cond = (curr == (prev+1))
        if(cond):
            ei = i
            prev = curr
        else:
            if(T):
                sec = (l[si],l[ei])
            else:
                sec = (ol[si],ol[ei])
            if(si == ei):
                sec = sec[0]
            else:
                pass
            secs.append(sec)
            si = i
            ei = i 
            prev = curr
    if(T):
        sec = (l[si],l[ei])
    else:
        sec = (ol[si],ol[ei])
    if(si == ei):
        sec = sec[0]
    else:
        pass
    secs.append(sec)
    return(secs)

def range_decompress(cl):
    '''
        #only support sorted-ints or sorted-ascii
        cl = [1, (5, 8), (13, 14), 18, (30, 34)]
        range_decompress(cl)
        cl = [1, (5, 8), (13, 14), 18, (30, 34), 40]
        range_decompress(cl)
        cl = [('a', 'd'), ('j', 'n'), 'u', ('y', 'z')]
        range_decompress(cl)
    '''
    def cond_func(ele):
        length = ele.__len__()
        cond = (length == 1)
        if(cond):
            return(ord(ele))
        else:
            x = ord(ele[0])
            y = ord(ele[1])
            return((x,y))
    if(type(cl[0])==type(0)):
        T = True
    elif(cl[0].__len__() == 1):
        T = (type(cl[0]) == type(0))
    else:
        T = (type(cl[0][0]) == type(0))
    if(T):
        l = cl 
    else:
        l = array_map(cl,cond_func)
    rslt = []
    for i in range(0,l.__len__()):
        ele = l[i]
        if(type(ele) == type(0)):
            arr = [ele]
        elif(ele.__len__() == 1):
            arr = [ele]
        else:
            sv = ele[0]
            ev = ele[1]
            arr = init_range(sv,ev+1,1)
        if(T):
            pass
        else:
            arr = array_map(arr,chr)
        rslt.extend(arr)
    return(rslt)
    

def interval_sizes2brks(sizes):
    '''
        >>> interval_sizes2brks([1,4,6,4])
        [1, 5, 11, 15]
        >>>
    '''
    rslt = []
    acc = 0
    for i in range(len(sizes)):
        acc = acc + sizes[i]
        rslt.append(acc)
    return(rslt)



def which_interval(val,intervals):
    rslt = find_first(intervals,lambda ele:(val>=ele[0])and(val <ele[1]))
    return(rslt['value'])

def which_interval_index(val,intervals):
    rslt = find_first(intervals,lambda ele:(val>=ele[0])and(val <ele[1]))
    return(rslt['index'])

def value_find_range_i(value,break_points,lngth):
    rngs = rangize(break_points,lngth)
    rslt = find_first(rngs,lambda ele:(value>=ele[0])and(value<ele[1]))
    return(rslt['index'])

def value_find_range_v(value,break_points,lngth):
    rngs = rangize(break_points,lngth)
    rslt = find_first(rngs,lambda ele:(value>=ele[0])and(value<ele[1]))
    return(rslt['value'])

def value_find_range_iv(value,break_points,lngth):
    rngs = rangize(break_points,lngth)
    rslt = find_first(rngs,lambda ele:(value>=ele[0])and(value<ele[1]))
    return(rslt)


def is_list(obj):
    '''
        from elist.elist import *
        is_list([1,2,3])
        is_list(200)
    '''
    if(type(obj)==type([])):
        return(True)
    else:
        return(False)

isArray = is_list


def broken_seqs(ol,break_points):
    '''
        ol = initRange(0,20,1)
        ol
        break_points = [1,6,14,9]
        secs = broken_seqs(ol,break_points)
        forEach(secs,print)
    '''
    bps = list(break_points)
    length = ol.__len__()
    rgs = rangize(bps,length)
    rslt = []
    for i in range(0,rgs.__len__()):
        si,ei = rgs[i]
        sec = ol[si:ei]
        rslt.append(sec)
    return(rslt)


def broken_some(ol,*break_points):
    '''
        ol = initRange(0,20,1)
        ol
        secs = broken_some(ol,1,6,14,9)
        forEach(secs,print)
    '''
    bps = list(break_points)
    return(broken_seqs(ol,bps))

###this is very special

def brkl2kvlist(arr,interval,sub_pos=1,**kwargs):
    '''
        arr = ["color1","r1","g1","b1","a1","color2","r2","g2","b2","a2"]
        brkl2kvlist(arr,5)
        (['color1', 'color2'], [['r1', 'g1', 'b1', 'a1'], ['r2', 'g2', 'b2', 'a2']])
        brkl2kvlist(arr,5,2)
        ([['color1', 'r1'], ['color2', 'r2']], [['g1', 'b1', 'a1'], ['g2', 'b2', 'a2']])
    '''
    lngth = arr.__len__()
    brkseqs1 = init_range(0,lngth,interval)
    brkseqs2 = init_range(sub_pos,lngth,interval)
    brkseqs = interleave(brkseqs1,brkseqs2)
    l = broken_seqs(arr,brkseqs)
    kl = select_evens(l)
    vl = select_odds(l)
    if("single_key" in kwargs):
        single_key = kwargs['single_key']
    else:
        single_key = True
    if(sub_pos == 1):
        if(single_key):
            kl = mapv(kl,lambda ele:ele[0])
        else:
            pass
    else:
        pass
    return((kl,vl))


###


####

def divide(ol,interval):
    '''
        #
        ol = elel.initRange(0,20,1)
        interval = 3
        rslt = elel.divide(ol,interval)
        rslt
        rslt = elel.divide(ol,4)
        rslt
    '''
    length = ol.__len__()
    seqs = initRange(0,length,interval)
    rslt = broken_seqs(ol,seqs)
    return(rslt)


chunk = divide

################

#
def repeat_every(l,times):
    nl = []
    for i in range(0,l.__len__()):
        for j in range(0,times):
            nl.append(l[i])
    return(nl)

########
def apadding(arr,value,num):
    args = init(value,num)
    return(append_some(arr,*args))


def padding(l,lngth,val):
    '''
        >>> padding([1,2,3],6,0)
        [1, 2, 3, 0, 0, 0]
        >>>
    '''
    llen = len(l)
    if(llen>=lngth):
        return(l)
    else:
        tail = init(lngth-llen,val)
        return(l+tail)

def prepadding(l,lngth,val):
    '''
        >>> prepadding([1,2,3],6,0)
        [0, 0, 0, 1, 2, 3]
        >>>
    '''
    llen = len(l)
    if(llen>=lngth):
        return(l)
    else:
        hl = init(lngth-llen,val)
        return(hl+l)


###########
#classify


def classify(dl,**kwargs):
    '''
    '''
    cond_func = kwargs['cond_func']
    if('cond_func_args' in kwargs):
        cond_func_args = kwargs['cond_func_args']
    else:
        cond_func_args = []
    rslt = {}
    rslt['yes'] = []
    rslt['no'] = []
    length = dl.__len__()
    for i in range(0,length):
        ele = dl[i]
        cond = cond_func(ele,*cond_func_args)
        if(cond):
            rslt['yes'].append(ele)
        else:
            rslt['no'].append(ele)
    return(rslt)



#classifyDictList


def classifyDictList(dl,**kwargs):
    '''
    '''
    key = kwargs['key']
    cond_func = kwargs['cond_func']
    if('cond_func_args' in kwargs):
        cond_func_args = kwargs['cond_func_args']
    else:
        cond_func_args = []        
    rslt = {}
    rslt['yes'] = []
    rslt['no'] = []
    length = dl.__len__()
    for i in range(0,length):
        ele = dl[i]
        cond = cond_func(ele,via,*cond_func_args)
        if(cond):
            rslt['yes'].append(ele)
        else:
            rslt['no'].append(ele)
    return(rslt)


#######@@
def split(ol,value,**kwargs):
    '''
        ol = ['a',1,'a',2,'a',3,'a',4,'a']
        split(ol,'a')
        split(ol,'a',whiches=[0])
        split(ol,'a',whiches=[1])
        split(ol,'a',whiches=[2])
        split(ol,'a',whiches=[0,2])
        ol = [1,'a',2,'a',3,'a',4]
        split(ol,'a')
        split('x=bcdsef=g','=',whiches=[0])
        
    '''
    if('whiches' in kwargs):
        whiches = kwargs['whiches']    
    else:
        whiches = None
    indexes =  indexes_all(ol,value)
    if(whiches == None):
        pass
    else:
        indexes = select_indexes(indexes,whiches)
    rslt = []
    rslt.append(ol[:indexes[0]])
    si = indexes[0]+1
    for i in range(1,indexes.__len__()):
        ei = indexes[i]
        ele = ol[si:ei]
        rslt.append(ele)
        si = ei + 1
    ele = ol[si:ol.__len__()]
    rslt.append(ele)
    return(rslt)

#def shrink_split 多个连续的sp当作一个
#def split_some(ol,*some):

def get_span_loc(spans,word_loc):
    for i in range(0,spans.__len__()):
        span = spans[i]
        if((word_loc>=span[0])&(word_loc<span[1])):
            return(i)
        else:
            pass
    return(None)


def where(ol,value):
    '''
        ol = [0, 4, 6, 8, 10, 14]
        where(ol,-1)
        where(ol,1)
        where(ol,2)
        where(ol,3)
        where(ol,4)
        where(ol,9)
        where(ol,14)
        where(ol,17)
    '''
    si = None
    ei = None
    for i in range(0,ol.__len__()):
        ele = ol[i]
        if(value >ele):
            si = i 
        elif(value == ele):
            return((i,i))
        else:
            ei = i 
            return((si,ei))
    return((si,ei))

where_index_interval = where
index_interval = where

def value_interval(ol,value):
    '''
        ol = [0, 4, 6, 8, 10, 14]
        value_interval(ol,-1)
        value_interval(ol,1)
        value_interval(ol,2)
        value_interval(ol,3)
        value_interval(ol,4)
        value_interval(ol,9)
        value_interval(ol,14)
        value_interval(ol,17)
    '''
    si,ei = where(ol,value)
    if(si == None):
        sv = None
    else:
        sv = ol[si]
    if(ei == None):
        ev = None
    else:
        ev = ol[ei]
    return((sv,ev))

where_value_interval = value_interval

def upper_bound(ol,value):
    '''
        ol = [0, 4, 6, 8, 10, 14]
        upper_bound(ol,-1)
        upper_bound(ol,1)
        upper_bound(ol,2)
        upper_bound(ol,3)
        upper_bound(ol,4)
        upper_bound(ol,9)
        upper_bound(ol,14)
        upper_bound(ol,17)
    '''
    return(value_interval(ol,value)[1])

def lower_bound(ol,value):
    '''
        ol = [0, 4, 6, 8, 10, 14]
        lower_bound(ol,-1)
        lower_bound(ol,1)
        lower_bound(ol,2)
        lower_bound(ol,3)
        lower_bound(ol,4)
        lower_bound(ol,9)
        lower_bound(ol,14)
        lower_bound(ol,17)
    '''
    return(value_interval(ol,value)[0])


def rand_some_indexes(si,ei,n,**kwargs):
    if('sort' in kwargs):
        sort = kwargs['sort']
    else:
        sort = True 
    rslt = []
    arr = init_range(si,ei,1)
    c = 0
    while(c<n):
        r = random.randrange(0,ei)
        p = arr.pop(r)
        rslt.append(p)
        ei = ei - 1
        c = c + 1
    if(sort):
        rslt.sort()
    else:
        pass
    return(rslt)


def rand_sub(arr,*args,**kwargs):
    '''
        arr = ['scheme', 'username', 'password', 'hostname', 'port', 'path', 'params', 'query', 'fragment']
        rand_sub(arr,3)
        rand_sub(arr,3)
        rand_sub(arr,3)
        rand_sub(arr)
        rand_sub(arr)
        rand_sub(arr)
    '''
    arr = copy.deepcopy(arr)
    lngth = arr.__len__()
    args = list(args)
    if(args.__len__() == 0):
        n = random.randrange(0,lngth)
    else:
        n = args[0]
        if(n>lngth):
            n = lngth
        else:
            pass
    indexes = rand_some_indexes(0,lngth,n,**kwargs)
    narr = select_seqs_keep_order(arr,indexes)
    return(narr)



#####

def max_length(ol):
    lngths = mapv(ol,len,[])
    lngth = max(lngths)
    return(lngth)


#########set#####################


def intersection(ol1,ol2):
    nl = list(set(ol1).intersection(set(ol2)))
    return(nl)



#def ordered_intersection(ol1,ol2):
#complicated  need LCS        

def strict_seq_intersection(ol1,ol2,**kwargs):
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

    




########set######################








####math 


def combinations(arr,*args):
    args = list(args)
    lngth = len(args)
    if(lngth == 0):
        start = 1
        end = len(arr) + 1
    elif(lngth == 1):
        start = uniform_index(args[0],lngth)
        end = len(arr) + 1
    else:
        start = uniform_index(args[0],lngth)
        end = uniform_index(args[1],lngth)
    rslt = []
    for i in range(start,end):
        tmp = list(itertools.combinations(arr,i))
        rslt.extend(tmp)
    return(rslt)






#the below is for nested analysis

def is_leaf(obj):
    '''
        the below is for nested-list
        any type is not list will be treated as a leaf
        empty list will be treated as a leaf
        from elist.elist import *
        is_leaf(1)
        is_leaf([1,2,3])
        is_leaf([])
    '''
    if(is_list(obj)):
        length = obj.__len__()
        if(length == 0):
            return(True)
        else:
            return(False)
    else:
        return(True)

class LevelCache():
    '''
        current level unhandled_data stored in .data
        current level unhandled_desc stored in .desc
        next level unhandled_data stored in .ndata
        next level unhandled_desc stored in .ndesc
    '''
    def help(self):
        print(self.__doc__)
    def __init__(self,**kwargs):
        if('datas' in kwargs):
            datas = kwargs['datas']
        else:
            datas = []
        if('descs' in kwargs):
            descs = kwargs['descs']
        else:
            descs = []
        self.data = [datas]
        self.desc = [descs]
        self.ndata = []
        self.ndesc = []
    def update(self):
        self.data = self.ndata
        self.desc = self.ndesc
        self.ndata = []
        self.ndesc = []
    def __repr__(self):
        print("data: {0}".format(self.data))
        print("desc: {0}".format(self.desc))
        print("ndata: {0}".format(self.ndata))
        print("ndesc: {0}".format(self.ndesc),end='')
        return("")
    def clear(self):
        self.data = []
        self.desc = []
        self.ndata = []
        self.ndesc = []

class StateCache():
    '''
        parent level handled_desc stored in .pdesc_level
        current level handled_desc stored in .desc_level
        过早优化乃万恶之源，之所以有LevelCache 和 StateCache 两个Cache 是为了利用我之前的旧代码，弃之可惜，尾大不掉
    '''
    def help(self):
        print(self.__doc__)
    def __init__(self,root_matrix):
        #there is only one level in root_matrix: level 0
        #there is only one element in root_matrix level 0 :element 0 
        self.matrix = root_matrix
        self.depth = 0
        self.pdesc_level = []
        self.desc_level = self.matrix[0]
    def update(self):
        self.pdesc_level = self.desc_level
        self.matrix.append([])
        self.depth = self.depth + 1
        self.desc_level = self.matrix[self.depth]
    def __repr__(self):
        print("depth: {0}".format(self.depth))
        print("pdesc_level: {0}".format(self.pdesc_level))
        print("desc_level: {0}".format(self.desc_level),end='')
        return("")

def pcache_bind_dynamic_method(pcache,**kwargs):
    '''
    '''
    mn = kwargs['method_name']
    func = kwargs['func']
    method_names = ['get_children_handler','parent_handler','child_begin_handler','leaf_handler','non_leaf_handler','child_end_handler']
    cond = (mn in method_names)
    if(cond):
        pcache.__setattr__(mn, MethodType(func,pcache))
    else:
        pass
    return(pcache)

def init_pcache_handler_inline(kwargs):
    pcache = PointerCache()
    for mn in kwargs:
        cond = (mn in ['get_children_handler','parent_handler','child_begin_handler','leaf_handler','non_leaf_handler','child_end_handler'])
        if(cond):
            func = kwargs[mn]
            pcache.__setattr__(mn, MethodType(func,pcache))
        else:
            pass
    return(pcache)

def pcache_reset_methods(pcache,**kwargs):
    '''
    '''
    def get_children_handler(self,*args):
        '''
            list's children list is self
        '''
        return(self.pdata)
    def parent_handler(self,lcache,i,*args):
        '''
            _update_pdesc_sons_info
        '''
        pdesc = lcache.desc[i]
        pdesc['sons_count'] = self.sibs_len
        pdesc['leaf_son_paths'] = []
        pdesc['non_leaf_son_paths'] = []
        return(pdesc)
    def child_begin_handler(self,scache,*args):
        '''
            _creat_child_desc
            update depth,parent_breadth_path,parent_path,sib_seq,path,lsib_path,rsib_path,lcin_path,rcin_path
        '''
        pdesc = self.pdesc
        depth = scache.depth
        sib_seq = self.sib_seq
        sibs_len = self.sibs_len
        pdesc_level = scache.pdesc_level
        desc = copy.deepcopy(pdesc)
        desc = reset_parent_desc_template(desc)
        desc['depth'] = depth
        desc['parent_breadth_path'] = copy.deepcopy(desc['breadth_path'])
        desc['sib_seq'] = sib_seq
        desc['parent_path'] = copy.deepcopy(desc['path'])
        desc['path'].append(sib_seq)
        update_desc_lsib_path(desc)
        update_desc_rsib_path(desc,sibs_len)
        if(depth == 1):
            pass
        else:
            update_desc_lcin_path(desc,pdesc_level)
            update_desc_rcin_path(desc,sibs_len,pdesc_level)
        return(desc)
    def leaf_handler(self,*args):
        '''#leaf child handler'''
        desc = self.desc
        pdesc = self.pdesc
        desc['leaf'] = True
        desc['sons_count'] = 0
        pdesc['leaf_son_paths'].append(copy.deepcopy(desc['path']))
    def non_leaf_handler(self,lcache):
        '''#nonleaf child handler'''
        desc = self.leaf
        pdesc = self.pdesc
        desc['leaf'] = False
        pdesc['non_leaf_son_paths'].append(copy.deepcopy(desc['path']))
        lcache.ndata.append(self.data)
        lcache.ndesc.append(desc)
    def child_end_handler(self,scache):
        '''
            _upgrade_breadth_info
            update breadth, breadth_path, and add desc to desc_level
        '''
        desc = self.desc
        desc_level = scache.desc_level
        breadth = desc_level.__len__()
        desc['breadth'] = breadth
        desc['breadth_path'].append(breadth)
        desc_level.append(desc)
    funcs = [get_children_handler,parent_handler,child_begin_handler,leaf_handler,non_leaf_handler,child_end_handler]
    method_names = ['get_children_handler','parent_handler','child_begin_handler','leaf_handler','non_leaf_handler','child_end_handler']
    for i in range(0,funcs.__len__()):
        mn = method_names[i]
        func = funcs[i]
        pcache.__setattr__(mn, MethodType(func,pcache))
    return(pcache)

class PointerCache():
    '''
    '''
    def get_children_handler(self,*args):
        '''
            list's children list is self
        '''
        return(self.pdata)
    def parent_handler(self,lcache,i,*args):
        '''
            _update_pdesc_sons_info
        '''
        pdesc = lcache.desc[i]
        pdesc['sons_count'] = self.sibs_len
        pdesc['leaf_son_paths'] = []
        pdesc['non_leaf_son_paths'] = []
        pdesc['leaf_descendant_paths'] = []
        pdesc['non_leaf_descendant_paths'] = []
        return(pdesc)
    def child_begin_handler(self,scache,*args):
        '''
            _creat_child_desc
            update depth,parent_breadth_path,parent_path,sib_seq,path,lsib_path,rsib_path,lcin_path,rcin_path
        '''
        pdesc = self.pdesc
        depth = scache.depth
        sib_seq = self.sib_seq
        sibs_len = self.sibs_len
        pdesc_level = scache.pdesc_level
        desc = copy.deepcopy(pdesc)
        desc = reset_parent_desc_template(desc)
        desc['depth'] = depth
        desc['parent_breadth_path'] = copy.deepcopy(desc['breadth_path'])
        desc['sib_seq'] = sib_seq
        desc['parent_path'] = copy.deepcopy(desc['path'])
        desc['path'].append(sib_seq)
        update_desc_lsib_path(desc)
        update_desc_rsib_path(desc,sibs_len)
        if(depth == 1):
            pass
        else:
            update_desc_lcin_path(desc,pdesc_level)
            update_desc_rcin_path(desc,sibs_len,pdesc_level)
        return(desc)
    def leaf_handler(self,*args):
        '''#leaf child handler'''
        desc = self.desc
        pdesc = self.pdesc
        desc['leaf'] = True
        desc['sons_count'] = 0
        pdesc['leaf_son_paths'].append(copy.deepcopy(desc['path']))
        pdesc['leaf_descendant_paths'].append(copy.deepcopy(desc['path']))
    def non_leaf_handler(self,lcache):
        '''#nonleaf child handler'''
        desc = self.desc
        pdesc = self.pdesc
        desc['leaf'] = False
        pdesc['non_leaf_son_paths'].append(copy.deepcopy(desc['path']))
        pdesc['non_leaf_descendant_paths'].append(copy.deepcopy(desc['path']))
        lcache.ndata.append(self.data)
        lcache.ndesc.append(desc)
    def child_end_handler(self,scache):
        '''
            _upgrade_breadth_info
            update breadth, breadth_path, and add desc to desc_level
        '''
        desc = self.desc
        desc_level = scache.desc_level
        breadth = desc_level.__len__()
        desc['breadth'] = breadth
        desc['breadth_path'].append(breadth)
        desc_level.append(desc)
    def update_pdesc(self,lcache,i):
        self.unhandled_seq = i
        self.pdata = lcache.data[i]
        self.children = self.get_children_handler(*self.get_children_handler_args)
        self.sibs_len = self.children.__len__()
        self.pdesc = self.parent_handler(lcache,i,*self.parent_handler_args)
    def update_desc(self,lcache,scache,sib_seq):
        self.sib_seq = sib_seq
        self.data = self.children[self.sib_seq]
        self.desc = self.child_begin_handler(scache)
        if(is_leaf(self.data)):
            self.leaf_handler()
        else:
            self.non_leaf_handler(lcache)
        self.child_end_handler(scache)
    def help(self):
        print(self.__doc__)
    def __init__(self,**kwargs):
        if('get_children_handler_args' in kwargs):
            self.get_children_handler_args = kwargs['get_children_handler_args']
        else:
            self.get_children_handler_args = []
        if('parent_handler_args' in kwargs):
            self.parent_handler_args = kwargs['parent_handler_args']
        else:
            self.parent_handler_args = []
        if('child_begin_handler_args' in kwargs):
            self.child_begin_handler_args = kwargs['child_begin_handler_args']
        else:
            self.child_begin_handler_args = []
        if('leaf_handler_args' in kwargs):
            self.leaf_handler_args = kwargs['leaf_handler_args']
        else:
            self.leaf_handler_args = []
        if('non_leaf_handler_args' in kwargs):
            self.non_leaf_handler_args = kwargs['non_leaf_handler_args']
        else:
            self.non_leaf_handler_args = []
        if('child_end_handler_args' in kwargs):
            self.child_end_handler_args = kwargs['child_end_handler_args']
        else:
            self.child_end_handler_args = []
        self.unhandled_seq = None
        self.children = None
        self.sibs_len = None
        self.pdesc = None
        self.sib_seq = None
        self.data = None
        self.desc = None

##the below is for each element desc handle
def new_ele_description(**kwargs):
    '''
        from elist.elist import *
        from elist.jprint import pobj
        root_desc = new_ele_description(leaf=False,depth=0,breadth_path=[],path=[],parent_path=[],parent_breadth_path=[])
        pobj(root_desc)
        #None means not handled
    '''
    desc = {
        'leaf':None,
        'depth':None,
        'breadth':None,
        'breadth_path':None,
        'sib_seq':None,
        'path':None,
        'parent_path':None,
        'parent_breadth_path':None,
        'lsib_path':None,
        'rsib_path':None,
        'lcin_path':None,
        'rcin_path':None,
        'sons_count':None,
        'leaf_son_paths':None,
        'non_leaf_son_paths':None,
        'leaf_descendant_paths':None,
        'non_leaf_descendant_paths':None,
        'flat_offset':None,
        'flat_len':None
    }
    for key in kwargs:
        desc[key.lower()] = kwargs[key]
    return(desc)

def root_list(*args):
    '''
        from elist.elist import *
        from elist.jprint import pobj
        root_list([1],2,[1,2,3])
    '''
    return(list(args))

def init_desc_matrix(l):
    '''
        from elist.elist import *
        from elist.jprint import pobj
        l = [1,[4],2,[3,[5,6]]]
        desc_matrix = init_desc_matrix(l)
        pobj(desc_matrix)
    '''
    leaf = is_leaf(l)
    root_desc = new_ele_description(leaf=leaf,depth=0,breadth_path=[],path=[],parent_path=[],parent_breadth_path=[])
    if(leaf):
        root_desc['sons_count'] = 0
    else:
        pass
    desc_matrix = [
        [root_desc]
    ]
    return(desc_matrix)

def reset_parent_desc_template(desc):
    '''
        from elist.elist import *
        from elist.jprint import pobj
        pobj(desc)
        tem = reset_parent_desc_template(desc)
        pobj(tem)
        #only inherit path  and breadth_path
    '''
    tem = new_ele_description()
    tem['path'] = desc['path']
    tem['breadth_path'] = desc['breadth_path']
    return(tem)

def _init_unhandled(l,inited_matrix):
    '''
        from elist.elist import *
        from elist.jprint import pobj
        l = [1,[4],2,[3,[5,6]]]
        desc_matrix = init_desc_matrix(l)
        unhandled = _init_unhandled(l,desc_matrix)
        unhandled_data = unhandled['data']
        unhandled_desc = unhandled['desc']
        unhandled_data[0]
        unhandled_desc[0]
        unhandled_data[1]
        unhandled_desc[1]
    '''
    root_desc = inited_matrix[0][0]
    unhandled = {'data':[],'desc':[]}
    length = l.__len__()
    root_desc['sons_count'] = length
    root_desc['leaf_son_paths'] = []
    root_desc['non_leaf_son_paths'] = []    
    if(length == 0):
        pass
    else:
        inited_matrix.append([])
        level = inited_matrix[1]
        for i in range(0,length):
            child = l[i]
            desc = copy.deepcopy(root_desc)
            desc = reset_parent_desc_template(desc)
            desc['depth'] = 1
            desc['breadth'] = i
            desc['parent_breadth_path'] = copy.deepcopy(desc['breadth_path'])
            desc['breadth_path'].append(i)
            desc['sib_seq'] = i
            desc['parent_path'] = copy.deepcopy(desc['path'])
            desc['path'].append(i)
            if(i==0):
                pass
            else:
                desc['lsib_path'] = [i-1]
            if(i == (length - 1)):
                pass
            else:
                desc['rsib_path'] = [i+1]
            if(is_leaf(child)):
                desc['leaf'] = True
                desc['sons_count'] = 0
                root_desc['leaf_son_paths'].append(copy.deepcopy(desc['path']))
            else:
                desc['leaf'] = False
                root_desc['non_leaf_son_paths'].append(copy.deepcopy(desc['path']))
                unhandled['data'].append(child)
                unhandled['desc'].append(desc)
            level.append(desc)
    return(unhandled)

def update_desc_lsib_path(desc):
    '''
        leftSibling
        previousSibling
        leftSib
        prevSib
        lsib
        psib
        
        have the same parent,and on the left
    '''
    if(desc['sib_seq']>0):
        lsib_path = copy.deepcopy(desc['path'])
        lsib_path[-1] = desc['sib_seq']-1
        desc['lsib_path'] = lsib_path
    else:
        pass
    return(desc)

def update_desc_rsib_path(desc,sibs_len):
    '''
        rightSibling
        nextSibling
        rightSib
        nextSib
        rsib
        nsib
        
        have the same parent,and on the right
    '''
    if(desc['sib_seq']<(sibs_len-1)):
        rsib_path = copy.deepcopy(desc['path'])
        rsib_path[-1] = desc['sib_seq']+1
        desc['rsib_path'] = rsib_path
    else:
        pass
    return(desc)

def update_desc_lcin_path(desc,pdesc_level):
    '''
        leftCousin
        previousCousin
        leftCin
        prevCin
        lcin
        pcin
        
        parents are neighbors,and on the left
    '''
    parent_breadth = desc['parent_breadth_path'][-1]
    if(desc['sib_seq']==0):
        if(parent_breadth==0):
            pass
        else:
            parent_lsib_breadth = parent_breadth - 1
            plsib_desc = pdesc_level[parent_lsib_breadth]
            if(plsib_desc['leaf']):
                pass
            else:
                lcin_path = copy.deepcopy(plsib_desc['path'])
                lcin_path.append(plsib_desc['sons_count'] - 1)
                desc['lcin_path'] = lcin_path
    else:
        pass
    return(desc)

def update_desc_rcin_path(desc,sibs_len,pdesc_level):
    '''
        rightCousin
        nextCousin
        rightCin
        nextCin
        rcin
        ncin
        
        parents are neighbors,and on the right
    '''
    psibs_len = pdesc_level.__len__()
    parent_breadth = desc['parent_breadth_path'][-1]
    if(desc['sib_seq']==(sibs_len - 1)):
        if(parent_breadth==(psibs_len -1)):
            pass
        else:
            parent_rsib_breadth = parent_breadth + 1
            prsib_desc = pdesc_level[parent_rsib_breadth]
            #because from left to right to handle each level
            #sons_count will only be updated in the next-round 
            if(prsib_desc['leaf']):
                pass
            else:
                rcin_path = copy.deepcopy(prsib_desc['path'])
                rcin_path.append(0)
                desc['rcin_path'] = rcin_path
    else:
        pass
    return(desc)

def scan(l,**kwargs):
    '''
        from elist.elist import *
        from elist.jprint import pobj
        l = [1,[4],2,[3,[5,6]]]
        desc = description(l)
        l = [1,2,[4],[3,[5,6]]]
        desc = description(l)
    '''
    if('itermode' in kwargs):
        itermode = True
    else:
        itermode = False
    ####level ==  0
    desc_matrix = init_desc_matrix(l)
    if(desc_matrix[0][0]['leaf'] == True):
        return(desc_matrix)
    else:
        pass
    ####cache
    lcache=LevelCache(datas=l,descs=desc_matrix[0][0])
    scache=StateCache(desc_matrix)
    pcache = init_pcache_handler_inline(kwargs)
    ####level > 0
    while(lcache.data.__len__() > 0):
        #add next desc_level 
        scache.update()
        for unhandled_seq in range(0,lcache.data.__len__()):
            #handle parent
            pcache.update_pdesc(lcache,unhandled_seq)
            for sib_seq in range(0,pcache.sibs_len):
                #handle child
                pcache.update_desc(lcache,scache,sib_seq)
        #update level lcache
        lcache.update()
    return(desc_matrix)

class DescMatrix():
    '''
    '''
    def __init__(self,matrix):
        self.matrix = matrix
    @classmethod
    def loc(cls,desc):
        return([desc['depth'],desc['breadth']])
    @classmethod
    def ploc(cls,desc):
        if(desc['parent_breadth_path'] == []):
            col = 0
        else:
            col = desc['parent_breadth_path'][-1]
        if(desc['depth'] == 0):
            row = 0
        else:
            row = desc['depth']-1
        return([row,col])
    def pdesc(self,desc):
        pd = getitem_via_pathlist(self.matrix,self.ploc(desc))
        return(pd)

def fullfill_descendants_info(desc_matrix):
    '''
       flat_offset
    '''
    pathloc_mapping = {}
    locpath_mapping = {}
    #def leaf_handler(desc,pdesc,offset):
    def leaf_handler(desc,pdesc):
        #desc['flat_offset'] = (offset,offset+1)
        desc['non_leaf_son_paths'] = []
        desc['leaf_son_paths'] = []
        desc['non_leaf_descendant_paths'] = []
        desc['leaf_descendant_paths'] = []
        desc['flat_len'] = 1
        if(pdesc['flat_len']):
            pdesc['flat_len'] = pdesc['flat_len'] + 1
        else:
            pdesc['flat_len'] = 1
    #def non_leaf_handler(desc,pdesc,offset):
    def non_leaf_handler(desc,pdesc):
        #desc['flat_offset'] = (offset,offset+desc['flat_len'])
        pdesc['non_leaf_descendant_paths'].extend(copy.deepcopy(desc['non_leaf_descendant_paths']))
        pdesc['leaf_descendant_paths'].extend(copy.deepcopy(desc['leaf_descendant_paths']))
        if(pdesc['flat_len']):
            pdesc['flat_len'] = pdesc['flat_len'] + desc['flat_len']
        else:
            pdesc['flat_len'] = desc['flat_len']
    def fill_path_mapping(desc):
        pmk = tuple(desc['path'])
        pmv = tuple(DescMatrix.loc(desc))
        pathloc_mapping[pmk] = pmv
        locpath_mapping[pmv] = pmk
    dm = DescMatrix(desc_matrix)
    depth = desc_matrix.__len__()
    desc_level = desc_matrix[depth - 1]
    length = desc_level.__len__()
    #the last level
    #offset = 0
    for j in range(length - 1,-1,-1):
        desc = desc_level[j]
        fill_path_mapping(desc)
        pdesc = dm.pdesc(desc)
        leaf_handler(desc,pdesc)
        #leaf_handler(desc,pdesc,offset)
        #offset = offset + 1
    for i in range(depth-2,0,-1):
        #offset = 0
        desc_level = desc_matrix[i]
        length = desc_level.__len__()
        for j in range(length-1,-1,-1):
            desc = desc_level[j]
            fill_path_mapping(desc)
            pdesc = dm.pdesc(desc)
            if(desc['leaf']):
                leaf_handler(desc,pdesc)
                #leaf_handler(desc,pdesc,offset)
                #offset = offset + 1
            else:
                non_leaf_handler(desc,pdesc)
                #non_leaf_handler(desc,pdesc,offset)
                #offset = offset + desc['flat_len']
    desc_matrix[0][0]['flat_offset'] = (0,desc_matrix[0][0]['flat_len'])
    for i in range(0,depth-1):
        pdesc_level = desc_matrix[i]
        length = pdesc_level.__len__()
        for j in range(0,length):
            pdesc = pdesc_level[j]
            si = pdesc['flat_offset'][0]
            for i in range(0,pdesc['sons_count']):
                spl = append(pdesc['path'],i,mode='new')
                pk = tuple(spl)
                locx,locy = pathloc_mapping[pk]
                son = desc_matrix[locx][locy]
                ei = si + son['flat_len']
                son['flat_offset'] = (si,ei)
                si = ei
    return(desc_matrix,pathloc_mapping,locpath_mapping)

def pathlist_to_getStr(path_list):
    '''
        >>> pathlist_to_getStr([1, '1', 2])
            "[1]['1'][2]"
        >>>
    '''
    t1 = path_list.__repr__()
    t1 = t1.lstrip('[')
    t1 = t1.rstrip(']')
    t2 = t1.split(", ")
    s = ''
    for i in range(0,t2.__len__()):
        s = ''.join((s,'[',t2[i],']'))
    return(s)

#pl path-list
#gs get-string
pl2gs = pathlist_to_getStr


#

#
def getStr_to_pathlist(gs):
    '''
        gs = "[1]['1'][2]"
        getStr_to_pathlist(gs)
        gs = "['u']['u1']"
        getStr_to_pathlist(gs)
    '''
    def numize(w):
        try:
            int(w)
        except:
            try:
                float(w)
            except:
                return(w)
            else:
                return(float(w))
        else:
           return(int(w))
    def strip_quote(w):
        if(type(w) == type('')):
            if(w[0]==w[-1]):
                if((w[0]=="'") |(w[0]=='"')):
                    return(w[1:-1])
                else:
                    return(w)
            else:
                return(w)
        else:
            return(w)
    gs = gs[1:-1]
    pl = gs.split("][")
    pl = array_map(pl,numize)
    pl = array_map(pl,strip_quote)
    return(pl)

gs2pl = getStr_to_pathlist

####from elist.jprint

def get_block_op_pairs(pairs_str):
    '''
        # >>> get_block_op_pairs("{}[]")  
        # {1: ('{', '}'), 2: ('[', ']')}
        # >>> get_block_op_pairs("{}[]()")
        # {1: ('{', '}'), 2: ('[', ']'), 3: ('(', ')')}
        # >>> get_block_op_pairs("{}[]()<>")
        # {1: ('{', '}'), 2: ('[', ']'), 3: ('(', ')'), 4: ('<', '>')}
    '''
    pairs_str_len = pairs_str.__len__()
    pairs_len = pairs_str_len // 2
    pairs_dict = {}
    for i in range(1,pairs_len +1):
        pairs_dict[i] = pairs_str[i*2-2],pairs_str[i*2-1]
    return(pairs_dict)

def is_lop(ch,block_op_pairs_dict=get_block_op_pairs('{}[]()')):
    '''
    # is_lop('{',block_op_pairs_dict)
    # is_lop('[',block_op_pairs_dict)
    # is_lop('}',block_op_pairs_dict)
    # is_lop(']',block_op_pairs_dict)
    # is_lop('a',block_op_pairs_dict)
    '''
    for i in range(1,block_op_pairs_dict.__len__()+1):
        if(ch == block_op_pairs_dict[i][0]):
            return(True)
        else:
            pass
    return(False)

def is_rop(ch,block_op_pairs_dict=get_block_op_pairs('{}[]()')):
    '''
        # is_rop('{',block_op_pairs_dict)
        # is_rop('[',block_op_pairs_dict)
        # is_rop('}',block_op_pairs_dict)
        # is_rop(']',block_op_pairs_dict)
        # is_rop('a',block_op_pairs_dict)
    '''
    for i in range(1,block_op_pairs_dict.__len__()+1):
        if(ch == block_op_pairs_dict[i][1]):
            return(True)
        else:
            pass
    return(False)

def get_next_char_level_in_j_str(curr_lv,curr_seq,j_str,block_op_pairs_dict=get_block_op_pairs("{}[]()")):
    ''' the first-char is level-1
        when current is  non-op, next-char-level = curr-level
        when current is  lop,  non-paired-rop-next-char-level = lop-level+1;
        when current is  lop,  paired-rop-next-char-level = lop-level
        when current is  rop,  next-char-level = rop-level - 1
        # {"key_4_UF0aJJ6v": "value_1", "key_2_Hd0t": ["value_16", "value_8", "value_8", "value_15", "value_14", "value_19", {......
        # 122222222222222222222222222222222222222222222333333333333333333333333333333333333333333333333333333333333333333333334......
        # {\n"key_4_UF0aJJ6v": "value_1", \n"key_2_Hd0t": [\n"value_16", \n"value_8", \n"value_8", \n"value_15", \n"value_14", \n"value_19",...... 
        # 1 222222222222222222222222222222 2222222222222222 3333333333333 333333333333 333333333333 3333333333333 3333333333333 3333333333333...... 
        '''
    curr_ch = j_str[curr_seq]
    next_ch = j_str[curr_seq + 1]
    cond = 0
    for i in range(1,block_op_pairs_dict.__len__()+1):
        if(curr_ch == block_op_pairs_dict[i][0]):
            if(next_ch == block_op_pairs_dict[i][1]):
                next_lv = curr_lv               
            else:
                next_lv = curr_lv + 1
            cond = 1
            break
        elif(curr_ch == block_op_pairs_dict[i][1]):
            if(is_rop(next_ch,block_op_pairs_dict)):
                next_lv = curr_lv - 1
            else:
                next_lv = curr_lv
            cond = 1
            break
        else:
            pass
    if(cond == 1):
        pass
    elif(is_rop(next_ch,block_op_pairs_dict)):
        next_lv = curr_lv - 1
    else:    
        next_lv = curr_lv
    curr_lv = next_lv
    curr_seq = curr_seq + 1
    return(curr_lv,curr_lv,curr_seq)

def get_j_str_lvs_dict(j_str,block_op_pairs_dict=get_block_op_pairs("{}[]()")):
    j_str_len = j_str.__len__()
    j_str_lvs_dict = {}
    if( j_str_len == 0):
        j_str_lvs_dict = {}
    elif(j_str_len == 1):
        j_str_lvs_dict = {0:1}
    else:
        curr_lv = 1
        j_str_lvs_dict = {0:1}
        seq = 1
        curr_seq = 0
        while(curr_seq < j_str_len - 1):
            level,curr_lv,curr_seq = get_next_char_level_in_j_str(curr_lv,curr_seq,j_str,block_op_pairs_dict)
            j_str_lvs_dict[seq] =level
            seq = seq + 1
    return(j_str_lvs_dict)



####from elist.utils
def str_display_width(s):
    '''
        from elist.utils import *
        str_display_width('a')
        str_display_width('去')
    '''
    s= str(s)
    width = 0
    len = s.__len__()
    for i in range(0,len):
        sublen = s[i].encode().__len__()
        sublen = int(sublen/2 + 1/2)
        width = width + sublen
    return(width)

####from elist.ltdict
def ltdict2list(ltdict):
    l = []
    length = ltdict.__len__()
    for i in range(0,length):
        l.append(ltdict[i])
    return(l)

####beautiful display
def spacize(s,lvnum):
    lvs = get_j_str_lvs_dict(s)
    lvs = ltdict2list(lvs)
    sl=list(s)
    length = sl.__len__()
    rslt =''
    for i in range(0,length):
        if(lvs[i]>=lvnum):
            rslt = rslt + sl[i]
        else:
            rslt = rslt + chr(32)*str_display_width(sl[i])
    return(rslt)

def table(l,depth,**kwargs):
    if('no_return' in kwargs):
        no_return = kwargs['no_return']
    else:
        no_return = True
    s = l.__str__()
    rslt = ''
    for i in range(1,depth+1):
        rslt = rslt + spacize(s,i) + '\n'
    rslt = rslt[:-1]
    if(no_return):
        print(rslt)
    else:
        return(rslt)

####mat func for description matrix

def matrix_map(mat,map_func,map_func_args=[]):
    '''
        mat = [
            [1,2,3],
            [4,5,6],
            [7,8,9]
        ]
        
        def map_func(value,indexr,indexc,prefix,suffix):
            msg = prefix + str((indexr,indexc)) + " : "+str(value) + suffix
            return(msg)
        
        mmat = matrix_map(mat,map_func,map_func_args=["<",">"])
        
        mmat 
    '''
    mmat = []
    for i in range(0,mat.__len__()):
        level = mat[i]
        mmat.append([])
        for j in range(0,level.__len__()):
            value = level[j]
            indexr = i
            indexc = j
            ele = map_func(value,indexr,indexc,*map_func_args)
            mmat[i].append(ele)
    return(mmat)

def is_matrix(m,**kwargs):
    def cond_func(ele,lngth):
        cond = (ele.__len__() == lngth)
        return(cond)
    cond_1 = every(m,is_list)[0]
    if(cond_1):
        if('mode' in kwargs):
            mode = kwargs['mode']
        else:
            mode = 'strict' 
        if(mode == 'strict'):
            try:
                lngth = m[0].__len__()
                cond_2 = every(m,cond_func,lngth)[0]
            except:
                return(False)
            else:
                pass
        else:
            cond_2 = True
        return(cond_1 & cond_2)
    else:
        return(True)



#

def mat_mapv(mat,map_func,map_func_args=[]):
    '''
    '''
    mmat = []
    for i in range(0,mat.__len__()):
        level = mat[i]
        mmat.append([])
        for j in range(0,level.__len__()):
            value = level[j]
            indexr = i
            indexc = j
            ele = map_func(value,*map_func_args)
            mmat[i].append(ele)
    return(mmat)


#

#dfs depth-first-search trace
def get_dfs(l):
    '''
        l = ['v_7', 'v_3', 'v_1', 'v_4', ['v_4', 'v_2'], 'v_5', 'v_6', 'v_1', 'v_6', 'v_7', 'v_5', ['v_4', ['v_1', 'v_8', 'v_3', 'v_4', 'v_2', 'v_7', [['v_3', 'v_2'], 'v_4', 'v_5', 'v_1', 'v_3', 'v_1', 'v_2', 'v_5', 'v_8', 'v_8', 'v_7'], 'v_5', 'v_8', 'v_7', 'v_1', 'v_5'], 'v_6'], 'v_4', 'v_5', 'v_8', 'v_5']
        dfs = get_dfs(l)
    '''
    ltree = ListTree(l)
    dfs = ltree.tree()
    return(dfs)


#wfs  width-first-search trace
#wfsmat width-first-search matrix

def get_wfsmat(l):
    '''
       l = ['v_7', 'v_3', 'v_1', 'v_4', ['v_4', 'v_2'], 'v_5', 'v_6', 'v_1', 'v_6', 'v_7', 'v_5', ['v_4', ['v_1', 'v_8', 'v_3', 'v_4', 'v_2', 'v_7', [['v_3', 'v_2'], 'v_4', 'v_5', 'v_1', 'v_3', 'v_1', 'v_2', 'v_5', 'v_8', 'v_8', 'v_7'], 'v_5', 'v_8', 'v_7', 'v_1', 'v_5'], 'v_6'], 'v_4', 'v_5', 'v_8', 'v_5']
       get_wfs(l)
    '''
    ltree = ListTree(l)
    vdescmat = ltree.desc
    wfsmat = matrix_map(vdescmat,lambda v,ix,iy:v['path'])
    wfsmat.pop(0)
    return(wfsmat)



def mat2wfs(wfsmat):
    trace = []
    for i in range(0,wfsmat.__len__()):
        trace.extend(wfsmat[i])
    return(trace)

def wfs2mat(wfs):
    '''
        wfs = [[0], [1], [2], [3], [4], [5], [6], [7], [8], [9], [10], [11], [12], [13], [14], [15], [4, 0], [4, 1], [11, 0], [11, 1], [11, 2], [11, 1, 0], [11, 1, 1], [11, 1, 2], [11, 1, 3], [11, 1, 4], [11, 1, 5], [11, 1, 6], [11, 1, 7], [11, 1, 8], [11, 1, 9], [11, 1, 10], [11, 1, 11], [11, 1, 6, 0], [11, 1, 6, 1], [11, 1, 6, 2], [11, 1, 6, 3], [11, 1, 6, 4], [11, 1, 6, 5], [11, 1, 6, 6], [11, 1, 6, 7], [11, 1, 6, 8], [11, 1, 6, 9], [11, 1, 6, 10], [11, 1, 6, 0, 0], [11, 1, 6, 0, 1]]
    '''
    wfsmat = []
    depth = 0
    level = filter(wfs,lambda ele:ele.__len__()==1)
    while(level.__len__()>0):
        wfsmat.append([])
        wfsmat[depth] = level
        depth = depth+1
        level = filter(wfs,lambda ele:ele.__len__()==depth+1)
    return(wfsmat)


def get_wfs(l):
    wfsmat = get_wfsmat(l)
    wfs =  mat2wfs(wfsmat)
    return(wfs)


def dfs2wfsmat(dfs):
    '''
        dfs = [[0], [1], [2], [3], [4], [4, 0], [4, 1], [5], [6], [7], [8], [9], [10], [11], [11, 0], [11, 1], [11, 1, 0], [11, 1, 1], [11, 1, 2], [11, 1, 3], [11, 1, 4], [11, 1, 5], [11, 1, 6], [11, 1, 6, 0], [11, 1, 6, 0, 0], [11, 1, 6, 0, 1], [11, 1, 6, 1], [11, 1, 6, 2], [11, 1, 6, 3], [11, 1, 6, 4], [11, 1, 6, 5], [11, 1, 6, 6], [11, 1, 6, 7], [11, 1, 6, 8], [11, 1, 6, 9], [11, 1, 6, 10], [11, 1, 7], [11, 1, 8], [11, 1, 9], [11, 1, 10], [11, 1, 11], [11, 2], [12], [13], [14], [15]]
        
        dfs2wfs(dfs)
    '''
    wfsmat = []
    depth = 0
    level = filter(dfs,lambda ele:ele.__len__()==1)
    while(level.__len__()>0):
        wfsmat.append([])
        wfsmat[depth] = level
        depth = depth+1
        level = filter(dfs,lambda ele:ele.__len__()==depth+1)
    return(wfsmat)


     


def wfsmat2dfs(wfsmat):
    '''
        wfs = [[[0], [1], [2], [3], [4], [5], [6], [7], [8], [9], [10], [11], [12], [13], [14], [15]], [[4, 0], [4, 1], [11, 0], [11, 1], [11, 2]], [[11, 1, 0], [11, 1, 1], [11, 1, 2], [11, 1, 3], [11, 1, 4], [11, 1, 5], [11, 1, 6], [11, 1, 7], [11, 1, 8], [11, 1, 9], [11, 1, 10], [11, 1, 11]], [[11, 1, 6, 0], [11, 1, 6, 1], [11, 1, 6, 2], [11, 1, 6, 3], [11, 1, 6, 4], [11, 1, 6, 5], [11, 1, 6, 6], [11, 1, 6, 7], [11, 1, 6, 8], [11, 1, 6, 9], [11, 1, 6, 10]], [[11, 1, 6, 0, 0], [11, 1, 6, 0, 1]]]
        wfs2dfs(wfs)
        
    '''
    dfs = mat2wfs(wfsmat)
    dfs.sort()
    return(dfs)




def dfs2wfs(dfs):
    wfsmat = dfs2wfsmat(dfs)
    wfs = mat2wfs(wfsmat)
    return(wfs)

def wfs2dfs(wfs):
    wfsmat = wfs2mat(wfs)
    dfs = wfsmat2dfs(wfsmat)
    return(dfs)

####


class ListTree():
    '''
        
        
        ltree.parent_path(3,1,0)
        ltree.parent(3,1,0)
        
        ltree.son_paths(3)
        ltree.sons(3)
        ltree.son_paths(3,leaf_only=True)
        ltree.son_paths(3,non_leaf_only=True)
        ltree.sons(3,leaf_only=True)
        ltree.sons(3,non_leaf_only=True)
        
        ltree.descendant_paths(3)
        ltree.descendants(3)
        ltree.descendant_paths(3,from_lv=3)
        ltree.descendants(3,from_lv=3)
        ltree.descendant_paths(3,from_lv=2,to_lv=2)
        ltree.descendants(3,from_lv=2,to_lv=2)
        ltree.descendant_paths(3,leaf_only=True)
        ltree.descendants(3,leaf_only=True)
        ltree.descendant_paths(3,non_leaf_only=True)
        ltree.descendants(3,non_leaf_only=True)
        
        ltree.ancestor_paths(3,1,0)
        ltree.ancestors(3,1,0)
    '''
    def __init__(self,l):
        self.list = l
        self.desc = scan(l)
        self.desc,self.pathloc_mapping,self.locpath_mapping= fullfill_descendants_info(self.desc)
        self.depth = self.desc.__len__()
        self.maxLevelWidth = max(array_map(self.desc,len))
        self.flatWidth = self.desc[0][0]['flat_len']
        self.total = self.desc[0][0]['leaf_descendant_paths'].__len__() + self.desc[0][0]['non_leaf_descendant_paths'].__len__()
        self.trace = self.tree(show=False)
        self.prevSibling = self.lsib
        self.prevSibPath = self.lsib_path
        self.nextSibling = self.rsib
        self.nextSibPath = self.rsib_path
        self.precedingSibPaths = self.preceding_sib_paths
        self.precedingSibs = self.preceding_sibs
        self.followingSibPaths = self.following_sib_paths
        self.followingSibs = self.following_sibs
        self.someSibPaths = self.some_sib_paths
        self.someSibs = self.some_sibs
        self.whichSibPath = self.which_sib_path
        self.whichSib = self.which_sib
        self.showlog = None
    def __repr__(self):
        s = table(self.list,self.depth,no_return=0)
        showl = s.split('\n')
        self.showlog = showl
        return(s)
    def tree(self,**kwargs):
        if('leaf_only' in kwargs):
            leaf_only = kwargs['leaf_only']
            prompt = 'leaf_only'
        else:
            leaf_only = False
            prompt = ''
        if('non_leaf_only' in kwargs):
            non_leaf_only = kwargs['non_leaf_only']
            prompt = 'non_leaf_only'
        else:
            non_leaf_only = False
            prompt = ''
        if('from_lv' in kwargs):
            from_lv = kwargs['from_lv']
        else:
            from_lv = 1
        if('to_lv' in kwargs):
            to_lv = kwargs['to_lv']
        else:
            to_lv = self.depth
        if('show' in kwargs):
            show = kwargs['show']
        else:
            show = True
        lpls = copy.deepcopy(self.desc[0][0]['leaf_descendant_paths'])
        nlpls = copy.deepcopy(self.desc[0][0]['non_leaf_descendant_paths'])
        if(leaf_only):
            rslt = lpls
        elif(non_leaf_only):
            rslt = nlpls
        else:
            rslt = lpls+nlpls
        nrslt = []
        for i in range(0,rslt.__len__()):
            pl = rslt[i]
            length = pl.__len__()
            cond1 = (length >= from_lv)
            cond2 = (length <= to_lv)
            if(cond1 & cond2):
                nrslt.append(pl)
            else:
                pass
        showl = array_map(nrslt,pathlist_to_getStr)
        nrslt,showl = batsorted(nrslt,nrslt,showl)
        if(show):
            forEach(showl,print)
            self.showlog = ['tree -'+prompt+' :']
            self.showlog.extend(showl)
        else:
            pass
        return(nrslt)
    def level(self,lvnum,**kwargs):
        if('leaf_only' in kwargs):
            leaf_only = kwargs['leaf_only']
            prompt = 'leaf_only'
        else:
            leaf_only = False
            prompt = ''
        if('non_leaf_only' in kwargs):
            non_leaf_only = kwargs['non_leaf_only']
            prompt = 'non_leaf_only'
        else:
            non_leaf_only = False
            prompt = ''
        desc_level = self.desc[lvnum]
        lpls = []
        nlpls = []
        for i in range(0,desc_level.__len__()):
            desc = desc_level[i]
            pathlist = copy.deepcopy(desc['path'])
            if(desc['leaf']):
                lpls.append(pathlist)
            else:
                nlpls.append(pathlist)
        if(leaf_only):
            rslt = lpls
        elif(non_leaf_only):
            rslt = nlpls
        else:
            rslt = lpls+nlpls
        showl = array_map(rslt,pathlist_to_getStr)
        rslt,showl = batsorted(rslt,rslt,showl)
        forEach(showl,print)
        self.showlog = ['level -' +prompt+' ' +str(lvnum)+' :']
        self.showlog.extend(showl)
    def flatten(self):
        lpls = self.tree(leaf_only=True,show=False)
        flat = array_map(lpls,getitem_via_pathlist2,self.list)
        return(flat)
    def include(self,*sibseqs,**kwargs):
        if('pathlist' in kwargs):
            pl = kwargs['pathlist']
        else:
            pl = list(sibseqs)
        try:
            getitem_via_pathlist(self.list,pl)
        except:
            return(False)
        else:
            return(True)
    def __getitem__(self,*sibseqs):
        #this is a trick for __getitem__
        sibseqs = sibseqs[0]
        return(getitem_via_sibseqs(self.list,*sibseqs))
    def loc(self,*sibseqs):
        pl = list(sibseqs)
        pk = tuple(pl)
        loc = self.pathloc_mapping[pk]
        return(list(loc))
    def path(self,locx,locy):
        loc = (locx,locy)
        pl = self.locpath_mapping[loc]
        pl = list(pl)
        return(pl)
    def path2loc(self,pathlist):
        pl = pathlist
        pk = tuple(pl)
        loc = self.pathloc_mapping[pk]
        return(list(loc))
    def loc2path(self,loc):
        loc = tuple(loc)
        pl = self.locpath_mapping[loc]
        pl = list(pl)
        return(pl)
    @classmethod
    def showroute(cls,arr):
        def arrow(ele):
            return(str(ele)+' ->')
        arr = array_map(arr,arrow)
        forEach(arr,print)
        return(arr)
    def dig(self,howmanysteps=None):
        if(howmanysteps):
            pass
        else:
            howmanysteps = self.total
        self.showlog = ['dig -steps '+howmanysteps+' :']
        self.showlog.extend(self.showroute(self.trace[:howmanysteps]))
        return(self.trace[:howmanysteps])
    def parent(self,*sibseqs,**kwargs):
        if('pathlist' in kwargs):
            pl = kwargs['pathlist']
        else:
            pl = list(sibseqs)
        loc = self.path2loc(pl)
        ppl = self.desc[loc[0]][loc[1]]['parent_path']
        value = getitem_via_pathlist(self.list,ppl)
        return(value)
    def parent_path(self,*sibseqs,**kwargs):
        if('pathlist' in kwargs):
            pl = kwargs['pathlist']
        else:
            pl = list(sibseqs)
        locx,locy = tuple(self.path2loc(pl))
        ppl = self.desc[locx][locy]['parent_path']
        return(ppl)
    def son_paths(self,*sibseqs,**kwargs):
        if('pathlist' in kwargs):
            pl = kwargs['pathlist']
        else:
            pl = list(sibseqs)
        if('leaf_only' in kwargs):
            leaf_only = kwargs['leaf_only']
        else:
            leaf_only = False
        if('non_leaf_only' in kwargs):
            non_leaf_only = kwargs['non_leaf_only']
        else:
            non_leaf_only = False
        locx,locy = tuple(self.path2loc(pl))
        lpls = copy.deepcopy(self.desc[locx][locy]['leaf_son_paths'])
        nlpls = copy.deepcopy(self.desc[locx][locy]['non_leaf_son_paths'])
        if(leaf_only):
            rslt = lpls
        elif(non_leaf_only):
            rslt = nlpls
        else:
            rslt = lpls+nlpls
        rslt,= batsorted(rslt,rslt)
        return(rslt)
    def sons(self,*sibseqs,**kwargs):
        if('pathlist' in kwargs):
            pl = kwargs['pathlist']
        else:
            pl = list(sibseqs)
        if('leaf_only' in kwargs):
            leaf_only = kwargs['leaf_only']
        else:
            leaf_only = False
        if('non_leaf_only' in kwargs):
            non_leaf_only = kwargs['non_leaf_only']
        else:
            non_leaf_only = False
        locx,locy = tuple(self.path2loc(pl))
        lpls = copy.deepcopy(self.desc[locx][locy]['leaf_son_paths'])
        nlpls = copy.deepcopy(self.desc[locx][locy]['non_leaf_son_paths'])
        if(leaf_only):
            rslt = lpls
        elif(non_leaf_only):
            rslt = nlpls
        else:
            rslt = lpls+nlpls
        rslt,= batsorted(rslt,rslt)
        rslt = array_map(rslt,getitem_via_pathlist2,self.list)
        return(rslt)
    def descendant_paths(self,*sibseqs,**kwargs):
        if('pathlist' in kwargs):
            pl = kwargs['pathlist']
        else:
            pl = list(sibseqs)
        if('leaf_only' in kwargs):
            leaf_only = kwargs['leaf_only']
        else:
            leaf_only = False
        if('non_leaf_only' in kwargs):
            non_leaf_only = kwargs['non_leaf_only']
        else:
            non_leaf_only = False
        if('from_lv' in kwargs):
            from_lv = kwargs['from_lv']
        else:
            from_lv = 1
        if('to_lv' in kwargs):
            to_lv = kwargs['to_lv']
        else:
            to_lv = self.depth
        locx,locy = tuple(self.path2loc(pl))
        lpls = copy.deepcopy(self.desc[locx][locy]['leaf_descendant_paths'])
        nlpls = copy.deepcopy(self.desc[locx][locy]['non_leaf_descendant_paths'])
        if(leaf_only):
            rslt = lpls
        elif(non_leaf_only):
            rslt = nlpls
        else:
            rslt = lpls+nlpls
        nrslt = []
        for i in range(0,rslt.__len__()):
            pl = rslt[i]
            length = pl.__len__()
            cond1 = (length >= from_lv)
            cond2 = (length <= to_lv)
            if(cond1 & cond2):
                nrslt.append(pl)
            else:
                pass
        nrslt, = batsorted(nrslt,nrslt)
        return(nrslt)
    def descendants(self,*sibseqs,**kwargs):
        if('pathlist' in kwargs):
            pl = kwargs['pathlist']
        else:
            pl = list(sibseqs)
        if('leaf_only' in kwargs):
            leaf_only = kwargs['leaf_only']
        else:
            leaf_only = False
        if('non_leaf_only' in kwargs):
            non_leaf_only = kwargs['non_leaf_only']
        else:
            non_leaf_only = False
        locx,locy = tuple(self.path2loc(pl))
        lpls = copy.deepcopy(self.desc[locx][locy]['leaf_descendant_paths'])
        nlpls = copy.deepcopy(self.desc[locx][locy]['non_leaf_descendant_paths'])
        if(leaf_only):
            rslt = lpls
        elif(non_leaf_only):
            rslt = nlpls
        else:
            rslt = lpls+nlpls
        if('from_lv' in kwargs):
            from_lv = kwargs['from_lv']
        else:
            from_lv = 1
        if('to_lv' in kwargs):
            to_lv = kwargs['to_lv']
        else:
            to_lv = self.depth
        nrslt = []
        for i in range(0,rslt.__len__()):
            pl = rslt[i]
            length = pl.__len__()
            cond1 = (length >= from_lv)
            cond2 = (length <= to_lv)
            if(cond1 & cond2):
                nrslt.append(pl)
            else:
                pass
        nrslt, = batsorted(nrslt,nrslt)
        nrslt = array_map(nrslt,getitem_via_pathlist2,self.list)
        return(nrslt)
    @classmethod
    def ancestlize(cls,l,**kwargs):
        length = l.__len__()
        if('from_lv' in kwargs):
            from_lv = kwargs['from_lv']
        else:
            from_lv = 1
        if('to_lv' in kwargs):
            to_lv = kwargs['to_lv']
        else:
            to_lv = length - 2
        nrslt = []
        si = from_lv - 1
        ei = to_lv + 1
        for i in range(si,ei):
            pl = l[:(i+1)]
            nrslt.append(pl)
        return(nrslt)
    def ancestor_paths(self,*sibseqs,**kwargs):
        if('pathlist' in kwargs):
            pl = kwargs['pathlist']
        else:
            pl = list(sibseqs)
        if('from_lv' in kwargs):
            from_lv = kwargs['from_lv']
        else:
            from_lv = 1
        if('to_lv' in kwargs):
            to_lv = kwargs['to_lv']
        else:
            to_lv = pl.__len__() - 2
        locx,locy = tuple(self.path2loc(pl))
        p = copy.deepcopy(self.desc[locx][locy]['path'])
        anps = self.ancestlize(p,from_lv=from_lv,to_lv=to_lv)
        return(anps)
    def ancestors(self,*sibseqs,**kwargs):
        if('pathlist' in kwargs):
            pl = kwargs['pathlist']
        else:
            pl = list(sibseqs)
        if('from_lv' in kwargs):
            from_lv = kwargs['from_lv']
        else:
            from_lv = 1
        if('to_lv' in kwargs):
            to_lv = kwargs['to_lv']
        else:
            to_lv = pl.__len__() - 2
        locx,locy = tuple(self.path2loc(pl))
        p = copy.deepcopy(self.desc[locx][locy]['path'])
        anps = self.ancestlize(p,from_lv=from_lv,to_lv=to_lv)
        ans = array_map(anps,getitem_via_pathlist2,self.list)
        return(ans)
    def lsib_path(self,*sibseqs,**kwargs):
        if('pathlist' in kwargs):
            pl = kwargs['pathlist']
        else:
            pl = list(sibseqs)
        if('from_lv' in kwargs):
            from_lv = kwargs['from_lv']
        else:
            from_lv = 1
        if('to_lv' in kwargs):
            to_lv = kwargs['to_lv']
        else:
            to_lv = pl.__len__() - 2
        locx,locy = tuple(self.path2loc(pl))
        lsibp = copy.deepcopy(self.desc[locx][locy]['lsib_path'])
        return(lsibp)
    def lsib(self,*sibseqs,**kwargs):
        if('pathlist' in kwargs):
            pl = kwargs['pathlist']
        else:
            pl = list(sibseqs)
        if('from_lv' in kwargs):
            from_lv = kwargs['from_lv']
        else:
            from_lv = 1
        if('to_lv' in kwargs):
            to_lv = kwargs['to_lv']
        else:
            to_lv = pl.__len__() - 2
        locx,locy = tuple(self.path2loc(pl))
        lsibp = copy.deepcopy(self.desc[locx][locy]['lsib_path'])
        lsibv = getitem_via_pathlist(self.list,lsibp) 
        return(lsibv)
    def rsib_path(self,*sibseqs,**kwargs):
        if('pathlist' in kwargs):
            pl = kwargs['pathlist']
        else:
            pl = list(sibseqs)
        if('from_lv' in kwargs):
            from_lv = kwargs['from_lv']
        else:
            from_lv = 1
        if('to_lv' in kwargs):
            to_lv = kwargs['to_lv']
        else:
            to_lv = pl.__len__() - 2
        locx,locy = tuple(self.path2loc(pl))
        rsibp = copy.deepcopy(self.desc[locx][locy]['rsib_path'])
        return(rsibp)
    def rsib(self,*sibseqs,**kwargs):
        if('pathlist' in kwargs):
            pl = kwargs['pathlist']
        else:
            pl = list(sibseqs)
        if('from_lv' in kwargs):
            from_lv = kwargs['from_lv']
        else:
            from_lv = 1
        if('to_lv' in kwargs):
            to_lv = kwargs['to_lv']
        else:
            to_lv = pl.__len__() - 2
        locx,locy = tuple(self.path2loc(pl))
        rsibp = copy.deepcopy(self.desc[locx][locy]['rsib_path'])
        rsibv = getitem_via_pathlist(self.list,rsibp) 
        return(rsibv)
    def lcin_path(self,*sibseqs,**kwargs):
        if('pathlist' in kwargs):
            pl = kwargs['pathlist']
        else:
            pl = list(sibseqs)
        if('from_lv' in kwargs):
            from_lv = kwargs['from_lv']
        else:
            from_lv = 1
        if('to_lv' in kwargs):
            to_lv = kwargs['to_lv']
        else:
            to_lv = pl.__len__() - 2
        locx,locy = tuple(self.path2loc(pl))
        lcinp = copy.deepcopy(self.desc[locx][locy]['lcin_path'])
        return(lcinp)
    def lcin(self,*sibseqs,**kwargs):
        if('pathlist' in kwargs):
            pl = kwargs['pathlist']
        else:
            pl = list(sibseqs)
        if('from_lv' in kwargs):
            from_lv = kwargs['from_lv']
        else:
            from_lv = 1
        if('to_lv' in kwargs):
            to_lv = kwargs['to_lv']
        else:
            to_lv = pl.__len__() - 2
        locx,locy = tuple(self.path2loc(pl))
        lcinp = copy.deepcopy(self.desc[locx][locy]['lcin_path'])
        lcinv = getitem_via_pathlist(self.list,lcinp) 
        return(lcinv)
    def rcin_path(self,*sibseqs,**kwargs):
        if('pathlist' in kwargs):
            pl = kwargs['pathlist']
        else:
            pl = list(sibseqs)
        if('from_lv' in kwargs):
            from_lv = kwargs['from_lv']
        else:
            from_lv = 1
        if('to_lv' in kwargs):
            to_lv = kwargs['to_lv']
        else:
            to_lv = pl.__len__() - 2
        locx,locy = tuple(self.path2loc(pl))
        rcinp = copy.deepcopy(self.desc[locx][locy]['rcin_path'])
        return(rcinp)
    def rcin(self,*sibseqs,**kwargs):
        if('pathlist' in kwargs):
            pl = kwargs['pathlist']
        else:
            pl = list(sibseqs)
        if('from_lv' in kwargs):
            from_lv = kwargs['from_lv']
        else:
            from_lv = 1
        if('to_lv' in kwargs):
            to_lv = kwargs['to_lv']
        else:
            to_lv = pl.__len__() - 2
        locx,locy = tuple(self.path2loc(pl))
        rcinp = copy.deepcopy(self.desc[locx][locy]['rcin_path'])
        rcinv = getitem_via_pathlist(self.list,rcinp) 
        return(rcinv)
    def sib_paths(self,*sibseqs,**kwargs):
        if('pathlist' in kwargs):
            pl = kwargs['pathlist']
        else:
            pl = list(sibseqs)
        if('leaf_only' in kwargs):
            leaf_only = kwargs['leaf_only']
        else:
            leaf_only = False
        if('non_leaf_only' in kwargs):
            non_leaf_only = kwargs['non_leaf_only']
        else:
            non_leaf_only = False
        locx,locy = tuple(self.path2loc(pl))
        ppl = self.desc[locx][locy]['parent_path']
        sibps = self.son_paths(pathlist=ppl,leaf_only=leaf_only,non_leaf_only=non_leaf_only)
        return(sibps)
    def sibs(self,*sibseqs,**kwargs):
        if('pathlist' in kwargs):
            pl = kwargs['pathlist']
        else:
            pl = list(sibseqs)
        if('leaf_only' in kwargs):
            leaf_only = kwargs['leaf_only']
        else:
            leaf_only = False
        if('non_leaf_only' in kwargs):
            non_leaf_only = kwargs['non_leaf_only']
        else:
            non_leaf_only = False
        locx,locy = tuple(self.path2loc(pl))
        ppl = self.desc[locx][locy]['parent_path']
        sibps = self.son_paths(pathlist=ppl,leaf_only=leaf_only,non_leaf_only=non_leaf_only)
        sibvs = array_map(sibps,getitem_via_pathlist2,self.list)
        return(sibvs)
    def preceding_sib_paths(self,*sibseqs,**kwargs):
        if('pathlist' in kwargs):
            pl = kwargs['pathlist']
        else:
            pl = list(sibseqs)
        if('leaf_only' in kwargs):
            leaf_only = kwargs['leaf_only']
        else:
            leaf_only = False
        if('non_leaf_only' in kwargs):
            non_leaf_only = kwargs['non_leaf_only']
        else:
            non_leaf_only = False
        locx,locy = tuple(self.path2loc(pl))
        ppl = self.desc[locx][locy]['parent_path']
        sibps = self.son_paths(pathlist=ppl,leaf_only=leaf_only,non_leaf_only=non_leaf_only)
        try:
            seq = sibps.index(pl)
        except:
            return(sibps)
        else:
            return(sibps[:seq])
    def preceding_sibs(self,*sibseqs,**kwargs):
        if('pathlist' in kwargs):
            pl = kwargs['pathlist']
        else:
            pl = list(sibseqs)
        if('leaf_only' in kwargs):
            leaf_only = kwargs['leaf_only']
        else:
            leaf_only = False
        if('non_leaf_only' in kwargs):
            non_leaf_only = kwargs['non_leaf_only']
        else:
            non_leaf_only = False
        locx,locy = tuple(self.path2loc(pl))
        ppl = self.desc[locx][locy]['parent_path']
        sibps = self.son_paths(pathlist=ppl,leaf_only=leaf_only,non_leaf_only=non_leaf_only)
        try:
            seq = sibps.index(pl)
        except:
            pre = sibps
        else:
            pre = sibps[:seq]
        sibvs = array_map(pre,getitem_via_pathlist2,self.list)
        return(sibvs)
    def following_sib_paths(self,*sibseqs,**kwargs):
        if('pathlist' in kwargs):
            pl = kwargs['pathlist']
        else:
            pl = list(sibseqs)
        if('leaf_only' in kwargs):
            leaf_only = kwargs['leaf_only']
        else:
            leaf_only = False
        if('non_leaf_only' in kwargs):
            non_leaf_only = kwargs['non_leaf_only']
        else:
            non_leaf_only = False
        locx,locy = tuple(self.path2loc(pl))
        ppl = self.desc[locx][locy]['parent_path']
        sibps = self.son_paths(pathlist=ppl,leaf_only=leaf_only,non_leaf_only=non_leaf_only)
        try:
            seq = sibps.index(pl)
        except:
            follow = sibps
        else:
            follow = sibps[(seq+1):]
        return(follow)
    def following_sibs(self,*sibseqs,**kwargs):
        if('pathlist' in kwargs):
            pl = kwargs['pathlist']
        else:
            pl = list(sibseqs)
        if('leaf_only' in kwargs):
            leaf_only = kwargs['leaf_only']
        else:
            leaf_only = False
        if('non_leaf_only' in kwargs):
            non_leaf_only = kwargs['non_leaf_only']
        else:
            non_leaf_only = False
        locx,locy = tuple(self.path2loc(pl))
        ppl = self.desc[locx][locy]['parent_path']
        sibps = self.son_paths(pathlist=ppl,leaf_only=leaf_only,non_leaf_only=non_leaf_only)
        try:
            seq = sibps.index(pl)
        except:
            follow = sibps
        else:
            follow = sibps[(seq+1):]
        sibvs = array_map(follow,getitem_via_pathlist2,self.list)
        return(sibvs)
    def some_sib_paths(self,*sibseqs,**kwargs):
        if('pathlist' in kwargs):
            pl = kwargs['pathlist']
        else:
            pl = list(sibseqs)
        if('leaf_only' in kwargs):
            leaf_only = kwargs['leaf_only']
        else:
            leaf_only = False
        if('non_leaf_only' in kwargs):
            non_leaf_only = kwargs['non_leaf_only']
        else:
            non_leaf_only = False
        #here "some" mean "seqs"
        some = kwargs['some']
        locx,locy = tuple(self.path2loc(pl))
        ppl = self.desc[locx][locy]['parent_path']
        seq = self.desc[locx][locy]['sib_seq']
        sibps = self.son_paths(pathlist=ppl,leaf_only=leaf_only,non_leaf_only=non_leaf_only)
        #sibps = select_some(sibps,some)
        sibps = select_seqs(sibps,some)
        return(sibps)
    def some_sibs(self,*sibseqs,**kwargs):
        if('pathlist' in kwargs):
            pl = kwargs['pathlist']
        else:
            pl = list(sibseqs)
        if('leaf_only' in kwargs):
            leaf_only = kwargs['leaf_only']
        else:
            leaf_only = False
        if('non_leaf_only' in kwargs):
            non_leaf_only = kwargs['non_leaf_only']
        else:
            non_leaf_only = False
        #here some mean seqs
        some = kwargs['some']
        locx,locy = tuple(self.path2loc(pl))
        ppl = self.desc[locx][locy]['parent_path']
        seq = self.desc[locx][locy]['sib_seq']
        sibps = self.son_paths(pathlist=ppl,leaf_only=leaf_only,non_leaf_only=non_leaf_only)
        #sibps = select_some(sibps,some)
        sibps = select_seqs(sibps,some)
        sibvs = array_map(sibps,getitem_via_pathlist2,self.list)
        return(sibvs)
    def which_sib_path(self,*sibseqs,**kwargs):
        if('pathlist' in kwargs):
            pl = kwargs['pathlist']
        else:
            pl = list(sibseqs)
        if('leaf_only' in kwargs):
            leaf_only = kwargs['leaf_only']
        else:
            leaf_only = False
        if('non_leaf_only' in kwargs):
            non_leaf_only = kwargs['non_leaf_only']
        else:
            non_leaf_only = False
        which = kwargs['which']
        locx,locy = tuple(self.path2loc(pl))
        ppl = self.desc[locx][locy]['parent_path']
        seq = self.desc[locx][locy]['sib_seq']
        sibps = self.son_paths(pathlist=ppl,leaf_only=leaf_only,non_leaf_only=non_leaf_only)
        sibp = sibps[which]
        return(sibp)
    def which_sib(self,*sibseqs,**kwargs):
        if('pathlist' in kwargs):
            pl = kwargs['pathlist']
        else:
            pl = list(sibseqs)
        if('leaf_only' in kwargs):
            leaf_only = kwargs['leaf_only']
        else:
            leaf_only = False
        if('non_leaf_only' in kwargs):
            non_leaf_only = kwargs['non_leaf_only']
        else:
            non_leaf_only = False
        which = kwargs['which']
        locx,locy = tuple(self.path2loc(pl))
        ppl = self.desc[locx][locy]['parent_path']
        seq = self.desc[locx][locy]['sib_seq']
        sibps = self.son_paths(pathlist=ppl,leaf_only=leaf_only,non_leaf_only=non_leaf_only)
        sibp = sibps[which]
        sibv = getitem_via_pathlist(self.list,sibp)
        return(sibv)
    def search(self,value,**kwargs):
        if('leaf_only' in kwargs):
            leaf_only = kwargs['leaf_only']
            prompt = 'leaf_only'
        else:
            leaf_only = False
            prompt = ''
        if('non_leaf_only' in kwargs):
            non_leaf_only = kwargs['non_leaf_only']
            prompt = 'non_leaf_only'
        else:
            non_leaf_only = False
            prompt = ''
        if('from_lv' in kwargs):
            from_lv = kwargs['from_lv']
        else:
            from_lv = 1
        if('to_lv' in kwargs):
            to_lv = kwargs['to_lv']
        else:
            to_lv = self.depth -1
        lpls = copy.deepcopy(self.desc[0][0]['leaf_descendant_paths'])
        nlpls = copy.deepcopy(self.desc[0][0]['non_leaf_descendant_paths'])
        if(leaf_only):
            rslt = lpls
        elif(non_leaf_only):
            rslt = nlpls
        else:
            rslt = lpls+nlpls
        nrslt = []
        for i in range(0,rslt.__len__()):
            pl = rslt[i]
            length = pl.__len__()
            cond1 = (length >= from_lv)
            cond2 = (length <= to_lv)
            v = getitem_via_pathlist(self.list,pl)
            cond3 = (v == value)
            if(cond1 & cond2 & cond3):
                nrslt.append(pl)
            else:
                pass
        showl = array_map(nrslt,pathlist_to_getStr)
        nrslt,showl = batsorted(nrslt,nrslt,showl)
        if(type(value)==type("")):
            vstr = '"' + str(value) + '"'
        else:
            vstr = str(value)
        self.showlog = ['search '+ vstr + ' -'+prompt+' :']
        self.showlog.extend(showl)
        forEach(showl,print)
        return(nrslt)
    def cond_search(self,**kwargs):
        ###
        cond_func = kwargs['cond_func']
        if('cond_func_args' in kwargs):
            cond_func_args = kwargs['cond_func_args']
        else:
            cond_func_args = []
        ###
        if('leaf_only' in kwargs):
            leaf_only = kwargs['leaf_only']
            prompt = 'leaf_only'
        else:
            leaf_only = False
            prompt = ''
        if('non_leaf_only' in kwargs):
            non_leaf_only = kwargs['non_leaf_only']
            prompt = 'non_leaf_only'
        else:
            non_leaf_only = False
            prompt = ''
        if('from_lv' in kwargs):
            from_lv = kwargs['from_lv']
        else:
            from_lv = 1
        if('to_lv' in kwargs):
            to_lv = kwargs['to_lv']
        else:
            to_lv = self.depth -1
        lpls = copy.deepcopy(self.desc[0][0]['leaf_descendant_paths'])
        nlpls = copy.deepcopy(self.desc[0][0]['non_leaf_descendant_paths'])
        if(leaf_only):
            rslt = lpls
        elif(non_leaf_only):
            rslt = nlpls
        else:
            rslt = lpls+nlpls
        nrslt = []
        nvs = []
        for i in range(0,rslt.__len__()):
            pl = rslt[i]
            length = pl.__len__()
            cond1 = (length >= from_lv)
            cond2 = (length <= to_lv)
            v = getitem_via_pathlist(self.list,pl)
            cond3 = cond_func(v,pl,*cond_func_args)
            if(cond1 & cond2 & cond3):
                nrslt.append(pl)
                nvs.append(v)
            else:
                pass
        def showlog_append(ele1,ele2,*args):
            return(ele1 + ' : ' + str(ele2))
        showl = array_map(nrslt,pathlist_to_getStr)
        showl2 = array_map2(showl,nvs,map_func=showlog_append)
        nrslt,showl = batsorted(nrslt,nrslt,showl)
        func_name = cond_func.__name__
        vstr = 'ele_value,ele_pathlist,' +str(cond_func_args)[1:-1]
        vstr = func_name + '(' + vstr + ')'
        self.showlog = ['search '+ vstr + ' -'+prompt+' :']
        self.showlog.extend(showl2)
        forEach(showl,print)
        return(nrslt)



##two list

def find_fst_cmmnval_index(l0,l1,**kwargs):
    '''
        l0 =         [[2, 0], [1, 2], [0, 0]]
        l1 = [[3, 0], [2, 0], [1, 2], [0, 0]]
        find_fst_cmmnval_index(l0,l1,reverse=True)
        (0,1)
        l0 = [1,2,33,4]
        l1 = [11,22,33]
        find_fst_cmmnval_index(l0,l1)
        (2,2)
    '''
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



def find_fst_cmmnval(l0,l1,**kwargs):
    rslt = find_fst_cmmnval_index(l0,l1,**kwargs)
    rslt = None if(rslt==None) else l0[rslt[0]]
    return(rslt)


######

def find_fst_indexpair_fstltsnd_via_reversing(arr):
    lngth = len(arr)
    for snd in range(lngth-1,0,-1):
        fst = snd - 1
        if(arr[fst]<arr[snd]):
            return((fst,snd))
        else:
            pass
    return(None)

def find_fst_valuepair_fstltsnd_via_reversing(arr):
    lngth = len(arr)
    for snd in range(lngth-1,0,-1):
        fst = snd - 1
        if(arr[fst]<arr[snd]):
            return((arr[fst],arr[snd]))
        else:
            pass
    return(None)



def find_fst_indexpair_fstgtsnd_via_reversing(arr):
    lngth = len(arr)
    for snd in range(lngth-1,0,-1):
        fst = snd - 1
        if(arr[fst]>arr[snd]):
            return((fst,snd))
        else:
            pass
    return(None)

def find_fst_valuepair_fstgtsnd_via_reversing(arr):
    lngth = len(arr)
    for snd in range(lngth-1,0,-1):
        fst = snd - 1
        if(arr[fst]>arr[snd]):
            return((arr[fst],arr[snd]))
        else:
            pass
    return(None)



def swap(i,j,arr):
    tmp = arr[i]
    arr[i] = arr[j]
    arr[j] = tmp
    return(arr)

######




#elelist


def el2iteml(el,k):
    iteml = elel.mapv(el,lambda ele:ele.__getitem__(k))
    return(iteml)

def el2attrl(el,attr):
    attrl = elel.mapv(el,lambda ele:ele.__getattribute__(attr))
    return(attrl)

