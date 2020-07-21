from enum import Enum
import random

class Form(Enum):
    '''Class containing every cells shape'''

    STABLE = {
        'BLOC': [
            ['a', 'a'],
            ['a', 'a']
        ],
        'PIPE': [
            ['d', 'a', 'd'],
            ['a', 'd', 'a'],
            ['d', 'a', 'd']
        ],
        'BOAT': [
            ['a', 'a', 'd'],
            ['a', 'd', 'a'],
            ['d', 'a', 'd']
        ],
        'SNAKE': [
            ['a', 'a', 'd', 'a'],
            ['a', 'd', 'a', 'a']
        ],
    }

    OSCILLATOR = {
        'BLINKER1': [
            ['a', 'a', 'a']
        ],
        'BLINKER2': [
            ['a'],
            ['a'],
            ['a']
        ]
    }

    SHIP = {
        'ANTS': [
            ['a', 'd', 'a'],
            ['d', 'd', 'a'],
            ['a', 'a', 'a']
        ]
    }

    @classmethod
    def get_shape_form(cls, shape):
        return {
            'x': len(shape[0]),
            'y': len(shape)
        }

    @classmethod
    def get_shape(cls, form_type=None):
        if(form_type is None):
            form_type = random.choice(list(Form))
        random_shape = random.choice(list(form_type.value))
        return form_type.value[random_shape]