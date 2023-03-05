from typing import Any
from API.app_data.base_requests import BaseRequests
from API.test_data.data_url import MainURL

headers = {}


class RequestsForTestAPI:
    def __init__(self) -> None:
        self.request = BaseRequests()
        self.base_url = MainURL().get_url_from_dict("base_url")
        self.headers = headers

    def auth_user(self, payload: dict) -> Any:
        return self.request.post(url=f"{self.base_url}/auth/login/", json=payload)

    def login_check(self):
        return self.request.get(url=f"{self.base_url}/auth/login_check/", headers=self.headers)


