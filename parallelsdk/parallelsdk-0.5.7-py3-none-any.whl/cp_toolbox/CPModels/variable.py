from ortools.sat.python import cp_model


#class BaseVariable(cp_model.IntVar):
#    def __init__(self, model, domain, name):
#        super().__init__(model, domain, name)

class Variable(cp_model.IntVar):
    """
    Class encapsulating a CP variable
    """

    def __init__(self, model, lb, ub, name=''):
        self.__id = id(self)
        self.__name = name
        if not name:
            self.__name = 'v_' + str(self.__id)
        super().__init__(model.Proto(), cp_model.Domain(lb, ub), self.__name)
        self.__domain = [lb, ub]
        self.__value = None

    def set_value(self, value):
        self.__value = value

    def get_id(self):
        return self.__id

    def get_value(self):
        return self.__value

    def to_string(self):
        var_str = 'Variable:\n'
        var_str += '\tid: ' + self.Name() + '\n'
        var_str += '\tdomain: ' + str(self.__domain)
        return var_str
