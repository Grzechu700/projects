import csv
import io


def task1(search: dict, data: str) -> str:
    reader = csv.DictReader(io.StringIO(data))
    fieldnames = reader.fieldnames

    if not fieldnames:
        raise ValueError("No header found in data.")

    available_fields = set(fieldnames) - {"value"}
    if not set(search) <= available_fields:
        raise ValueError("Key mismatch")

    return next(
        (row["value"] for row in reader
         if all(row.get(key) == value for key, value in search.items())),
        "-1"
    )


def task2(search_list: list, data: str) -> str:
    reader = csv.DictReader(io.StringIO(data))
    fieldnames = reader.fieldnames

    if not fieldnames:
        raise ValueError("No header found in data.")

    rows = list(reader)

    available_fields = set(fieldnames) - {"value"}
    for search_dict in search_list:
        if not set(search_dict) <= available_fields:
            raise ValueError("Key mismatch")

    weighted_sum = 0
    total_weight = 0

    for row in rows:
        if any(all(row.get(key) == value for key, value in search_dict.items())
               for search_dict in search_list):
            val = int(row["value"])
            weight = 10 if val % 2 == 1 else 20
            weighted_sum += val * weight
            total_weight += weight

    return str(weighted_sum / total_weight) if total_weight > 0 else "-1"
