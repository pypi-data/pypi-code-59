import requests
import json


class DoccanoApi:
    def __init__(self, username: str, password: str, url: str):
        self._url = url
        self._username = username
        self._password = password
        self._token = self._login()

    def get_projects(self) -> list:
        response = requests.get(url=f"{self._url}/v1/projects",
                                headers=self._get_headers(accept="application/json"))

        response.raise_for_status()

        try:
            projects = [{"name": project["name"],
                         "id": project["id"]} for project in response.json()]

        except KeyError as error:
            raise KeyError(error)
        else:
            return projects

    def get_texts(self, project_id: int) -> list:
        response = requests.get(url=f"{self._url}/v1/projects/{project_id}/docs/download",
                                headers=self._get_headers(accept="application/json"),
                                params={"q": "json"})
        response.raise_for_status()

        docs_list = response.text.split("\n")
        try:
            docs = self._format_docs(docs_list)
        except KeyError as error:
            raise KeyError(error)
        else:

            labels = self.get_labels(project_id)
            self._substitute_labels(docs, labels)

        return docs

    def put_text(self, project_id: int, text: str) -> None:

        loaded_text = self._load_text(text)

        response = requests.post(url=f"{self._url}/v1/projects/{project_id}/docs/upload",
                                 headers=self._get_headers(),
                                 files={"file": ("text.txt", loaded_text, "plain")},
                                 data={"file": ("text.txt", loaded_text, "plain"),
                                       "format": "plain"})
        response.raise_for_status()

    def get_labels(self, project_id: int) -> list:
        response = requests.get(url=f"{self._url}/v1/projects/{project_id}/labels",
                                headers=self._get_headers(accept="application/json"))

        response.raise_for_status()
        try:
            labels = [{"id": label["id"],
                       "text": label["text"]} for label in response.json()]

        except KeyError as error:
            raise KeyError(error)
        else:
            return labels

    def _login(self) -> str:
        response = requests.post(url=f"{self._url}/v1/auth-token",
                                 json={"username": self._username,
                                       "password": self._password})
        response.raise_for_status()

        try:
            token = response.json()["token"]
        except KeyError as error:
            raise KeyError(error)
        else:
            return token

    def _get_headers(self, accept: str = None) -> dict:
        headers = {"Authorization": f"Token {self._token}"}

        if accept:
            headers["Accept"] = accept

        return headers

    def _substitute_labels(self, docs: list, labels: list) -> None:
        for doc in docs:
            for annotation in doc["annotations"]:
                annotation["label"] = self._get_label_by_id(annotation["label"], labels)

    def _load_text(self, text: str) -> str:
        if self._is_txt_file(text):
            with open(text, "r") as file:
                return file.read()
        else:
            return text

    @staticmethod
    def _is_txt_file(text: str) -> bool:
        return ".txt" in text

    @staticmethod
    def _format_docs(docs_list: list):
        docs = []
        for i in range(len(docs_list) - 1):
            current_doc = json.loads(docs_list[i])
            for annotation in current_doc["annotations"]:
                annotation.pop("user")

            docs.append({"id": current_doc["id"],
                         "text": current_doc["text"],
                         "annotations": current_doc["annotations"]})

        return docs

    @staticmethod
    def _get_label_by_id(label_id: int, labels: list) -> str:
        for label in labels:
            if label["id"] == label_id:
                return label["text"]

        raise ValueError(f"No label found for id {label_id}.")

