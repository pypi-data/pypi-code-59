from PyErr import ArgError as _ArgError

def write(name, value):
    err = _ArgError("Parameter 'value' is not parsable") 
    if not isinstance(value, str):
        raise err
    if value.replace('0', '').replace('1', ''):
        raise err
    if len(value)%8:
        raise err
    tridouble = lambda x: x*8
    result = b''
    for i in map(tridouble, range(int(len(value)/8))):
        b = '0b'+value[i:i+8]
        h = 'b\'\\'+hex(eval(b))[1:]+'\''
        result += eval(h)
    with open(name, 'wb') as f:
        f.write(result)