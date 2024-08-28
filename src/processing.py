from typing import Any


def filter_by_state(operations: list[dict[str, Any]], state: str = "EXECUTED") -> Any:
    """Функция принимает список операций и возвращает список со статусом 'EXECUTED'"""

    return [i for i in operations if i.get("state") == state]


print(
    filter_by_state(
        [
            {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
            {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        ]
    )
)


def sort_by_date(operations: list[dict[str, Any]], reverse: bool = True) -> Any:
    """Функция принимает список операций и возвращает отсортированный по дате список"""

    sort_operations_date = sorted(operations, key=lambda new_operations: new_operations["date"], reverse=reverse)
    return sort_operations_date


print(
    sort_by_date(
        [
            {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
            {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        ]
    )
)
