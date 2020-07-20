import json
import logging
import time
from io import BytesIO
from typing import TYPE_CHECKING, Optional

from forecastflow import api
from forecastflow.enums import Status
from forecastflow.exceptions import InvalidID, OperationFailed
from forecastflow.firebase_api import cloud_firestore, storage
from forecastflow.firebase_api.exceptions import NotFound
from forecastflow.model import Model

if TYPE_CHECKING:
    from forecastflow import Project, User
    from forecastflow.training import TrainingSettings

logger = logging.getLogger(__name__)


class DataSource:
    """
    ForecastFlow data source class
    """

    def __init__(self, project: 'Project', data_source_id: str):
        """
        Instantiate object with given data source ID

        Args:
            project:
                Project which data source belong to.

            data_source_id:
                ID of data source you want to open.
        """
        self.project = project
        self.data_source_id = data_source_id
        self.name = None
        self.status = None
        self.__profile_path = None
        self.__profile = None
        self.update()

    @property
    def _document(self) -> dict:
        doc = cloud_firestore.get(f"users/{self.user.user_id}"
                                  f"/projects/{self.project.project_id}"
                                  f"/dataSources/{self.data_source_id}",
                                  self.user.id_token)
        return doc['fields']

    @property
    def did(self) -> str:
        return self.data_source_id

    def update(self):
        """
        Update name, status
        """
        try:
            document = self._document
        except NotFound:
            raise InvalidID('Given Data Source ID is not found')

        self.name = document['name']

        if document['profile'].startswith(self.user.user_id):  # TODO: use status instead of profile in future
            self.status = Status.COMPLETED
            self.__profile_path = document['profile']
        elif document['profile'] == '':
            self.status = Status.WAITING
        else:
            self.status = Status(document['profile'])

        logger.info(f"Profiling '{self.name}': {self.status.value}")

    @property
    def user(self) -> 'User':
        return self.project.user

    @property
    def uid(self) -> str:
        return self.project.user.user_id

    def wait_until_done(self):
        """
        Wait until ForecastFlow finish profiling.
        """
        while self.status != Status.COMPLETED \
                and self.status != Status.ERROR:
            self.update()
            time.sleep(5)

        if self.status == Status.ERROR:
            document = self._document
            error_info = document.get('errorInfo')
            if error_info is None:
                raise OperationFailed("Profiler quit with Error")
            else:
                raise OperationFailed(f"{error_info['message']}\n"
                                      f"error_log_id: {error_info['errorLogId']}")

    def create_model(self, train_settings: 'TrainingSettings', name: str, test_frac: Optional[float]=None,
                     test_data_source: Optional['DataSource']=None, description: str=''):
        """
        Train model with this datasource.

        Args:
            train_settings:
                Object of ClassifierTrainingSettings or RegressorTrainingSettings
            
            name:
                Name of model.

            test_frac:
                Fraction of rows in train that will belong to the test.
                Round off to two decimal places.

            test_data_source:
                Data to test with.

            description:
                Description of model.

        Returns:
            ForecastFlow model object.
        """
        if test_data_source is not None:
            test_pid = test_data_source.pid
            test_did = test_data_source.data_source_id
        else:
            test_pid = None
            test_did = None
        mid = api.v3.create_model(
            id_token=self.user.id_token,
            name=name,
            train_settings=train_settings,
            train_pid=self.pid,
            train_did=self.data_source_id,
            test_pid=test_pid,
            test_did=test_did,
            test_frac=test_frac,
            description=description
        )
        return Model(project=self.project, model_id=mid)

    @property
    def pid(self) -> str:
        return self.project.project_id

    @property
    def file_path(self) -> str:
        """
        Firebase storage path to data file.
        """
        return f'{self.uid}/rawData/{self.data_source_id}'

    @property
    def profile_path(self) -> str:
        """
        Firebase storage path to profile.
        """
        if self.__profile_path is None:
            self.wait_until_done()
        return self.__profile_path

    @property
    def profile(self) -> dict:
        if self.__profile is None:
            with BytesIO() as f:
                storage.download(self.profile_path, f, self.user.id_token)
                f.seek(0)
                self.__profile = json.loads(f.read())
        return self.__profile
