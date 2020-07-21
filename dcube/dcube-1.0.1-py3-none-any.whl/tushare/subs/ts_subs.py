# -*- coding:utf-8 -*- 
'''
@group:waditu
@author: DY
'''

import logging, sys
logging.basicConfig(stream=sys.stdout, level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
import logging

logger = logging.getLogger(__name__)


from tushare.subs import Subs
app = Subs(
    token='7208a3732f8926138b4277a916f68500b89fbbb397f9e36978e09688',
)

#  code 可以包含 * （通配符）
@app.register(topic='HQ_STK_TICK', codes=['*'])
def print_message(record):
    """
    订阅主题topic，并指定codes列表，在接收到topic的推送消息时，符合code条件，就会执行回调
    :param record:
    :return:
    """
    logger.info('用户定义业务代码输出 print_message(%s)' % str(record))

if __name__ == '__main__':
    app.run()