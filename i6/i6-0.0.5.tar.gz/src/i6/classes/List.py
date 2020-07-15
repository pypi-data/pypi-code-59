from i6.classes.Base import Base
from i6.util import util

import json
import pickle
import typing


class List(typing.List[Base]):
    """
        i6 Standard List class for the i6 standard Base class.

        Example:
        ```
        class Person(i6.Base):
            def __init__(self, name):
                self.name = name

        p1 = Person('John1')
        p2 = Person('John2')
        persons = i6.List(p1, p2)

        print(persons)
        '''
        [{'name': 'John1'}, {'name': 'John2'}]
        '''
        ```
    """
    
    def __init__(self, *argv) -> None:
        super().__init__(argv)

    def append(self, item: Base) -> None:
        util.type_check(item, Base)
        super().append(item)

    def get_dict(self) -> dict:
        """
            Get __dict__

            Example:
            ```
            class Person(i6.Base):
                def __init__(self, name):
                    self.name = name
            
            print(i6.List(Person('John').get_dict()))
            '''
            [{'name': 'John'}]
            '''
            ```
        """

        return self

    def csv(self, delim = ', ', header = True, newline = False) -> str:
        """
            Returns a valid csv representation of the list.

            Example:
            ```
            class Person(i6.Base):
                def __init__(self, name):
                    self.name = name

            p1 = Person('John1')
            p2 = Person('John2')
            persons = i6.List(p1, p2)

            print(persons.csv())
            '''
            name
            John1
            John2
            '''
            ```
        """

        if len(self) == 0:
            return ''
        
        def strip_delim(data, newline = '\n'):
            return f"{data[:-len(delim)]}{newline}"

        result = ''

        if header:
            for key in self[0].get_dict():
                result += f"{key}{delim}"
            result = strip_delim(result)
        
        for i in range(len(self)):
            for key, value in self[i].get_dict().items():
                result += f"{value}{delim}"
            result = strip_delim(result)
        result = result[:-1]

        if newline:
            result += '\n'

        return result

    def load_csv(self, data: str, delim = ', ') -> None:
        """
            Load data from csv.

            Example:
            ```
            class Person(i6.Base):
                def __init__(self, name):
                    self.name = name

            p1 = Person('John1')
            p2 = Person('John2')

            persons = i6.List(p1)
            persons2 = i6.List(p1, p2)

            persons.load_csv(persons2.csv())
            print(persons)
            '''
            [{'name': 'John1'}, {'name': 'John2'}]
            '''
            ```
        """

        rows = data.splitlines()
        if len(rows) == 0:
            return

        header = rows[0].split(delim)

        temp_list = []

        for row in rows[1:]:
            temp_obj = {}
            values = row.split(delim)

            for i in range(len(header)):
                temp_obj[header[i]] = values[i]
            
            temp_base = Base()
            temp_base.set_dict(temp_obj)
            temp_list.append(temp_base)

        self.clear()
        for item in temp_list:
            self.append(item)

    def json(self) -> str:
        """
            Returns a valid json representation of the list.

            Example:
            ```
            class Person(i6.Base):
                def __init__(self, name):
                    self.name = name
            
            p1 = Person('John1')
            p2 = Person('John2')
            persons = i6.List(p1, p2)

            print(persons.json())
            '''
            [
                {
                    "name": "John1"
                },
                {
                    "name": "John2"
                }
            ]
            '''
            ```
        """
        
        temp_items = []
        for item in self:
            try:
                temp_items.append(item.get_dict())
            except AttributeError:
                temp_items.append(item)
        return json.dumps(temp_items, indent=4, default=str)

    def load_json(self, data: str) -> None:
        """
            Load data from json.

            Example:
            ```
            class Person(i6.Base):
                def __init__(self, name):
                    self.name = name

            p1 = Person('John1')
            p2 = Person('John2')

            persons = i6.List(p1)
            persons2 = i6.List(p1, p2)

            persons.load_json(persons2.json())
            print(persons)
            '''
            [{'name': 'John1'}, {'name': 'John2'}]
            '''
            ```
        """

        temp_list = []
        for item in json.loads(data):
            temp_base = Base()
            temp_base.set_dict(item)
            temp_list.append(temp_base)

        self.clear()
        for item in temp_list:
            self.append(item)

    def serialize(self) -> bytes:
        """
            Returns a binary serialization of the list.

            Example:
            ```
            class Person(i6.Base):
                def __init__(self, name):
                    self.name = name
            
            p1 = Person('John1')
            p2 = Person('John2')
            persons = i6.List(p1, p2)

            with open('persons.pkl', 'wb') as f:
                f.write(persons.serialize())
            ```
        """

        return pickle.dumps(self)

    def deserialize(self, data: bytes) -> None:
        """
            Deserialize a valid binary serialization of the list.

            Example:
            ```
            class Person(i6.Base):
                def __init__(self, name):
                    self.name = name

            persons = i6.List()

            with open('persons.pkl', 'rb') as f:
                persons.deserialize(f.read())

            print(persons)
            '''
            [{'name': 'John1'}, {'name': 'John2'}]
            '''
            ```
        """

        self.clear()
        for item in pickle.loads(data):
            self.append(item)
    