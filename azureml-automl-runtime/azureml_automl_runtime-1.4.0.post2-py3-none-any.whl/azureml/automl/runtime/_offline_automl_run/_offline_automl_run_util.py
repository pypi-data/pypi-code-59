# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------
from typing import List
import os

from azureml.automl.runtime._offline_automl_run._offline_automl_run import _OfflineAutoMLRun


class _OfflineAutoMLRunUtil:
    """Utility methods for offline AutoML runs."""

    @staticmethod
    def create_child_run(path: str, parent_run_id: str, iteration: int, pipeline_spec: str) -> _OfflineAutoMLRun:
        """Create a child run."""
        child_run_id = "{}_{}".format(parent_run_id, iteration)
        run_folder = os.path.join(path, parent_run_id, child_run_id)
        child_run = _OfflineAutoMLRun(child_run_id, run_folder)
        child_run.add_properties({
            'iteration': str(iteration),
            'pipeline_spec': pipeline_spec,
            'runTemplate': 'automl_child'
        })
        return child_run

    @staticmethod
    def get_all_sibling_child_runs(child_run: _OfflineAutoMLRun) -> List[_OfflineAutoMLRun]:
        """Get all sibling child runs."""
        folder_containing_all_child_runs = os.path.dirname(child_run.run_folder)
        child_run_ids_and_folders = [
            (f.name, f.path) for f in os.scandir(folder_containing_all_child_runs)
            if f.is_dir() and os.path.basename(folder_containing_all_child_runs) in f.name]
        return [_OfflineAutoMLRun(run_id, run_folder) for (run_id, run_folder) in child_run_ids_and_folders]
