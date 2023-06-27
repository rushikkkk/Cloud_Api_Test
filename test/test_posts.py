import pytest

from api_client import ApiClient
from helper.schema_helper import Schema
from random import randint


class TestPosts:
    def test_expected_200_get_all_posts(self, api: ApiClient, get_schema) -> None:
        res = api.get_posts()
        assert res.status_code == 200
        assert Schema.validate(res.json(), get_schema) is True

    def test_expected_200_get_one_posts(self, api: ApiClient, get_one_schema) -> None:
        data = randint(1, 50)
        res = api.get_posts(path_param=f"/{data}")
        assert res.status_code == 200
        assert res.json()["id"] == data
        assert Schema.validate(res.json(), get_one_schema) is True

    @pytest.mark.xfail
    def test_expect_not_found_posts(self, api: ApiClient):
        data = randint(500, 1000)
        res = api.get_posts(path_param=f"/{data}")
        assert res.status_code == 404
        assert res.json() == {}

    def test_expected_201_create_posts(self, api: ApiClient, post_schema) -> None:
        data = {"userId": 6, "title": "test title", "body": "test body"}
        res = api.post_posts(data)
        assert res.status_code == 201
        assert Schema.validate(res.json(), post_schema) is True

    def test_expected_200_delete_posts(
        self, create_posts: dict, api: ApiClient
    ) -> None:
        res = api.delete_posts(f"/{create_posts['id']}")
        assert res.status_code == 200
