import json


def to_send(l_vars: list[str]) -> str:  # передаём с бэка
    return json.dumps(l_vars)  # можно отправить на фронт


def to_accept(json_string: str) -> dict[str, str]:  # передаём с фронта
    return json.loads(json_string)  # можно использовать в бэке
