"""
    i6 Standard classes

    Example:
    ```
    class Person(i6.classes.Base):
        def __init__(self, name):
            self.name = name

    print(Person('John'))
    '''
    {
        'id': 1,
        'name': 'John',
    }
    '''
    ```
"""

from i6.classes.Base import Base
from i6.classes.List import List
