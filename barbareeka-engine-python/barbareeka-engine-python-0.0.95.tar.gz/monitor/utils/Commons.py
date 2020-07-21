import os


class Commons(object):
    def convert_to_mb(self, data_in_kb):
        try:
            data = data_in_kb
            data_in_float = data / 1024
            return data_in_float
        except Exception:
            raise "Unable to convert {} to MB".format(data_in_kb)

    def create_temp_folder(self, smartBOT):
        try:
            os.popen("adb -s {} shell mkdir /sdcard/{}".format(smartBOT.deviceUdid,
                                                               smartBOT.testCase.test_case.id.replace(
                                                                   "[^a-zA-Z0-9]", ""))).read()
        except Exception as error:
            print(error)

    def delete_temp_folder(self, smartBOT):
        try:
            os.popen("adb -s {} shell rm -rf /sdcard/{}".format(smartBOT.smartBOT.deviceUdid,
                                                                smartBOT.smartBOT.testCase.test_case.id.replace(
                                                                    "[^a-zA-Z0-9]", ""))).read()
        except Exception as error:
            print(error)
