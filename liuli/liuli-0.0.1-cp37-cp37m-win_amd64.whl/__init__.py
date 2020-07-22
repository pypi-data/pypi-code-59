from liuli.liuli import Liuli
import logging

logging.basicConfig(format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
                    level=logging.INFO)


# 绑定到库全局方法
liuli = Liuli()

load_userdict = liuli.load_userdict
cut = liuli.cut
lcut = liuli.lcut
cut_for_search = liuli.cut_for_search
lcut_for_search = liuli.lcut_for_search
