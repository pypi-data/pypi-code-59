from .cmmn import inplace_wrapper

@inplace_wrapper
def mapfivo(ol,map_funcs,map_func_other_args_array,**kwargs):
    lngth = ol.__len__()
    rslt = []
    for i in range(0,lngth):
        index = i
        value = ol[i]
        map_func = map_funcs[i]
        other_args = map_func_other_args_array[i]
        ele = map_func(index,value,*other_args)
        rslt.append(ele)
    return(rslt)    


@inplace_wrapper
def mapfiv(ol,map_funcs,*other_args,**kwargs):
    lngth = ol.__len__()
    other_args = list(other_args)
    rslt = []
    for i in range(0,lngth):
        index = i
        value = ol[i]
        map_func = map_funcs[i]
        ele = map_func(index,value,*other_args)
        rslt.append(ele)
    return(rslt)


@inplace_wrapper
def mapfio(ol,map_funcs,map_func_other_args_array,**kwargs):
    lngth = ol.__len__()
    rslt = []
    for i in range(0,lngth):
        index = i
        map_func = map_funcs[i]
        other_args = map_func_other_args_array[i]
        ele = map_func(index,*other_args)
        rslt.append(ele)
    return(rslt)


@inplace_wrapper
def mapfvo(ol,map_funcs,map_func_other_args_array,**kwargs):
    lngth = ol.__len__()
    rslt = []
    for i in range(0,lngth):
        value = ol[i]
        map_func = map_funcs[i]
        other_args = map_func_other_args_array[i]
        ele = map_func(value,*other_args)
        rslt.append(ele)
    return(rslt)


@inplace_wrapper
def mapivo(ol,map_func,map_func_other_args_array,**kwargs):
    lngth = ol.__len__()
    map_func = map_func
    rslt = []
    for i in range(0,lngth):
        index = i
        value = ol[i]
        other_args = map_func_other_args_array[i]
        ele = map_func(index,value,*other_args)
        rslt.append(ele)
    return(rslt)


@inplace_wrapper
def mapfio(ol,map_funcs,map_func_other_args_array,**kwargs):
    lngth = ol.__len__()
    rslt = []
    for i in range(0,lngth):
        index = i
        map_func = map_funcs[i]
        other_args = map_func_other_args_array[i]
        ele = map_func(index,*other_args)
        rslt.append(ele)
    return(rslt)


@inplace_wrapper
def mapfi(ol,map_funcs,*other_args,**kwargs):
    lngth = ol.__len__()
    other_args = list(other_args)
    rslt = []
    for i in range(0,lngth):
        index = i
        map_func = map_funcs[i]
        ele = map_func(index,*other_args)
        rslt.append(ele)
    return(rslt)


@inplace_wrapper
def mapfv(ol,map_funcs,*other_args,**kwargs):
    lngth = ol.__len__()
    other_args = list(other_args)
    rslt = []
    for i in range(0,lngth):
        value = ol[i]
        map_func = map_funcs[i]
        ele = map_func(value,*other_args)
        rslt.append(ele)
    return(rslt)


@inplace_wrapper
def mapfo(ol,map_funcs,map_func_other_args_array,**kwargs):
    lngth = ol.__len__()
    rslt = []
    for i in range(0,lngth):
        map_func = map_funcs[i]
        other_args = map_func_other_args_array[i]
        ele = map_func(*other_args)
        rslt.append(ele)
    return(rslt)


@inplace_wrapper
def mapiv(ol,map_func,*other_args,**kwargs):
    lngth = ol.__len__()
    other_args = list(other_args)
    rslt = []
    for i in range(0,lngth):
        index = i
        value = ol[i]
        ele = map_func(index,value,*other_args)
        rslt.append(ele)
    return(rslt)


@inplace_wrapper
def mapio(ol,map_func,map_func_other_args_array,**kwargs):
    lngth = ol.__len__()
    rslt = []
    for i in range(0,lngth):
        index = i
        other_args = map_func_other_args_array[i]
        ele = map_func(index,*other_args)
        rslt.append(ele)
    return(rslt)

@inplace_wrapper
def mapvo(ol,map_func,map_func_other_args_array,**kwargs):
    lngth = ol.__len__()
    rslt = []
    for i in range(0,lngth):
        value = ol[i]
        other_args = map_func_other_args_array[i]
        ele = map_func(value,*other_args)
        rslt.append(ele)
    return(rslt)


@inplace_wrapper
def mapf(ol,map_funcs,*other_args,**kwargs):
    lngth = ol.__len__()
    other_args = list(other_args)
    rslt = []
    for i in range(0,lngth):
        map_func = map_funcs[i]
        ele = map_func(*other_args)
        rslt.append(ele)
    return(rslt)


@inplace_wrapper
def mapi(ol,map_func,*other_args,**kwargs):
    lngth = ol.__len__()
    other_args = list(other_args)
    rslt = []
    for i in range(0,lngth):
        index = i
        ele = map_func(index,*other_args)
        rslt.append(ele)
    return(rslt)


@inplace_wrapper
def mapv(ol,map_func,*other_args,**kwargs):
    lngth = ol.__len__()
    other_args = list(other_args)
    rslt = []
    for i in range(0,lngth):
        value = ol[i]
        ele = map_func(value,*other_args)
        rslt.append(ele)
    return(rslt)


@inplace_wrapper
def mapo(ol,map_func,map_func_other_args_array,**kwargs):
    lngth = ol.__len__()
    rslt = []
    for i in range(0,lngth):
        other_args = map_func_other_args_array[i]
        ele = map_func(*other_args)
        rslt.append(ele)
    return(rslt)


@inplace_wrapper
def mapiv_with_dual(ol,map_func,index_map_func,map_func_other_args,index_map_func_other_args,**kwargs):
    lngth = ol.__len__()
    rslt = []
    for i in range(0,lngth):
        index = index_map_func(i,*index_map_func_other_args)
        value = map_func(index,ol[i],*_map_func_other_args)
        rslt.append(value)
    return(rslt)


def for_eachfivo(ol,for_each_funcs,for_each_func_other_args_array):
    lngth = ol.__len__()
    for i in range(0,lngth):
        index = i
        value = ol[i]
        for_each_func = for_each_funcs[i]
        other_args = for_each_func_other_args_array[i]
        value = for_each_func(index,value,*other_args)
        ol[i] = value
    return(ol)

def for_eachfiv(ol,for_each_funcs,*other_args):
    lngth = ol.__len__()
    other_args = list(other_args)
    for i in range(0,lngth):
        index = i
        value = ol[i]
        for_each_func = for_each_funcs[i]
        value = for_each_func(index,value,*other_args)
        ol[i] = value
    return(ol)

def for_eachfio(ol,for_each_funcs,for_each_func_other_args_array):
    lngth = ol.__len__()
    for i in range(0,lngth):
        index = i
        for_each_func = for_each_funcs[i]
        other_args = for_each_func_other_args_array[i]
        value = for_each_func(index,*other_args)
        ol[i] = value
    return(ol)

def for_eachfvo(ol,for_each_funcs,for_each_func_other_args_array):
    lngth = ol.__len__()
    for i in range(0,lngth):
        value = ol[i]
        for_each_func = for_each_funcs[i]
        other_args = for_each_func_other_args_array[i]
        value = for_each_func(value,*other_args)
        ol[i] = value
    return(ol)

def for_eachivo(ol,for_each_func,for_each_func_other_args_array):
    lngth = ol.__len__()
    for i in range(0,lngth):
        index = i
        value = ol[i]
        other_args = for_each_func_other_args_array[i]
        value = for_each_func(index,value,*other_args)
        ol[i] = value
    return(ol)

def for_eachfio(ol,for_each_funcs,for_each_func_other_args_array):
    lngth = ol.__len__()
    for i in range(0,lngth):
        index = i
        for_each_func = for_each_funcs[i]
        other_args = for_each_func_other_args_array[i]
        value = for_each_func(index,*other_args)
        ol[i] = value
    return(ol)

def for_eachfi(ol,for_each_funcs,*other_args):
    lngth = ol.__len__()
    other_args = list(other_args)
    for i in range(0,lngth):
        index = i
        for_each_func = for_each_funcs[i]
        value = for_each_func(index,*other_args)
        ol[i] = value
    return(ol)

def for_eachfv(ol,for_each_funcs,*other_args):
    lngth = ol.__len__()
    other_args = list(other_args)
    for i in range(0,lngth):
        value = ol[i]
        for_each_func = for_each_funcs[i]
        value = for_each_func(value,*other_args)
        ol[i] = value
    return(ol)

def for_eachfo(ol,for_each_funcs,for_each_func_other_args_array):
    lngth = ol.__len__()
    for i in range(0,lngth):
        for_each_func = for_each_funcs[i]
        other_args = for_each_func_other_args_array[i]
        value = for_each_func(*other_args)
        ol[i] = value
    return(ol)

def for_eachiv(ol,for_each_func,*other_args):
    lngth = ol.__len__()
    other_args = list(other_args)
    for i in range(0,lngth):
        index = i
        value = ol[i]
        value = for_each_func(index,value,*other_args)
        ol[i] = value
    return(ol)

def for_eachio(ol,for_each_func,for_each_func_other_args_array):
    lngth = ol.__len__()
    for i in range(0,lngth):
        index = i
        other_args = for_each_func_other_args_array[i]
        value = for_each_func(index,*other_args)
        ol[i] = value
    return(ol)

def for_eachvo(ol,for_each_func,for_each_func_other_args_array):
    lngth = ol.__len__()
    for i in range(0,lngth):
        value = ol[i]
        other_args = for_each_func_other_args_array[i]
        value = for_each_func(value,*other_args)
        ol[i] = value
    return(ol)

def for_eachf(ol,for_each_funcs,*other_args):
    lngth = ol.__len__()
    other_args = list(other_args)
    for i in range(0,lngth):
        for_each_func = for_each_funcs[i]
        value = for_each_func(*other_args)
        ol[i] = value
    return(ol)

def for_eachi(ol,for_each_func,*other_args):
    lngth = ol.__len__()
    other_args = list(other_args)
    for i in range(0,lngth):
        index = i
        value = for_each_func(index,*other_args)
        ol[i] = value
    return(ol)

def for_eachv(ol,for_each_func,*other_args):
    lngth = ol.__len__()
    other_args = list(other_args)
    for i in range(0,lngth):
        value = ol[i]
        value = for_each_func(value,*other_args)
        ol[i] = value
    return(ol)

def for_eacho(ol,for_each_func,for_each_func_other_args_array):
    lngth = ol.__len__()
    for i in range(0,lngth):
        other_args = for_each_func_other_args_array[i]
        value = for_each_func(*other_args)
        ol[i] = value
    return(ol)

def for_eachiv_with_dual(ol,for_each_func,index_for_each_func,for_each_func_other_args,index_for_each_func_other_args):
    lngth = ol.__len__()
    for i in range(0,lngth):
        index = index_for_each_func(i,*index_for_each_func_other_args)
        value = for_each_func(index,ol[i],*_for_each_func_other_args)
        ol[i] = value
    return(ol)


@inplace_wrapper
def intlize(ol):
    return(list(map(lambda ele:int(ele),ol)))

@inplace_wrapper
def strlize(ol):
    return(list(map(lambda ele:str(ele),ol)))




def el2iteml(el,k):
    iteml = list(map(lambda ele:ele.__getitem__(k),el))
    return(iteml)

def el2attrl(el,attr):
    attrl = list(map(lambda ele:ele.__getattribute__(attr),el))
    return(attrl)




def reduce_left(ol,callback,initialValue):
    length = ol.__len__()
    accumulator = initialValue
    for i in range(0,length):
        accumulator = callback(accumulator,ol[i])
    return(accumulator)


def reduce_right(ol,callback,initialValue):
    length = ol.__len__()
    accumulator = initialValue
    for i in range(length-1,-1,-1):
        accumulator = callback(accumulator,ol[i])
    return(accumulator)


