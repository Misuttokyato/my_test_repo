# TODO решите задачу
import json

FILENAME = "input.json"


def task() -> float:
    with open(FILENAME) as json_file:
        json_data = json.load(json_file)

    result = sum([item["score"] * item["weight"] for item in json_data])

    return round(result, 3)


print(task())
