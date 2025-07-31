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
    rows = list(reader)

    found_values = []
    weights = []

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
                found_values.append(val)
                weights.append(weight)

    if found_values:
        weighted_sum = sum(val * weight for val, weight in zip(found_values, weights))
        total_weight = sum(weights)
        weighted_average = weighted_sum / total_weight
        return str(weighted_average)
    else:
        return "-1"
