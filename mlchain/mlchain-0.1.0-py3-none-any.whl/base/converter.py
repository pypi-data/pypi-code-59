import json
from PIL import Image, ImageSequence
import io
import numpy as np
from mlchain.base.exceptions import MLChainAssertionError
import os
from typing import *
from inspect import signature, _empty
from collections import defaultdict

cv2 = None
ALL_LOWER_TRUE = ["true", "yes", "yeah", "y"]


def import_cv2():
    global cv2
    if cv2 is None:
        import cv2 as cv
        cv2 = cv


def str2ndarray(value: str) -> np.ndarray:
    if value[0:4] == 'http':
        from mlchain.base.utils import is_image_url_and_ready
        # If it is a url image
        if is_image_url_and_ready(value):
            from mlchain.base.utils import url_to_image
            return url_to_image(value)
        else:
            raise MLChainAssertionError("Image url is not valid")
    elif os.path.exists(value):
        import_cv2()
        return cv2.imread(value)
    else:
        import_cv2()
        # If it is a base64 encoded array
        try:
            from base64 import b64decode
            nparr = np.fromstring(b64decode(value), np.uint8)
            img = cv2.imdecode(nparr, cv2.IMREAD_ANYCOLOR)
            return img
        except:
            pass

        try:
            # If it is a string array
            import ast
            return np.array(ast.literal_eval(value))
        except:
            raise MLChainAssertionError("There's no way to convert to numpy array with variable {}".format(value))

    return value


def list2ndarray(value: list) -> np.ndarray:
    raise MLChainAssertionError("Not allow multi value", code="convert")


def str2int(value: str) -> int:
    return int(value)


def str2float(value: str) -> float:
    try:
        return float(value)
    except:
        raise MLChainAssertionError("Can't convert {0} to type float".format(value))


def str2bool(value: str) -> bool:
    if value.lower() in ALL_LOWER_TRUE:
        return True
    if value.lower() in ["none", 'false', 'n', 'null', 'no']:
        return False
    raise MLChainAssertionError("Can't convert {0} to type boolean".format(value))


def str2list(value: str) -> List:
    try:
        l = json.loads(value)
        return l
    except:
        return [value]


def str2dict(value: str) -> dict:
    try:
        l = json.loads(value)
        return l
    except:
        raise MLChainAssertionError("Can't convert {0} to dict".format(value))


def str2bytes(value: str) -> bytes:
    return value.encode()


def cv2imread(filename, value) -> np.ndarray:
    import_cv2()
    value = cv2.imdecode(
        np.asarray(bytearray(value), dtype="uint8"),
        cv2.IMREAD_COLOR)
    if value is None:
        raise MLChainAssertionError("Can't read image from {0}".format(filename))
    return value


def cv2imread_to_list(filename, value) -> List[np.ndarray]:
    import_cv2()
    value = cv2.imdecode(
        np.asarray(bytearray(value), dtype="uint8"),
        cv2.IMREAD_COLOR)
    if value is None:
        raise MLChainAssertionError("Can't read image from {0}".format(filename))
    return [value]


def pilimread_one_img(filename, img_bytes) -> np.ndarray:
    output = []
    im = Image.open(io.BytesIO(img_bytes))

    for i, page in enumerate(ImageSequence.Iterator(im)):
        return np.array(page)
    raise MLChainAssertionError("Can't convert file {0} to ndarray".format(filename))


def pilimread_list_img(filename, img_bytes) -> List[np.ndarray]:
    output = []
    im = Image.open(io.BytesIO(img_bytes))

    for i, page in enumerate(ImageSequence.Iterator(im)):
        output.append(np.array(page))
    return output


def storage2bytes(filename, value) -> bytes:
    return value


def storage2json(filename, value) -> Union[List, Dict]:
    return json.loads(value, encoding='utf-8')


def storage2str(filename, value) -> str:
    return value.decode()


class Converter:
    convert_dict = defaultdict(dict)
    file_converters = {}

    def __init__(self, file_storage_type=None, get_file_name=None, get_data=None):
        self.FILE_STORAGE_TYPE = file_storage_type
        self._get_file_name = get_file_name
        self._get_data = get_data

    @staticmethod
    def add_convert(function, in_type=None, out_type=None):
        sig = signature(function)
        parameters = sig.parameters
        for key, input_types in parameters.items():
            if in_type is None:
                input_types = input_types.annotation
            else:
                input_types = in_type
            if out_type is None:
                output_types = sig.return_annotation
            else:
                output_types = out_type
            if input_types == Union:
                input_types = input_types.__args__
            else:
                input_types = [input_types]

            if output_types == Union:
                output_types = output_types.__args__
            else:
                output_types = [output_types]

            for i_type in input_types:
                for o_type in output_types:
                    Converter.convert_dict[i_type][o_type] = function
            break

    @staticmethod
    def add_convert_file(extensions, function, output_type=None):
        sig = signature(function)
        input_types = extensions.split(',')
        input_types = tuple(sorted(e.strip() for e in input_types))
        if output_type is None:
            output_types = sig.return_annotation

            if output_types == Union:
                output_types = output_types.__args__
            else:
                output_types = (output_types,)
        else:
            output_types = (output_type,)
        for o_type in output_types:
            Converter.file_converters[(input_types, o_type)] = function

    def convert_file(self, file_name, data, out_type):
        ext = file_name.rsplit('.')[-1].lower()
        out_type = Union[out_type]
        if out_type == Union:
            out_type = out_type.__args__
        else:
            out_type = (out_type,)
        for (k, o), converter in self.file_converters.items():
            if (ext in k or '*' in k) and (out_type == o or o in out_type):
                return converter(file_name, data)
        raise MLChainAssertionError("Not found convert file {0} to {1}".format(file_name, out_type))

    def convert(self, value, out_type):
        '''
        Convert type of value to out_type
        :param value:
        :param out_type:
        :return:
        '''
        if out_type == _empty:
            return value
        if getattr(out_type, '__origin__', None) in [List, Set, Dict, list, set,
                                                     dict] and out_type.__origin__ is not None:
            if isinstance(value, (List, list)):
                if out_type.__origin__ in [List, list]:
                    return [self.convert(v, out_type.__args__) for v in value]
                elif out_type.__origin__ in [Set, set]:
                    return set(self.convert(v, out_type.__args__) for v in value)
            elif isinstance(value, (Dict, dict)):
                if out_type.__origin__ in [Dict, list]:
                    args = out_type.__args__
                    if len(args) == 2:
                        return {self.convert(k, args[0]): self.convert(v, args[1]) for k, v in value.items()}
                    elif len(args) == 1:
                        return {k: self.convert(v, args[0]) for k, v in value.items()}
            else:
                if type(value) == self.FILE_STORAGE_TYPE:
                    return self.convert_file(self._get_file_name(value), self._get_data(value), out_type)
                if out_type.__origin__ in [List, list]:
                    return [self.convert(value, out_type.__args__)]
                elif out_type.__origin__ in [Set, set]:
                    return {self.convert(value, out_type.__args__)}
                else:
                    raise MLChainAssertionError("Can't convert value {0} to {1}".format(value, out_type),
                                                code="convert")
        else:
            try:
                if isinstance(value, out_type):
                    return value
            except:
                pass
        out_type = Union[out_type]
        if out_type == Union:
            out_type = out_type.__args__
        else:
            out_type = (out_type,)
        if type(value) in out_type:
            return value
        else:
            for i_type in self.convert_dict:
                if isinstance(value, i_type):
                    for o_type in self.convert_dict[i_type]:
                        if o_type in out_type:
                            return self.convert_dict[i_type][o_type](value)
        if type(value) == self.FILE_STORAGE_TYPE:
            return self.convert_file(self._get_file_name(value), self._get_data(value), out_type)
        raise MLChainAssertionError("Not found converter from {0} to {1}".format(type(value), out_type))
        return value


Converter.add_convert(lambda x: str(x), int, str)
Converter.add_convert(str2ndarray)
Converter.add_convert(list2ndarray)
Converter.add_convert(str2int)
Converter.add_convert(str2float)
Converter.add_convert(str2bool)
Converter.add_convert(str2bytes, str, bytes)
Converter.add_convert(str2bytes, str, bytearray)
Converter.add_convert(str2list, str, list)
Converter.add_convert(str2list, str, List)
Converter.add_convert(str2dict, str, Dict)
Converter.add_convert(str2dict, str, dict)
Converter.add_convert_file('jpg,jpeg,png,gif,bmp,jpe,jp2,pbm,pgm,ppm,sr,ras', cv2imread, output_type=np.ndarray)
Converter.add_convert_file('jpg,jpeg,png,gif,bmp,jpe,jp2,pbm,pgm,ppm,sr,ras', cv2imread_to_list,
                           output_type=List[np.ndarray])
Converter.add_convert_file('tif,tiff', pilimread_one_img, output_type=np.ndarray)
Converter.add_convert_file('tif,tiff', pilimread_list_img, output_type=List[np.ndarray])
Converter.add_convert_file('*', storage2bytes, output_type=bytes)
Converter.add_convert_file('json', storage2json, output_type=dict)
Converter.add_convert_file('txt', storage2str, output_type=str)
