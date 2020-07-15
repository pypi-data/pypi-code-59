from __future__ import annotations
from i6.util import util

import json
import pickle


class Base():
    """
        i6 Standard base class.

        Example:
        ```
        class Person(i6.Base):
            def __init__(self, name):
                self.name = name

        print(Person('John'))
        '''
        {'name': 'John'}
        '''
        ```
    """

    def __repr__(self) -> str:
        return str(self.__dict__)

    def __eq__(self, other: Base) -> bool:
        util.type_check(other, self)
        return self.__dict__ == other.__dict__

    def set_dict(self, obj: dict) -> None:
        """
            Construct self with provided dict object.

            Example:
            ```
            base = i6.Base()
            base.set_dict({'name': 'John'})
            print(base)
            '''
            {'name': 'John'}
            '''
            ```
        """

        util.type_check(obj, dict)
        self.__dict__ = obj

    def get_dict(self) -> dict:
        """
            Get __dict__

            Example:
            ```
            class Person(i6.Base):
                def __init__(self, name):
                    self.name = name
            
            print(Person('John').get_dict())
            '''
            {'name': 'John'}
            '''
            ```
        """

        return self.__dict__

    def csv(self, delim = ', ', header = True, newline = False) -> str:
        """
            Returns a valid csv representation of the class.

            Example:
            ```
            class Person(i6.Base):
                def __init__(self, name):
                    self.name = name

            print(Person('John').csv())
            '''
            name
            John
            '''
            ```
        """

        def strip_delim(data, newline_char = '\n'):
            return f"{data[:-len(delim)]}{newline_char}"

        result = ''

        if header:
            for key in self.__dict__:
                result += f"{key}{delim}"
            result = strip_delim(result)
        
        for key, value in self.__dict__.items():
            result += f"{value}{delim}"
        result = strip_delim(result, '')

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

            p2.load_csv(p1.csv())
            print(p2)
            ```
        """

        rows = data.splitlines()
        header = rows[0].split(delim)

        for row in rows[1:]:
            values = row.split(delim)
            for i in range(len(header)):
                self.__dict__[header[i]] = values[i]

    def json(self) -> str:
        """
            Returns a valid json representation of the class.

            Example:
            ```
            class Person(i6.Base):
                def __init__(self, name):
                    self.name = name

            print(Person('John').json())

            '''
            {
                "name": "John"
            }
            '''
            ```
        """

        return json.dumps(self.__dict__, indent=4, default=str)

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

            p2.load_json(p1.json())
            print(p2)
            '''
            {'name': 'John1'}
            '''
            ```
        """

        self.__dict__ = json.loads(data)

    def serialize(self) -> bytes:
        """
            Returns a binary serialization of the class.

            Example:
            ```
            class Person(i6.Base):
                def __init__(self, name):
                    self.name = name

            with open('person.pkl', 'wb') as f:
                f.write(Person('John').serialize())
            ```
        """

        return pickle.dumps(self)

    def deserialize(self, data: bytes) -> None:
        """
            Deserialize a valid binary serialization of the class.

            Example:
            ```
            class Person(i6.Base):
                def __init__(self, name):
                    self.name = name

            person = Person('Doe')

            with open('person.pkl', 'rb') as f:
                person.deserialize(f.read())

            print(person)
            '''
            {'name': 'John'}
            '''
            ```
        """

        self.__dict__ = pickle.loads(data).__dict__
