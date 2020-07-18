import os
<<<<<<< HEAD
from spongebox.reg import filter_list
=======
import pandas as pd
from spongebox.reg import filter_list
from spongebox.time import timeit

pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)
pd.set_option('display.unicode.ambiguous_as_wide', True)
pd.set_option("display.unicode.east_asian_width", True)
pd.set_option("display.float_format", lambda x: "%.4f" % x)
>>>>>>> cfca8de16d85de609bf33ab0ea4829830c8c8f6c


def list_dir(dir_path, exp=None):
    if exp is None:
        return os.listdir(dir_path)
    else:
        return filter_list(os.listdir(dir_path), exp=exp)

<<<<<<< HEAD

def list_all_files(dir_path, lst=[]):
    children = os.listdir(dir_path)
    for f in children:
        _path_ = os.path.join(dir_path, f)
        if os.path.isdir(_path_):
            list_all_files(_path_)
        else:
            lst.append(_path_)
=======
@timeit
def list_all_files(dir_path):
    lst=[]
    for root,dir,flst in os.walk(dir_path):
        # print(root)
        # print(dir)
        # print(flst)
        lst.extend([root+"\\"+f for f in flst])
>>>>>>> cfca8de16d85de609bf33ab0ea4829830c8c8f6c
    return lst


if __name__ == "__main__":
<<<<<<< HEAD
    print(list_dir("../", exp=".*md$"))
    print(list_all_files("C:\\Users\\LuoJi\\Documents\\01Python"))
=======
    # print(list_dir("../", exp=".*md$"))
    lst=[]
    # lst1=[]
    # print(list_all_files("C:\\Users\\LuoJi\\Downloads\\test",lst))
    # print(list_all_files("C:\\Users\\LuoJi\\Downloads\\test",lst1))
    # print(walk_all_files("C:\\Users\\LuoJi\\Downloads\\test"))
    list_all_files("C:\\Users\\LuoJi\\Documents\\05照片")
    # print(list_all_files("C:\\Users\\LuoJi\\Downloads\\test"))
>>>>>>> cfca8de16d85de609bf33ab0ea4829830c8c8f6c
