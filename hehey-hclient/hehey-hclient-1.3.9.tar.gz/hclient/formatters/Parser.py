
import abc
from ..utils import CommonUtil

class Parser(object):

    @classmethod
    def make(self, parserName):

        if not parserName:
            raise RuntimeError('Parser is empty')

        if parserName.find('.') == -1:
            clazzName = CommonUtil.ucfirst(parserName) + 'Parser'
            parserClazz = __package__ + "." + clazzName + '.' + clazzName
        else:
            parserClazz = parserName

        parserMeta = CommonUtil.getModuleMeta(parserClazz)

        return parserMeta()

    @abc.abstractmethod
    def format(self, response):

        pass
