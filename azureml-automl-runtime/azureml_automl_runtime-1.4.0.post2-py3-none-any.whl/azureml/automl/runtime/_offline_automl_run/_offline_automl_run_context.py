# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------
from azureml.automl.runtime._offline_automl_run._offline_automl_run import _OfflineAutoMLRunBase
from azureml.automl.runtime.automl_run_context import AutoMLAbstractRunContext


class _OfflineAutoMLRunContext(AutoMLAbstractRunContext):
    """Run context for an offline AutoML run."""

    def __init__(self, run: _OfflineAutoMLRunBase) -> None:
        super().__init__()
        self._run = run

    def _get_run_internal(self) -> _OfflineAutoMLRunBase:
        return self._run
