
def fltrfivo(ol,fltr_funcs,fltr_func_other_args_array):
    lngth = ol.__len__()
    rslt = []
    for i in range(0,lngth):
        index = i
        value = ol[i]
        fltr_func = fltr_funcs[i]
        other_args = fltr_func_other_args_array[i]
        cond = fltr_func(index,value,*other_args)
        if(cond):
            rslt.append(ol[i])
        else:
            pass
    return(rslt)    



def fltrfiv(ol,fltr_funcs,*other_args):
    lngth = ol.__len__()
    other_args = list(other_args)
    rslt = []
    for i in range(0,lngth):
        index = i
        value = ol[i]
        fltr_func = fltr_funcs[i]
        cond = fltr_func(index,value,*other_args)
        if(cond):
            rslt.append(ol[i])
        else:
            pass
    return(rslt)


def fltrfio(ol,fltr_funcs,fltr_func_other_args_array):
    lngth = ol.__len__()
    rslt = []
    for i in range(0,lngth):
        index = i
        fltr_func = fltr_funcs[i]
        other_args = fltr_func_other_args_array[i]
        cond = fltr_func(index,*other_args)
        if(cond):
            rslt.append(ol[i])
        else:
            pass
    return(rslt)



def fltrfvo(ol,fltr_funcs,fltr_func_other_args_array):
    lngth = ol.__len__()
    rslt = []
    for i in range(0,lngth):
        value = ol[i]
        fltr_func = fltr_funcs[i]
        other_args = fltr_func_other_args_array[i]
        cond = fltr_func(value,*other_args)
        if(cond):
            rslt.append(ol[i])
        else:
            pass
    return(rslt)


def fltrivo(ol,fltr_func,fltr_func_other_args_array):
    lngth = ol.__len__()
    fltr_func = fltr_func
    rslt = []
    for i in range(0,lngth):
        index = i
        value = ol[i]
        other_args = fltr_func_other_args_array[i]
        cond = fltr_func(index,value,*other_args)
        if(cond):
            rslt.append(ol[i])
        else:
            pass
    return(rslt)



def fltrfio(ol,fltr_funcs,fltr_func_other_args_array):
    lngth = ol.__len__()
    rslt = []
    for i in range(0,lngth):
        index = i
        fltr_func = fltr_funcs[i]
        other_args = fltr_func_other_args_array[i]
        cond = fltr_func(index,*other_args)
        if(cond):
            rslt.append(ol[i])
        else:
            pass
    return(rslt)



def fltrfi(ol,fltr_funcs,*other_args):
    lngth = ol.__len__()
    other_args = list(other_args)
    rslt = []
    for i in range(0,lngth):
        index = i
        fltr_func = fltr_funcs[i]
        cond = fltr_func(index,*other_args)
        if(cond):
            rslt.append(ol[i])
        else:
            pass
    return(rslt)



def fltrfv(ol,fltr_funcs,*other_args):
    lngth = ol.__len__()
    other_args = list(other_args)
    rslt = []
    for i in range(0,lngth):
        value = ol[i]
        fltr_func = fltr_funcs[i]
        cond = fltr_func(value,*other_args)
        if(cond):
            rslt.append(ol[i])
        else:
            pass
    return(rslt)



def fltrfo(ol,fltr_funcs,fltr_func_other_args_array):
    lngth = ol.__len__()
    rslt = []
    for i in range(0,lngth):
        fltr_func = fltr_funcs[i]
        other_args = fltr_func_other_args_array[i]
        cond = fltr_func(*other_args)
        if(cond):
            rslt.append(ol[i])
        else:
            pass
    return(rslt)



def fltriv(ol,fltr_func,*other_args):
    lngth = ol.__len__()
    other_args = list(other_args)
    rslt = []
    for i in range(0,lngth):
        index = i
        value = ol[i]
        cond = fltr_func(index,value,*other_args)
        if(cond):
            rslt.append(ol[i])
        else:
            pass
    return(rslt)



def fltrio(ol,fltr_func,fltr_func_other_args_array):
    lngth = ol.__len__()
    rslt = []
    for i in range(0,lngth):
        index = i
        other_args = fltr_func_other_args_array[i]
        cond = fltr_func(index,*other_args)
        if(cond):
            rslt.append(ol[i])
        else:
            pass
    return(rslt)


def fltrvo(ol,fltr_func,fltr_func_other_args_array):
    lngth = ol.__len__()
    rslt = []
    for i in range(0,lngth):
        value = ol[i]
        other_args = fltr_func_other_args_array[i]
        cond = fltr_func(value,*other_args)
        if(cond):
            rslt.append(ol[i])
        else:
            pass
    return(rslt)



def fltrf(ol,fltr_funcs,*other_args):
    lngth = ol.__len__()
    other_args = list(other_args)
    rslt = []
    for i in range(0,lngth):
        fltr_func = fltr_funcs[i]
        cond = fltr_func(*other_args)
        if(cond):
            rslt.append(ol[i])
        else:
            pass
    return(rslt)



def fltri(ol,fltr_func,*other_args):
    lngth = ol.__len__()
    other_args = list(other_args)
    rslt = []
    for i in range(0,lngth):
        index = i
        cond = fltr_func(index,*other_args)
        if(cond):
            rslt.append(ol[i])
        else:
            pass
    return(rslt)


def fltrv(ol,fltr_func,*other_args):
    lngth = ol.__len__()
    other_args = list(other_args)
    rslt = []
    for i in range(0,lngth):
        value = ol[i]
        cond = fltr_func(value,*other_args)
        if(cond):
            rslt.append(ol[i])
        else:
            pass
    return(rslt)



def fltro(ol,fltr_func,fltr_func_other_args_array):
    lngth = ol.__len__()
    rslt = []
    for i in range(0,lngth):
        other_args = fltr_func_other_args_array[i]
        cond = fltr_func(*other_args)
        if(cond):
            rslt.append(ol[i])
        else:
            pass
    return(rslt)


def fltriv_with_dual(ol,fltr_func,index_fltr_func,fltr_func_other_args,index_fltr_func_other_args):
    lngth = ol.__len__()
    rslt = []
    for i in range(0,lngth):
        index = index_fltr_func(i,*index_fltr_func_other_args)
        value = fltr_func(index,ol[i],*_fltr_func_other_args)
        if(cond):
            rslt.append(ol[i])
        else:
            pass
    return(rslt)



####
def lngth_lt(ol,lngth):
    return(fltrv(ol,lambda v:len(v)<lngth))

def lngth_le(ol,lngth):
    return(fltrv(ol,lambda v:len(v)<=lngth))

def lngth_eq(ol,lngth):
    return(fltrv(ol,lambda v:len(v)==lngth))

def lngth_ge(ol,lngth):
    return(fltrv(ol,lambda v:len(v)>=lngth))

def lngth_gt(ol,lngth):
    return(fltrv(ol,lambda v:len(v)>lngth))


