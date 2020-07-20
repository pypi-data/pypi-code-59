from sentence_spliter.spliter_sentence import Spliter

#
def test_cut_to_sentences_en():
    options = {
        'language': 'en',
        'long_short_sent_handle': False,
        'max_length': 100,
        'min_length': 15,
        'hard_max_length': 100,
        'remove_blank': False
    }
    spliter = Spliter(**options)
    text = 'Hello world.kkkkk!'
    cut_sent_actual = spliter.cut_to_sentences(text=text)
    print(cut_sent_actual)
    cut_sent_expect = ['''Hello world.''', '''kkkkk!''']
    assert cut_sent_expect == cut_sent_actual


def test_cut_to_sentences_zh_1():
    '''
    短句合并,如果合并后仍然是长句，则不合并
    :return:
    '''
    options = {
        'language': 'zh',
        'long_short_sent_handle': True,
        'max_length': 20,
        'min_length': 5,
        'hard_max_length': 20,
        'remove_blank': True
    }
    spliter = Spliter(**options)

    text = '旁听席.座无虚席,但法庭里并未显现出乡间谋杀.'

    cut_sent_actual = spliter.cut_to_sentences(text=text)
    print(cut_sent_actual)
    cut_sent_expect = ['旁听席.', '座无虚席,但法庭里并未显现出乡间谋杀.']
    assert cut_sent_expect == cut_sent_actual

def test_cut_to_sentences_zh_9():
    '''
    短句合并,如果合并后仍然是长句，则不合并
    :return:
    '''
    options = {
        'language': 'zh',
        'long_short_sent_handle': True,
        'max_length': 20,
        'min_length': 5,
        'hard_max_length': 20,
        'remove_blank': True
    }
    spliter = Spliter(**options)

    text = '旁听席.座无虚席,但法庭里并未显现出乡间谋杀.旁听席.座无虚席,但法庭里并未显现出乡间谋杀.'

    cut_sent_actual = spliter.cut_to_sentences(text=text)
    print(cut_sent_actual)
    cut_sent_expect = ['旁听席.', '座无虚席,但法庭里并未显现出乡间谋杀.','旁听席.', '座无虚席,但法庭里并未显现出乡间谋杀.']
    assert cut_sent_expect == cut_sent_actual


def test_cut_to_sentences_zh_2():
    '''
    长句切开
    :return:
    '''
    options = {
        'language': 'zh',
        'long_short_sent_handle': True,
        'max_length': 20,
        'min_length': 3,
        'hard_max_length': 20,
        'remove_blank': True
    }
    spliter = Spliter(**options)
    text = '旁听席，座无虚席,但法庭里并未显现出乡间谋杀案庭审过程中常见的狂欢氛围。'
    cut_sent_actual = spliter.cut_to_sentences(text=text)
    print(cut_sent_actual)
    cut_sent_expect = ['旁听席，座无虚席,', '但法庭里并未显现出乡间谋杀案庭审过程中常', '见的狂欢氛围。']
    assert cut_sent_expect == cut_sent_actual

def test_cut_to_sentences_zh_8():
    '''
    长句切开
    :return:
    '''
    options = {
        'language': 'zh',
        'long_short_sent_handle': True,
        'max_length': 20,
        'min_length': 3,
        'hard_max_length': 20,
        'remove_blank': True
    }
    spliter = Spliter(**options)
    text = '旁听席.座无虚席,但法庭里并未显现出乡间谋杀案庭审过程中常见的狂欢氛围。'
    cut_sent_actual = spliter.cut_to_sentences(text=text)
    print(cut_sent_actual)
    cut_sent_expect = ['旁听席.','座无虚席,', '但法庭里并未显现出乡间谋杀案庭审过程中常', '见的狂欢氛围。']
    assert cut_sent_expect == cut_sent_actual


def test_cut_to_sentences_zh_3():
    '''
    长句切开,强制截断
    :return:
    '''
    options = {
        'language': 'zh',
        'long_short_sent_handle': True,
        'max_length': 20,
        'min_length': 5,
        'hard_max_length': 20,
        'remove_blank': True
    }
    spliter = Spliter(**options)
    text = '但法庭里并未显现出乡间谋杀案庭审过程中常见的狂欢氛围。'
    cut_sent_actual = spliter.cut_to_sentences(text=text)
    # print(cut_sent_actual)
    cut_sent_expect = ['但法庭里并未显现出乡间谋杀案庭审过程中常', '见的狂欢氛围。']
    assert cut_sent_expect == cut_sent_actual


def test_cut_to_sentences_zh_4():
    '''
    连着两个长句切开
    :return:
    '''
    options = {
        'language': 'zh',
        'long_short_sent_handle': True,
        'max_length': 15,
        'min_length': 5,
        'hard_max_length': 15,
        'remove_blank': True
    }
    spliter = Spliter(**options)
    text = '我看着镜子里的自己,我知道我受洗时的名字叫克莱门汀.所以如果大伙儿管我叫克莱门想想看就算是叫我克莱门汀.'
    cut_sent_actual = spliter.cut_to_sentences(text=text)
    print(cut_sent_actual)
    cut_sent_expect = ['我看着镜子里的自己,', '我知道我受洗时的名字叫克莱门汀', '.', '所以如果大伙儿管我叫克莱门想想', '看就算是叫我克莱门汀.']
    assert cut_sent_expect == cut_sent_actual

def test_cut_to_sentences_zh_5():
    '''
    连着两个长句切开
    :return:
    '''
    options = {
        'language': 'zh',
        'long_short_sent_handle': True,
        'max_length': 15,
        'min_length': 5,
        'hard_max_length': 15,
        'remove_blank': True
    }
    spliter = Spliter(**options)
    text = '我看着镜子里的自己,我知道我受洗时的名字叫克莱门汀.所以如果大伙儿管我叫,克莱门想想看就算是叫我克莱门汀.'
    cut_sent_actual = spliter.cut_to_sentences(text=text)
    print(cut_sent_actual)
    cut_sent_expect = ['我看着镜子里的自己,', '我知道我受洗时的名字叫克莱门汀', '.', '所以如果大伙儿管我叫,', '克莱门想想看就算是叫我克莱门汀', '.']
    assert cut_sent_expect == cut_sent_actual


def test_cut_to_sentences_zh_6():
    '''
    长句切开后最后一句是短句
    :return:
    '''
    options = {
        'language': 'zh',
        'long_short_sent_handle': True,
        'max_length': 10,
        'min_length': 5,
        'hard_max_length': 10,
        'remove_blank': True
    }
    spliter = Spliter(**options)
    text = '我看着镜子里的自己,我知道我受洗时的名字叫克莱.所以如果大伙儿,管我叫克莱门，想想看就算是叫我克莱门汀.哈哈哈．'
    cut_sent_actual = spliter.cut_to_sentences(text=text)
    print(cut_sent_actual)
    assert cut_sent_actual == ['我看着镜子里的自己,', '我知道我受洗时的名字', '叫克莱.', '所以如果大伙儿,', '管我叫克莱门，', '想想看就算是叫我克莱', '门汀.哈哈哈．']



def test_cut_to_sentences_zh_7():
    '''
    :return:
    '''
    options = {
        'language': 'zh',
        'long_short_sent_handle': True,
        'max_length': 5,
        'min_length': 4,
        'hard_max_length': 5,
        'remove_blank': True
    }
    spliter = Spliter(**options)
    text = '我看.着镜.子里.的自己我知道.'
    expect = ['我看.','着镜.','子里.','的自己我知','道.']
    cut_sent_actual = spliter.cut_to_sentences(text=text)
    print(cut_sent_actual)
    assert expect == cut_sent_actual

def test_cut_to_sentences_zh_10():
    '''
    :return:
    '''
    options = {
        'language': 'zh',
        'long_short_sent_handle': True,
        'max_length': 200,
        'min_length': 20,
        'hard_max_length': 200,
        'remove_blank': True
    }
    spliter = Spliter(**options)
    text = '到荷兰境内，干粮完了；但听说当地人人皆是富翁，并且是基督徒，便深信他们待客的情谊决不亚于男爵府上，就是说和他没有为了美丽的居内贡而被逐的时代一样。他向好几位道貌岸然的人求布施。'
    expect = ['我看.','着镜.','子里.','的自己我知','道.']
    cut_sent_actual = spliter.cut_to_sentences(text=text)
    print(cut_sent_actual)
    # assert expect == cut_sent_actual

def test_cut_sentences_book_simple():
    options = {
        'language': 'zh',
        'long_short_sent_handle': False,
        'max_length': 200,
        'min_length': 10,
        'hard_max_length': 200,
        'remove_blank': True
    }
    spliter = Spliter(**options)
    with open('./data/249-老实人-zh.txt', 'r', encoding='utf-8') as f:
        sentence = f.read()
    output_lines = []
    output_lines.extend(spliter.cut_to_sentences(sentence))
    output_path = './data/249-老实人-zh-cut.txt'
    open(output_path, 'w', encoding='utf-8').write('\n'.join(output_lines))

    # ---判断每条句子的长度----
    # with open(output_path, 'r', encoding='utf-8') as f:
    #     data = f.readlines()
    # for line in data:
    #     if len(line) < options['min_length'] or len(line) < options['max_length']:
    #         assert Exception('error')

def test_cut_sentences_book():
    options = {
        'language': 'zh',
        'long_short_sent_handle': True,
        'max_length': 200,
        'min_length': 10,
        'hard_max_length': 200,
        'remove_blank': True
    }
    spliter = Spliter(**options)
    with open('./data/249-老实人-zh.txt', 'r', encoding='utf-8') as f:
        sentence = f.read()
    output_lines = []
    output_lines.extend(spliter.cut_to_sentences(sentence))
    output_path = './data/249-老实人-zh-long-short-cut.txt'
    open(output_path, 'w', encoding='utf-8').write('\n'.join(output_lines))


if __name__ == '__main__':
    # test_cut_to_sentences_en()
    test_cut_to_sentences_zh_1()
    test_cut_to_sentences_zh_2()
    test_cut_to_sentences_zh_3()
    test_cut_to_sentences_zh_4()
    test_cut_to_sentences_zh_5()
    test_cut_to_sentences_zh_6()
    test_cut_to_sentences_zh_7()
    test_cut_to_sentences_zh_8()
    test_cut_to_sentences_zh_9()
    # test_cut_sentences_book_simple()
    # test_cut_sentences_book()
    test_cut_to_sentences_zh_10()
    print(len('''他说：“显而易见，事无大小，皆系定数；万物既皆有归宿，此归宿自必为最美>|  他说：“显而易见，事无大小，皆系定数；万物既皆有归宿，此归宿自必为最美
  满的归宿。岂不见鼻子是长来戴眼镜的吗？所以我们有眼镜。身上安放两条腿是|  满的归宿。岂不见鼻子是长来戴眼镜的吗？所以我们有眼镜。身上安放两条腿>
  为穿长裤的，所以我们有长裤。石头是要人开凿，盖造宫堡的，所以男爵大人有|  是为穿长裤的，所以我们有长裤。石头是要人开凿，盖造宫堡的，所以男爵大>
  一座美轮美奂的宫堡；本省最有地位的男爵不是应当住得最好吗？猪是生来给人|  人有一座美轮美奂的宫堡；本省最有地位的男爵不是应当住得最好吗？猪是生>
  吃的，所以我们终年吃猪肉；谁要说一切皆善简直是胡扯，应当说尽善尽美才对|  来给人吃的，所以我们终年吃猪肉；谁要说一切皆善简直是胡扯，应当说尽善>
  。”老实人一心一意的听着，好不天真的相信着；'''))