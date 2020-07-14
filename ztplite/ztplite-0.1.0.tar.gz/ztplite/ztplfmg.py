import os
import sys
import datetime
from . import ztpllogging
import base64
import time
from pyFMG.fortimgr import FortiManager, FMGBaseException, FMGConnectionError
from abc import ABC, abstractmethod
from enum import IntEnum
from logging import Formatter, FileHandler, INFO
from jinja2 import Template


class CustomResponseCode(IntEnum):
    """
    Basic ENUM to provide code response codes that can be utilized by the caller.
        - SUCCESS = 0
        - NON_SUCCESS = -100000
        - GEN_EXCEPTION = -100001
        - KEY_NOT_EXIST = -100002
        - KEY_ERROR = -100003
        - TASK_EXCEPTION = -100004
    """
    SUCCESS = 0
    NON_SUCCESS = -100000
    GEN_EXCEPTION = -100001
    KEY_NOT_EXIST = -100002
    KEY_ERROR = -100003
    TASK_EXCEPTION = -100004


class TaskTimedOutException(Exception):
    """Used to maintain details on if a task did not finish in time"""

    def __init__(self, *args):
        super(TaskTimedOutException, self).__init__(*args)


class TaskReportedErrorException(Exception):
    """Used to maintain details on if a task did not finish in time"""

    def __init__(self, *args):
        super(TaskReportedErrorException, self).__init__(*args)


class ZTPConnectionError(FMGConnectionError):
    """Simple wrapper for connection error issues"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class BaseFMGAction(ABC):
    """
    The BaseClass for an action that will be encapsulated for the ZTP FMG. This is an abstract base class and is not meant to be instantiated as a concrete class but provides the perform method which is where action is meant to take place in the command

    :param ztplfmg: Reference to the FMG
    :type ztplfmg: ZTPLFortiManager
    :param cleanup_script_location: File location of where text-based CLI scripts will be located if required by configuration file
    :type cleanup_script_location: str
    """

    def __init__(self, ztplfmg):
        super().__init__()
        self._fmg = ztplfmg
        self._logger = ztpllogging.get_logger()

    @property
    def ext_logger(self):
        """
        Get property to retrieve logging instance

        :return: A ZTPLLogging instance for logging perform function activity
        :rtype: ZTPLLogging
        """
        return self._logger

    @ext_logger.setter
    def ext_logger(self, logger):
        """
        Setter to set logging capability

        :param logger: ZTPLogging instance utilized to log perform function activity
        :type logger: ZTPLLogging
        """
        self._logger = logger

    @staticmethod
    def non_success_code_warning_str(class_name, code, *args):
        """
        Standard static function that returns a string denoting the fact that a code that was not 0 was returned

        :param class_name: Class name that has the issue
        :type class_name: str
        :param code: Code provided by FMG
        :type code: int
        :param args: Used in case specific information needs to be added to the default string. Helps with loops that have information that needs to be spelled out even more than the default
        :type args: str list
        :return: Static string denoting a consistent logging capability for code responses that are not 0
        :rtype: str
        """
        return f"While the {class_name} was performing its function the FMG returned a response code that indicated " \
               f"a non-successful response. Normally this means that data provided to the FMG was not correct for " \
               f"the call at hand. The data will be returned but likely the response does not contain the required " \
               f"data. The code returned from the FMG was {code}. " \
               f"{' Specifics are: ' + '. '.join(args) if args else ''}"

    @staticmethod
    def not_proper_parameter_info_str(class_name, device_name, *args):
        """
        Standard static function that returns a string denoting the fact that the required information to make the call was not provded as a parameter

        :param class_name: Class name that has the issue
        :type class_name: str
        :param device_name: Name of the device that is being provisioned during the exception
        :type device_name: str
        :return: Static string denoting a consistent logging capability for when perform is called on a class without the correct input information
        :rtype: str
        """
        return f"Information required to ensure the correct data was retrieved from the FMG was not presented to " \
               f"the process being performed by {class_name} while working on device {device_name}." \
               f"{' Specifics are: ' + '. '.join(args) if args else ''}"

    @staticmethod
    def task_exception_warning_str(class_name, device_name, *args):
        return f"Task exception encountered during a process being performed by {class_name} on " \
               f"device {device_name}. {' Specifics are: ' + '. '.join(args) if args else ''}"

    @staticmethod
    def generic_exception_warning_str(class_name, device_name, *args):
        return f"A generic exception was encountered during a process being performed by {class_name} " \
               f"on {device_name}. {' Specifics are: ' + '. '.join(args) if args else ''}"

    @abstractmethod
    def perform(self, **kwargs):
        """
        Abstract method used to perform some activity on the FMG

        :param kwargs: Key word arguments needed for the perform function to work when key-words are required
        :return: Return (code, result) consisting of the code returned as the first element and a result object dictionary or None
        :rtype: tuple
        """
        pass

    @abstractmethod
    def test_it(self, **kwargs):
        """
        Abstract method used to perform test activity on the FMG

        :param kwargs: Key word arguments needed for the perform function to work when key-words are required
        :return: Return (code, result) consisting of the code returned as the first element and a result object dictionary or None
        :rtype: tuple
        """
        pass

    @staticmethod
    def test_class_entry_log(class_name, ext_logger):
        ext_logger.info(f"Beginning a test process on the Action '{class_name}'")

    @staticmethod
    def test_required_entry_found(req_entry, class_name, ext_logger):
        ext_logger.info(f"Action passes - The information for '{req_entry}' was found and is proper to run "
                        f"the {class_name} action")

    @staticmethod
    def test_required_entry_not_found(req_entry, class_name, ext_logger):
        ext_logger.error(f"The '{req_entry}' information was not added and is required to run the {class_name} "
                         f"action. Please ensure your instruction file has the '{req_entry}' information as a "
                         f"member of the DATA_REQ")

    @staticmethod
    def test_possible_entry_log(poss_entry, ext_logger):
        ext_logger.warning(f"This action could require '{poss_entry}'. Please remember to provide those "
                           f"data if needed")

    @staticmethod
    def test_class_exit_log(class_name, ext_logger, passed=True):
        if passed:
            ext_logger.info(f"The Action '{class_name}' passed its testing process")
        else:
            ext_logger.warning(f"The Action '{class_name}' failed. See log entries above to determine data not being "
                               f"sent")

    @staticmethod
    def test_class_functionality(incoming_dict, instruct_req_list, class_name, *args):
        ext_logger = ztpllogging.get_logger()
        BaseFMGAction.test_class_entry_log(class_name, ext_logger)
        passed = True
        for req_entry in instruct_req_list:
            entry = incoming_dict.get(req_entry, False)
            if not entry:
                passed = False
                BaseFMGAction.test_required_entry_not_found(req_entry, class_name, ext_logger)
            else:
                BaseFMGAction.test_required_entry_found(req_entry, class_name, ext_logger)
        if args:
            for arg in args:
                BaseFMGAction.test_possible_entry_log(arg, ext_logger)
        BaseFMGAction.test_class_exit_log(class_name, ext_logger, passed)

    def handle_task_run(self, result_dict, proc_name, fgt_name, sleep_time=5, retrieval_fail_gate=10, timeout=120):
        """
        Function to handle all aspects of a task's process

        :param result_dict: Result of the call to the FMG returning a response about the task being monitored
        :type result_dict: dict
        :param proc_name: Name of the calling class
        :type proc_name: str
        :param fgt_name: FGT name that the FMG is working on for this task
        :type fgt_name: str
        :param sleep_time: Number of seconds to sleep between each task call. Default is 5 seconds
        :type sleep_time: int
        :param retrieval_fail_gate: Number of times a non-zero code response from a Task request is allowed. This is to ensure the task even exists and will give the FMG time to catch up if it is having issues. The Default is 10 times, but this is seldom used or changed
        :type retrieval_fail_gate: int
        :param timeout: Number of seconds that the Task is allowed to run before timing out. Default is 120 seconds, which is fine for most tasks, however for tasks such as Upgrading this may need to be upped significantly
        :type timeout: int
        :return: Return (code, result) tuple from FMG task consisting of the code returned as the first element and a result object dictionary
        :rtype: tuple
        :raises: FMGBaseException if no task id is found in the result_dict parameter or task id is found to be None. Also raised if a reply from a task call within the loop comes back with a num_err attribute missing entirely
        :raises: TaskTimedOutException if a task continues to run past the task timout time set in the PyFMG module
        :raises: TaskReportedErrorException if a call to the task returns with the num_err attribute having a value other than 0
        """

        task_code = 0
        taskid = None
        if "task" in result_dict or "taskid" in result_dict:
            taskid = result_dict.get("task")
            if taskid is None:
                taskid = result_dict.get("taskid")
        else:
            self.ext_logger.error(f"Error encountered during {proc_name} while provisioning {fgt_name}. "
                                  f"The task was either not created or not formatted correctly. "
                                  f"Terminating...please check issue manually")
            raise FMGBaseException
        if taskid is not None:
            task_code, task_res = self._fmg.track_task(taskid, sleep_time, retrieval_fail_gate, timeout)
            if task_code == 1:
                self.ext_logger.error(f"Error encountered during {proc_name} while provisioning {fgt_name}. "
                                      f"The task more than likely did not finish in time or correctly and as such "
                                      f"the process failed. Terminating...please check issue manually. "
                                      f"The Task ID is {taskid}")
                raise TaskTimedOutException
            elif task_code == 0:
                number_err = task_res.get("num_err")
                if number_err is None:
                    self.ext_logger.error(f"Error encountered during {proc_name} while provisioning {fgt_name}. "
                                          f"The task completed, but was not formatted correctly upon completion and "
                                          f"had no report on if there were errors within the process or not. "
                                          f"Terminating...please check issue manually. The Task ID is {taskid}")
                    raise FMGBaseException(f"Response returned did not have proper data to find task info")
                elif number_err != 0:
                    self.ext_logger.error(f"Error encountered during {proc_name} while provisioning {fgt_name}. "
                                          f"The task completed, but reported that there was an error during the run. "
                                          f"The number of errors reported is {number_err}. Terminating...please "
                                          f"check issue manually. The Task ID is {taskid}")
                    raise TaskReportedErrorException(f"Number of errors was {number_err}")
                else:
                    # return in case code wants to use task output
                    return task_code, task_res
        else:
            self.ext_logger.error(f"Error encountered during {proc_name} while provisioning {fgt_name}. "
                                  f"The task result from the create task process does not seem to have created a "
                                  f"sufficient task. Terminating...please check issue manually")
            raise FMGBaseException

    def handle_standard_exceptions(func):
        """
        Utilized as a decorator for all BaseFMGAction perform() functions. This wraps the functions in
        try..except blocks that catch the most problematic issues so the code does not need to be repeated on each
        Action

        :param func: Original perform() function reference
        :type func: function
        :return: Decorator function reference
        :rtype: function
        """
        def wrap_action(self, *args, **kwargs):
            ext_logger = ztpllogging.get_logger()
            if not kwargs:
                ext_logger.error(BaseFMGAction.not_proper_parameter_info_str(func.__class__.__name__,
                                                                             "No device name provided"))
                return CustomResponseCode.KEY_NOT_EXIST, None
            try:
                return func(self, **kwargs)
            except KeyError as ke:
                ext_logger.error(BaseFMGAction.not_proper_parameter_info_str(func.__class__.__name__,
                                                                             kwargs["devicename"], str(ke)))
                return CustomResponseCode.KEY_ERROR, None
            except (FMGBaseException, TaskReportedErrorException, TaskTimedOutException) as ex:
                ext_logger.error(BaseFMGAction.task_exception_warning_str(func.__class__.__name__,
                                                                          kwargs["devicename"], str(ex)))
                return CustomResponseCode.TASK_EXCEPTION, None
            except:
                ext_logger.error(BaseFMGAction.generic_exception_warning_str(func.__class__.__name__,
                                                                             kwargs["devicename"]))
                return CustomResponseCode.GEN_EXCEPTION, None
        return wrap_action

    handle_standard_exceptions = staticmethod(handle_standard_exceptions)


class ZTPLFortiManager(FortiManager):
    """
    Class utilized to embody functions that the FMG provides. ZTPLFortiManager utilizes pyFMG as a backend solution,
    but provides functions specific to ZTP

    :param host: IP Address or FQDN of FMG
    :type host: str
    :param user: Username of API user. Default is empty string
    :type user: str
    :param passwd: Password of API user. Default is empty string
    :type passwd: str
    :param debug: Sets debug options for FMG. If debug is set to true logging of all FMG actions will take place and be placed within the debug log
    :type debug: bool
    :param use_ssl: Mandates whether the FMG connection will use SSL. Default is True
    :type use_ssl: bool
    :param verify_ssl: Mandates whether the connection will verify the certificate on the FMG. Default is False
    :type verify_ssl: bool
    :param timeout: Timeout setting of the connection object that will connect to the FMG. Default is 300 seconds
    :type timeout: int
    :param disable_request_warnings: Mandates whether the connection request will log warnings about errors/exceptions. Default is False
    :type disable_request_warnings: bool
    """

    def __init__(self, host=None, user="", passwd="", debug=False, use_ssl=True,
                 verify_ssl=False, timeout=300, disable_request_warnings=False):
        super().__init__(host, user, passwd, debug, use_ssl, verify_ssl, timeout, disable_request_warnings)
        self._debug = debug

    def set_debug_logger(self, log_loc,
                         fmt=Formatter("%(asctime)s - %(name)s: %(message)s ", "%m/%d/%Y %I:%M:%S %p"),
                         *args):
        """
        Sets the logger for debug information from the FMG. By default this is a FileHandler located at log_loc.

        :param log_loc: Location for the default debug log handler
        :type log_loc: str
        :param fmt: Formatter for default log handler. Default is "%(asctime)s - %(name)s: %(message)s ", "%m/%d/%Y %I:%M:%S %p"
        :type fmt: logging.Formatter
        :param args: Args list of handlers added to FMG debug log capability
        """
        if self._debug:
            if args:
                for log_obj in args:
                    self.addHandler(log_obj)
            else:
                self.getLog("fmg.debug", INFO)
                fh = FileHandler(log_loc)
                fh.setLevel(INFO)
                fh.setFormatter(fmt)
                self.addHandler(fh)

    def get_unauthorized_devices(self):
        """
        Function that utilizes the FMG instance (self) and does a call to get all unregistered FGT devices

        :return: CustomResponse code that identifies if the process was successful, and the unregistered devices that were found (if any) in the format {fgt_sn: fgt_name, fgt_sn: fgt_name}. If there are no items found in the unregistered device API response, None is returned in place of the dictionary
        :rtype: tuple
        """
        ext_logger = ztpllogging.get_logger()
        try:
            ext_logger.info(f"Retrieving unregistered devices from FMG")
            code, res = self.get("/dvmdb/device", fields=["name", "sn"], filter=["mgmt_mode", "==", "UNREG"], loadsub=0)
            if code == CustomResponseCode.SUCCESS:
                if res:
                    if len(res) > 0:
                        unreg_dict_of_fgts = {n["sn"]: n["name"] for n in res if "fg" in n["sn"].lower()}
                        ext_logger.info(f"Found the following serial numbers as unregistered "
                                        f"devices: {', '.join(list(unreg_dict_of_fgts))}")
                        return code, unreg_dict_of_fgts
                else:
                    return CustomResponseCode.SUCCESS, {}
            else:
                ext_logger.warning(BaseFMGAction.non_success_code_warning_str("get_unauthorized_devices", code))
            return CustomResponseCode.NON_SUCCESS, None
        except:
            ext_logger.error(f"An exception was handled during the operation to retrieve unregistered devices "
                             f"from FMG. FMG possibly is not accessible or the credentials provided are "
                             f"incorrect.")
            return CustomResponseCode.GEN_EXCEPTION, None

    class AssignToDeviceGroups(BaseFMGAction):
        """
        Requires 'devicename', 'adom', and 'grouplists.groups_list'  k:v information

        Calling perform(key word arguments from configuration):

        **Instructs the FMG to make a FGT a member of the Device Group(s)**

        :param kwargs: FGT configuration dictionary (normally pulled from a YAML config file) required for the perform function. Requires 'devicename', 'adom', and 'groups'  k:v information
        :type kwargs: dict
        :return: Return (code, dictionary) tuple in the format (code from FMG response, {"groups": ["grp_name", "grp_name"]]}) of all unregistered devices found during the perform function call or tuple of (CustomCode, None) in the case that there is an exception or if the process was found to be not successful
        :rtype: tuple
        """

        def __init__(self, ztplfmg):
            super().__init__(ztplfmg)

        @BaseFMGAction.handle_standard_exceptions
        def perform(self, **kwargs):
            """
            Requires 'devicename', 'adom', and 'grouplists.groups_list'  k:v information
            Instructs the FMG to make a FGT a member of the Device Group(s)

            :param kwargs: FGT configuration dictionary (normally pulled from a YAML config file) required for the perform function. Requires 'devicename', 'adom', and 'groups'  k:v information
            :type kwargs: dict
            :return: Return (code, dictionary) tuple in the format (code from FMG response, {"groups": ["grp_name", "grp_name"]]}) of all unregistered devices found during the perform function call or tuple of (CustomCode, None) in the case that there is an exception or if the process was found to be not successful
            :rtype: tuple
            """
            successful_runs = []
            all_success = True
            for group in kwargs["group_lists"]:
                if group is not None:
                    self.ext_logger.info(f"Attempting to add FGT {kwargs['devicename']} to the {group} device group")
                    code, res = self._fmg.add(f"/dvmdb/adom/{kwargs['adom']}/group/{group}/object member",
                                              data=[{"name": kwargs["devicename"], "vdom": "root"}])
                    if code == CustomResponseCode.SUCCESS:
                        self.ext_logger.info(f"FGT {kwargs['devicename']} added successfully to the {group} group")
                        successful_runs.append(group)
                    else:
                        all_success = False
                        self.ext_logger.warning(
                            BaseFMGAction.non_success_code_warning_str(self.__class__.__name__, code,
                                                                       f"Group name affected is {group}"))
            if all_success:
                return CustomResponseCode.SUCCESS, {"groups": successful_runs}
            else:
                return CustomResponseCode.NON_SUCCESS, {"groups": successful_runs}

        def test_it(self, **kwargs):
            BaseFMGAction.test_class_functionality(kwargs, ["group_lists", ], self.__class__.__name__)

    class AssignMetaData(BaseFMGAction):
        """
        Requires 'devicename', 'adom', and 'meta' (metadata dictionary)  k:v information

        Calling perform(key word arguments from configuration):

        **Instructs the FMG to update a device's metadata with values that are sent from the configuration file**

        :param kwargs: FGT configuration dictionary (normally pulled from a YAML config file) required for the perform function. Requires 'devicename', 'adom', and 'meta' (metadata dictionary)  k:v information
        :type kwargs: dict
        :return: Return (code, dictionary) tuple in the format (code from FMG response, {"meta fields": meta_hash_none_removed}) or tuple of (CustomCode, None) in the case that there is an exception or if the process was found to be not successful
        :rtype: tuple
        """

        def __init__(self, ztplfmg):
            super().__init__(ztplfmg)

        def check_and_add_metadata(self, meta_required_hash, **kwargs):
            """
            Instructs the FMG to add Metadata fields if they are not already in the FMG Database

            :param meta_required_hash: Dictionary describing metadata that needs to updated on the FMG
            :type meta_required_hash: dict
            :param kwargs: FGT configuration dictionary pass from the internal perform function
            :type kwargs: dict
            :return: CustomResponseCode describing success or not
            :rtype: CustomResponseCode
            """
            code, res = self._fmg.get(f"/dvmdb/adom/{kwargs['adom']}/device/{kwargs['devicename']}",
                                      option=["get meta"], fields=["meta fields"])
            try:
                meta_field_required_hash_list = [
                    {"data": {"name": meta, "importance": "optional", "length": 255, "status": 1},
                     "url": "/dvmdb/_meta_fields/device"} for meta in list(meta_required_hash.keys()) if
                    meta not in list(res["meta fields"].keys())]
                if len(meta_field_required_hash_list) > 0:
                    code, res = self._fmg.free_form("add", data=meta_field_required_hash_list)
                    if code == CustomResponseCode.SUCCESS:
                        self.ext_logger.info(f"Metadata attribute(s) successfully added to the FMG")
                        return CustomResponseCode.SUCCESS
                else:
                    self.ext_logger.info(f"Metadata attribute(s) were not required to be added to the FMG")
                    return CustomResponseCode.SUCCESS
            except:
                self.ext_logger.error("Error encountered when adding metadata")
            return CustomResponseCode.NON_SUCCESS

        @BaseFMGAction.handle_standard_exceptions
        def perform(self, **kwargs):
            """
            Requires 'devicename', 'adom', and 'meta' (metadata dictionary)  k:v information
            Instructs the FMG to update a device's metadata with values that are sent from the configuration file

            :param kwargs: FGT configuration dictionary (normally pulled from a YAML config file) required for the perform function. Requires 'devicename', 'adom', and 'meta' (metadata dictionary)  k:v information
            :type kwargs: dict
            :return: Return (code, dictionary) tuple in the format (code from FMG response, {"meta fields": meta_hash_none_removed}) or tuple of (CustomCode, None) in the case that there is an exception or if the process was found to be not successful
            :rtype: tuple
            """
            meta_hash = kwargs["meta"]
            # ensure all are strings
            for k, v in meta_hash.items():
                meta_hash[k] = str(v)
            if meta_hash:
                # ensure anything with value of None or empty string is removed
                meta_hash_none_removed = {k: v for k, v in meta_hash.items() if v != "None" and v != ""}
                if meta_hash_none_removed:
                    # check if any metadata needs to be added to the FMG
                    self.ext_logger.info(f"Checking if metadata attributes need to be added to FMG")
                    code = self.check_and_add_metadata(meta_hash_none_removed, **kwargs)
                    if code == CustomResponseCode.SUCCESS:
                        self.ext_logger.info(f"Attempting to update FGT {kwargs['devicename']}'s metadata info")
                        code, res = self._fmg.update(f"/dvmdb/adom/{kwargs['adom']}/device/{kwargs['devicename']}",
                                                     meta___fields=meta_hash_none_removed)
                        if code == CustomResponseCode.SUCCESS:
                            self.ext_logger.info(f"Added metadata values successfully to {kwargs['devicename']}")
                            return CustomResponseCode.SUCCESS, {"meta fields": meta_hash_none_removed}
                        else:
                            self.ext_logger.error(
                                BaseFMGAction.non_success_code_warning_str(self.__class__.__name__, code))
                            return CustomResponseCode.NON_SUCCESS, None
            return CustomResponseCode.NON_SUCCESS, None

        def test_it(self, **kwargs):
            BaseFMGAction.test_class_functionality(kwargs, ["meta", ], self.__class__.__name__)

    class ChangePassword(BaseFMGAction):
        """
        Requires 'devicename', 'adom', and 'device_pw' k:v information

        Calling perform(key word arguments from configuration):

        **Instructs the FMG to update a device's password both on the device and on the FMG device db**

        :param kwargs: FGT configuration dictionary (normally pulled from a YAML config file) required for the perform function. Requires 'devicename', 'adom', and 'device_pw' k:v information
        :type kwargs: dict
        :return: Return (code, dictionary) tuple in the format (code from FMG response, {"success": True}) or tuple of (CustomCode, None) in the case that there is an exception or if the process was found to be not successful
        :rtype: tuple
        """

        def __init__(self, ztplfmg):
            super().__init__(ztplfmg)

        @BaseFMGAction.handle_standard_exceptions
        def perform(self, **kwargs):
            """
            Requires 'devicename', 'adom', and 'device_pw' k:v information
            Instructs the FMG to update a device's password both on the device and on the FMG device db

            :param kwargs: FGT configuration dictionary (normally pulled from a YAML config file) required for the perform function. Requires 'devicename', 'adom', and 'device_pw' k:v information
            :type kwargs: dict
            :return: Return (code, dictionary) tuple in the format (code from FMG response, {"success": True}) or tuple of (CustomCode, None) in the case that there is an exception or if the process was found to be not successful
            :rtype: tuple
            """
            self.ext_logger.info(f"Attempting to change the password on FGT {kwargs['devicename']}")
            code, res = self._fmg.update(f"/dvmdb/adom/{kwargs['adom']}/device/{kwargs['devicename']}",
                                         adm_pass=kwargs["device_pw"])
            if code == CustomResponseCode.SUCCESS:
                self.ext_logger.info(f"Password changed on the FMG Device DB for FGT {kwargs['devicename']}")
                self.ext_logger.info(f"Password change now being attempted on FGT {kwargs['devicename']} directly")
                pword_script_text = f"config system admin\nedit admin\nset password {kwargs['device_pw']}\nnext\nend"
                script_name = f"{kwargs['devicename']}_pword"
                code, res = self._fmg.set(f"/dvmdb/adom/{kwargs['adom']}/script/", content=pword_script_text,
                                          name=script_name, type="cli", target="remote_device")
                if code == CustomResponseCode.SUCCESS:
                    self.ext_logger.info(f"Script {script_name} has been created on the FMG. Executing script on "
                                         f"FGT {kwargs['devicename']}")
                    code, res = self._fmg.execute(f"/dvmdb/adom/{kwargs['adom']}/script/execute", script=script_name,
                                                  adom=kwargs["adom"],
                                                  scope=[{"name": kwargs["devicename"], "vdom": "root"}])
                    self.handle_task_run(res, type(self).__name__, kwargs["devicename"])
                    self.ext_logger.info(f"Password script {script_name} run successfully on "
                                         f"FGT {kwargs['devicename']}")
                    self.ext_logger.info(f"Attempting deletion of script {script_name} from FMG")
                    code, res = self._fmg.delete(f"/dvmdb/adom/{kwargs['adom']}/script/{script_name}")
                    if code == CustomResponseCode.SUCCESS:
                        self.ext_logger.info(f"The script {script_name} was deleted successfully from the FMG")
                        return CustomResponseCode.SUCCESS, {"success": True}
                    else:
                        self.ext_logger.warning(
                            f"The script {script_name} was not deleted successfully from the FMG. Please check the "
                            f"FMG manually and delete this script. Processing will continue.")
                else:
                    self.ext_logger.warning(f"Password change directly on FGT {kwargs['devicename']} did not complete "
                                            f"successfully. The FMG Device DB and the local FGT passwords do not "
                                            f"match. Please correct this manually or the FMG may have issues with "
                                            f"future actions on this FGT.")
            return CustomResponseCode.NON_SUCCESS, None

        def test_it(self, **kwargs):
            BaseFMGAction.test_class_functionality(kwargs, ["device_pw", ], self.__class__.__name__)

    class ApplyPolPkg(BaseFMGAction):
        """
        Requires 'devicename', pol_pkg, 'adom', and 'vdom_list' (if more vdoms than root) k:v information

        Calling perform(key word arguments from configuration):

        **Instructs the FMG to apply a policy package to a device**

        :param kwargs: FGT configuration dictionary (normally pulled from a YAML config file) required for the perform function. Requires 'devicename', pol_pkg, 'adom', and 'vdom_list' (if more vdoms than root) k:v information
        :type kwargs: dict
        :return: Return (code, dictionary) tuple in the format (code from FMG response, {"pol_pkg": kwargs["pol_pkg"]}) or tuple of (CustomCode, None) in the case that there is an exception or if the process was found to be not successful
        :rtype: tuple
        """

        def __init__(self, ztplfmg):
            super().__init__(ztplfmg)

        @BaseFMGAction.handle_standard_exceptions
        def perform(self, **kwargs):
            """
            Requires 'devicename', pol_pkg, 'adom', and 'vdom_list' (if more vdoms than root) k:v information
            Instructs the FMG to apply a policy package to a device

            :param kwargs: FGT configuration dictionary (normally pulled from a YAML config file) required for the perform function. Requires 'devicename', pol_pkg, 'adom', and 'vdom_list' (if more vdoms than root) k:v information
            :type kwargs: dict
            :return: Return (code, dictionary) tuple in the format (code from FMG response, {"pol_pkg": kwargs["pol_pkg"]}) or tuple of (CustomCode, None) in the case that there is an exception or if the process was found to be not successful
            :rtype: tuple
            """
            # handle vdoms
            scope = [{"name": kwargs["devicename"], "vdom": "root"}]
            if kwargs.get('vdom_lists', False):
                scope = [{"name": kwargs["devicename"], "vdom": vdom} for vdom in kwargs["vdom_lists"]]
            self.ext_logger.info(f"Attempting to assign FGT {kwargs['devicename']} as a target of the "
                                 f"policy package {kwargs['pol_pkg']}")
            code, res = self._fmg.add(f"/pm/pkg/adom/{kwargs['adom']}/{kwargs['pol_pkg']}/scope member",
                                      data=scope)
            if code == CustomResponseCode.SUCCESS:
                self.ext_logger.info(f"FGT {kwargs['devicename']} has been added as a target of the policy "
                                     f"package {kwargs['pol_pkg']} successfully")
                return CustomResponseCode.SUCCESS, {"pol_pkg": kwargs["pol_pkg"]}
            else:
                self.ext_logger.error(BaseFMGAction.non_success_code_warning_str(self.__class__.__name__, code))
            return CustomResponseCode.NON_SUCCESS, None

        def test_it(self, **kwargs):
            BaseFMGAction.test_class_functionality(kwargs, ["pol_pkg", ], self.__class__.__name__, "vdom_lists")

    class AssignSDWANTemplate(BaseFMGAction):
        """
        Requires 'devicename', 'adom', 'sd_wan', and 'vdom_list' (if more vdoms than root) k:v information

        Calling perform(key word arguments from configuration):

        **Instructs the FMG to add a device as a target of an SDWAN template**

        :param kwargs: FGT configuration dictionary (normally pulled from a YAML config file) required for the perform function. Requires 'devicename', 'adom', 'sd_wan', and 'vdom_list' (if more vdoms than root) k:v information
        :type kwargs: dict
        :return: Return (code, dictionary) tuple in the format (code from FMG response, {"sd_wan": kwargs["sd_wan"]}) or tuple of (CustomCode, None) in the case that there is an exception or if the process was found to be not successful
        :rtype: tuple
        """

        def __init__(self, ztplfmg):
            super().__init__(ztplfmg)

        @BaseFMGAction.handle_standard_exceptions
        def perform(self, **kwargs):
            """
            Requires 'devicename', 'adom', 'sd_wan', and 'vdom_list' (if more vdoms than root) k:v information
            Instructs the FMG to add a device as a target of an SDWAN template

            :param kwargs: FGT configuration dictionary (normally pulled from a YAML config file) required for the perform function. Requires 'devicename', 'adom', 'sd_wan', and 'vdom_list' (if more vdoms than root) k:v information
            :type kwargs: dict
            :return: Return (code, dictionary) tuple in the format (code from FMG response, {"sd_wan": kwargs["sd_wan"]}) or tuple of (CustomCode, None) in the case that there is an exception or if the process was found to be not successful
            :rtype: tuple
            """
            # handle vdoms
            scope = [{"name": kwargs["devicename"], "vdom": "root"}]
            if kwargs.get('vdom_lists', False):
                scope = [{"name": kwargs["devicename"], "vdom": vdom} for vdom in kwargs["vdom_lists"]]
            self.ext_logger.info(f"Attempting to assign FGT {kwargs['devicename']} as a target of the "
                                 f"SD-WAN template {kwargs['sd_wan']}")
            sdwan_add_info = [
                {
                    "data": scope,
                    "url": f"/pm/wanprof/adom/{kwargs['adom']}/{kwargs['sd_wan']}/scope member",
                }
            ]
            code, res = self._fmg.free_form("add", data=sdwan_add_info)
            if code == CustomResponseCode.SUCCESS:
                self.ext_logger.info(f"FGT {kwargs['devicename']} has been added as a target of the SD-WAN "
                                     f"template {kwargs['sd_wan']} successfully")
                return CustomResponseCode.SUCCESS, {"sd_wan": kwargs["sd_wan"]}
            else:
                self.ext_logger.error(BaseFMGAction.non_success_code_warning_str(self.__class__.__name__, code))
            return CustomResponseCode.NON_SUCCESS, None

        def test_it(self, **kwargs):
            BaseFMGAction.test_class_functionality(kwargs, ["sd_wan", ], self.__class__.__name__, "vdom_lists")

    class InstallPolicyPackage(BaseFMGAction):
        """
        Requires 'pol_pkg', 'adom', 'devicename', 'vdom_list' (if more vdoms) k:v information

        Calling perform(key word arguments from configuration):

        **Instructs the FMG to execute the installation of a policy package on a device**

        :param kwargs: FGT configuration dictionary (normally pulled from a YAML config file) required for the perform function. Requires 'pol_pkg', 'adom', 'devicename', 'vdom_list' (if more vdoms) k:v information
        :type kwargs: dict
        :return: Return (code, dictionary) tuple in the format (code from FMG response, {"scope": scope, "pol_pkg": kwargs["pol_pkg"]}) or tuple of (CustomCode, None) in the case that there is an exception or if the process was found to be not successful
        :rtype: tuple
        """

        def __init__(self, ztplfmg):
            super().__init__(ztplfmg)

        @BaseFMGAction.handle_standard_exceptions
        def perform(self, **kwargs):
            """
            Requires 'pol_pkg', 'adom', 'devicename', 'vdom_list' (if more vdoms) k:v information
            Instructs the FMG to execute the installation of a policy package on a device

            :param kwargs: FGT configuration dictionary (normally pulled from a YAML config file) required for the perform function. Requires 'pol_pkg', 'adom', 'devicename', 'vdom_list' (if more vdoms) k:v information
            :type kwargs: dict
            :return: Return (code, dictionary) tuple in the format (code from FMG response, {"scope": scope, "pol_pkg": kwargs["pol_pkg"]}) or tuple of (CustomCode, None) in the case that there is an exception or if the process was found to be not successful
            :rtype: tuple
            """
            # handle vdoms
            scope = [{"name": kwargs["devicename"], "vdom": "root"}]
            if kwargs.get('vdom_lists', False):
                scope = [{"name": kwargs["devicename"], "vdom": vdom} for vdom in kwargs["vdom_lists"]]

            self.ext_logger.info(f"Attempting the installation of Policy Package {kwargs['pol_pkg']}")
            code, res = self._fmg.execute("securityconsole/install/package", adom=kwargs["adom"],
                                          scope=scope, pkg=kwargs["pol_pkg"])
            if code == CustomResponseCode.SUCCESS:
                self.ext_logger.info(f"Policy Package {kwargs['pol_pkg']} has been set for execution on "
                                     f"FGT {kwargs['devicename']}")
                self.handle_task_run(res, type(self).__name__, kwargs["devicename"])
                self.ext_logger.info(f"Policy Package {kwargs['pol_pkg']} reported successful completion on "
                                     f"FGT {kwargs['devicename']}")
                return CustomResponseCode.SUCCESS, {"scope": scope, "pol_pkg": kwargs["pol_pkg"]}

            self.ext_logger.error(BaseFMGAction.non_success_code_warning_str(self.__class__.__name__, code))
            return CustomResponseCode.NON_SUCCESS, None

        def test_it(self, **kwargs):
            BaseFMGAction.test_class_functionality(kwargs, ["pol_pkg", ], self.__class__.__name__, "vdom_lists")

    class ExecuteCLITemplateGrp(BaseFMGAction):
        """
        Requires 'cli_template_groups.name', 'adom', 'devicename', and 'vdom_list' (if more vdoms) k:v information

        Calling perform(key word arguments from configuration):

        **Instructs the FMG to assign a CLI Template Group, execute it (if told to do so in the configuration information), and then remove it from assignment (again if told to do so in the configuration information) on a device**

        :param kwargs: FGT configuration dictionary (normally pulled from a YAML config file) required for the perform function. Requires 'cli_template_groups.name', 'adom', 'devicename', and 'vdom_list' (if more vdoms) k:v information
        :type kwargs: dict
        :return: Return (code, dictionary) tuple in the format (code from FMG response, {"template_groups": [list of templates run]]}) or tuple of (CustomCode, None) in the case that there is an exception or if the process was found to be not successful
        :rtype: tuple
        """

        def __init__(self, ztplfmg):
            super().__init__(ztplfmg)

        @BaseFMGAction.handle_standard_exceptions
        def perform(self, **kwargs):
            """
            Requires 'cli_template_groups.name', 'adom', 'devicename', and 'vdom_list' (if more vdoms) k:v information
            Instructs the FMG to assign a CLI Template Group, execute it (if told to do so in the configuration information), and then remove it from assignment (again if told to do so in the configuration information) on a device

            :param kwargs: FGT configuration dictionary (normally pulled from a YAML config file) required for the perform function. Requires 'cli_template_groups.name', 'adom', 'devicename', and 'vdom_list' (if more vdoms) k:v information
            :type kwargs: dict
            :return: Return (code, dictionary) tuple in the format (code from FMG response, {"template_groups": [list of templates run]]}) or tuple of (CustomCode, None) in the case that there is an exception or if the process was found to be not successful
            :rtype: tuple
            """
            # handle vdoms
            scope = [{"name": kwargs["devicename"], "vdom": "root"}]
            if kwargs.get('vdom_lists', False):
                scope = [{"name": kwargs["devicename"], "vdom": vdom} for vdom in kwargs["vdom_lists"]]
            self.ext_logger.info(f"Attempting the execution of CLI template "
                                 f"group{'s' if len(kwargs['cli_template_groups']) > 1 else ''}")
            successful_runs = []
            all_success = True
            for cli_template_group in kwargs["cli_template_groups"]:
                code, res = self._fmg.add(f"/pm/config/adom/{kwargs['adom']}/obj/cli/"
                                          f"template-group/{cli_template_group['name']}/scope member",
                                          data=scope)
                if code == CustomResponseCode.SUCCESS:
                    self.ext_logger.info(f"FGT {kwargs['devicename']} has been added as a target "
                                         f"to {cli_template_group['name']}")
                    if cli_template_group["execute"][0].lower() == "y":
                        code, res = self._fmg.execute(f"securityconsole/install/device",
                                                      scope=scope,
                                                      adom=kwargs["adom"], flags=["install_chg", ])
                        if code == CustomResponseCode.SUCCESS:
                            self.ext_logger.info(f"CLI Template Group {cli_template_group['name']} has been set for "
                                                 f"execution on FGT {kwargs['devicename']}")
                            self.handle_task_run(res, type(self).__name__, kwargs["devicename"])
                            self.ext_logger.info(f"CLI Template Group {cli_template_group['name']} reported successful "
                                                 f"completion on FGT {kwargs['devicename']}")
                            successful_runs.append(cli_template_group)
                        else:
                            all_success = False
                            self.ext_logger.warning(
                                BaseFMGAction.non_success_code_warning_str(self.__class__.__name__, code,
                                                                            f"Template group affected is "
                                                                            f"{cli_template_group}"))
                    else:
                        self.ext_logger.info(f"The CLI Template Group {cli_template_group['name']} is not set to "
                                             f"execute")
                        continue  # no use checking if one that is set not to execute should be deleted
                else:
                    all_success = False
                    self.ext_logger.warning(
                        BaseFMGAction.non_success_code_warning_str(self.__class__.__name__, code,
                                                                   f"Template group affected is "
                                                                   f"{cli_template_group}"))
                    continue  # no use checking if one that is set not to execute should be deleted
                # if not marked to remain delete it. if remain not on this object consider it needing to be removed
                try:
                    if cli_template_group["remain"][0].lower() == "n":
                        code, res = self._fmg.delete(f"/pm/config/adom/{kwargs['adom']}/obj/cli/"
                                                     f"template-group/{cli_template_group['name']}/scope member",
                                                     data=scope)
                        if code == CustomResponseCode.SUCCESS:
                            self.ext_logger.info(f"FGT {kwargs['devicename']} has been removed as a target for "
                                                 f"{cli_template_group['name']}")
                    else:
                        self.ext_logger.info(f"FGT {kwargs['devicename']} remains as a target to "
                                             f"{cli_template_group['name']} as instructed by the configuration")
                except (KeyError, IndexError):
                    code, res = self._fmg.delete(f"/pm/config/adom/{kwargs['adom']}/obj/cli/template-group/"
                                                 f"{cli_template_group['name']}/scope member",
                                                 data=scope)
                    if code == CustomResponseCode.SUCCESS:
                        self.ext_logger.info(f"FGT {kwargs['device']} has been removed as a target for "
                                             f"{cli_template_group['name']}")
            if all_success:
                return CustomResponseCode.SUCCESS, {"template_groups": successful_runs}
            else:
                return CustomResponseCode.NON_SUCCESS, {"template_groups": successful_runs}

        def test_it(self, **kwargs):
            BaseFMGAction.test_class_functionality(kwargs, ["cli_template_groups", ], self.__class__.__name__,
                                                   "vdom_lists")

    class ExecuteCLIScriptGrp(BaseFMGAction):
        """
        Requires 'cli_script_groups.name', 'adom' 'devicename', 'vdom_list' (if more vdoms), and pol_pkg (if run on pp) k:v information

        Calling perform(key word arguments from configuration):

        **Instructs the FMG to execute a CLI Script Group on the FMG**

        :param kwargs: FGT configuration dictionary (normally pulled from a YAML config file) required for the perform function. Requires 'cli_script_groups.name', 'adom' 'devicename', 'vdom_list' (if more vdoms), and pol_pkg (if run on pp) k:v information
        :type kwargs: dict
        :return: Return (code, dictionary) tuple in the format (code from FMG response, {"scripts_groups": [successful script group list]]}) or tuple of (CustomCode, None) in the case that there is an exception or if the process was found to be not successful
        :rtype: tuple
        """

        def __init__(self, ztplfmg):
            super().__init__(ztplfmg)

        @BaseFMGAction.handle_standard_exceptions
        def perform(self, **kwargs):
            """
            Requires 'cli_script_groups.name', 'adom' 'devicename', 'vdom_list' (if more vdoms), and pol_pkg (if run on pp) k:v information
            Instructs the FMG to execute a CLI Script Group on the FMG

            :param kwargs: FGT configuration dictionary (normally pulled from a YAML config file) required for the perform function. Requires 'cli_script_groups.name', 'adom' 'devicename', 'vdom_list' (if more vdoms), and pol_pkg (if run on pp) k:v information
            :type kwargs: dict
            :return: Return (code, dictionary) tuple in the format (code from FMG response, {"scripts_groups": [successful script group list]]}) or tuple of (CustomCode, None) in the case that there is an exception or if the process was found to be not successful
            :rtype: tuple
            """
            # handle vdoms
            scope = [{"name": kwargs["devicename"], "vdom": "root"}]
            if kwargs.get('vdom_lists', False):
                scope = [{"name": kwargs["devicename"], "vdom": vdom} for vdom in kwargs["vdom_lists"]]
            self.ext_logger.info(f"Attempting the execution of CLI script "
                                 f"group{'s' if len(kwargs['cli_script_groups']) > 1 else ''}")
            successful_runs = []
            all_success = True
            for cli_script in kwargs["cli_script_groups"]:
                if kwargs.get("pol_pkg", False):
                    code, res = self._fmg.execute(f"/dvmdb/adom/{kwargs['adom']}/script/execute", script=cli_script,
                                                  adom=kwargs["adom"], scope=scope, package=kwargs["pol_pkg"])
                else:
                    code, res = self._fmg.execute(f"/dvmdb/adom/{kwargs['adom']}/script/execute", script=cli_script,
                                                  adom=kwargs["adom"], scope=scope)
                if code == CustomResponseCode.SUCCESS:
                    self.ext_logger.info(f"CLI script {cli_script} has been set for "
                                         f"execution during FGT {kwargs['devicename']}'s provisioning process")
                    self.handle_task_run(res, type(self).__name__, kwargs["devicename"])
                    self.ext_logger.info(f"CLI script {cli_script} reported successful completion during FGT "
                                    f"{kwargs['devicename']}'s provisioning process")
                    successful_runs.append(cli_script)
                else:
                    all_success = False
                    self.ext_logger.warning(
                        BaseFMGAction.non_success_code_warning_str(self.__class__.__name__, code,
                                                                   f"Script group affected is {cli_script}"))
            if all_success:
                return CustomResponseCode.SUCCESS, {"scripts_groups": successful_runs}
            else:
                return CustomResponseCode.NON_SUCCESS, {"scripts_groups": successful_runs}

        def test_it(self, **kwargs):
            BaseFMGAction.test_class_functionality(kwargs, ["cli_script_groups", ], self.__class__.__name__,
                                                   "vdom_lists")

    class ExecuteLocalCLIScript(BaseFMGAction):
        """
        Requires 'local_cli_scripts.groupname', 'local_cli_scripts.location', 'adom' and 'devicename', 'pol_pkg' (if running on policy package), and 'vdom_list' (if more vdoms) k:v information

        Calling perform(key word arguments from configuration):

        **Instructs the FMG to find a local script in a location on the local directory, render the script using Jinja2, apply it to the FMG and then either execute it directly on a device, on a device db, or on a pol pkg on the FMG based on the configuration file setting and then delete the script
        'local_cli_scripts.scripts_location will default to a directory local to script path/local_scr/**

        :param kwargs: FGT configuration dictionary (normally pulled from a YAML config file) required for the perform function. Requires 'local_cli_scripts.groupname', 'local_cli_scripts.location', 'adom' and 'devicename', 'pol_pkg' (if running on policy package), and 'vdom_list' (if more vdoms) k:v information
        :type kwargs: dict
        :return: Return (code, dictionary) tuple in the format (code from FMG response, {"local_scripts": [successful local scripts that were run]}) or tuple of (CustomCode, None) in the case that there is an exception or if the process was found to be not successful
        :rtype: tuple
        """

        def __init__(self, ztplfmg):
            super().__init__(ztplfmg)
            self._created_scripts = []

        def __script_exists(self, path, devicename):
            if os.path.exists(path):
                return True
            else:
                self.ext_logger.error(f"Error encountered during execution processes on {devicename}. "
                                      f"The location for scripts is set for {path} but does not exist. "
                                      f"Please ensure the script repository on the automation machine is "
                                      f"in the correct location and the correct scripts are created and named "
                                      f"appropriately. Terminating...please check issue manually")
                return False

        def __delete_scripts(self, scripts_created, **kwargs):
            if len(scripts_created) > 0:
                for script_name_on_fmg in scripts_created:
                    code, res = self._fmg.delete(
                        f"/dvmdb/adom/{kwargs['adom']}/script/{script_name_on_fmg}")
                    if code == CustomResponseCode.SUCCESS:
                        self.ext_logger.info(
                            f"The script {script_name_on_fmg} was deleted successfully from the FMG")
                    else:
                        self.ext_logger.warning(
                            f"The script {script_name_on_fmg} was not deleted successfully from the FMG. "
                            f"Please check the FMG manually and delete this script. Deletion process will "
                            f"continue, as this is not seen as a critical failure")

        @BaseFMGAction.handle_standard_exceptions
        def perform(self, **kwargs):
            """
            Requires 'local_cli_scripts.groupname', 'local_cli_scripts.location', 'adom' and 'devicename', 'pol_pkg' (if running on policy package), and 'vdom_list' (if more vdoms) k:v information
            Instructs the FMG to find a local script in a location on the local directory, render the script using Jinja2, apply it to the FMG and then either execute it directly on a device, on a device db, or on a pol pkg on the FMG based on the configuration file setting and then delete the script
            'local_cli_scripts.scripts_location will default to a directory local to script path/local_scr/

            :param kwargs: FGT configuration dictionary (normally pulled from a YAML config file) required for the perform function. Requires 'local_cli_scripts.groupname', 'local_cli_scripts.location', 'adom' and 'devicename', 'pol_pkg' (if running on policy package), and 'vdom_list' (if more vdoms) k:v information
            :type kwargs: dict
            :return: Return (code, dictionary) tuple in the format (code from FMG response, {"local_scripts": [successful local scripts that were run]}) or tuple of (CustomCode, None) in the case that there is an exception or if the process was found to be not successful
            :rtype: tuple
            """
            if kwargs.get("scripts_location", None) is None:
                kwargs["scripts_location"] = os.path.join(os.path.dirname(sys.argv[0]), "local_scr/")
            self.ext_logger.info(f"Attempting the execution of local CLI "
                                 f"script{'s' if len(kwargs['local_cli_scripts']) > 1 else ''}")
            # handle vdoms
            scope = [{"name": kwargs["devicename"], "vdom": "root"}]
            if kwargs.get('vdom_lists', False):
                scope = [{"name": kwargs["devicename"], "vdom": vdom} for vdom in kwargs["vdom_lists"]]
            # need a reference to this if object dies
            successful_runs = []
            scripts_created = []
            all_success = True
            for local_cli_script in kwargs["local_cli_scripts"]:
                script_loc = os.path.join(kwargs["scripts_location"], local_cli_script.get("name", ""))
                if not self.__script_exists(script_loc, kwargs["devicename"]):
                    all_success = False
                    return CustomResponseCode.NON_SUCCESS, None
                script_name_on_fmg = f"{local_cli_script['name']}_{datetime.datetime.now().microsecond}"
                target = local_cli_script.get("run_on", "").lower()
                if target == "db" or target == "device_db":
                    target = "device_database"
                elif target == "pol_pkg" or target == "pp" or target == "adom" or target == "adom_database":
                    target = "adom_database"
                else:
                    target = "remote_device"
                template_out = ""
                with open(script_loc, "r", encoding="utf-8-sig") as scr_fil:
                    script_contents = scr_fil.read()
                    template_out = Template(script_contents).render(**kwargs)
                code, res = self._fmg.set(f"/dvmdb/adom/{kwargs['adom']}/script/", content=template_out,
                                          name=script_name_on_fmg, type="cli", target=target)
                if code == CustomResponseCode.SUCCESS:
                    scripts_created.append(script_name_on_fmg)
                    self.ext_logger.info(f"Script {script_name_on_fmg} has been created on the FMG and is being "
                                         f"executed")
                    if target == "adom_database":
                        code, res = self._fmg.execute(f"/dvmdb/adom/{kwargs['adom']}/script/execute",
                                                      adom=kwargs["adom"], script=script_name_on_fmg,
                                                      package=kwargs["pol_pkg"], scope=scope,
                                                      flags=["create_task", "nonblocking"])
                    else:
                        code, res = self._fmg.execute(f"/dvmdb/adom/{kwargs['adom']}/script/execute",
                                                      adom=kwargs["adom"], script=script_name_on_fmg, scope=scope,
                                                      flags=["create_task", "nonblocking"])
                    try:
                        self.handle_task_run(res, type(self).__name__, kwargs["devicename"])
                        self.ext_logger.info(f"CLI script {script_name_on_fmg} run successfully during FGT "
                                             f"{kwargs['devicename']} provisioning")
                        successful_runs.append(script_name_on_fmg)
                    except (TaskReportedErrorException, TaskTimedOutException, FMGBaseException):
                        self.ext_logger.warning(f"Due to the previous exception that was logged, the script that had "
                                                f"issues - {script_name_on_fmg} - will not be deleted. This should "
                                                f"give the author the capability to identify what the problem with "
                                                f"{script_name_on_fmg} is. However, after the process is over, the "
                                                f"script will need to be deleted manually")
                        try:
                            scripts_created.remove(script_name_on_fmg)
                        except ValueError:
                            self.ext_logger.warning(f"A removal attempt was made against a script that was not in the "
                                                    f"scripts_created collection. This is not harmful to the overall "
                                                    f"process but is indicative of a possible issue with the "
                                                    f"underlying concept. Report this warning to the developer if "
                                                    f"possible. The script name that was attempted to be removed was "
                                                    f"{script_name_on_fmg}")
                else:
                    all_success = False
                    self.ext_logger.error(f"The script {script_name_on_fmg} was not created successfully on the FMG. "
                                          f"Stopping execution of all cleanup scripts and terminating provisioning "
                                          f"process. Please check the FMG and this device manually")
            self.__delete_scripts(scripts_created, **kwargs)
            if all_success:
                return CustomResponseCode.SUCCESS, {"local_scripts": successful_runs}
            else:
                return CustomResponseCode.NON_SUCCESS, {"local_scripts": successful_runs}

        def test_it(self, **kwargs):
            BaseFMGAction.test_class_functionality(kwargs, ["local_cli_scripts", ], self.__class__.__name__,
                                                   "vdom_lists", "pol_pkg")

    class InstallDevice(BaseFMGAction):
        """
        Requires 'adom', 'devicename', and 'vdom_list' (if more vdoms) k:v information

        Calling perform(key word arguments from configuration):

        **Instructs the FMG to execute the installation of a device configuration on a device**

        :param kwargs: FGT configuration dictionary (normally pulled from a YAML config file) required for the perform function. Requires 'adom', 'devicename', and 'vdom_list' (if more vdoms) k:v information
        :type kwargs: dict
        :return: Return (code, dictionary) tuple in the format (code from FMG response, {"success": True}) or tuple of (CustomCode, None) in the case that there is an exception or if the process was found to be not successful
        :rtype: tuple
        """

        def __init__(self, ztplfmg):
            super().__init__(ztplfmg)

        @BaseFMGAction.handle_standard_exceptions
        def perform(self, **kwargs):
            """
            Requires 'adom', 'devicename', and 'vdom_list' (if more vdoms) k:v information
            Instructs the FMG to execute the installation of a device configuration on a device

            :param kwargs: FGT configuration dictionary (normally pulled from a YAML config file) required for the perform function. Requires 'adom', 'devicename', and 'vdom_list' (if more vdoms) k:v information
            :type kwargs: dict
            :return: Return (code, dictionary) tuple in the format (code from FMG response, {"success": True}) or tuple of (CustomCode, None) in the case that there is an exception or if the process was found to be not successful
            :rtype: tuple
            """
            # handle vdoms
            scope = [{"name": kwargs["devicename"], "vdom": "root"}]
            if kwargs.get('vdom_lists', False):
                scope = [{"name": kwargs["devicename"], "vdom": vdom} for vdom in kwargs["vdom_lists"]]
            code, res = self._fmg.execute(f"securityconsole/install/device", scope=scope, adom=kwargs["adom"],
                                          flags=["install_chg", ])
            if code == CustomResponseCode.SUCCESS:
                self.ext_logger.info(f"Device installation set for {kwargs['devicename']}")
                self.handle_task_run(res, type(self).__name__, kwargs["devicename"])
                self.ext_logger.info(f"Device installation on {kwargs['devicename']} reported successful completion")
                return CustomResponseCode.SUCCESS, {"success": True}
            else:
                self.ext_logger.warning(
                    BaseFMGAction.non_success_code_warning_str(self.__class__.__name__, code,
                                                                f"Device affected was {kwargs['devicename']}"))
            return CustomResponseCode.NON_SUCCESS, None

        def test_it(self, **kwargs):
            BaseFMGAction.test_class_functionality(kwargs, ["devicename", ], self.__class__.__name__,
                                                   "vdom_lists")

    class DeleteDevice(BaseFMGAction):
        """
        Requires 'devicename' and 'adom' k:v information

        Calling perform(key word arguments from configuration):

        **Instructs the FMG to delete a FGT from the managed device list**

        :param kwargs: FGT configuration dictionary (normally pulled from a YAML config file) required for the perform function. Requires 'devicename' and 'adom' k:v information
        :type kwargs: dict
        :return: Return (code, dictionary) tuple in the format (code from FMG response, {"device": device name}) or tuple of (CustomCode, None) in the case that there is an exception or if the process was found to be not successful
        :rtype: tuple
        """

        def __init__(self, ztplfmg):
            super().__init__(ztplfmg)

        @BaseFMGAction.handle_standard_exceptions
        def perform(self, **kwargs):
            """
            Requires 'devicename' and 'adom' k:v information
            Instructs the FMG to delete a registered device from the FMG

            :param kwargs: FGT configuration dictionary (normally pulled from a YAML config file) required for the perform function. Requires 'devicename' and 'adom' k:v information
            :type kwargs: dict
            :return: Return (code, dictionary) tuple in the format (code from FMG response, {"device": device name}) or tuple of (CustomCode, None) in the case that there is an exception or if the process was found to be not successful
            :rtype: tuple
            """
            self.ext_logger.info(f"Attempting the deletion of FGT {kwargs['devicename']} from the "
                                 f"{kwargs['adom']} ADOM")
            code, res = self._fmg.execute("dvm/cmd/del/dev-list", adom=kwargs["adom"],
                                          del__dev__member__list=[{"name": kwargs["devicename"]}])
            if code == CustomResponseCode.SUCCESS:
                self.ext_logger.info(f"FGT {kwargs['devicename']} deleted as a managed device from the "
                                     f"{kwargs['adom']} ADOM")
                return CustomResponseCode.SUCCESS, {"device": kwargs["devicename"]}
            else:
                self.ext_logger.error(BaseFMGAction.non_success_code_warning_str(self.__class__.__name__, code))
            return CustomResponseCode.NON_SUCCESS, None

        def test_it(self, **kwargs):
            BaseFMGAction.test_class_functionality(kwargs, ["devicename", ], self.__class__.__name__)

    class PromoteDevice(BaseFMGAction):
        """
        Requires 'serialnumber' and 'adom' k:v information

        Calling perform(key word arguments from configuration):

        **Instructs the FMG to promote an unregistered device to a specific adom**

        :param kwargs: FGT configuration dictionary (normally pulled from a YAML config file) required for the perform function. Requires 'serialnumber' and 'adom' k:v information
        :type kwargs: dict
        :return: Return (code, dictionary) tuple in the format (code from FMG response, {"device action": "promote_unreg", "mgmt_mode": "fmg", "name": name of fmg, "adm_usr": "admin"}) or tuple of (CustomCode, None) in the case that there is an exception or if the process was found to be not successful
        :rtype: tuple
        """

        def __init__(self, ztplfmg):
            super().__init__(ztplfmg)

        @BaseFMGAction.handle_standard_exceptions
        def perform(self, **kwargs):
            """
            Requires 'serialnumber' and 'adom' k:v information
            Instructs the FMG to promote an unregistered device to a specific adom

            :param kwargs: FGT configuration dictionary (normally pulled from a YAML config file) required for the perform function. Requires 'serialnumber' and 'adom' k:v information
            :type kwargs: dict
            :return: Return (code, dictionary) tuple in the format (code from FMG response, {"device action": "promote_unreg", "mgmt_mode": "fmg", "name": name of fmg, "adm_usr": "admin"}) or tuple of (CustomCode, None) in the case that there is an exception or if the process was found to be not successful
            :rtype: tuple
            """
            device = {
                "device action": "promote_unreg",
                "mgmt_mode": "fmg",
                "name": kwargs["serialnumber"],
                "adm_usr": "admin"
            }
            self.ext_logger.info(f"Attempting the promotion of FGT identified as {kwargs['serialnumber']} to "
                                 f"the {kwargs['adom']} ADOM")
            code, res = self._fmg.execute("/dvm/cmd/add/device", adom=kwargs["adom"], device=device,
                                          flags=["create_task", "nonblocking"])
            if code == CustomResponseCode.SUCCESS:
                self.handle_task_run(res, type(self).__name__, kwargs["serialnumber"])
                self.ext_logger.info(f"FGT {kwargs['devicename']} added as a managed device in "
                                     f"the {kwargs['adom']} ADOM")
                return CustomResponseCode.SUCCESS, device
            else:
                self.ext_logger.error(BaseFMGAction.non_success_code_warning_str(self.__class__.__name__, code))
            return CustomResponseCode.NON_SUCCESS, None

        def test_it(self, **kwargs):
            BaseFMGAction.test_class_functionality(kwargs, ["devicename", ], self.__class__.__name__)

    class AssignDeviceName(BaseFMGAction):
        """
        Requires 'serialnumber', 'devicename', and 'adom' k:v information

        Calling perform(key word arguments from configuration):

        **Instructs the FMG to set the devicename of a device on the FMG so it can be used as a handle for the device throughout the provision process**

        :param kwargs: FGT configuration dictionary (normally pulled from a YAML config file) required for the perform function. 'serialnumber', 'devicename', and 'adom' k:v information
        :type kwargs: dict
        :return: Return (code, dictionary) tuple in the format (code from FMG response, {"name": kwargs["devicename"], "serialnumber": kwargs["serialnumber"]) or tuple of (CustomCode, None) in the case that there is an exception or if the process was found to be not successful
        :rtype: tuple
        """

        def __init__(self, ztplfmg):
            super().__init__(ztplfmg)

        @BaseFMGAction.handle_standard_exceptions
        def perform(self, **kwargs):
            """
            Requires 'serialnumber', 'devicename', and 'adom' k:v information
            Instructs the FMG to set the devicename of a device on the FMG so it can be used as a handle for the device throughout the provision process

            :param kwargs: FGT configuration dictionary (normally pulled from a YAML config file) required for the perform function. 'serialnumber', 'devicename', and 'adom' k:v information
            :type kwargs: dict
            :return: Return (code, dictionary) tuple in the format (code from FMG response, {"name": kwargs["devicename"], "serialnumber": kwargs["serialnumber"]) or tuple of (CustomCode, None) in the case that there is an exception or if the process was found to be not successful
            :rtype: tuple
            """
            self.ext_logger.info(f"Attempting to update the device name for the FGT with identified as "
                                 f"{kwargs['serialnumber']} after promotion to {kwargs['devicename']}")
            code, res = self._fmg.update(f"/dvmdb/adom/{kwargs['adom']}/device/{kwargs['serialnumber']}",
                                         name=kwargs["devicename"])
            if code == CustomResponseCode.SUCCESS:
                self.ext_logger.info(f"FGT identified as {kwargs['serialnumber']} after promotion had its devicename on "
                                     f"the system changed to {kwargs['devicename']} successfully")
                return CustomResponseCode.SUCCESS, {"name": kwargs["devicename"],
                                                    "serialnumber": kwargs["serialnumber"]}
            else:
                self.ext_logger.error(BaseFMGAction.non_success_code_warning_str(self.__class__.__name__, code))
            return CustomResponseCode.NON_SUCCESS, None

        def test_it(self, **kwargs):
            BaseFMGAction.test_class_functionality(kwargs, ["devicename", ], self.__class__.__name__)

    class CheckDeviceIsAlive(BaseFMGAction):
        """
        Requires 'devicename', 'adom', 'timers.timer' k:v information

        Calling perform(key word arguments from configuration):

        **Instructs the application to check for a response from a get system status call on the FGT**

        :param kwargs: FGT configuration dictionary (normally pulled from a YAML config file) required for the perform function. 'devicename', 'adom', 'timers.timer', k:v information
        :type kwargs: dict
        :return: Return (code, dictionary) tuple in the format (code from FMG response, {"target": kwargs["devicename"]}) or tuple of (CustomCode, None) in the case that there is an exception or if the process was found to be not successful
        :rtype: tuple
        """

        def __init__(self, ztplfmg):
            super().__init__(ztplfmg)

        def __fgt_responded(self, **kwargs):
            # WON'T WORK ON 5.6 FGTs
            inner_dict = {
                "action": "get",
                "resource": "/api/v2/monitor/system/status/select",
                "target": [f"adom/{kwargs['adom']}/device/{kwargs['devicename']}"]
            }
            try:
                code, res = self._fmg.execute("sys/proxy/json", data=inner_dict)
                if code == CustomResponseCode.SUCCESS:
                    status = res[0]["response"].get("status", "failed")
                    if status == "success":
                        return {"success": True}
                return {"success": False}
            except:
                return {"success": False, "exception": True}

        def __delay_and_check(self, **kwargs):
            timed_out = True
            delay_after_process = kwargs["timers"]["delay_after_process"]
            delay_per_check_cycle = kwargs["timers"]["delay_per_check_cycle"]
            delay_max_check_times = kwargs["timers"]["delay_max_check_times"]
            self.ext_logger.info(f"Allowing FGT {kwargs['devicename']} time to finish the previous process. "
                                 f"Sleeping for {delay_after_process} secs")
            time.sleep(delay_after_process)
            for timehack in range(0, int(delay_max_check_times) + 1):
                self.ext_logger.info(f"Executing status lookup on FGT {kwargs['devicename']}...this is "
                                     f"cycle: {timehack + 1}")
                fgt_responded_dict = self.__fgt_responded(**kwargs)
                if not fgt_responded_dict["success"]:
                    if fgt_responded_dict.get("exception", False):
                        timed_out = False
                        break
                    else:
                        time.sleep(delay_per_check_cycle)
                else:
                    timed_out = False
                    self.ext_logger.info(f"Rcvd response from status check on FGT {kwargs['devicename']}. "
                                         f"Inserting 10s delay then continuing")
                    time.sleep(10.0)
                    break
            if timed_out:
                self.ext_logger.error(f"FGT {kwargs['devicename']} never responded after a Check Device Is Alive "
                                      f"action was sent. This FGT is considered down and will probably not be able to "
                                      f"continue through any further processes. Check this FGT's connectivity")
                return {"success": False}
            return {"success": True}

        @BaseFMGAction.handle_standard_exceptions
        def perform(self, **kwargs):
            """
            Requires 'devicename', 'adom', 'timers.timer', k:v information
            Instructs the FMG to proxy an a call to the FGT looking just for a response. It then will wait and check the FGT's process based on what is set in timers in the configuration file

            :param kwargs: FGT configuration dictionary (normally pulled from a YAML config file) required for the perform function. 'devicename', 'adom', 'timers.timer', k:v information
            :type kwargs: dict
            :return: Return (code, dictionary) tuple in the format (code from FMG response, {"target": kwargs["devicename"]}) or tuple of (CustomCode, None) in the case that there is an exception or if the process was found to be not successful
            :rtype: tuple
            """
            if self.__delay_and_check(**kwargs)["success"]:
                self.ext_logger.info(f"FGT {kwargs['devicename']} responded successfully. Continuing....")
                return CustomResponseCode.SUCCESS, {"target": kwargs["devicename"]}

            return CustomResponseCode.NON_SUCCESS, None

        def test_it(self, **kwargs):
            BaseFMGAction.test_class_functionality(kwargs, ["timers", ], self.__class__.__name__)

    class RebootDevice(BaseFMGAction):
        """
        Requires 'devicename', 'adom' k:v information

        Calling perform(key word arguments from configuration):

        **Instructs the application to push a reboot action to the FGT via the sys/proxy/json using monitor/system/os/reboot**

        :param kwargs: FGT configuration dictionary (normally pulled from a YAML config file) required for the perform function. 'devicename', 'adom', k:v information
        :type kwargs: dict
        :return: Return (code, dictionary) tuple in the format (code from FMG response, {"target": kwargs["devicename"]}) or tuple of (CustomCode, None) in the case that there is an exception or if the process was found to be not successful
        :rtype: tuple
        """

        def __init__(self, ztplfmg):
            super().__init__(ztplfmg)

        def __reboot_device(self, **kwargs):
            inner_dict = {
                "action": "post",
                "resource": "/api/v2/monitor/system/os/reboot",
                "target": [f"adom/{kwargs['adom']}/device/{kwargs['devicename']}"]
            }
            try:
                code, res = self._fmg.execute("sys/proxy/json", data=inner_dict)
                if code == CustomResponseCode.SUCCESS:
                    status = res[0]["response"].get("status", "failed")
                    if status == "success":
                        self.ext_logger.info(f"FGT {kwargs['devicename']} was successfully issued the reboot action")
                        return {"success": True}
                    else:
                        self.ext_logger.warning(f"FGT {kwargs['devicename']} was issued the reboot action and the "
                                                f"action was received by the FGT, however, the FGT reported back that "
                                                f"the execution of the reboot was not successful")
                        return {"success": False}
                self.ext_logger.error(BaseFMGAction.non_success_code_warning_str(self.__class__.__name__, code))
                return {"success": False}
            except:
                self.ext_logger.error(BaseFMGAction.non_success_code_warning_str(self.__class__.__name__, code))
                return {"success": False, "exception": True}

        @BaseFMGAction.handle_standard_exceptions
        def perform(self, **kwargs):
            """
            Requires 'devicename', 'adom', k:v information
            Instructs the FMG to proxy a call to FGT to reboot. This action will not wait for a response. If the FGT needs to respond, the proper step would be to add another action using CheckDeviceIsAlive action

            :param kwargs: FGT configuration dictionary (normally pulled from a YAML config file) required for the perform function. 'devicename', 'adom', k:v information
            :type kwargs: dict
            :return: Return (code, dictionary) tuple in the format (code from FMG response, {"target": kwargs["devicename"]}) or tuple of (CustomCode, None) in the case that there is an exception or if the process was found to be not successful
            :rtype: tuple
            """
            if self.__reboot_device(**kwargs)["success"]:
                return CustomResponseCode.SUCCESS, {"target": kwargs["devicename"]}
            return CustomResponseCode.NON_SUCCESS, None

        def test_it(self, **kwargs):
            BaseFMGAction.test_class_functionality(kwargs, ["devicename", ], self.__class__.__name__)

    class UpgradeManagedDevice(BaseFMGAction):
        """
        Requires 'devicename', 'adom', and 'enforced.enforced_version' k:v information.

        Could require 'timers.timer', If timers are not provided, the application will default to 'delay_after_process' of 1 minute, PER firmware step required (if skip_upgrade steps, there is only one step required), delay_per_check_cycle of 10 seconds, and delay_max_check_times of 60 - which is 60 times per delay cycle (10 in this case) times EACH step in the upgrade path

        Could require 'enforced.from_fgd', 'enforced.skip_upgrade_steps'. If 'enforced.from_fgd' is not provided, default is 'N'. If 'enforced.skip_upgrade_steps' is not provided default is 'N'

        Calling perform(key word arguments from configuration):

        **Instructs the FMG to upgrade a managed device to a specific release using the native FMG capabilities released in FMG 6.4.0 and above**

        :param kwargs: FGT configuration dictionary (normally pulled from a YAML config file) required for the perform function. Requires 'serialnumber' and 'adom' k:v information
        :type kwargs: dict
        :return: Return (code, dictionary) tuple in the format (code from FMG response, {"device action": "promote_unreg", "mgmt_mode": "fmg", "name": name of fmg, "adm_usr": "admin"}) or tuple of (CustomCode, None) in the case that there is an exception or if the process was found to be not successful
        :rtype: tuple
        """

        def __init__(self, ztplfmg):
            super().__init__(ztplfmg)

        def __upgrade_and_delay(self, path, **kwargs):
            # "IMAGE_UPGRADE_BOOT_ALT_PARTITION": 1,
            # "IMAGE_UPGRADE_SKIP_RETRIEVE": 2, - don't do retrieve after image upgrade
            # "IMAGE_UPGRADE_SKIP_MULTI_STEPS": 4, - skip multi steps
            # "IMAGE_UPGRADE_FORTIGUARD_IMG": 8, - download from FGD
            # "IMAGE_UPGRADE_PREVIEW": 16, -

            enforced_version = kwargs["enforced"]["enforced_version"]
            firmware_flag = 0
            image_from_fgd = False
            skip_multi_steps = False
            device = [{"name": kwargs["devicename"]}]
            image = {"release": enforced_version}
            try:
                if kwargs["enforced"]["from_fgd"] == "Y" or kwargs["enforced"]["from_fgd"] == "y":
                    image_from_fgd = True
                    firmware_flag += 8
            except KeyError:
                pass
            try:
                if kwargs["enforced"]["skip_upgrade_steps"] == "Y" or kwargs["enforced"]["skip_upgrade_steps"] == "y":
                    skip_multi_steps = True
                    firmware_flag += 4
                    # since skipping steps add not to do retrieve after upgrade as well
                    firmware_flag += 2
            except KeyError:
                pass
            try:
                delay_after_process = kwargs["timers"]["delay_after_process"]
            except KeyError:
                delay_after_process = 60
            try:
                delay_per_check_cycle = kwargs["timers"]["delay_per_check_cycle"]
            except KeyError:
                delay_per_check_cycle = 10
            try:
                delay_max_check_times = kwargs["timers"]["delay_max_check_times"]
            except KeyError:
                delay_max_check_times = 60

            log_str = f"Firmware information is: Enforced version: {enforced_version}, Skip multi steps: " \
                      f"{skip_multi_steps}, Pull from FGD: {image_from_fgd}"
            if not skip_multi_steps:
                log_str += f". Upgrade Steps are: {', '.join(path)}"
            else:
                log_str += f". Since skipping upgrade steps was configured, the FMG will be told to not perform a " \
                           f"retrieve after the image upgrade is complete"

            timeout = delay_max_check_times * delay_per_check_cycle
            if not skip_multi_steps:
                timeout *= len(path)

            self.ext_logger.info(f"Attempting to upgrade the managed device FGT {kwargs['devicename']}. The following "
                                 f"applies: Delay after process: {delay_after_process}, Delay per task check: "
                                 f"{delay_per_check_cycle}, Number of times task checked prior to timeout: "
                                 f"{delay_max_check_times}. Total timeout is: {timeout}. {log_str}")
            code, res = self._fmg.execute("/um/image/upgrade", adom=kwargs["adom"], device=device, flags=firmware_flag,
                                          create_task="enable", image=image)
            if code == CustomResponseCode.SUCCESS:
                self.handle_task_run(res, type(self).__name__, kwargs["devicename"], sleep_time=delay_per_check_cycle,
                                     timeout=timeout)
                self.ext_logger.info(f"FGT {kwargs['devicename']} has completed its upgrade to release "
                                     f"{enforced_version}. Sleeping for {delay_after_process} seconds as requested")
                time.sleep(delay_after_process)
                return {"success": True}
            else:
                self.ext_logger.error(f"FGT {kwargs['devicename']} failed to complete its upgrade to release "
                                      f"{enforced_version}. Foregoing the delay after process as instructed, as a "
                                      f"failure will be registered and process execution will be managed by the "
                                      f"instructions provided")
            return {"success": False}

        def __check_if_upgrade_required(self, **kwargs):
            device = [{"name": kwargs["devicename"]}]
            image = {"release": kwargs["enforced"]["enforced_version"]}
            code, res = self._fmg.execute("/um/image/upgrade", adom=kwargs["adom"], device=device, flags=16,
                                          create_task="disable", image=image)
            path = None
            upgrade_path_arr = res.get("upgrade_path", None)
            if upgrade_path_arr is not None:
                try:
                    path = upgrade_path_arr[0].get("path", None)
                except IndexError:
                    pass

            if code != 0:
                self.ext_logger.error(f"During a call to determine upgrade path for the Managed Device "
                                      f"{kwargs['devicename']}, the FMG returned an error with a code integer "
                                      f"of {code}. This operation cannot continue and will report that there was a "
                                      f"failure on the entire UpgradeManagedDevice Action")
                return {"success": False, "path": None}
            if path is None:
                self.ext_logger.error(f"During a call to determine upgrade path for the Managed Device "
                                      f"{kwargs['devicename']}, the FMG returned an successful call result but "
                                      f"returned an improper response in the result body. This operation cannot "
                                      f"continue and will report that there was a failure on the entire "
                                      f"UpgradeManagedDevice Action")
                return {"success": False, "path": None}
            if len(path) == 0:
                self.ext_logger.warning(f"An attempt to upgrade the Managed Device identified as "
                                        f"{kwargs['devicename']} returned a response that it could not be upgraded. "
                                        f"This is not necessarily a negative report. The Managed Device could already "
                                        f"be on the correct version, or the version sent as required could be "
                                        f"incorrect. A successful response is being returned because this is not "
                                        f"necessarily indicative of an error.")
            else:
                self.ext_logger.info(f"During a call to determine upgrade path for the Managed Device "
                                     f"{kwargs['devicename']}, the FMG determined that the proper upgrade path is as "
                                     f"follows: {', '.join(path)}")
            return {"success": True, "path": path}

        def __check_version_successful(self):
            code, res = self._fmg.get("/cli/global/system/status")
            major = 0
            minor = 0
            if code != 0:
                return {"success": False}
            try:
                major = int(res["Major"])
                minor = int(res["Minor"])
                if major >= 6 and minor >= 4:
                    return {"success": True}
            except (KeyError, ValueError):
                return {"success": False}
            return {"success": False}

        @BaseFMGAction.handle_standard_exceptions
        def perform(self, **kwargs):
            """
            Requires 'devicename', 'adom', and 'enforced_firmware.enforced' k:v information.

            Could require 'timers.timer', If timers are not provided, the application will default to 'delay_after_process' of 2 minutes, PER firmware step required (if skip_upgrade steps, there is only one step required), delay_per_check_cycle of 10 seconds, and delay_max_check_times of 60 - which is a ten minute upgrade PER step

            Could require 'enforced_firmware.from_fgd', 'enforced_firmware.skip_upgrade_steps'. If 'enforced_firmware.from_fgd' is not provided, default is 'N'. If 'enforced_firmware.skip_upgrade_steps' is not provided default is 'N'

            Calling perform(key word arguments from configuration):

            **Instructs the FMG to upgrade a managed device to a specific release using the native FMG capabilities released in FMG 6.4.0 and above. By default, the **

            :param kwargs: FGT configuration dictionary (normally pulled from a YAML config file) required for the perform function. Requires 'serialnumber' and 'adom' k:v information
            :type kwargs: dict
            :return: Return (code, dictionary) tuple in the format (code from FMG response, {"target": kwargs["devicename"], "version": required_version}) or tuple of (CustomCode, None) in the case that there is an exception or if the process was found to be not successful
            :rtype: tuple
            """
            if not self.__check_version_successful()["success"]:
                self.ext_logger.warning(f"An attempt to upgrade the Managed Device cannot be performed, the FMG "
                                        f"version either returned an error or returned that it was not version "
                                        f"6.4.0 or higher which is a requirement for this action.")
                return CustomResponseCode.NON_SUCCESS, None

            try:
                enforced_version = kwargs["enforced"]["enforced_version"]
            except KeyError:
                enforced_version = None

            if enforced_version is None:
                self.ext_logger.warning("An attempt to upgrade the Managed Device cannot be performed, a FOS version "
                                        "that is being enforced needs to be applied as an enforced_version in the "
                                        "configuration file")
                return CustomResponseCode.NON_SUCCESS, None

            # Check to ensure that what version has been asked for makes sense and that there's even an update needed
            upgrade_required = self.__check_if_upgrade_required(**kwargs)
            # return {"success": True, "path": path}
            if upgrade_required["success"]:
                if len(upgrade_required["path"]) == 0:
                    return CustomResponseCode.SUCCESS, {"target": kwargs["devicename"],
                                                        "version": enforced_version}
                else:
                    # Run an upgrade and follow the task.
                    if self.__upgrade_and_delay(upgrade_required["path"], **kwargs)["success"]:
                        return CustomResponseCode.SUCCESS, {"target": kwargs["devicename"], "version": enforced_version}
            return CustomResponseCode.NON_SUCCESS, None

        def test_it(self, **kwargs):
            BaseFMGAction.test_class_functionality(kwargs, ["enforced_version", ], self.__class__.__name__)

    class UpgradeFortiGate(BaseFMGAction):
        """
        Requires 'devicename', 'adom', 'timers.timer', 'firmware_objects.firmware_info' k:v information

        Calling perform(key word arguments from configuration):

        **Instructs the FMG to proxy an upgrade firmware call to the FGT. It then will wait and check the FGT's process based on what is set in timers in the configuration file**

        :param kwargs: FGT configuration dictionary (normally pulled from a YAML config file) required for the perform function. 'devicename', 'adom', 'timers.timer', 'firmware_objects.firmware_info' k:v information
        :type kwargs: dict
        :return: Return (code, dictionary) tuple in the format (code from FMG response, {"target": kwargs["devicename"], "payload": full_path_to_file}) or tuple of (CustomCode, None) in the case that there is an exception or if the process was found to be not successful
        :rtype: tuple
        """

        def __init__(self, ztplfmg):
            super().__init__(ztplfmg)

        def __firmware_exists(self, path, devicename):
            if os.path.exists(path):
                return True
            else:
                self.ext_logger.error(f"Error encountered during execution processes on {devicename}. "
                                      f"The location for firmware is set for {path} but does not exist. "
                                      f"Please ensure the firware repository on the automation machine is "
                                      f"in the correct location and the firmware can be referenced. "
                                      f"Terminating...please check issue manually")
                return False

        def __fgt_on_requested_build(self, **kwargs):
            required_build = "1111"
            code, res = self._fmg.get(f"/dvmdb/adom/{kwargs['adom']}/device/{kwargs['devicename']}", fields=["build", ])
            if code == CustomResponseCode.SUCCESS:
                reported_build = str(res.get("build", "0000"))
                required_build = str(kwargs.get("firmware_objects", {}).get("firmware_build", "1111"))
                if required_build[0] == "0":
                    required_build = required_build[1:]
                if reported_build == required_build:
                    self.ext_logger.info(f"FGT {kwargs['devicename']} is already on build {reported_build}, no "
                                         f"upgrade required")
                    return True
            self.ext_logger.info(f"FGT {kwargs['devicename']} is not on build {required_build}...upgrade required")
            return False

        def __fgt_responded_after_upgrade(self, **kwargs):
            # WON'T WORK ON 5.6 FGTs
            inner_dict = {
                "action": "get",
                "resource": "/api/v2/monitor/system/status/select",
                "target": [f"adom/{kwargs['adom']}/device/{kwargs['devicename']}"]
            }
            try:
                code, res = self._fmg.execute("sys/proxy/json", data=inner_dict)
                if code == CustomResponseCode.SUCCESS:
                    status = res[0]["response"].get("status", "failed")
                    if status == "success":
                        return {"success": True}
                return {"success": False}
            except:
                return {"success": False, "exception": True}

        def __delay_for_upgrade_and_check(self, **kwargs):
            timed_out = True
            delay_after_process = kwargs["timers"]["delay_after_process"]
            delay_per_check_cycle = kwargs["timers"]["delay_per_check_cycle"]
            delay_max_check_times = kwargs["timers"]["delay_max_check_times"]
            self.ext_logger.info(f"Allowing FGT {kwargs['devicename']} to upgrade and reboot. "
                                 f"Sleeping for {delay_after_process} secs")
            time.sleep(delay_after_process)
            for timehack in range(0, int(delay_max_check_times) + 1):
                self.ext_logger.info(f"Executing status lookup on FGT {kwargs['devicename']}..."
                                     f"this is cycle: {timehack + 1}")
                fgt_responded_dict = self.__fgt_responded_after_upgrade(**kwargs)
                if not fgt_responded_dict["success"]:
                    if fgt_responded_dict.get("exception", False):
                        timed_out = False
                        break
                    else:
                        time.sleep(delay_per_check_cycle)
                else:
                    timed_out = False
                    self.ext_logger.info(f"Rcvd response from status check on FGT {kwargs['devicename']}. "
                                         f"Inserting 60s delay then continuing")
                    time.sleep(60.0)
                    break
            if timed_out:
                return {"success": False}
            return {"success": True}

        @BaseFMGAction.handle_standard_exceptions
        def perform(self, **kwargs):
            """
            Requires 'devicename', 'adom', 'timers.timer', 'firmware_objects.firmware_info' k:v information
            Instructs the FMG to proxy an upgrade firmware call to the FGT. It then will wait and check the FGT's process based on what is set in timers in the configuration file

            :param kwargs: FGT configuration dictionary (normally pulled from a YAML config file) required for the perform function. 'serialnumber', 'devicename', and 'adom' k:v information
            :type kwargs: dict
            :return: Return (code, dictionary) tuple in the format (code from FMG response, {"target": kwargs["devicename"], "payload": full_path_to_file}) or tuple of (CustomCode, None) in the case that there is an exception or if the process was found to be not successful
            :rtype: tuple
            """
            if kwargs.get("firmware_objects", {}).get("firmware_location", None) is None:
                kwargs["firmware_objects"]["firmware_location"] = os.path.join(os.path.dirname(sys.argv[0]),
                                                                               "firmware/")
            full_path = f"{kwargs['firmware_objects']['firmware_location']}" \
                        f"{kwargs['firmware_objects']['firmware_file']}"
            if not self.__firmware_exists(full_path, kwargs["devicename"]):
                return CustomResponseCode.NON_SUCCESS, None
            if self.__fgt_on_requested_build(**kwargs):
                return CustomResponseCode.SUCCESS, {"target": kwargs["devicename"], "payload": full_path}
            self.ext_logger.info(f"Attempting to modify the firmware on FGT {kwargs['devicename']}")
            with open(full_path, 'rb') as db_file:
                b64file = base64.b64encode(db_file.read())
            body = {
                "action": "post",
                "resource": "/api/v2/monitor/system/firmware/upgrade",
                "target": [f"adom/{kwargs['adom']}/device/{kwargs['devicename']}"],
                "payload": {
                    "file_content": b64file.decode("utf-8"),
                    "source": "upload"
                }
            }
            code, res = self._fmg.execute("sys/proxy/json", data=body)
            if code == CustomResponseCode.SUCCESS:
                self.ext_logger.info(f"FGT {kwargs['devicename']} was successfully pushed firmware and instructed to "
                                     f"execute an upgrade")
                if self.__delay_for_upgrade_and_check(**kwargs)["success"]:
                    self.ext_logger.info(f"FGT {kwargs['devicename']} reported a successful upgrade. Continuing....")
                    return CustomResponseCode.SUCCESS, {"target": kwargs["devicename"], "payload": full_path}
                else:
                    self.ext_logger.error(BaseFMGAction.non_success_code_warning_str(self.__class__.__name__, code))
            else:
                self.ext_logger.error(BaseFMGAction.non_success_code_warning_str(self.__class__.__name__, code))
            return CustomResponseCode.NON_SUCCESS, None

        def test_it(self, **kwargs):
            BaseFMGAction.test_class_functionality(kwargs, ["timers", "firmware_objects", ], self.__class__.__name__)
