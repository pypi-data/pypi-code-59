import logging
from . import ztpllogging
import time
from .ztplargs import Arguments
from .ztplfmg import CustomResponseCode, ZTPLFortiManager, FMGConnectionError
from .ztplconfiguration import Configurator


def set_local_loggers(log_location, *args):
    """
    Sets the local logger. For default location see the args module. To add more handlers the provision_unregistered_devices() call just needs handlers (as many as you'd like) sent in via the args reference. For instance if a syslog handler AND the default log was wanted, the call to this function would look like 'logger = set_local_loggers(args.log_location, sysloghandler_ref)'

    :param log_location: Location of the log provided by the arguments or left to default will be a local directory file called ztplite.log
    :type log_location: str
    :param args: List reference provided by the python runtime. Used in this function to add multiple handlers in this one call. If multiple handlers are needed, create them in the main() function and add them as arguments at the end of this call as shown in the instructions to this function
    :type args: list
    :return: logger ref
    :rtype: logging.logger
    """
    ztpllogging.set_loggers(logging.FileHandler(log_location, mode="a"), *args)
    logger = ztpllogging.get_logger()
    return logger


def get_config_and_instruction_info(config_file_location, ins_file_location, logger_ref):
    """
    Retrieves an in-memory hash of the configuration file and the instruction file. The application initially has a YAML file and a JSON file for the configuration file. There is a CSV converter as well, however it is not fully fleshed out as of release due to the fact that the CSV mapping will need to be hard coded. The instruction file is a JSON file.

    :param config_file_location: Location of the configuration file that will be used as set in the arguments of the application
    :type config_file_location: str
    :param ins_file_location: Location of the instruction file that will be used as set in the arguments of the application
    :type ins_file_location: str
    :param logger_ref: Reference to the logger instance
    :type logger_ref: logging.logger
    :return: Full dictionary in-memory representations of the configuration file in use (by default the YAML file) and the instruction file in use (by default the JSON file)
    :rtype: tuple
    """
    program_config = Configurator.get_translation(config_file_location, logger_ref)
    full_instructions = Configurator.get_translation(ins_file_location, logger_ref)
    # program_config = Configurator.get_translation("/home/huberjr/Files/Fortinet/DevOps/ztplite/ztplite/ztplcsv.csv",
    #                                               logger, **{"meta": ["dup", "blap", "meta"]})
    # program_config = Configurator.get_translation("/home/huberjr/Files/Fortinet/DevOps/ztplite/ztplite/ztpljson.json",
    #                                               logger)

    if program_config is None or full_instructions is None:
        logger_ref.critical(
            f"A critical configuration requirement was not met. The application had critical issues retrieving "
            f"information from {config_file_location if program_config is None else ins_file_location}. The "
            f"application cannot continue in this state. Please correct the issue. Terminating...")
        exit(1)
    return program_config, full_instructions


def get_unregistered_devices(fmg_ref, program_config_hash_ref, logger_ref):
    """

    :param fmg_ref: Reference to a Fortimanager instance
    :type fmg_ref: ZTPLFortiManager
    :param program_config_hash_ref: Reference to an in-memory hash of the entire program config file - normally the YAML file
    :type program_config_hash_ref: dict
    :param logger_ref: Reference to the logger instance
    :type logger_ref: logging.logger
    :return: Dictionary of all device serial numbers and their names if it matched a serial number setting in the configuration file referenced with program_config_hash_ref. Format is: {fgt_sn2: fgt_name2, fgt_sn2: fgt_name2}
    :rtype: dict
    """
    fgt_sn_to_promote_dict = None
    res_code, unauth_device_dict = fmg_ref.get_unauthorized_devices()
    if res_code == CustomResponseCode.SUCCESS:
        fgt_sn_to_promote_dict = {sn: name for sn, name in unauth_device_dict.items() if sn in
                                  Configurator.match_lists(list(unauth_device_dict.keys()),
                                                           [fgt for fgt in program_config_hash_ref])}
        if not fgt_sn_to_promote_dict:
            logger_ref.info(f"There are no FGTs that match the requirements for provisioning. Terminating....")
            exit(0)
    else:
        logger_ref.critical("The capability to retrieve Unauthorized Devices did not succeed and a "
                            "non-successful response was retrieved. This issue must be corrected prior "
                            "to the application continuing. Please correct the issue. Terminating...")
        exit(1)
    return fgt_sn_to_promote_dict


def promote_device(fmg_ref, dict_info_required_ref, logger_ref):
    """
    Handles the promotion process of an unregistered device by calling the correct BaseFMGAction object (PromoteDevice)

    :param fmg_ref: Reference to a Fortimanager instance
    :type fmg_ref: ZTPLFortiManager
    :param dict_info_required_ref: Reference to the Key,Value information required to promote a device (ADOM, devicename, etc...)
    :type dict_info_required_ref: Dictionary
    :param logger_ref: Reference to the logger instance
    :type logger_ref: logging.logger
    :return: Code from the PromoteDevice BaseFMGAction object PromoteDevice
    :rtype: int
    """
    code, res = fmg_ref.PromoteDevice(fmg_ref).perform(**dict_info_required_ref)
    if code != CustomResponseCode.SUCCESS:
        logger_ref.critical(f"FGT with SN {dict_info_required_ref['serialnumber']} could not be promoted. See "
                            f"errors above in the log. This is critical and this FGT will not be able to be "
                            f"provisioned further. The app will continue with further provisionings efforts if "
                            f"any are required.")
    return code


def assign_device_name(fmg_ref, dict_info_required_ref, logger_ref):
    """
    Handles the device name assignment in the FMG - this ensures the code has the proper reference to address the Managed Device for the rest of the application's processing. The function calls the correct BaseFMGAction object (AssignDeviceName)

    :param fmg_ref: Reference to a Fortimanager instance
    :type fmg_ref: ZTPLFortiManager
    :param dict_info_required_ref:
    :type dict_info_required_ref:
    :param logger_ref: Reference to the logger instance
    :type logger_ref: logging.logger
    :return: Code from the PromoteDevice BaseFMGAction object PromoteDevice
    :rtype: int
    """
    code, res = fmg_ref.AssignDeviceName(fmg_ref).perform(**dict_info_required_ref)
    if code != CustomResponseCode.SUCCESS:
        logger_ref.critical(f"FGT with SN {dict_info_required_ref['serialnumber']} could not be assigned a device "
                            f"name properly. See if there are any descriptive errors above in the log. "
                            f"This is critical and this FGT will not be able to be provisioned further. The app "
                            f"will continue with further provisioning efforts if any are required.")
    return code


def run_fmg_actions_on_device(fmg_ref, cmd, fgt_sn, fgt_configuration, variables, logger_ref):
    """
    Performs each Action that a FMG can perform on the FGT being provisioned. Each Action is called out in an Instruction provided in the instruction file

    :param fmg_ref: Reference to a Fortimanager instance
    :type fmg_ref: ZTPLFortiManager
    :param cmd: Command entry that houses all information that a FMG needs to run a discrete action
    :type cmd: Dictionary
    :param fgt_sn: Serial number of the FGT that is being looked for in the dictionary - will be a key if it exists
    :type fgt_sn: str
    :param fgt_configuration: Configuration items associated with this specific FGT pulled from the configuration file
    :type fgt_configuration: Dictionary
    :param variables: Key,Val pairs found in the instruction file as ADHOC_DATA for this specific FGT
    :type variables: Dictionary or None
    :param logger_ref: Reference to the logger instance
    :type logger_ref: logging.logger
    :return: Dictionary representing success or failure in the following format. {"success": True} | {"success": False}
    :rtype: Dictionary
    """
    time.sleep(cmd.get("DELAY_BEFORE", 0))
    fmg_action = getattr(fmg_ref, cmd["ACTION"])
    dict_info_required = Configurator.config_key_val_finder(fgt_configuration, cmd["DATA_REQ"])
    if dict_info_required is not None:
        dict_info_required["ADHOC_DATA"] = variables
        continue_instruction = cmd.get("CONTINUE_ON_FAILURE", "n")
        code, res = fmg_action(fmg_ref).perform(**dict_info_required)
        if code != CustomResponseCode.SUCCESS and continue_instruction.lower() == "n":
            logger_ref.warning(f"The response from the command {cmd['ACTION']} was not successful "
                               f"and the action controller for that action is set to not continue "
                               f"without success. Continuing with further FGTs if any are required, but "
                               f"the FGT with serial number {fgt_sn} will have to be handled manually "
                               f"once the issue that caused this status is fixed")
            return {"success": False}
    else:
        logger_ref.error(f"Data for an instruction could not be found while performing the "
                         f"provisioning on FGT with serial number {fgt_sn}. This FGT will not be able "
                         f"to continue provisioning. The app will continue with other FGTs if required. "
                         f"The command where this failure took place was {cmd['ACTION']}")
        return {"success": False}
    return {"success": True}


def run_config_values_test(fmg_ref, cmd, fgt_sn, fgt_configuration, logger_ref):
    """
    Called only if the argument --run_test was utilized in the initial instantiation of the program. Runs a test to determine if there are missing data values required for an instruction or action to be performed

    :param fmg_ref: Reference to a Fortimanager instance
    :type fmg_ref: ZTPLFortiManager
    :param cmd: Command entry that houses all information that a FMG needs to run a discrete action
    :type cmd: Dictionary
    :param fgt_sn: Serial number of the FGT that is being looked for in the dictionary - will be a key if it exists
    :type fgt_sn: str
    :param fgt_configuration: Configuration items associated with this specific FGT pulled from the configuration file
    :type fgt_configuration: Dictionary
    :param logger_ref: Reference to the logger instance
    :type logger_ref: logging.logger
    :return: Dictionary representing success or failure in the following format. {"success": True} | {"success": False}
    :rtype: Dictionary
    """
    action = getattr(fmg_ref, cmd["ACTION"])
    dict_info_required = Configurator.config_key_val_finder(fgt_configuration, cmd["DATA_REQ"])
    if dict_info_required is not None:
        action(fmg_ref).test_it(**dict_info_required)
    else:
        logger_ref.error(f"Data for an instruction could not be found while performing the test on the FGT with "
                         f"serial number {fgt_sn}. This means your configuration file does not have the information "
                         f"needed as asked for in your instruction file.")


def provision_unregistered_devices():
    """
    Used as a kickoff point for a "main" file to call to get a full provision cycle going. This entire module is so that any function can be called from "main" and the file can be whatever name the engineer wants to make it as long as it has access to the module itself everything will work. If a "main" driver needs to call another function one can be created in this module with ease and other options will be able to be built from here. Arguments could be expanded with subparsers as well to have sub-actions utilized if someone wanted to expand this.

    Function loops through each FGT in the promotion dictionary after it's been compared with the configuration file. If the Serial Number of an unregistered device matches a serial number found in the configuration file (normally a YAML file), then it is considered for provisioning.
    After the provisioning determination is made, the FGTs specific actions are pulled from the instructions file (the JSON file), which allows the engineer to tell the FMG each action that should be performed on a FGT just by utilizing the correct names of the Commands that the BaseFMGAction object gives. Using these instructions and a reference to where the data are found in the configuration file, again just in text, the code knows where to get all the data required to perform all actions on the device
    """
    ###############################################
    # Get arguments and set loggers up
    args = Arguments("ZTP Lite Base")
    logger = set_local_loggers(args.log_location)

    ###############################################
    # Get configuration and instruction information
    program_config, full_instructions = get_config_and_instruction_info(args.config_file, args.instruction_file, logger)

    try:
        with ZTPLFortiManager(args.fmg_address, args.fmg_uname, args.fmg_pword,
                              args.debug_mode, use_ssl=args.use_ssl, disable_request_warnings=True) as fmg:
            fmg.set_debug_logger(args.debug_log_location)
            fgt_sn_to_promote_dict = get_unregistered_devices(fmg, program_config, logger)

            ###############################################
            # Run through each FGT's provision instructions
            for fgt_sn in fgt_sn_to_promote_dict:
                # inject the new password if it's coming from args
                if args.new_pass is not None:
                    if not program_config[fgt_sn]["configuration"].get("device_pw", False):
                        program_config[fgt_sn]["configuration"]["device_pw"] = args.new_pass
                fgt_configuration = program_config[fgt_sn]
                # determine if an instruction template reference is called in the YAML file
                config_instruction_ref = None
                try:
                    config_instruction_ref = program_config[fgt_sn]["templates"]["instructions"]
                except KeyError:
                    pass
                logger.info(f"Beginning instructions search for the FGT with SN {fgt_sn}.")
                instructions = Configurator.get_instruction_for_fgt(full_instructions, fgt_sn, fgt_sn,
                                                                    config_instruction_ref)
                if instructions is None:
                    continue
                variables = Configurator.get_adhoc_data_for_fgt(full_instructions, fgt_sn)

                if not args.run_test:
                    # promotion and the setting the devicename is a requirement, no use to use inspection for these.
                    dict_info_required = Configurator.config_key_val_finder(fgt_configuration,
                                                                            ["configuration.adom",
                                                                             "configuration.devicename"])
                    dict_info_required["serialnumber"] = fgt_sn_to_promote_dict[fgt_sn]
                    if promote_device(fmg, dict_info_required, logger) != CustomResponseCode.SUCCESS:
                        continue
                    if assign_device_name(fmg, dict_info_required, logger) != CustomResponseCode.SUCCESS:
                        continue

                ###############################################
                # Run through each Action for a FGT's provisioning instructions
                for cmd in instructions:
                    if args.run_test:
                        run_config_values_test(fmg, cmd, fgt_sn, fgt_configuration, logger)
                    else:
                        if not run_fmg_actions_on_device(fmg, cmd, fgt_sn, fgt_configuration, variables,
                                                         logger)["success"]:
                            break
                else:
                    time.sleep(cmd.get("DELAY_AFTER", 0))
                    logger.info(f"All actions completed on FGT with serial number {fgt_sn}. Continuing...")
            else:
                logger.info(f"Application process for all FGTs is complete")
    except AttributeError as ae:
        logger.error(f"Handled an attribute error - more than likely an instruction was called in the instruction "
                     f"file that has not been created in the ztplfmg class or there was a misspelling or "
                     f"misconfiguration with one of the instructions entered in the instruction file. The "
                     f"error information is: {str(ae)}")
    except FMGConnectionError as fce:
        logger.error(f"Handled a connection error - more than likely FMG IP address or FQDN is incorrect or the FMG "
                     f"is not currently active on the network. The error information is: {str(fce)}")


def __debug_action_run(fgt_sn_to_promote_dict):
    """
    Used as a kickoff point for a "main" file only for debug.

    Function loops through each FGT in the promotion dictionary after it's been compared with the configuration file. If the Serial Number of an unregistered device matches a serial number found in the configuration file (normally a YAML file), then it is considered for provisioning.
    After the provisioning determination is made, the FGTs specific actions are pulled from the instructions file (the JSON file), which allows the engineer to tell the FMG each action that should be performed on a FGT just by utilizing the correct names of the Commands that the BaseFMGAction object gives. Using these instructions and a reference to where the data are found in the configuration file, again just in text, the code knows where to get all the data required to perform all actions on the device
    """
    ###############################################
    # Get arguments and set loggers up
    args = Arguments("ZTP Lite Base Debug")
    args["instruction_file"] = "/home/huberjr/Files/Fortinet/DevOps/ztplite/debuginstructions.json"
    args["config_file"] = "/home/huberjr/Files/Fortinet/DevOps/ztplite/debugyml.yaml"
    logger = set_local_loggers(args.log_location)

    ###############################################
    # Get configuration and instruction information
    program_config, full_instructions = get_config_and_instruction_info(args.config_file, args.instruction_file, logger)

    try:
        with ZTPLFortiManager(args.fmg_address, args.fmg_uname, args.fmg_pword,
                              args.debug_mode, use_ssl=args.use_ssl, disable_request_warnings=True) as fmg:
            fmg.set_debug_logger(args.debug_log_location)
            ###############################################
            # Run through each FGT's provision instructions

            for fgt_sn in fgt_sn_to_promote_dict:
                fgt_configuration = program_config[fgt_sn]
                # determine if an instruction template reference is called in the YAML file
                config_instruction_ref = None
                try:
                    config_instruction_ref = program_config[fgt_sn]["templates"]["instructions"]
                except KeyError:
                    pass
                logger.info(f"Beginning instructions search for the FGT with SN {fgt_sn}.")
                instructions = Configurator.get_instruction_for_fgt(full_instructions, fgt_sn, fgt_sn,
                                                                    config_instruction_ref)
                if instructions is None:
                    continue
                variables = Configurator.get_adhoc_data_for_fgt(full_instructions, fgt_sn)

                # promotion and the setting the devicename is a requirement, no use to use inspection for these.
                dict_info_required = Configurator.config_key_val_finder(fgt_configuration, ["configuration.adom",
                                                                                            "configuration.devicename"])
                dict_info_required["serialnumber"] = fgt_sn_to_promote_dict[fgt_sn]
                ###############################################
                # Run through each Action for a FGT's provisioning instructions
                for cmd in instructions:
                    if args.run_test:
                        run_config_values_test(fmg, cmd, fgt_sn, fgt_configuration, logger)
                    else:
                        if not run_fmg_actions_on_device(fmg, cmd, fgt_sn, fgt_configuration, variables,
                                                         logger)["success"]:
                            break
                else:
                    time.sleep(cmd.get("DELAY_AFTER", 0))
                    logger.info(f"All actions completed on FGT with serial number {fgt_sn}. Continuing...")
    except AttributeError as ae:
        logger.error(f"Handled an attribute error - more than likely an instruction was called in the instruction "
                     f"file that has not been created in the ztplfmg class or there was a misspelling or "
                     f"misconfiguration with one of the instructions entered in the instruction file. The "
                     f"error information is: {str(ae)}")
    except FMGConnectionError as fce:
        logger.error(f"Handled a connection error - more than likely FMG IP address or FQDN is incorrect or the FMG "
                     f"is not currently active on the network. The error information is: {str(fce)}")