# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['exclock']

package_data = \
{'': ['*'], 'exclock': ['assets/clock/*', 'assets/sound/*']}

install_requires = \
['json5', 'python-vlc', 'tqdm']

entry_points = \
{'console_scripts': ['exclock = exclock.main:main']}

setup_kwargs = {
    'name': 'exclock',
    'version': '0.1.19',
    'description': 'exclock is a cui extended timer.',
    'long_description': 'Exclock\n================================================================================\n\n.. image:: https://gitlab.com/yassu/exclock/badges/master/pipeline.svg\n  :target: https://gitlab.com/yassu/exclock/pipelines/latest\n\n.. image:: https://gitlab.com/yassu/exclock/badges/master/coverage.svg\n  :target: https://gitlab.com/yassu/exclock/-/commits/master\n\n\n`exclock` is a cui extended timer.\n\nRequired\n----------\n\n* vlc\n* xmessage\n\nUsage\n----------\n\n::\n\n    $ exclock [options] {clock-filename}\n\nFeatures\n--------------------------------------------------------------------------------\n\n* Sound an alarm at a specified time.\n* Sound the alarm after the specified time has elapsed.\n* You can flexibly set the alarm.\n\nOptions\n--------------------------------------------------------------------------------\n\n* `--version`: show program\'s version number and exit\n* `-h, --help`: show this help message and exit\n* `-l, --list`: show clock names in your PC and exit\n* `-t, --time`: Time which spends until or to specified\n* `-r, --ring-filename`: Sound-filename which used for ringing with `-t, --time` option. Note that you can use EXCLOCK_RING_FILENAME system variable if you often indicate ring-filename option.\n* `--trace, --traceback`: show traceback\n\nHow to sound an alarm at a specified time\n--------------------------------------------------------------------------------\n\nEnter\n\n::\n\n    $ exclock -t {time}\n\nformat command.\n\nWhere time is given in the `%H:%m` or `%H:%m:%S` format.\n\nEx.\n\n::\n\n    $ exclock -t "1:00"\n    $ exclock -t "1:00:20"\n\nHow to sound the alarm after the specified time has elapsed\n--------------------------------------------------------------------------------\n\nEnter\n\n::\n\n    $ exclock -t {time}\n\nformat command.\n\nWhere time is given in the `%S`, `%Ss`, `%mm` or `%mm%ss`.\n\nEx.\n\n::\n\n    $ exclock -t 3\n    $ exclock -t 3s\n    $ exclock -t 2m\n    $ exclock -t 2m3s\n\nHow to flexibly set the alarm\n--------------------------------------------------------------------------------\n\nEnter\n\n::\n\n    $ exclock {clock-filename}\n\nformat command.\nAlthough `{clock-filename}` can be omitted as descrived below.\n\nclock-file should be a file in json5 format.\n\nOfficial page for json5 format is `Here <https://json5.org/>`_.\n\nclock file format\n--------------------------------------------------------------------------------\n\n::\n\n    {\n      "title": "title(optional)",\n      "sounds": {\n        "time1": {\n          "message": "message1",\n          "sound_filename": "sound_filename1",\n        },\n        "time2":{\n        "message": "message2",\n        "sound_filename": "sound_filename2",\n        },\n        ...\n      },\n      "loop": loop_number\n    }\n\n* title: string which be used for notification. This is the optional option. Then the property is computed from clock-filename.\n* sounds: dictionary from time to dictionary which includes message and sound_filename.\n\n  - time format is "{sec}", "{sec}s", "{min}m" or "{min}m{sec}s" format.\n\n  - message is a string which be used for notification and terminal output.\n\n  - sound_filename is a string which be used for play the sound.\n\n* loop: number of iterations for above clock timer. If this is nil, this means repeatation a number of times.\n\nThere are sample files in `sample dir in gitlab <https://gitlab.com/yassu/exclock/-/tree/master/exclock/assets/clock>`_.\n\nHow to omit clock filename\n--------------------------------------------------------------------------------\n\nClock filename can be omitted for some case.\n\nRules are\n\n* If extension of clock filename is .json5, extension can be omitted(ex: pomodoro.json5 => pomodoro).\n* If dir is in the specified directory(~/.exclock/clock/ or environment variable EXCLOCK_CLOCK_DIR), dir is omitted (ex: ~/.exclock/clock/abc.json5 => abc).\n* Buitin clock file can be accessed. There are in `sample dir in gitlab`_ (ex: 3m or pomodoro).\n\nHow to omit sound filename\n--------------------------------------------------------------------------------\n\nSound filename can be omitted for some case.\n\nRules are\n\n* If dir is in the specified directory(~/.exclock/sound/ or environment variable EXCLOCK_SOUND_DIR), dir is omitted (ex: ~/.exclock/sound/abc.mp3 => abc.mp3).\n* Buitin sound file can be accessed. There are in `sample sound dir in gitlab <https://gitlab.com/yassu/exclock/-/tree/master/exclock/assets/sound>`_ (ex: silent.mp3 or warning.mp3).\n\nLICENSE\n-------\n\n`Apache 2.0 <https://gitlab.com/yassu/exclock/blob/master/LICENSE>`_\n\nTodo\n-------\n\n* [x] 環境にあるclock一覧を表示するコマンドを追加\n* Exception対応\n\n  * [x] \'Error: No available formula with the name "vlc"\'対応\n  * [x] xmessageがない場合のエラー処理\n\n* [x] 指定された時間になったらタイマーを発火させるコマンドを追加\n* [x] 0病後にSoundが指定されていた場合 そのSoundのとき tqdmを使わない\n* [x] プログレスバーの出力をいい感じにする\n* [-] Add n variable\n* [x] secの変数名を_secというようにする\n* [x] KeyboardInteraptのエラー処理を書く\n* [x] 🐛  二つ同じ名前がなくても一つしか表示されないようにする\n* [x] 🎨 main関数のテストを追加\n* [-] is_bgm flag\n* [ ] poetry導入\n* [x] confirm_fの削除\n* [ ] loopのデフォルト値を1にする\n* [-] --debug optionを付ける\n* [x] warningの音を設定できるような項目を追加する\n* [x] CLOCK_DIR_IN_SYSを指定できるような環境変数を定義する\n* [x] SOUND_DIR_IN_SYSを指定できるような環境変数を定義する\n* [x] setup.pyでPipenvのpackagesを使うようにする\n* [x] 真面目にdocumentを書く\n',
    'author': 'yassu',
    'author_email': 'yasu0320.dev@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
