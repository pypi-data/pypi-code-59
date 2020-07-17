import os
from typing import List


def write_file(file_path, content, mode='w', encoding='utf-8'):
    """
    写文件. 如果目录存在会自动新建. 默认以覆盖的方式写入.
    :param file_path:
    :param content:
    :param mode:
    :param encoding:
    :return:
    """
    abspath = os.path.abspath(file_path)
    abs_dir = os.path.dirname(abspath)

    if not os.path.exists(abs_dir):
        os.makedirs(abs_dir)

    with open(abspath, mode=mode, encoding=encoding) as fp:
        fp.write(content)


def get_all_file_ab_path(path, ex: List[str] = None):
    """
    获取路径下所有文件的绝对路径
    :param ex: 过滤的文件名
    :param path:
    :return: [文件绝对路径, 文件名]
    """
    files_ab_path = []
    if os.path.isdir(path):
        os.chdir(path)
        all_file = os.listdir()
        for f in all_file:
            files_ab_path.extend(get_all_file_ab_path(f, ex))

    else:

        if ex is not None and len(ex) != 0:
            if os.path.basename(path) in ex:
                return []
        if os.path.isabs(path):
            files_ab_path.append([path, os.path.basename(path)])
        else:
            files_ab_path.append([os.path.abspath(path), os.path.basename(path)])

    return files_ab_path


if __name__ == '__main__':
    write_file('./testData/write', '1测试1')
    files_ab_path = get_all_file_ab_path(
        "../ariestools",
        ["yaml_util.py", "json_path_util.py"]
    )
    for i in files_ab_path:
        print(i)
