from .cmmn import null,undefined


def find_fst_iv(ol,test_func,*args):
    length = ol.__len__()
    for i in range(0,length):
        cond = test_func(ol[i],*args)
        if(cond):
            return({'index':i,'value':ol[i]})
        else:
            pass
    return(null)


def find_fst_v(ol,test_func,*args):
    length = ol.__len__()
    for i in range(0,length):
        cond = test_func(ol[i],*args)
        if(cond):
            return(ol[i])
        else:
            pass
    return(null)


def find_fst_i(ol,test_func,*args):
    length = ol.__len__()
    for i in range(0,length):
        cond = test_func(ol[i],*args)
        if(cond):
            return(i)
        else:
            pass
    return(null)



def find_fst_not_iv(ol,test_func,*args):
    length = ol.__len__()
    for i in range(0,length):
        cond = test_func(ol[i],*args)
        if(not(cond)):
            return({'index':i,'value':ol[i]})
        else:
            pass
    return(null)


def find_fst_not_v(ol,test_func,*args):
    length = ol.__len__()
    for i in range(0,length):
        cond = test_func(ol[i],*args)
        if(not(cond)):
            return(ol[i])
        else:
            pass
    return(null)


def find_fst_not_i(ol,test_func,*args):
    length = ol.__len__()
    for i in range(0,length):
        cond = test_func(ol[i],*args)
        if(not(cond)):
            return(i)
        else:
            pass
    return(null)



def find_lst_iv(ol,test_func,*args):
    length = ol.__len__()
    for i in range(length-1,-1,-1):
        cond = test_func(ol[i],*args)
        if(cond):
            return({'index':i,'value':ol[i]})
        else:
            pass
    return(null)



def find_lst_i(ol,test_func,*args):
    length = ol.__len__()
    for i in range(length-1,-1,-1):
        cond = test_func(ol[i],*args)
        if(cond):
            return(i)
        else:
            pass
    return(null)



def find_lst_v(ol,test_func,*args):
    length = ol.__len__()
    for i in range(length-1,-1,-1):
        cond = test_func(ol[i],*args)
        if(cond):
            return(ol[i])
        else:
            pass
    return(null)


def find_lst_not_iv(ol,test_func,*args):
    length = ol.__len__()
    for i in range(length-1,-1,-1):
        cond = test_func(ol[i],*args)
        if(not(cond)):
            return({'index':i,'value':ol[i]})
        else:
            pass
    return(null)



def find_lst_not_i(ol,test_func,*args):
    length = ol.__len__()
    for i in range(length-1,-1,-1):
        cond = test_func(ol[i],*args)
        if(not(cond)):
            return(i)
        else:
            pass
    return(null)



def find_lst_not_v(ol,test_func,*args):
    length = ol.__len__()
    for i in range(length-1,-1,-1):
        cond = test_func(ol[i],*args)
        if(not(cond)):
            return(ol[i])
        else:
            pass
    return(null)


###
def find_which_iv(ol,test_func,which,*args):
    length = ol.__len__()
    seq = -1
    for i in range(0,length):
        cond = test_func(ol[i],*args)
        if(cond):
            seq = seq + 1
            if(seq == which):
                return({'index':i,'value':ol[i]})
            else:
                pass
        else:
            pass
    return(null)


def find_which_i(ol,test_func,which,*args):
    rslt = find_which_iv(ol,test_func,which,*args)
    rslt = rslt if(rslt == null) else rslt['index']
    return(rslt)

def find_which_v(ol,test_func,which,*args):
    rslt = find_which_iv(ol,test_func,which,*args)
    rslt = rslt if(rslt == null) else rslt['value']
    return(rslt)



def find_which_not_iv(ol,test_func,which,*args):
    length = ol.__len__()
    seq = -1
    for i in range(0,length):
        cond = not(test_func(ol[i],*args))
        if(cond):
            seq = seq + 1
            if(seq == which):
                return({'index':i,'value':ol[i]})
            else:
                pass
        else:
            pass
    return(null)



def find_which_not_i(ol,test_func,which,*args):
    rslt = find_which_not_iv(ol,test_func,which,*args)
    rslt = rslt if(rslt == null) else rslt['index']
    return(rslt)

def find_which_not_v(ol,test_func,which,*args):
    rslt = find_which_not_iv(ol,test_func,which,*args)
    rslt = rslt if(rslt == null) else rslt['value']
    return(rslt)


def find_some_iv(ol,test_func,*seqs,**kwargs):
    rslt =[]
    seqs = list(seqs)
    length = ol.__len__()
    seq = -1
    other_args = kwargs['other_args'] if('other_args' in kwargs) else []
    for i in range(0,length):
        cond = test_func(ol[i],*other_args)
        if(cond):
            seq = seq + 1
            if(seq in seqs):
                rslt.append({'index':i,'value':ol[i]})
            else:
                pass
        else:
            pass
    return(rslt)


def find_some_i(ol,test_func,*seqs,**kwargs):
    rslt = find_some_iv(ol,test_func,*seqs,**kwargs)
    rslt = list(map(lambda r:r['index'],rslt))
    return(rslt)


def find_some_v(ol,test_func,*seqs,**kwargs):
    rslt = find_some_iv(ol,test_func,*seqs,**kwargs)
    rslt = list(map(lambda r:r['value'],rslt))
    return(rslt)



def find_some_not_iv(ol,test_func,*seqs,**kwargs):
    rslt =[]
    seqs = list(seqs)
    length = ol.__len__()
    seq = -1
    other_args = kwargs['other_args'] if('other_args' in kwargs) else []
    for i in range(0,length):
        cond = not(test_func(ol[i],*other_args))
        if(cond):
            seq = seq + 1
            if(seq in seqs):
                rslt.append({'index':i,'value':ol[i]})
            else:
                pass
        else:
            pass
    return(rslt)


def find_some_not_i(ol,test_func,*seqs,**kwargs):
    rslt = find_some_not_iv(ol,test_func,*seqs,**kwargs)
    rslt = list(map(lambda r:r['index'],rslt))
    return(rslt)


def find_some_not_v(ol,test_func,*seqs,**kwargs):
    rslt = find_some_not_iv(ol,test_func,*seqs,**kwargs)
    rslt = list(map(lambda r:r['value'],rslt))
    return(rslt)



def find_all_iv(ol,test_func,*args):
    rslt =[]
    length = ol.__len__()
    for i in range(0,length):
        cond = test_func(ol[i],*args)
        if(cond):
            rslt.append({'index':i,'value':ol[i]})
        else:
            pass
    return(rslt)


def find_all_i(ol,test_func,*args):
    rslt = find_all_iv(ol,test_func,*args)
    rslt = list(map(lambda r:r['index'],rslt))
    return(rslt)


def find_all_v(ol,test_func,*args):
    rslt = find_all_iv(ol,test_func,*args)
    rslt = list(map(lambda r:r['value'],rslt))
    return(rslt)



def find_all_not_iv(ol,test_func,*args):
    rslt =[]
    length = ol.__len__()
    for i in range(0,length):
        cond = test_func(ol[i],*args)
        if(cond):
            pass
        else:
            rslt.append({'index':i,'value':ol[i]})
    return(rslt)



def find_all_not_i(ol,test_func,*args):
    rslt = find_all_not_iv(ol,test_func,*args)
    rslt = list(map(lambda r:r['index'],rslt))
    return(rslt)


def find_all_not_v(ol,test_func,*args):
    rslt = find_all_not_iv(ol,test_func,*args)
    rslt = list(map(lambda r:r['value'],rslt))
    return(rslt)


############

def find_fst_gt_iv(ol,value):
    test_func = lambda r,v:(r>v)
    rslt = find_fst_iv(ol,test_func,value)
    return(rslt)


def find_fst_gt_i(ol,value):
    test_func = lambda r,v:(r>v)
    rslt = find_fst_i(ol,test_func,value)
    return(rslt)


def find_fst_gt_v(ol,value):
    test_func = lambda r,v:(r>v)
    rslt = find_fst_v(ol,test_func,value)
    return(rslt)


def find_lst_gt_iv(ol,value):
    test_func = lambda r,v:(r>v)
    rslt = find_lst_iv(ol,test_func,value)
    return(rslt)


def find_lst_gt_i(ol,value):
    test_func = lambda r,v:(r>v)
    rslt = find_lst_i(ol,test_func,value)
    return(rslt)


def find_lst_gt_v(ol,value):
    test_func = lambda r,v:(r>v)
    rslt = find_lst_v(ol,test_func,value)
    return(rslt)




def find_which_gt_iv(ol,value):
    test_func = lambda r,v:(r>v)
    rslt = find_which_iv(ol,test_func,which,value)
    return(rslt)


def find_which_gt_i(ol,value):
    test_func = lambda r,v:(r>v)
    rslt = find_which_i(ol,test_func,which,value)
    return(rslt)


def find_which_gt_v(ol,value):
    test_func = lambda r,v:(r>v)
    rslt = find_which_v(ol,test_func,which,value)
    return(rslt)



def find_some_gt_iv(ol,value,*seqs):
    test_func = lambda r,v:(r>v)
    rslt = find_some_iv(ol,test_func,value,*seqs)
    return(rslt)


def find_some_gt_i(ol,value,*seqs):
    test_func = lambda r,v:(r>v)
    rslt = find_some_i(ol,test_func,value,*seqs)
    return(rslt)


def find_some_gt_v(ol,value,*seqs):
    test_func = lambda r,v:(r>v)
    rslt = find_some_v(ol,test_func,value,*seqs)
    return(rslt)



def find_all_gt_iv(ol,value):
    test_func = lambda r,v:(r>v)
    rslt = find_all_iv(ol,test_func,value)
    return(rslt)


def find_all_gt_i(ol,value):
    test_func = lambda r,v:(r>v)
    rslt = find_all_i(ol,test_func,value)
    return(rslt)


def find_all_gt_v(ol,value):
    test_func = lambda r,v:(r>v)
    rslt = find_all_v(ol,test_func,value)
    return(rslt)



def find_fst_lt_iv(ol,value):
    test_func = lambda r,v:(r<v)
    rslt = find_fst_iv(ol,test_func,value)
    return(rslt)


def find_fst_lt_i(ol,value):
    test_func = lambda r,v:(r<v)
    rslt = find_fst_i(ol,test_func,value)
    return(rslt)


def find_fst_lt_v(ol,value):
    test_func = lambda r,v:(r<v)
    rslt = find_fst_v(ol,test_func,value)
    return(rslt)


def find_lst_lt_iv(ol,value):
    test_func = lambda r,v:(r<v)
    rslt = find_lst_iv(ol,test_func,value)
    return(rslt)


def find_lst_lt_i(ol,value):
    test_func = lambda r,v:(r<v)
    rslt = find_lst_i(ol,test_func,value)
    return(rslt)


def find_lst_lt_v(ol,value):
    test_func = lambda r,v:(r<v)
    rslt = find_lst_v(ol,test_func,value)
    return(rslt)


def find_which_lt_iv(ol,value):
    test_func = lambda r,v:(r<v)
    rslt = find_which_iv(ol,test_func,which,value)
    return(rslt)


def find_which_lt_i(ol,value):
    test_func = lambda r,v:(r<v)
    rslt = find_which_i(ol,test_func,which,value)
    return(rslt)


def find_which_lt_v(ol,value):
    test_func = lambda r,v:(r<v)
    rslt = find_which_v(ol,test_func,which,value)
    return(rslt)

def find_some_lt_iv(ol,value,*seqs):
    test_func = lambda r,v:(r<v)
    rslt = find_some_iv(ol,test_func,value,*seqs)
    return(rslt)


def find_some_lt_i(ol,value,*seqs):
    test_func = lambda r,v:(r<v)
    rslt = find_some_i(ol,test_func,value,*seqs)
    return(rslt)


def find_some_lt_v(ol,value,*seqs):
    test_func = lambda r,v:(r<v)
    rslt = find_some_v(ol,test_func,value,*seqs)
    return(rslt)


def find_all_lt_iv(ol,value):
    test_func = lambda r,v:(r<v)
    rslt = find_all_iv(ol,test_func,value)
    return(rslt)


def find_all_lt_i(ol,value):
    test_func = lambda r,v:(r<v)
    rslt = find_all_i(ol,test_func,value)
    return(rslt)


def find_all_lt_v(ol,value):
    test_func = lambda r,v:(r<v)
    rslt = find_all_v(ol,test_func,value)
    return(rslt)




def find_fst_eq_iv(ol,value):
    test_func = lambda r,v:(r==v)
    rseq = find_fst_iv(ol,test_func,value)
    return(rseq)


def find_fst_eq_i(ol,value):
    test_func = lambda r,v:(r==v)
    rseq = find_fst_i(ol,test_func,value)
    return(rseq)


def find_fst_eq_v(ol,value):
    test_func = lambda r,v:(r==v)
    rseq = find_fst_v(ol,test_func,value)
    return(rseq)


def find_lst_eq_iv(ol,value):
    test_func = lambda r,v:(r==v)
    rseq = find_lst_iv(ol,test_func,value)
    return(rseq)


def find_lst_eq_i(ol,value):
    test_func = lambda r,v:(r==v)
    rseq = find_lst_i(ol,test_func,value)
    return(rseq)


def find_lst_eq_v(ol,value):
    test_func = lambda r,v:(r==v)
    rseq = find_lst_v(ol,test_func,value)
    return(rseq)


def find_which_eq_iv(ol,value):
    test_func = lambda r,v:(r==v)
    rseq = find_which_iv(ol,test_func,which,value)
    return(rseq)


def find_which_eq_i(ol,value):
    test_func = lambda r,v:(r==v)
    rseq = find_which_i(ol,test_func,which,value)
    return(rseq)


def find_which_eq_v(ol,value):
    test_func = lambda r,v:(r==v)
    rseq = find_which_v(ol,test_func,which,value)
    return(rseq)

def find_some_eq_iv(ol,value,*seqs):
    test_func = lambda r,v:(r==v)
    rseq = find_some_iv(ol,test_func,value,*seqs)
    return(rseq)


def find_some_eq_i(ol,value,*seqs):
    test_func = lambda r,v:(r==v)
    rseq = find_some_i(ol,test_func,value,*seqs)
    return(rseq)


def find_some_eq_v(ol,value,*seqs):
    test_func = lambda r,v:(r==v)
    rseq = find_some_v(ol,test_func,value,*seqs)
    return(rseq)


def find_all_eq_iv(ol,value):
    test_func = lambda r,v:(r==v)
    rseq = find_all_iv(ol,test_func,value)
    return(rseq)


def find_all_eq_i(ol,value):
    test_func = lambda r,v:(r==v)
    rseq = find_all_i(ol,test_func,value)
    return(rseq)


def find_all_eq_v(ol,value):
    test_func = lambda r,v:(r==v)
    rseq = find_all_v(ol,test_func,value)
    return(rseq)



