from json import load
from jsonschema import ValidationError, validate


class Schema:
    @staticmethod
    def read_schema(path_file: str) -> dict:
        try:
            with open(path_file) as schema:
                return load(schema)
        except Exception("not found file") as err:
            print(err)

    @staticmethod
    def validate(json: list, schema: dict):
        try:
            validate(instance=json, schema=schema)
            return True
        except ValidationError("bad json"):
            return False
