
import abc
from ..utils import CommonUtil

class Formatter(object):

    @classmethod
    def make(self, formatName):

        if not formatName:
            raise RuntimeError('format is empty')

        if formatName.find('.') == -1:
            clazzName = CommonUtil.ucfirst(formatName) + 'Formatter'
            formatClazz = __package__ + "." + clazzName + '.' + clazzName
        else:
            formatClazz = formatName

        formatMeta = CommonUtil.getModuleMeta(formatClazz)

        return formatMeta()

    @abc.abstractmethod
    def format(self,request):

        pass
