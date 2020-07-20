# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------
from typing import Optional

from azureml._common._error_definition import error_decorator
from azureml._common._error_definition.user_error import ArgumentInvalid, ArgumentMismatch, NotReady, NotSupported, \
    BadArgument, NotFound, InvalidDimension, BadData, ArgumentOutOfRange, Authentication, MalformedArgument
from azureml.automl.core.shared._diagnostics.error_strings import AutoMLErrorStrings


# region ArgumentInvalid
@error_decorator(use_parent_error_code=True, details_uri="https://aka.ms/AutoMLConfig")
class InvalidArgumentType(ArgumentInvalid):
    @property
    def message_format(self) -> str:
        return AutoMLErrorStrings.INVALID_ARGUMENT_TYPE


@error_decorator(use_parent_error_code=True, details_uri="https://aka.ms/AutoMLConfig")
class InvalidArgumentWithSupportedValues(ArgumentInvalid):
    @property
    def message_format(self) -> str:
        return AutoMLErrorStrings.INVALID_ARGUMENT_WITH_SUPPORTED_VALUES


@error_decorator(use_parent_error_code=True, details_uri="https://aka.ms/AutoMLConfig")
class InvalidArgumentWithSupportedValuesForTask(ArgumentInvalid):
    @property
    def message_format(self) -> str:
        return AutoMLErrorStrings.INVALID_ARGUMENT_WITH_SUPPORTED_VALUES_FOR_TASK


@error_decorator(use_parent_error_code=True, details_uri="https://aka.ms/AutoMLConfig")
class InvalidArgumentForTask(ArgumentInvalid):
    @property
    def message_format(self) -> str:
        return AutoMLErrorStrings.INVALID_ARGUMENT_FOR_TASK


@error_decorator(use_parent_error_code=True, details_uri="https://aka.ms/AutoMLConfig")
class TensorflowAlgosAllowedButDisabled(ArgumentInvalid):
    @property
    def message_format(self) -> str:
        return AutoMLErrorStrings.TENSORFLOW_ALGOS_ALLOWED_BUT_DISABLED


@error_decorator(use_parent_error_code=True, details_uri="https://aka.ms/AutoMLConfig")
class InvalidCVSplits(ArgumentInvalid):
    @property
    def message_format(self) -> str:
        return AutoMLErrorStrings.INVALID_CV_SPLITS


@error_decorator(use_parent_error_code=True, details_uri="https://aka.ms/AutoMLConfig")
class InvalidInputDatatype(ArgumentInvalid):
    @property
    def message_format(self) -> str:
        return AutoMLErrorStrings.INVALID_INPUT_DATATYPE


@error_decorator(use_parent_error_code=True, details_uri="https://aka.ms/AutoMLConfig")
class InputDataWithMixedType(ArgumentInvalid):
    @property
    def message_format(self) -> str:
        return AutoMLErrorStrings.INPUT_DATA_WITH_MIXED_TYPE


@error_decorator(use_parent_error_code=True, details_uri="https://aka.ms/AutoMLConfig")
class AllAlgorithmsAreBlocked(ArgumentInvalid):
    @property
    def message_format(self) -> str:
        return AutoMLErrorStrings.ALL_ALGORITHMS_ARE_BLOCKED


@error_decorator(details_uri="https://aka.ms/AutoMLConfig")
class InvalidComputeTargetForDatabricks(ArgumentInvalid):
    @property
    def message_format(self) -> str:
        return AutoMLErrorStrings.INVALID_COMPUTE_TARGET_FOR_DATABRICKS


@error_decorator(use_parent_error_code=True, details_uri="https://aka.ms/AutoMLConfig")
class EmptyLagsForColumns(ArgumentInvalid):
    @property
    def message_format(self) -> str:
        return AutoMLErrorStrings.EMPTY_LAGS_FOR_COLUMNS


@error_decorator(use_parent_error_code=True)
class TimeseriesInvalidDateOffsetType(ArgumentInvalid):
    @property
    def message_format(self) -> str:
        return AutoMLErrorStrings.TIMESERIES_INVALID_DATE_OFFSET_TYPE
# endregion


# region ArgumentMismatch
@error_decorator(use_parent_error_code=True, details_uri="https://aka.ms/AutoMLConfig")
class AllowedModelsSubsetOfBlockedModels(ArgumentMismatch):
    @property
    def message_format(self) -> str:
        return AutoMLErrorStrings.ALLOWED_MODELS_SUBSET_OF_BLOCKED_MODELS


@error_decorator(details_uri="https://aka.ms/AutoMLConfig")
class ConflictingValueForArguments(ArgumentMismatch):
    @property
    def message_format(self) -> str:
        return AutoMLErrorStrings.CONFLICTING_VALUE_FOR_ARGUMENTS


@error_decorator(use_parent_error_code=True)
class InvalidDampingSettings(ConflictingValueForArguments):
    @property
    def message_format(self) -> str:
        return AutoMLErrorStrings.INVALID_DAMPING_SETTINGS
# endregion


# region BadArgument
@error_decorator(details_uri="https://aka.ms/AutoMLConfig")
class InvalidFeaturizer(BadArgument):
    @property
    def message_format(self) -> str:
        return AutoMLErrorStrings.INVALID_FEATURIZER


@error_decorator(use_parent_error_code=True)
class InvalidSTLFeaturizerForMultiplicativeModel(InvalidFeaturizer):
    @property
    def message_format(self) -> str:
        return AutoMLErrorStrings.INVALID_STL_FEATURIZER_FOR_MULTIPLICATIVE_MODEL
# endregion


# region ArgumentOutOfRange
@error_decorator(use_parent_error_code=True)
class NCrossValidationsExceedsTrainingRows(ArgumentOutOfRange):
    @property
    def message_format(self) -> str:
        return AutoMLErrorStrings.N_CROSS_VALIDATIONS_EXCEEDS_TRAINING_ROWS
# endregion


# region MalformedArgument
class MalformedJsonString(MalformedArgument):
    @property
    def message_format(self):
        return AutoMLErrorStrings.MALFORMED_JSON_STRING
# endregion


# region NotReady
class ComputeNotReady(NotReady):
    @property
    def message_format(self) -> str:
        return AutoMLErrorStrings.COMPUTE_NOT_READY
# endregion


# region NotFound
class MethodNotFound(NotFound):
    @property
    def message_format(self) -> str:
        return AutoMLErrorStrings.METHOD_NOT_FOUND


class DatastoreNotFound(NotFound):
    @property
    def message_format(self) -> str:
        return AutoMLErrorStrings.DATASTORE_NOT_FOUND


class DataPathNotFound(NotFound):
    @property
    def message_format(self):
        return AutoMLErrorStrings.DATA_PATH_NOT_FOUND


class MissingSecrets(NotFound):
    @property
    def message_format(self):
        return AutoMLErrorStrings.MISSING_SECRETS
# endregion


# region NotSupported
@error_decorator(details_uri="https://aka.ms/AutoMLConfig")
class AllowedModelsUnsupported(NotSupported):
    @property
    def message_format(self) -> str:
        return AutoMLErrorStrings.ALLOWED_MODELS_UNSUPPORTED


@error_decorator(use_parent_error_code=True, details_uri="https://aka.ms/AutoMLConfig")
class FeatureUnsupportedForIncompatibleArguments(NotSupported):
    @property
    def message_format(self) -> str:
        return AutoMLErrorStrings.FEATURE_UNSUPPORTED_FOR_INCOMPATIBLE_ARGUMENTS


@error_decorator(use_parent_error_code=True, details_uri="https://aka.ms/AutoMLConfig")
class NonDnnTextFeaturizationUnsupported(NotSupported):
    @property
    def message_format(self) -> str:
        return AutoMLErrorStrings.NON_DNN_TEXT_FEATURIZATION_UNSUPPORTED


class InvalidOperationOnRunState(NotSupported):
    @property
    def message_format(self) -> str:
        return AutoMLErrorStrings.INVALID_OPERATION_ON_RUN_STATE
# endregion


# region InvalidDimension
class DatasetsFeatureCountMismatch(InvalidDimension):
    @property
    def message_format(self) -> str:
        return AutoMLErrorStrings.DATASETS_FEATURE_COUNT_MISMATCH
# endregion


# region BadData
class TimeseriesColumnNamesOverlap(BadData):
    @property
    def message_format(self) -> str:
        return AutoMLErrorStrings.TIMESERIES_COLUMN_NAMES_OVERLAP
# endregion


# region Authentication
class DataPathInaccessible(Authentication):
    @property
    def message_format(self):
        return AutoMLErrorStrings.DATA_PATH_INACCESSIBLE
# endregion
