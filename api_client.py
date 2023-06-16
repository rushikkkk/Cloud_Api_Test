import requests
from requests import Response
from helper.logger import log


class ApiClient:
    __endpoint = "/posts"

    def __init__(self, url):
        self.url = url

    def get_posts(self, path_param: str = "") -> Response:
        res = requests.get(f"{self.url}{self.__endpoint}{path_param}")
        log(res)
        return res

    def post_posts(self, payload: dict) -> Response:
        res = requests.post(f"{self.url}{self.__endpoint}", json=payload)
        log(res)
        return res

    def delete_posts(self, path_param) -> Response:
        res = requests.delete(f"{self.url}{self.__endpoint}{path_param}")
        log(res)
        return res
