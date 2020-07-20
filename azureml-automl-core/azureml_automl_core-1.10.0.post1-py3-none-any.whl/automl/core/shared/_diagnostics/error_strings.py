# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------


class AutoMLErrorStrings:
    """
    All un-formatted error strings that accompany the common error codes in AutoML.

    Dev note: Please keep this list sorted on keys.
    """

    ALL_ALGORITHMS_ARE_BLOCKED = "All models are blocked. Please ensure that at least one model is allowed."
    COMPUTE_NOT_READY = "Compute not in 'Succeeded' state. Please choose another compute or wait till it is ready."
    CONFLICTING_VALUE_FOR_ARGUMENTS = "Conflicting or duplicate values are provided for arguments: [{arguments}]"
    DATASETS_FEATURE_COUNT_MISMATCH = "The number of features in [{first_dataset_name}]({first_dataset_shape}) does " \
                                      "not match with those in [{second_dataset_name}]({second_dataset_shape}). " \
                                      "Please inspect your data, and make sure that features are aligned in " \
                                      "both the Datasets."
    DATASTORE_NOT_FOUND = "The provided Datastore was not found. Error: {dprep_error}"
    DATA_PATH_INACCESSIBLE = "The provided path to the data in the Datastore was inaccessible. Please make sure " \
                             "you have the necessary access rights on the resource. Error: {dprep_error}"
    DATA_PATH_NOT_FOUND = "The provided path to the data in the Datastore does not exist. Error: {dprep_error}"
    EMPTY_LAGS_FOR_COLUMNS = "The lags for all columns are represented by empty lists. Please set the " \
                             "target_lags parameter to None to turn off the lag feature and run the experiment again."
    FEATURE_UNSUPPORTED_FOR_INCOMPATIBLE_ARGUMENTS = "Feature [{feature_name}] is unsupported due to incompatible " \
                                                     "values for argument(s): [{arguments}]"
    INPUT_DATA_WITH_MIXED_TYPE = "A mix of Dataset and Pandas objects provided. " \
                                 "Please provide either all Dataset or all Pandas objects."
    INVALID_ARGUMENT_TYPE = "Argument [{argument}] is of unsupported type: [{actual_type}]. " \
                            "Supported type(s): [{expected_types}]"
    INVALID_ARGUMENT_WITH_SUPPORTED_VALUES = "Invalid argument(s) '{arguments}' specified. " \
                                             "Supported value(s): '{supported_values}'."
    INVALID_ARGUMENT_WITH_SUPPORTED_VALUES_FOR_TASK = "Invalid argument(s) '{arguments}' specified for task type " \
                                                      "'{task_type}'. Supported value(s): '{supported_values}'."
    INVALID_ARGUMENT_FOR_TASK = "Invalid argument(s) '{arguments}' for task type '{task_type}'."
    INVALID_COMPUTE_TARGET_FOR_DATABRICKS = "Databricks compute cannot be directly attached for AutoML runs. " \
                                            "Please pass in a spark context instead using the spark_context " \
                                            "parameter and set compute_target to 'local'."
    INVALID_CV_SPLITS = "cv_splits_indices should be a List of List[numpy.ndarray]. \
                            Each List[numpy.ndarray] corresponds to a CV fold and should have just 2 elements: " \
                        "The indices for training set and for the validation set."
    INVALID_DAMPING_SETTINGS = "Conflicting values are provided for arguments [{model_type}] and [{is_damped}]. " \
                               "Damping can only be applied when there is a trend term."
    INVALID_FEATURIZER = "[{featurizer_name}] is not a valid featurizer for featurizer type: [{featurizer_type}]"
    INVALID_INPUT_DATATYPE = "Input of type '{input_type}' is not supported. Supported types: [{supported_types}]"
    INVALID_OPERATION_ON_RUN_STATE = "Operation [{operation_name}] on the RunID [{run_id}] is invalid. " \
                                     "Current run state: [{run_state}]"
    INVALID_STL_FEATURIZER_FOR_MULTIPLICATIVE_MODEL = "Cannot use multiplicative model type [{model_type}] because " \
                                                      "trend contains negative or zero values."
    MALFORMED_JSON_STRING = "Failed to parse the provided JSON string. Error: {json_decode_error}"
    METHOD_NOT_FOUND = "Required method [{method_name}] is not found."
    MISSING_SECRETS = "Failed to get data from the Datastore due to missing secrets. Error: {dprep_error}"
    NON_DNN_TEXT_FEATURIZATION_UNSUPPORTED = "For non-English pre-processing of text data, please set " \
                                             "enable_dnn=True and make sure you are using GPU compute."
    N_CROSS_VALIDATIONS_EXCEEDS_TRAINING_ROWS = "Number of training rows ({training_rows}) is less than total " \
                                                "requested CV splits ({n_cross_validations}). " \
                                                "Please reduce the number of splits requested."
    TENSORFLOW_ALGOS_ALLOWED_BUT_DISABLED = "Tensorflow isn't enabled but only Tensorflow models were specified in " \
                                            "allowed_models."
    TIMESERIES_COLUMN_NAMES_OVERLAP = "Some of the columns that are about to be created by LagLeadOperator already " \
                                      "exist in the input TimeSeriesDataFrame: [{column_names}. Please set " \
                                      "`overwrite_columns` to `True` to proceed anyways."
    TIMESERIES_INVALID_DATE_OFFSET_TYPE = "The data set frequency must be a string or None. The string must " \
                                          "represent a pandas date offset. Please refer to pandas documentation on " \
                                          "date offsets: {pandas_url}"
    ALLOWED_MODELS_UNSUPPORTED = "Allowed models [{allowed_models}] are not supported for scenario: " \
                                 "{scenario}."
    ALLOWED_MODELS_SUBSET_OF_BLOCKED_MODELS = "All models allowed models are within blocked models list. Please " \
                                              "remove models from the exclude list or add models to the allow list."
