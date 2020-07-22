class Constraint:
    """
    Class encapsulating a CP constriant
    """

    def __init__(self, model, expr, name=''):
        self.__id = id(self)
        if not name:
            name = 'c_' + str(self.__id)
        self.__con = model.Add(expr)
        self.__name = name

    def to_string(self):
        con_str = 'Constraint:\n'
        con_str += '\tid: ' + self.__name + '\n'
        return con_str
