#!/usr/bin/python
# ##################################################################
#
# Copyright 2020 Teradata. All rights reserved.                    #
# TERADATA CONFIDENTIAL AND TRADE SECRET                           #
#
# Primary Owner: Gouri Patwardhan (gouri.patwardhan@teradata.com)  #
# Secondary Owner: Trupti Purohit (trupti.purohit@teradata.com)    #
#
# Function Version: 1.0                                            #
#
# Description: Script is a TeradataML wrapper around Teradata's    #
# Script Table Operator                                            #
# ##################################################################

import docker
import tarfile
import os
from pathlib import Path
import sys
from teradataml.common.wrapper_utils import AnalyticsWrapperUtils
from teradataml.common.utils import UtilFuncs
from teradataml.dataframe.dataframe import DataFrame
from teradataml.dataframe.dataframe_utils import DataFrameUtils as df_utils
from teradataml.dbutils.filemgr import install_file
from teradataml.dbutils.filemgr import remove_file
from teradataml.table_operators.table_operator_query_generator import TableOperatorQueryGenerator
from teradataml.common.exceptions import TeradataMlException
from teradataml.common.messages import Messages
from teradataml.common.messagecodes import MessageCodes
from teradataml.utils.validators import _Validators
from teradataml.options.display import display
from teradataml.options.configure import configure
from teradatasqlalchemy.dialect import dialect as td_dialect
from teradatasqlalchemy import (BYTEINT, SMALLINT, INTEGER, BIGINT, DECIMAL, FLOAT, NUMBER)
from teradatasqlalchemy import (TIMESTAMP, DATE, TIME)
from teradatasqlalchemy import (CHAR, VARCHAR, CLOB)
from teradatasqlalchemy import (BYTE, VARBYTE, BLOB)
from teradatasqlalchemy import (PERIOD_DATE, PERIOD_TIME, PERIOD_TIMESTAMP)
from teradatasqlalchemy import (INTERVAL_YEAR, INTERVAL_YEAR_TO_MONTH, INTERVAL_MONTH, INTERVAL_DAY,
                                INTERVAL_DAY_TO_HOUR, INTERVAL_DAY_TO_MINUTE, INTERVAL_DAY_TO_SECOND,
                                INTERVAL_HOUR, INTERVAL_HOUR_TO_MINUTE, INTERVAL_HOUR_TO_SECOND,
                                INTERVAL_MINUTE, INTERVAL_MINUTE_TO_SECOND, INTERVAL_SECOND)
from teradataml.context.context import _get_current_databasename
from teradataml.context.context import get_context

class Script:

    def __init__(self,
                 data=None,
                 script_name=None,
                 files_local_path=None,
                 script_command=None,
                 delimiter="\t",
                 returns=None,
                 auth=None,
                 charset=None,
                 quotechar=None,
                 data_partition_column=None,
                 data_hash_column=None,
                 data_order_column=None,
                 is_local_order=False,
                 sort_ascending=True,
                 nulls_first=True):
        """
        DESCRIPTION:
            The Script table operator function executes a user-installed script or
            any LINUX command inside database on Teradata Vantage.

        PARAMETERS:
            script_command:
                Required Argument.
                Specifies the command/script to run.
                Types: str

            script_name:
                Required Argument.
                Specifies the name of user script.
                Types: str

            files_local_path:
                Required Argument.
                Specifies the absolute local path where user script and all supporting files like model files,
                input data file reside.
                Types: str

            returns:
                Required Argument.
                Specifies output column definition.
                Types: Dictionary specifying column name to teradatasqlalchemy type mapping.
                Default: None

            data:
                Optional Argument.
                Specifies a teradataml DataFrame containing the input data for the script.

            data_hash_column:
                Optional Argument.
                Specifies the column to be used for hashing.
                The rows in the data are redistributed to AMPs based on the hash value of the column specified.
                The user-installed script file then runs once on each AMP.
                If there is no data_partition_column, then the entire result set,
                delivered by the function, constitutes a single group or partition.
                Types: str
                Note:
                    "data_hash_column" can not be specified along with "data_partition_column",
                    "is_local_order" and "data_order_column".

            data_partition_column:
                Optional Argument.
                Specifies Partition By columns for data.
                Values to this argument can be provided as a list, if multiple
                columns are used for partition.
                Default Value: ANY
                Types: str OR list of Strings (str)
                Note:
                    1) "data_partition_column" can not be specified along with "data_hash_column".
                    2) "data_partition_column" can not be specified along with "is_local_order = True".

            is_local_order:
                Optional Argument.
                Specifies a boolean value to determine whether the input data is to be ordered locally or not.
                Order by specifies the order in which the values in a group, or partition, are sorted.
                Local Order By specifies orders qualified rows on each AMP in preparation to be input
                to a table function. This argument is ignored, if data_order_column is None.
                When set to True, data is ordered locally.
                Default Value: False
                Types: bool
                Note:
                    "is_local_order" can not be specified along with "data_hash_column".
                    When "is_local_order" is set to True, "data_order_column" should be specified, and the columns
                    specified in "data_order_column" are used for local ordering.

            data_order_column:
                Optional Argument.
                Specifies Order By columns for data.
                Values to this argument can be provided as a list, if multiple
                columns are used for ordering. This argument is used with in both cases: "is_local_order = True"
                and "is_local_order = False".
                Types: str OR list of Strings (str)
                Note:
                    "data_order_column" can not be specified along with "data_hash_column".

            sort_ascending:
                Optional Argument.
                Specifies a boolean value to determine if the result set is to be sorted on
                the data_order_column column in ascending or descending order.
                The sorting is ascending when this argument is set to True, and descending when set to False.
                This argument is ignored, if data_order_column is None.
                Default Value: True
                Types: bool

            nulls_first:
                Optional Argument.
                Specifies a boolean value to determine whether NULLS are listed first or last during ordering.
                This argument is ignored, if data_order_column is None.
                NULLS are listed first when this argument is set to True, and last when set to False.
                Default Value: True
                Types: bool

            delimiter:
                Optional Argument.
                Specifies a delimiter to use when reading columns from a row and
                writing result columns.
                Types: str

            auth:
                Optional Argument.
                Specifies an authorization to use when running the script.
                Types: str

            charset:
                Optional Argument.
                Specifies the character encoding for data.
                Permitted values: utf16, latin
                Types: str

        RETURNS:
            Script Object

        RAISES:
            TeradataMlException

        EXAMPLES:
            # Note - Refer to User Guide for setting search path and required permissions.
            # Load example data.
            load_example_data("Script", ["barrier"])

            # Example - The script mapper.py reads in a line of text input ("Old Macdonald Had A Farm") from csv and
            # splits the line into individual words, emitting a new row for each word.

            # Create teradataml DataFrame objects.
            >>> barrierdf = DataFrame.from_table("barrier")

            # Set SEARCHUIFDBPATH
            >>> get_context().execute("SET SESSION SEARCHUIFDBPATH = alice;")

            # Create a Script object that allows us to execute script on Vantage.
            >>> sto = Script(data=barrierdf,
                        script_name='mapper.py',
                        files_local_path= 'data/scripts',
                        script_command='python ./alice/mapper.py',
                        data_order_column="Id",
                        is_local_order=False,
                        nulls_first=False,
                        sort_ascending=False,
                        charset='latin', returns={"word": VARCHAR(15), "count_input": VARCHAR(2)}
                        )

            # Run user script locally within docker container and using data from csv.
            # This helps the user to fix script level issues outside Vantage.
            # Setup the environment by providing local path to docker image file.
            >>> sto.setup_sto_env(docker_image_location='/tmp/sto_sandbox_docker_image.tar'))
            Loading image from /tmp/sto_sandbox_docker_image.tar. It may take few minutes.
            Image loaded successfully.

            >>> sto.test_script(input_data_file='../barrier.csv')
            ############ STDOUT Output ############

                    word count_input
            0  Macdonald           1
            1          A           1
            2       Farm           1
            3        Had           1
            4        Old           1
            5          1           1

            # Script results look good. Now install file on Vantage.
            >>> sto.install_file(file_identifier='mapper', file_name='mapper.py', is_binary=False)

            # Execute the user script on Vantage.
            >>> sto.execute_script()
            ############ STDOUT Output ############

                    word count_input
            0  Macdonald           1
            1          A           1
            2       Farm           1
            3        Had           1
            4        Old           1
            5          1           1

            # Remove the installed file from Vantage.
            >>> sto.remove_file(file_identifier='mapper', force_remove=True)
        """
        self.result = None
        self.data = data
        self.script_name = script_name
        self.files_local_path = files_local_path
        self.script_command = script_command
        self.delimiter = delimiter
        self.returns = returns
        self.auth = auth
        self.charset = charset
        self.quotechar = quotechar
        self.data_partition_column = data_partition_column
        self.data_hash_column = data_hash_column
        self.data_order_column = data_order_column
        self.is_local_order = is_local_order
        self.sort_ascending = sort_ascending
        self.nulls_first = nulls_first

        # Create AnalyticsWrapperUtils instance which contains validation functions.
        # This is required for is_default_or_not check.
        # Rest all validation is done using _Validators
        self.__awu = AnalyticsWrapperUtils()

        # Below matrix is a list of lists, where in each row contains following elements:
        # Let's take an example of following, just to get an idea:
        #   [element1, element2, element3, element4, element5, element6]
        #   e.g.
        #       ["join", join, True, (str), True, concat_join_permitted_values]

        #   1. element1 --> Argument Name, a string. ["join" in above example.]
        #   2. element2 --> Argument itself. [join]
        #   3. element3 --> Specifies a flag that mentions argument is optional or not.
        #                   False, means required and True means optional.
        #   4. element4 --> Tuple of accepted types. (str) in above example.
        #   5. element5 --> True, means validate for empty value. Error will be raised, if empty values is passed.
        #                   If not specified, means same as specifying False.
        #   6. element6 --> A list of permitted values, an argument can accept.
        #                   If not specified, it is as good as passing None. If a list is passed, validation will be
        #                   performed for permitted values.

        self.awu_matrix = []
        self.awu_matrix.append(["data", self.data, True, (DataFrame)])
        self.awu_matrix.append(["data_partition_column", self.data_partition_column, True, (str, list), True])
        self.awu_matrix.append(["data_hash_column", self.data_hash_column, True, (str, list), True])
        self.awu_matrix.append(["data_order_column", self.data_order_column, True, (str, list), True])
        self.awu_matrix.append(["is_local_order", self.is_local_order, True, (bool)])
        self.awu_matrix.append(["sort_ascending", self.sort_ascending, True, (bool)])
        self.awu_matrix.append(["nulls_first", self.nulls_first, True, (bool)])
        self.awu_matrix.append(["script_command", self.script_command, False, (str), True])
        self.awu_matrix.append(["script_name", self.script_name, True, (str), True])
        self.awu_matrix.append(["files_local_path", self.files_local_path, True, (str), True])
        self.awu_matrix.append(["delimiter", self.delimiter, True, (str), False])
        self.awu_matrix.append(["returns", self.returns, False, (dict), True])
        self.awu_matrix.append(["auth", self.auth, True, (str), True])
        self.awu_matrix.append(["charset", self.charset, True, (str), True, ["utf16", "latin"]])
        self.awu_matrix.append(["quotechar", self.quotechar, True, (str), True])

        # Perform the function validations
        self.__validate()

    def __validate(self):
        """
        Function to validate Table Operator Function arguments, which verifies missing
        arguments, input argument and table types. Also processes the
        argument values.
        """
        # Make sure that a non-NULL value has been supplied for all mandatory arguments
        _Validators._validate_missing_required_arguments(self.awu_matrix)

        # Validate argument types
        _Validators._validate_function_arguments(self.awu_matrix)

        # permissible_datatypes in returns
        allowed_datatypes = (BYTEINT, SMALLINT, INTEGER, BIGINT, DECIMAL, FLOAT, NUMBER,
                             TIMESTAMP, DATE, TIME, CHAR, VARCHAR, CLOB, BYTE, VARBYTE,
                             BLOB, PERIOD_DATE, PERIOD_TIME, PERIOD_TIMESTAMP, INTERVAL_YEAR,
                             INTERVAL_YEAR_TO_MONTH, INTERVAL_MONTH, INTERVAL_DAY, INTERVAL_DAY_TO_HOUR,
                             INTERVAL_DAY_TO_MINUTE, INTERVAL_DAY_TO_SECOND, INTERVAL_HOUR,
                             INTERVAL_HOUR_TO_MINUTE, INTERVAL_HOUR_TO_SECOND, INTERVAL_MINUTE,
                             INTERVAL_MINUTE_TO_SECOND, INTERVAL_SECOND
                             )

        # Validate keys and datatypes in returns
        self.awu_matrix_returns = []
        for key in self.returns.keys():
            self.awu_matrix_returns.append(["keys in returns", key, False, (str), True])
            self.awu_matrix_returns.append(["value in returns", self.returns[key], False, allowed_datatypes])
        _Validators._validate_function_arguments(self.awu_matrix_returns)

        if self.data is not None:
            # Either hash or partition can be used
            if all([self.data_hash_column, self.data_partition_column]):
                raise TeradataMlException(Messages.get_message(MessageCodes.EITHER_THIS_OR_THAT_ARGUMENT,
                                                               "data_hash_column", "data_partition_column"),
                                          MessageCodes.EITHER_THIS_OR_THAT_ARGUMENT)
            # Either hash or local order by can be used
            elif all([self.data_hash_column, self.is_local_order]):
                raise TeradataMlException(Messages.get_message(MessageCodes.EITHER_THIS_OR_THAT_ARGUMENT,
                                                               "data_hash_column", "is_local_order = True"),
                                          MessageCodes.EITHER_THIS_OR_THAT_ARGUMENT)
            # Either hash or order by can be used
            elif all([self.data_hash_column, self.data_order_column]):
                raise TeradataMlException(Messages.get_message(MessageCodes.EITHER_THIS_OR_THAT_ARGUMENT,
                                                               "data_hash_column", "data_order_column"),
                                          MessageCodes.EITHER_THIS_OR_THAT_ARGUMENT)
            # Either local order by or partition by can be used
            if all([self.is_local_order, self.data_partition_column]):
                raise TeradataMlException(Messages.get_message(MessageCodes.EITHER_THIS_OR_THAT_ARGUMENT,
                                                               "is_local_order=True",
                                                               "data_partition_column"),
                                          MessageCodes.EITHER_THIS_OR_THAT_ARGUMENT)
            # local order by requires column name
            if self.is_local_order and self.data_order_column is None:
                raise TeradataMlException(Messages.get_message(MessageCodes.DEPENDENT_ARG_MISSING,
                                                               "data_order_column",
                                                               "is_local_order=True"),
                                          MessageCodes.DEPENDENT_ARG_MISSING)

            if self.__awu._is_default_or_not(self.data_partition_column, "ANY"):
                self.__awu._validate_dataframe_has_argument_columns(self.data_partition_column, "data_partition_column",
                                                                    self.data, "data", True)

            if self.data_order_column is not None:
                self.__awu._validate_dataframe_has_argument_columns(self.data_order_column, "data_order_column",
                                                                    self.data, "data", False)

            if self.data_hash_column is not None:
                self.__awu._validate_dataframe_has_argument_columns(self.data_hash_column, "data_hash_column",
                                                                    self.data, "data", False)

            if self.data_partition_column is not None:
                self.__awu._validate_dataframe_has_argument_columns(self.data_partition_column, "data_partition_column",
                                                                    self.data, "data", False)

    def set_data(self,
                 data,
                 data_partition_column=None,
                 data_hash_column=None,
                 data_order_column=None,
                 is_local_order=False,
                 sort_ascending=True,
                 nulls_first=True):
        """
        DESCRIPTION:
            Function enables user to set data and data related arguments without having to re-create Script object.

        PARAMETERS:
            data:
                Required Argument.
                Specifies a teradataml DataFrame containing the input data for the script.

            data_hash_column:
                Optional Argument.
                Specifies the column to be used for hashing.
                The rows in the data are redistributed to AMPs based on the
                hash value of the column specified.
                The user installed script then runs once on each AMP.
                If there is no data_partition_column, then the entire result set delivered by the function,
                constitutes a single group or partition.
                Types: str
                Note:
                    "data_hash_column" can not be specified along with "data_partition_column",
                    "is_local_order" and "data_order_column".

            data_partition_column:
                Optional Argument.
                Specifies Partition By columns for data.
                Values to this argument can be provided as a list, if multiple
                columns are used for partition.
                Default Value: ANY
                Types: str OR list of Strings (str)
                Note:
                    1) "data_partition_column" can not be specified along with "data_hash_column".
                    2) "data_partition_column" can not be specified along with "is_local_order = True".

            is_local_order:
                Optional Argument.
                Specifies a boolean value to determine whether the input data is to be ordered locally or not.
                "Order by" specifies the order in which the values in a group or partition are sorted.
                "Local Order By" specifies orders qualified rows on each AMP in preparation to be input
                to a table function. This argument is ignored, if data_order_column is None.
                When set to True, data is ordered locally.
                Default Value: False
                Types: bool
                Note:
                    "is_local_order" can not be specified along with "data_hash_column".
                    When "is_local_order" is set to True, "data_order_column" should be specified, and the columns
                    specified in "data_order_column" are used for local ordering.

            data_order_column:
                Optional Argument.
                Specifies Order By columns for data.
                Values to this argument can be provided as a list, if multiple
                columns are used for ordering. This argument is used in both cases: "is_local_order = True"
                and "is_local_order = False".
                Types: str OR list of Strings (str)
                Note:
                    "data_order_column" can not be specified along with "data_hash_column".

            sort_ascending:
                Optional Argument.
                Specifies a boolean value to determine if the result set is to be sorted on
                the column specified in data_order_column, in ascending or descending order.
                The sorting is ascending when this argument is set to True, and descending when set to False.
                This argument is ignored, if data_order_column is None.
                Default Value: True
                Types: bool

            nulls_first:
                Optional Argument.
                Specifies a boolean value to determine whether NULLS are listed first or last during ordering.
                This argument is ignored, if data_order_column is None.
                NULLS are listed first when this argument is set to True, and last when set to False.
                Default Value: True
                Types: bool

        RETURNS:
            None.

        RAISES:
            TeradataMlException

        EXAMPLES:
            # Note - Refer to User Guide for setting search path and required permissions.
            # Load example data.
            load_example_data("Script", ["barrier"])

            # Example 1
            # Create teradataml DataFrame objects.
            >>> barrierdf = DataFrame.from_table("barrier")

            # Set SEARCHUIFDBPATH
            >>> get_context().execute("SET SESSION SEARCHUIFDBPATH = alice;")

            # The script mapper.py reads in a line of text input ("Old Macdonald Had A Farm") from csv and
            # splits the line into individual words, emitting a new row for each word.
            # Create a Script object without data and its arguments.
            >>> sto = Script(
                        script_name='mapper.py',
                        files_local_path= 'data/scripts',
                        script_command='python ./alice/mapper.py',
                        charset='latin',
                        returns={"word": VARCHAR(15), "count_input": VARCHAR(2)}
                        )


            # Test script using data from file
            >>> sto.test_script(input_data_file='../barrier.csv')
            ############ STDOUT Output ############

                    word count_input
            0  Macdonald           1
            1          A           1
            2       Farm           1
            3        Had           1
            4        Old           1
            5          1           1

            # Test script using data from DB
            >>> sto.test_script(password='alice')
            ############ STDOUT Output ############

                    word count_input
            0  Macdonald           1
            1          A           1
            2       Farm           1
            3        Had           1
            4        Old           1
            5          1           1

            # Test script using data from DB and with data_row_limit
            >>> sto.test_script(password='alice', data_row_limit=5)
            ############ STDOUT Output ############

                    word count_input
            0  Macdonald           1
            1          A           1
            2       Farm           1
            3        Had           1
            4        Old           1
            5          1           1
            # Now in order to test / run script on actual data on Vantage user must set data and related arguments.
            # Note: All data related arguments that are not specified in set_data() are reset to default values.
            >>> sto.set_data(data='barrier',
            data_order_column="Id",
            is_local_order=False,
            nulls_first=False,
            sort_ascending=False
            )
            # Execute the user script on Vantage.
            >>> sto.execute_script()
            ############ STDOUT Output ############

                    word count_input
            0  Macdonald           1
            1          A           1
            2       Farm           1
            3        Had           1
            4        Old           1
            5          1           1

            # Example 2
            # Create teradataml DataFrame objects.
            >>> barrierdf_new = DataFrame.from_table("barrier_new")
            # Create a Script object that allows us to execute script on Vantage.
            >>> sto = Script(data=barrierdf,
                        script_name='mapper.py',
                        files_local_path= 'data/scripts',
                        script_command='python ./alice/mapper.py',
                        data_order_column="Id",
                        is_local_order=False,
                        nulls_first=False,
                        sort_ascending=False,
                        charset='latin', returns={"word": VARCHAR(15), "count_input": VARCHAR(2)}
                        )
            # Script is tested using test_script and executed on Vantage.
            >>> sto.execute_script()
            ############ STDOUT Output ############

                    word count_input
            0  Macdonald           1
            1          A           1
            2       Farm           1
            3        Had           1
            4        Old           1
            5          1           1

            # Now in order to run the script with a different dataset, user can use set_data()
            # Re-set data and some data related parameters.
            # Note: All data related arguments that are not specified in set_data() are reset to default values.
            >>> sto.set_data(data=barrierdf_new, data_order_column='Id', is_local_order=True, nulls_first=True)
            >>> sto.execute_script()
                    word  count_input
            0  Macdonald            1
            1          A            1
            2       Farm            1
            3          2            1
            4        his            1
            5       farm            1
            6         On            1
            7        Had            1
            8        Old            1
            9          1            1

            # Example 3
            # Script is tested using test_script and executed on Vantage.
            # In order to run the script with same dataset but different data related arguments, use set_data()
            # to reset arguments.
            # Note: All data related arguments that are not specified in set_data() are reset to default values.
            >>> sto.set_data(data=barrierdf, data_order_column='Id', is_local_order=True, nulls_first=True)
            >>> sto.execute_script()
            ############ STDOUT Output ############

                    word count_input
            0  Macdonald           1
            1          A           1
            2       Farm           1
            3        Had           1
            4        Old           1
            5          1           1
        """

        self.awu_matrix_setter = []
        self.awu_matrix_setter.append(["data", data, True, (DataFrame)])
        self.awu_matrix_setter.append(["data_partition_column", data_partition_column, True, (str, list), True])
        self.awu_matrix_setter.append(["data_hash_column", data_hash_column, True, (str, list), True])
        self.awu_matrix_setter.append(["data_order_column", data_order_column, True, (str, list), True])
        self.awu_matrix_setter.append(["is_local_order", is_local_order, True, (bool)])
        self.awu_matrix_setter.append(["sort_ascending", sort_ascending, True, (bool)])
        self.awu_matrix_setter.append(["nulls_first", nulls_first, True, (bool)])

        # Perform the function validations
        _Validators._validate_missing_required_arguments([["data", data, False, (DataFrame)]])
        _Validators._validate_function_arguments(self.awu_matrix_setter)

        self.data = data
        self.data_partition_column = data_partition_column
        self.data_hash_column = data_hash_column
        self.data_order_column = data_order_column
        self.is_local_order = is_local_order
        self.sort_ascending = sort_ascending
        self.nulls_first = nulls_first

        self.__validate()

    def setup_sto_env(self, docker_image_location):
        """
        DESCRIPTION:
            Function enables user to load already downloaded sandbox image.

        PARAMETERS:
            docker_image_location:
                Required Argument.
                Specifies the location of image on user's system.
                Types: str

                Note:
                    For location to download docker image refer teradataml User Guide.

        RETURNS:
            None.

        RAISES:
            TeradataMlException

        EXAMPLES:
            # Note - Refer to User Guide for setting search path and required permissions.
            # Load example data.
            load_example_data("Script", ["barrier"])

            # Example - The script mapper.py reads in a line of text input ("Old Macdonald Had A Farm") from csv and
            # splits the line into individual words, emitting a new row for each word.

            # Create teradataml DataFrame objects.
            >>> barrierdf = DataFrame.from_table("barrier")

            # Set SEARCHUIFDBPATH
            >>> get_context().execute("SET SESSION SEARCHUIFDBPATH = alice;")

            # Create a Script object that allows us to execute script on Vantage.
            >>> sto = Script(data=barrierdf,
                        script_name='mapper.py',
                        files_local_path= 'data/scripts',
                        script_command='python ./alice/mapper.py',
                        data_order_column="Id",
                        is_local_order=False,
                        nulls_first=False,
                        sort_ascending=False,
                        charset='latin', returns={"word": VARCHAR(15), "count_input": VARCHAR(2)}
                        )

            # Run user script locally within docker container and using data from csv.
            # This helps the user to fix script level issues outside Vantage.
            # Setup the environment by providing local path to docker image file.
            >>> sto.setup_sto_env(docker_image_location='/tmp/sto_sandbox_docker_image.tar'))
            Loading image from /tmp/sto_sandbox_docker_image.tar. It may take few minutes.
            Image loaded successfully.

        """
        self.awu_matrix_setup=[]
        self.awu_matrix_setup.append((["docker_image_location", docker_image_location, False, (str), True]))

        # Validate missing arguments
        _Validators._validate_missing_required_arguments(self.awu_matrix_setup)

        # Validate argument types
        _Validators._validate_function_arguments(self.awu_matrix_setup)

        # Load image from user provided location
        client = docker.from_env()
        if not Path(docker_image_location).exists():
            raise TeradataMlException(
                Messages.get_message(MessageCodes.INPUT_FILE_NOT_FOUND).format(docker_image_location),
                MessageCodes.INPUT_FILE_NOT_FOUND)
        else:
            try:
                print("Loading image from {0}. It may take few minutes.".format(docker_image_location))
                with open(docker_image_location, 'rb') as f:
                    client.images.load(f)
                print("Image loaded successfully.")
            except:
                raise

        # Set _latest_sandbox_exists to True - which indicates sandbox image for STO exists on the system
        configure._latest_sandbox_exists = True

    def test_script(self, supporting_files=None, input_data_file=None, script_args="", **kwargs):
        """
        DESCRIPTION:
            Function enables user to run script in docker container environment outside Vantage.
            Input data for user script is read from file.

        PARAMETERS:
            supporting_files:
                Optional Argument
                Specifies a file or list of supporting files like model files to be copied to the container.
                Types: string or list of str

            input_data_file:
                Required Argument.
                Specifies the absolute local path of input data file.
                If set to None, read data from AMP, else from file passed in the argument 'input_data_file'.
                Types: str

            script_args:
                Optional Argument.
                Specifies command line arguments required by the user script.
                Types: str

            kwargs:
                Optional Argument.
                Specifies the arguments used for reading data from all AMPs.
                Keys can be:
                    1. data_row_limit:
                        Specifies the number of rows to be taken from all amps when reading from a table or view
                        on Vantage.
                        Default Value: 1000
                        Types: int
                    2. password:
                        Specifies the password to connect to vantage where the data resides.
                        Types: str
                Types: dict
                Note: When data is read from file, if these arguments are passed, they will be ignored.

        RETURNS:
            Output from user script.

        RAISES:
            TeradataMlException

        EXAMPLES:
            Refer to help(Script)
        """


        self.awu_matrix_test=[]
        self.awu_matrix_test.append((["supporting_files", supporting_files, True, (str, list), True]))
        self.awu_matrix_test.append((["input_data_file", input_data_file, True, (str), True]))
        self.awu_matrix_test.append((["script_args", script_args, True, (str), False]))

        data_row_limit = kwargs.pop("data_row_limit", 1000)

        self.awu_matrix_test.append((["data_row_limit", data_row_limit, True, (int), True]))

        # Validate argument types
        _Validators._validate_function_arguments(self.awu_matrix_test)

        self.__validate()

        if data_row_limit <= 0:
            raise ValueError(Messages.get_message(MessageCodes.TDMLDF_POSITIVE_INT).
                             format("data_row_limit", "greater than"))

        # Either of 'input_data_file' or 'password' argument is required.
        password = kwargs.pop("password", None)
        if not (input_data_file or (self.data and password)):
            raise TeradataMlException(Messages.get_message(
                MessageCodes.EITHER_THIS_OR_THAT_ARGUMENT, "input_data_file",
                "Script data and password"), MessageCodes.EITHER_THIS_OR_THAT_ARGUMENT)

        if not self.script_name and self.files_local_path:
            raise TeradataMlException(Messages.get_message(MessageCodes.MISSING_ARGS,
                "script_name and files_local_path"), MessageCodes.MISSING_ARGS)

        docker_image_name = "stosandbox:1.0"
        client = docker.from_env()

        # Check if sandbox image exists on system
        if not client.images.list(docker_image_name):
            raise RuntimeError("STO sandbox image not found. Please run setup_sto_env.")

        try:
            # Create container
            container = client.containers.run(docker_image_name
                                              , stdin_open=True
                                              , tty=True
                                              , detach=True
                                              )

            path_in_docker_container = "/home/tdatuser"

            if script_args:
                script_args = "--script-args='{}'".format(script_args)

            files_to_copy = [self.script_name]

            if supporting_files is not None:
                if isinstance(supporting_files, str):
                    if supporting_files == "":
                        raise ValueError(Messages.get_message(MessageCodes.LIST_SELECT_NONE_OR_EMPTY, 'supporting_files'))
                    else:
                        files_to_copy.append(supporting_files)
                elif isinstance(supporting_files, list) and (len(supporting_files) == 0 or
                                                             any(file in [None, "None", ""] for file in supporting_files)):
                    raise ValueError(Messages.get_message(MessageCodes.LIST_SELECT_NONE_OR_EMPTY, 'supporting_files'))
                else:
                    files_to_copy.extend(supporting_files)

            if input_data_file is not None:
                files_to_copy.append(input_data_file)
                input_file_name = os.path.basename(input_data_file)

            for file in files_to_copy:
                file_path = os.path.join(self.files_local_path, file)
                if not Path(file_path).exists():
                    raise TeradataMlException(Messages.get_message(MessageCodes.INPUT_FILE_NOT_FOUND).format(file_path),
                                                MessageCodes.INPUT_FILE_NOT_FOUND)
                try:
                    self.__copy_to_docker_container(file_path, path_in_docker_container, container)
                except Exception as exp:
                    raise TeradataMlException(Messages.get_message(
                         MessageCodes.SANDBOX_CONTAINER_ERROR).format(str(exp)),
                         MessageCodes.SANDBOX_CONTAINER_ERROR)

            if input_data_file is not None:
                exec_cmd = ("python3 /home/tdatuser/script_executor.py file --script-type=py " 
                            "--user-script-path={0}/{1} --data-file-path={0}/{2} {3}".format(
                    path_in_docker_container, self.script_name, input_file_name, script_args))
            else:
                if self.data.shape[0] > data_row_limit:
                    raise ValueError(
                        Messages.get_message(MessageCodes.DATAFRAME_LIMIT_ERROR, 'data_row_limit', 'data_row_limit', data_row_limit))
                db_host = get_context().url.host
                user_name = get_context().url.username
                if not self.data._table_name:
                    self.data._table_name = df_utils._execute_node_return_db_object_name(
                                                self.data._nodeid, self.data._metaexpr)
                temp_db_name = '"{}"'.format(_get_current_databasename())
                table_name = self.data._table_name.replace(temp_db_name, "")
                table_name = table_name.replace("\"", "")
                if table_name and table_name[0] == '.':
                    table_name = table_name[1:]

                db_name = "--db-name='{}'".format(_get_current_databasename())

                if self.delimiter:
                    delimiter = "--delimiter='{}'".format(self.delimiter)

                exec_cmd = ("python3 /home/tdatuser/script_executor.py db --script-type=py "
                    "--user-script-path={}/{} --db-host={} --user={} --passwd={} --table={} "
                    "{} {} {}".format(path_in_docker_container, self.script_name, db_host,
                    user_name, password, table_name, db_name, script_args, delimiter))
            try:
                # Run user script
                exec_cmd_output = container.exec_run(exec_cmd)
                return exec_cmd_output.output.decode()
            except Exception as exp:
                raise TeradataMlException(Messages.get_message(
                     MessageCodes.SANDBOX_CONTAINER_ERROR).format(str(exp)),
                     MessageCodes.SANDBOX_CONTAINER_ERROR)
        finally:
            # Cleanup container
            container.stop()
            container.remove()

    def execute_script(self):
        """
        DESCRIPTION:
            Function enables user to run script on Vantage.

        PARAMETERS:
            None.

        RETURNS:
            Output teradataml DataFrames can be accessed using attribute
            references, such as ScriptObj.<attribute_name>.
            Output teradataml DataFrame attribute name is:
                result

        RAISES:
            TeradataMlException

        EXAMPLES:
            Refer to help(Script)
        """
        # Validate arguments
        self.__validate()

        # Generate the Table Operator query
        self.__form_table_operator_query()

        # Execute Table Operator query and return results
        return self.__execute()

    def install_file(self, file_identifier, file_name, is_binary = False, replace = False, force_replace = False):
        """
        DESCRIPTION:
            Function to install script on Vantage.
            On success, prints a message that file is installed.
            This language script can be executed via execute_script() function.

        PARAMETERS:
            file_identifier:
                Required Argument.
                Specifies the name associated with the user-installed file.
                It cannot have a schema name associated with it,
                as the file is always installed in the current schema.
                The name should be unique within the schema. It can be any valid Teradata identifier.
                Types: str

            file_name:
                Required Argument:
                Specifies the name of the file user wnats to install.
                Types: str

            is_binary:
                Optional Argument.
                Specifies if file to be installed is a binary file.
                Default Value: False
                Types: bool

            replace:
                Optional Argument.
                Specifies if the file is to be installed or replaced.
                If set to True, then the file is replaced based on value the of force_replace.
                If set to False, then the file is installed.
                Default Value: False
                Types: bool

            force_replace:
                Optional Argument.
                Specifies if system should check for the file being used before replacing it.
                If set to True, then the file is replaced even if it is being executed.
                If set to False, then an error is thrown if it is being executed.
                Default Value: False
                Types: bool

        RETURNS:
             True, if success

        RAISES:
            TeradataMLException.

        EXAMPLES:
            # Note - Refer to User Guide for setting search path and required permissions.
            # Example 1: Install the file mapper.py found at the relative path data/scripts/ using
            #            the default text mode.

            # Set SEARCHUIFDBPATH
            >>> get_context().execute("SET SESSION SEARCHUIFDBPATH = alice;")

            # Create a Script object that allows us to execute script on Vantage.
            >>> sto = Script(data=barrierdf,
                        script_local_path='data/scripts/mapper.py',
                        script_command='python ./alice/mapper.py',
                        data_order_column="Id",
                        is_local_order=False,
                        nulls_first=False,
                        sort_ascending=False,
                        charset='latin', returns='word VARCHAR(15), count_input VARCHAR(2)'
                        )
            # Install file on Vantage
            >>> sto.install_file(file_identifier='mapper', file_name='mapper.py', is_binary=False)
            File mapper.py installed in Vantage

            # Replace file on Vantage
            >>> sto.install_file(file_identifier='mapper', file_name='mapper.py', is_binary=False, replace=True, force_replace=True)
            File mapper.py replaced in Vantage
        """
        # Install/Replace file on Vantage
        try:
            file_path = os.path.join(self.files_local_path, file_name)
            # Install file on Vantage
            install_file(file_identifier=file_identifier, file_path=file_path, is_binary=is_binary,
                         replace=replace, force_replace=force_replace)
        except:
            raise

    def remove_file(self, file_identifier, force_remove=False):
        """
        DESCRIPTION:
            Function to remove user installed files/scripts from Vantage.

        PARAMETERS:
            file_identifier:
                Required Argument.
                Specifies the name associated with the user-installed file.
                It cannot have a database name associated with it,
                as the file is always installed in the current database.
                Types: str

            force_remove:
                Required Argument.
                Specifies if system should check for the file being used before removing it.
                If set to True, then the file is removed even if it is being executed.
                If set to False, then an error is thrown if it is being executed.
                Default value: False
                Types: bool

        RETURNS:
             True, if success.

        RAISES:
            TeradataMLException.

        EXAMPLES:
            # Note - Refer to User Guide for setting search path and required permissions.
            # Run install_file example before removing file.

            # Set SEARCHUIFDBPATH
            >>> get_context().execute("SET SESSION SEARCHUIFDBPATH = alice;")

            # Create a Script object that allows us to execute script on Vantage.
            >>> sto = Script(data=barrierdf,
                        script_local_path='data/scripts/mapper.py',
                        script_command='python ./alice/mapper.py 4 5 10 6 480',
                        data_order_column="Id",
                        is_local_order=False,
                        nulls_first=False,
                        sort_ascending=False,
                        charset='latin', returns='word VARCHAR(15), count_input VARCHAR(2)'
                        )
            # Install file on Vantage
            >>> sto.install_file(file_identifier='mapper', file_name='mapper.py', is_binary=False)

            # Remove the installed file.
            # Example 1:
            >>> sto.remove_file(file_identifier='mapper', force_remove=True)
            File mapper removed from Vantage

        """
        # Remove file from Vantage
        try:
            remove_file(file_identifier, force_remove)
        except:
            raise

    def __copy_to_docker_container(self, local_file_path, path_in_docker_container, container):
        """
        DESCRIPTION:
            Function to copy files to docker container.

        PARAMETERS:
            local_file_path:
                Required Argument.
                Specifies the path to the file to be copied.
                Types: str

            path_in_docker_container:
                Required Argument.
                Specifies destination path in the docker container where file will be copied to.
                Types: str

            container:
                Required Argument.
                Specifies container id.
                Types: str

            RETURNS:
                None.

            RAISES:
                TeradataMLException.

        """
        # Create tar file
        tar_file_path = "{}.tar".format(local_file_path)
        file_name = os.path.basename(local_file_path)
        tar = tarfile.open(tar_file_path, mode='w')
        try:
            tar.add(local_file_path, arcname=file_name)
        finally:
            tar.close()
        data = open(tar_file_path, 'rb').read()

        # Copy file to docker container
        copy_status = container.put_archive(path_in_docker_container, data)
        os.remove(tar_file_path)

        if copy_status:
            return

    def __form_table_operator_query(self):
        """
        Function to generate the Table Operator queries. The function defines
        variables and list of arguments required to form the query.
        """
        # Output table arguments list
        self.__func_output_args_sql_names = []
        self.__func_output_args = []

        # Generate lists for rest of the function arguments
        self.__func_other_arg_sql_names = []
        self.__func_other_args = []
        self.__func_other_arg_json_datatypes = []

        self.__func_other_arg_sql_names.append("SCRIPT_COMMAND")
        self.__func_other_args.append(UtilFuncs._teradata_collapse_arglist(self.script_command, "'"))
        self.__func_other_arg_json_datatypes.append("STRING")

        if self.delimiter is not None:
            self.__func_other_arg_sql_names.append("delimiter")
            self.__func_other_args.append(UtilFuncs._teradata_collapse_arglist(self.delimiter, "'"))
            self.__func_other_arg_json_datatypes.append("STRING")

        # Generate returns clause
        returns_clause = ', '.join(
            '{} {}'.format(key, self.returns[key].compile(td_dialect())) for key in self.returns.keys())
        self.__func_other_arg_sql_names.append("returns")
        self.__func_other_args.append(UtilFuncs._teradata_collapse_arglist(returns_clause, "'"))
        self.__func_other_arg_json_datatypes.append("STRING")

        if self.auth is not None:
            self.__func_other_arg_sql_names.append("auth")
            self.__func_other_args.append(UtilFuncs._teradata_collapse_arglist(self.auth, "'"))
            self.__func_other_arg_json_datatypes.append("STRING")

        if self.charset is not None:
            self.__func_other_arg_sql_names.append("charset")
            self.__func_other_args.append(UtilFuncs._teradata_collapse_arglist(self.charset, "'"))
            self.__func_other_arg_json_datatypes.append("STRING")

        if self.quotechar is not None:
            self.__func_other_arg_sql_names.append("quotechar")
            self.__func_other_args.append(UtilFuncs._teradata_collapse_arglist(self.quotechar, "'"))
            self.__func_other_arg_json_datatypes.append("STRING")

        # Declare empty lists to hold input table information.
        self.__func_input_arg_sql_names = []
        self.__func_input_table_view_query = []
        self.__func_input_dataframe_type = []
        self.__func_input_distribution = []
        self.__func_input_partition_by_cols = []
        self.__func_input_order_by_cols = []
        self.__func_input_order_by_type = None
        self.__func_input_sort_ascending = self.sort_ascending
        self.__func_input_nulls_first = None

        # Process data
        if self.data is not None:
            data_distribution = "FACT"
            if self.data_hash_column is not None:
                data_distribution = "HASH"
                self.data_partition_column = UtilFuncs._teradata_collapse_arglist(self.data_hash_column, "\"")
            elif self.is_local_order:
                data_distribution = None
                self.__func_input_order_by_type = "LOCAL"
                if self.__awu._is_default_or_not(self.data_partition_column, "ANY"):
                    self.data_partition_column = UtilFuncs._teradata_collapse_arglist(self.data_partition_column, "\"")
                else:
                    self.data_partition_column = None
            if self.data_order_column is not None:
                self.__func_input_order_by_cols.append(UtilFuncs._teradata_collapse_arglist(self.data_order_column, "\""))
            else:
                self.__func_input_order_by_cols.append("NA_character_")

            self.__table_ref = self.__awu._teradata_on_clause_from_dataframe(self.data, False)
            self.__func_input_distribution.append(data_distribution)
            self.__func_input_arg_sql_names.append("input")
            self.__func_input_table_view_query.append(self.__table_ref["ref"])
            self.__func_input_dataframe_type.append(self.__table_ref["ref_type"])
            self.__func_input_partition_by_cols.append(self.data_partition_column)
            self.__func_input_nulls_first = self.nulls_first
        function_name = "Script"
        # Create instance to generate Table Operator Query.
        aqg_obj = TableOperatorQueryGenerator(function_name
                                         , self.__func_input_arg_sql_names
                                         , self.__func_input_table_view_query
                                         , self.__func_input_dataframe_type
                                         , self.__func_input_distribution
                                         , self.__func_input_partition_by_cols
                                         , self.__func_input_order_by_cols
                                         , self.__func_other_arg_sql_names
                                         , self.__func_other_args
                                         , self.__func_other_arg_json_datatypes
                                         , self.__func_output_args_sql_names
                                         , self.__func_output_args
                                         , self.__func_input_order_by_type
                                         , self.__func_input_sort_ascending
                                         , self.__func_input_nulls_first
                                         , engine="ENGINE_SQL"
                                         )

        # Invoke call to Table operator query generation.
        self._tblop_query = aqg_obj._gen_table_operator_select_stmt_sql()

        # Print Table Operator query if requested to do so.
        if display.print_sqlmr_query:
            print(self._tblop_query)

    def __execute(self):
        """
        Function to execute Table Operator queries.
        Create DataFrames for the required Table Operator output.
        """
        # Generate STDOUT table name and add it to the output table list.
        tblop_stdout_temp_tablename = UtilFuncs._generate_temp_table_name(prefix="td_tblop_out_",
                                                                          use_default_database=True, gc_on_quit=True,
                                                                          quote=False)
        try:
            UtilFuncs._create_view(tblop_stdout_temp_tablename, self._tblop_query)
        except Exception as emsg:
            raise TeradataMlException(Messages.get_message(MessageCodes.TDMLDF_EXEC_SQL_FAILED, str(emsg)),
                                      MessageCodes.TDMLDF_EXEC_SQL_FAILED)

        self.result = self.__awu._create_data_set_object(
            df_input=UtilFuncs._extract_table_name(tblop_stdout_temp_tablename), source_type="table",
            database_name=UtilFuncs._extract_db_name(tblop_stdout_temp_tablename))

        return self.result

    def __repr__(self):
        """
        Returns the string representation for a Script class instance.
        """
        if self.result is None:
            repr_string = "Result is empty. Please run execute_script first."
        else:
            repr_string = "############ STDOUT Output ############"
            repr_string = "{}\n\n{}".format(repr_string, self.result)
        return repr_string

