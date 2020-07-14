from uuid import uuid4
import hmac
import urllib
import hashlib
from instapv.config import Config
import locale
import time
from datetime import datetime, date
from dateutil.relativedelta import relativedelta, MO
import random
import os.path

class Tools:

    def __init__(self):
        self.config = Config()
        self._last_upload_id = None
        super().__init__()

    def generate_uuid(self, type):
        generated_uuid = str(uuid4())
        if (type):
            return generated_uuid
        else:
            return generated_uuid.replace('-', '')

    def generate_signature(self, data, skip_quote=False):
        if not skip_quote:
            try:
                parsedData = urllib.parse.quote(data)
            except AttributeError:
                parsedData = urllib.quote(data)
        else:
            parsedData = data
        return 'ig_sig_key_version=' + self.config.SIG_KEY_VERSION + '&signed_body=' + hmac.new(self.config.IG_SIG_KEY.encode('utf-8'), data.encode('utf-8'), hashlib.sha256).hexdigest() + '.' + parsedData

    def number_format(self, num, places=0):
        return locale.format_string("%.*f", (places, num), False)

    def microtime(self, get_as_float = False) :
        d = datetime.now()
        t = time.mktime(d.timetuple())
        if get_as_float:
            return t
        else:
            ms = d.microsecond / 1000000.
            return '%f %d' % (ms, t)


    def generate_upload_id(self, use_nano = False):
        locale.setlocale(locale.LC_NUMERIC, '')
        result = None
        if not use_nano:
            while True:
                result = self.number_format(
                    round(self.microtime(True) * 1000), 0
                )
                if self._last_upload_id != None and result == self._last_upload_id:
                    time.sleep(0.001)
                else:
                    self._last_upload_id = result
                    break
        else:
            today = date.today()
            _last_monday = today + relativedelta(weekday=MO(-1))
            result = self.number_format(
                int(self.microtime(True)) - int(_last_monday.strftime("%d")), 6
            )
            result += str(random.randint(1, 999)).ljust(3, '0') # str_pad
        return result
    
    def base_name(self, path, suffix=None):
        basename = os.path.basename(path)
        if suffix and basename.endswith(suffix):
          basename = basename[:-len(suffix)]
        return basename
