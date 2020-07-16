import os

from beauty_print import bp_list


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


def get_all_file_ab_path(path):
    """
    获取路径下所有文件的绝对路径
    :param path:
    :return:
    """
    files_ab_path = []
    if os.path.isdir(path):
        os.chdir(path)
        all_file = os.listdir()
        for f in all_file:
            files_ab_path.extend(get_all_file_ab_path(f))

    else:
        if os.path.isabs(path):
            files_ab_path.append(path)
        else:
            files_ab_path.append(os.path.abspath(path))

    return files_ab_path


if __name__ == '__main__':
    write_file('./testData/write', '1测试1')
    files_ab_path = get_all_file_ab_path("../ariestools")
    bp_list(files_ab_path)
