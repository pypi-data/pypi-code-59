import copy
from operator import itemgetter
from .cmmn import inplace_wrapper
from .map import mapv


@inplace_wrapper
def sort(ol,**kwargs):
    ol.sort()
    return(ol)



@inplace_wrapper
def sort_refer_to(l,referer,reverse=False,**kwargs):
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



def sort_sublist(ol,sub):
    def cond_func(ele,ol):
        index = ol.index(ele)
        return(index)
    indexes = mapv(sub,cond_func,ol)
    nsub = sort_refer_to(sub,indexes)['list']
    return(nsub)


def bat_sort(referer,*lists,**kwargs):
    if('reverse' in kwargs):
        reverse = kwargs['reverse']
    else:
        reverse = False
    length = referer.__len__()
    indexes = list(range(0,length))
    rslt = sort_refer_to(indexes,referer,reverse=reverse)
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



def sort_dtb(dtb,*cond_keys,**kwargs):
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
    keys = cond_keys
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
    ndl = dtb
    ndl = sorted(ndl,key=functools.cmp_to_key(cmp_dict),reverse=reverse)
    return(ndl)



