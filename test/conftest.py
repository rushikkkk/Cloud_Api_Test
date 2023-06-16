import os
from api_client import ApiClient


from pytest import fixture
from helper.schema_helper import Schema
from random import randint


@fixture(scope="function")
def get_schema() -> dict:
    get_path_schema = os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
        "schema",
        "get_200_posts.json",
    )
    return Schema.read_schema(get_path_schema)


@fixture(scope="function")
def get_one_schema() -> dict:
    get_path_schema = os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
        "schema",
        "get_200_one_posts.json",
    )
    return Schema.read_schema(get_path_schema)


@fixture(scope="function")
def post_schema() -> dict:
    get_path_schema = os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
        "schema",
        "post_201_posts.json",
    )
    return Schema.read_schema(get_path_schema)


@fixture(scope="function")
def create_posts(api: ApiClient) -> dict:
    userId = randint(1, 10)
    data = {"userId": userId, "title": "test title", "body": "test body"}
    return api.post_posts(data).json()
