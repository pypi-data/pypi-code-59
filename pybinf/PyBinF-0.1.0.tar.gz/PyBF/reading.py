_builtin_open = open

def read(name):
    with _builtin_open(name, 'rb') as f:
        s = str(f.read())[2:-1]
    result = ''
    redouble = lambda x: x*4
    for i in map(redouble, range(int(len(s)/4))):
        parsing = '0x'+s[i+2:i+4]
        parsing = eval(parsing)
        result += bin(parsing)[2:]
    return result