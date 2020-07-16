import requests

from monitor.entities.MongoService import MongoService
from monitor.requests.BuildsRequest import BuildRequest


class BuildsClient:
    BUILDS = "{}{}".format(MongoService.MONGO_SERVICE, "/builds")

    def create_new_build(self):
        print("Build path {}".format(self.BUILDS))

        build_request = BuildRequest().build()
        post = requests.post(
            url=self.BUILDS,
            headers={"Content-Type": "application/json"},
            json=build_request.__dict__,
        )
        return post.json()

    def find_build_by_id(self, id):
        build_request = requests.get(
            url="{}{}".format(self.BUILDS, "/search/findById"),
            headers={"Content-Type": "application/json"},
            params={"id": id}
        )
        return build_request.json()

    def get_latest_build_id(self):
        request = requests.get(
            url="{}{}".format(self.BUILDS, "/search/findAllBuildsByOrderByBuildStartTimeDesc"),
            headers={"Content-Type": "application/json"},
        )
        json_get = request.json()["content"]
        return json_get[0]["id"]

    def update_build_record(self, build):
        response = requests.patch(
            url="{}/{}".format(self.BUILDS, build["id"]),
            headers={"Content-Type": "application/json"},
            json=build
        )
        return response.json()
