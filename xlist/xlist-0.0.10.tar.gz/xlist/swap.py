from .cmmn import inplace_wrapper


@inplace_wrapper
def iswap(arr,i,j,*kwargs):
    tmp = arr[i]
    arr[i] = arr[j]
    arr[j] = tmp
    return(arr)

@inplace_wrapper
def vswap(arr,v1,v2,**kwargs):
    i1 = arr.index(v1)
    i2 = arr.index(v2)
    arr = iswap(arr,i1,i2,**kwargs)
    return(arr)


@inplace_wrapper
def reindex(arr,*nindexes,**kwargs):
    for i in range(nindexes.__len__()):
        arr[nindexes[i]] = arr[i]
    return(arr)



