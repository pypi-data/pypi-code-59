from .fltr import fltrv
from .sort import sort_dtb


def fltrv_via_loose_in(arr,k):
    fltred  = fltrv(arr,lambda ele:(ele in k))
    return(fltred)



def is_loose_in(arr,k):
    for each in arr:
        cond = (each in k)
        if(cond):
            return(True)
        else:
            pass
    return(False)



def fltrv_via_loose_contain(arr,k):
    fltred  = fltrv(arr,lambda ele:(k in ele))
    return(fltred)



def is_loose_contain(arr,k):
    for each in arr:
        cond = (k in each)
        if(cond):
            return(True)
        else:
            pass
    return(False)




def fltrv_via_regex_match(arr,regex):
    def test_func(v):
        m = regex.search(ele)
        cond = False if(m==None) else True
        return(cond)
    fltred  = fltrv(arr,test_func)
    return(fltred)


def is_regex_match(arr,regex):
    def test_func(v):
        m = regex.search(ele)
        cond = False if(m==None) else True 
        return(cond)
    for each in arr:
        cond = test_func(each)
        if(cond):
            return(True)
        else:
            pass
    return(False)




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
            rslt = sort_dtb(rslt,cond_keys=['len'])
        return(rslt)
    rslt = get_comm_substr(len0,len1,label_s0_end)
    return(rslt)



def join(ol,separator=","):
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



def join_with_sp_list(ol,*sps):
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




