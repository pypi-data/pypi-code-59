__version__ = '0.1.0'

#pip install python-docx
#作者：陈沁
import sys
import difflib
import docx

def read_file(filename):
    try:
        with open(filename, 'r', encoding='UTF-8') as f:
            return f.readlines()
    except IOError:
        print("ERROR: 没有找到文件:%s或读取文件失败！" % filename)
        sys.exit(1)

def compare_file(file1, file2, out_file):
    file1_content = read_file(file1)
    file2_content = read_file(file2)
    d = difflib.HtmlDiff()
    result = d.make_file(file1_content, file2_content)
    with open(out_file, 'w', encoding='UTF-8') as f:
        f.writelines(result)

def get_docx(file_name):
    d = docx.Document(file_name)
    doc = ''
    for i in d.paragraphs:  #迭代docx文档里面的每一个段落
       doc += i.text + '\n'
    return doc

def fiilecmp(file1, file2):
    doc = get_docx(file1)
    with open(file1+'.txt', 'w', encoding='UTF-8') as f:
        f.write(doc)
    doc = get_docx(file2)
    with open(file2+'.txt', 'w', encoding='UTF-8') as f:
        f.write(doc)
    compare_file(file1+'.txt', file2+'.txt', r'result.html')