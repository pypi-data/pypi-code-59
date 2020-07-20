
import abc
from ..utils import CommonUtil
"""
 * 传输协议基类
 *<B>说明：</B>
 *<pre>
 *  使用
 *</pre>
"""
class Transport(object):

    @classmethod
    def make(cls, transportName) -> 'Transport':
        if not transportName:
            raise RuntimeError('transport {0} is empty'.format(transportName))

        if transportName.find('.') == -1:
            transportClazzName = CommonUtil.ucfirst(transportName) + 'Transport'
            transportClazz = __package__ + "." + transportClazzName + '.' + transportClazzName
        else:
            transportClazz = transportName

        transportMeta = CommonUtil.getModuleMeta(transportClazz)

        return transportMeta()


    @abc.abstractmethod
    def send(self,request):
        pass

    def batchSend(self,requests)->'dict':

        for key, request in requests.items():
            self.send(request)

