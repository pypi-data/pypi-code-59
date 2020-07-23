import copy
from .cmmn  import inplace_wrapper
from .index import uniform_index,indexes_all,indexes_some
from .sort  import sort_refer_to
from .map   import mapv
from .fltr  import fltrv
from .slct  import some_keeping_order,some
from .init  import from_range,init


@inplace_wrapper
def append(ol,ele,**kwargs):
    ol.append(ele)
    return(ol)


@inplace_wrapper
def push(ol,ele,**kwargs):
    ol.append(ele)
    return(ol)


@inplace_wrapper
def append_some(ol,*eles,**kwargs):
    return(extend(ol,list(eles),**kwargs))


@inplace_wrapper
def prepend(ol,ele,**kwargs):
    new = [ele]
    new.extend(ol)
    return(new)


@inplace_wrapper
def extend(ol,nl,**kwargs):
    ol.extend(nl)
    return(ol)

@inplace_wrapper
def prextend(ol,nl,**kwargs):
    nl.extend(ol)
    return(nl)

@inplace_wrapper
def prepend_some(ol,*eles,**kwargs):
    return(prextend(ol,list(eles),**kwargs))


@inplace_wrapper
def unshift(ol,*eles,**kwargs):
    return(prextend(ol,list(eles),**kwargs))


@inplace_wrapper
def concat(*arrays,**kwargs):
    new = []
    length = arrays.__len__()
    for i in range(0,length):
        array = arrays[i]
        new.extend(array)
    return(new)

@inplace_wrapper
def cons(head_ele,l,**kwargs):
    return(prepend(l,head_ele,**kwargs))


@inplace_wrapper
def insert(ol,start_index,ele,**kwargs):
    ol.insert(start_index,ele)
    return(ol)


@inplace_wrapper
def insert_some(ol,start_index,*eles,**kwargs):
    start_index = kwargs['index']
    length = ol.__len__()
    si = uniform_index(start_index,length)
    new = ol[0:si]
    new.extend(list(eles))
    new.extend(cpol[si:])
    return(new)


def insert_many(ol,eles,locs,**kwargs):
    if('mode' in kwargs):
        mode = kwargs["mode"]
    else:
        mode = "deepcopy"
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
    tmp = sort_refer_to(eles,locs)
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
    if(mode == "deepcopy"):
        return(new)
    else:
        ol.clear()
        ol.extend(new)
        return(ol)



def insert_section(ol,sec,loc,**kwargs):
    if('mode' in kwargs):
        mode = kwargs["mode"]
    else:
        mode = "deepcopy"
    secs = [sec]
    locs = [loc]
    return(insert_sections_many(ol,secs,locs,mode=mode))




def insert_sections_some(ol,*secs,**kwargs):
    if('mode' in kwargs):
        mode = kwargs["mode"]
    else:
        mode = "deepcopy"
    loc = kwargs['index']
    secs = list(secs)
    secs = [concat(*secs)]
    locs = [loc]
    return(insert_sections_many(ol,secs,locs,mode=mode))


def insert_sections_many(ol,secs,locs,**kwargs):
    if('mode' in kwargs):
        mode = kwargs["mode"]
    else:
        mode = "deepcopy"
    secs = copy.deepcopy(secs)
    locs = copy.deepcopy(locs)
    brked = broke_via_seqs(ol,locs)
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
    if(mode == "deepcopy"):
        return(new)
    else:
        ol.clear()
        ol.extend(new)
        return(ol)


def repeat_every(l,times):
    nl = []
    for i in range(0,l.__len__()):
        for j in range(0,times):
            nl.append(l[i])
    return(nl)



def apadding(l,lngth,val):
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




#####
#####

def pop(ol,index,**kwargs):
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

def shift(ol,**kwargs):
    if('mode' in kwargs):
        mode = kwargs['mode']
    else:
        mode = "new"
    length = ol.__len__()
    rslt = pop(ol,0,mode=mode)
    return(rslt)



def cond_pop(ol,index,**kwargs):
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



def pop_range(ol,start_index,end_index,**kwargs):
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


def another_pop_some(l,*seqs):
    seqs = list(seqs)
    seqs = sorted(seqs)
    count = 0
    for i in range(0,seqs.__len__()):
        seq = seqs[i]
        seq = seq -count
        l.pop(seq)
        count = count + 1
    return(l)



#####
#####


def rm_fst(ol,value,**kwargs):
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


def rm_fst_not(ol,value,**kwargs):
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


def rm_lst(ol,value,**kwargs):
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




def rm_lst_not(ol,value,**kwargs):
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


def rm_which(ol,value,which,**kwargs):
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



def rm_which_not(ol,value,which,**kwargs):
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


def rm_some(ol,value,*seqs,**kwargs):
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

def rm_some_not(ol,value,*seqs,**kwargs):
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


def rm_all(ol,value,**kwargs):
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



def rm_all_not(ol,value,**kwargs):
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



def rm_many(ol,values,seqs,**kwargs):
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



def rm_many_not(ol,values,seqs,**kwargs):
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



@inplace_wrapper
def reverse(ol,**kwargs):
    ol.reverse()
    return(ol)




def splice(ol,start,deleteCount,*eles,**kwargs):
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
        arr = fltrv(ol,test_func,gnum,i)
        rslt.append(arr)
    return(rslt)


def split(ol,value,*whiches,**kwargs):
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
        indexes = some(indexes,*whiches)
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



#####
#####

def repl_some(ol,value,*indexes,**kwargs):
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


def repl_some_eq(ol,src_value,dst_value,*seqs,**kwargs):
    if('mode' in kwargs):
        mode = kwargs["mode"]
    else:
        mode = "new"
    indexes = indexes_some(ol,src_value,*list(seqs))
    return(replace_some(ol,dst_value,*indexes,mode=mode))



def repl_fst_eq(ol,src_value,dst_value,**kwargs):
    return(repl_some_eq(ol,src_value,dst_value,0,**kwargs))

def repl_lst_eq(ol,src_value,dst_value,**kwargs):
    return(repl_some_eq(ol,src_value,dst_value,-1,**kwargs))


def repl_which_eq(ol,src_value,dst_value,which,**kwargs):
    return(repl_some_eq(ol,src_value,dst_value,which,**kwargs))


def repl_all_eq(ol,src_value,dst_value,**kwargs):
    for i in range(len(ol)):
        if(ol[i] == src_value):
            ol[i] = dst_value
        else:
            pass
    return(ol)


def cond_repl_some(ol,cond_func,dst_value,*seqs,**kwargs):
    other_args = kwargs['cond_func_other_args'] if('cond_func_other_args' in kwargs) else []
    for i in range(len(ol)):
        cond0 = cond_func(i,ol[i],*other_args)  
        cond1 = (i in list(seqs))
        cond = (cond0 and cond1)
        if(cond):
            ol[i] = dst_value
        else:    
            pass
    return(ol)


def cond_repl_which(ol,cond_func,dst_value,which,**kwargs):
    return(cond_repl_some(ol,cond_func,dst_value,which,**kwargs))



def cond_repl_fst(ol,cond_func,dst_value,**kwargs):
    return(cond_repl_some(ol,cond_func,dst_value,0,**kwargs))


def cond_repl_lst(ol,cond_func,dst_value,**kwargs):
    other_args = kwargs['cond_func_other_args'] if('cond_func_other_args' in kwargs) else []
    lst_index = None
    for i in range(len(ol)-1,-1,-1):
        cond0 = cond_func(i,ol[i],*other_args)
        cond1 = (i in list(seqs))
        cond = (cond0 and cond1)
        if(cond):
            lst_index = i
            break
        else:
            pass
    if(lst_index != None):
        ol[lst_index] = dst_value
    else:
        pass
    return(ol)


def cond_repl_all(ol,cond_func,dst_value,**kwargs):
    other_args = kwargs['cond_func_other_args'] if('cond_func_other_args' in kwargs) else []
    for i in range(len(ol)):
        cond = cond_func(i,ol[i],*other_args)
        if(cond):
            ol[i] = dst_value
        else:
            pass
    return(ol)


