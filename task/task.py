import csv
import io


def validate_headers(data: str, search_params):
    # Creating csv.DictReader object
    reader = csv.DictReader(io.StringIO(data))
    fieldnames = reader.fieldnames

    # Checks if fieldnames exist
    if not fieldnames:
        raise ValueError("No header found in data.")

    # Creates Set of available fields
    available_fields = set(fieldnames) - {"value"}

    # Validates keys if searching
    if isinstance(search_params, dict):
        if not set(search_params) <= available_fields:
            raise ValueError("Key mismatch")
    elif isinstance(search_params, list):
        for search_dict in search_params:
            if not set(search_dict) <= available_fields:
                raise ValueError("Key mismatch")

    # Returns reader and available fields
    return reader, available_fields


def task1(search: dict, data: str) -> str:
    reader, _ = validate_headers(data, search)

    return next(
        (row["value"] for row in reader
         if all(row.get(key) == value for key, value in search.items())),
        "-1"
    )


def task2(search_list: list, data: str) -> str:
    reader, _ = validate_headers(data, search_list)

    rows = list(reader)

    weighted_sum = 0
    total_weight = 0

    for row in rows:
        if any(all(row.get(key) == value for key, value in search_dict.items())
               for search_dict in search_list):
            val = int(row["value"])
            weight = 10 if val % 2 == 1 else 20
            weighted_sum += val * weight
            total_weight += weight

    return str(round(weighted_sum / total_weight, 1)) if total_weight > 0 else "-1"