import csv
import io


def task1(search: dict, data: str) -> str:
    reader = csv.DictReader(io.StringIO(data))
    fieldnames = reader.fieldnames

    if not set(search.keys()).issubset(set(fieldnames)):
        raise ValueError("Key mismatch")

    for row in reader:
        match = True
        for key, value in search.items():
            if row[key] != value:
                match = False
                break

        if match:
            return row["value"]

    return "-1"


def task2(search_list: list, data: str) -> str:
    reader = csv.DictReader(io.StringIO(data))
    fieldnames = reader.fieldnames
    rows = list(reader)

    for search_dict in search_list:
        if not set(search_dict.keys()).issubset(set(fieldnames)):
            raise ValueError("Key mismatch")

    weighted_sum = 0
    total_weight = 0

    for search_dict in search_list:
        for row in rows:
            match = True
            for key, value in search_dict.items():
                if row.get(key) != value:
                    match = False
                    break

            if match:
                val = int(row["value"])
                weight = 10 if val % 2 == 1 else 20
                weighted_sum += val * weight
                total_weight += weight

    if total_weight > 0:
        weighted_average = weighted_sum / total_weight
        return str(weighted_average)
    else:
        return "-1"
