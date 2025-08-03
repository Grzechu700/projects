import csv
import io


def _validate_search_keys(search_dict: dict, available_fields: set) -> None:
    """Validate that all search keys exist in available fields.

    Args:
        search_dict: Dictionary with search keys
        available_fields: Set of available field names

    Raises:
        ValueError: If any search key is not in available fields
    """
    if not set(search_dict) <= available_fields:
        raise ValueError("Key mismatch")


def validate_headers(data: str, search_params: dict | list) -> tuple[csv.DictReader, set]:
    """Validates CSV headers and search parameters.

    Args:
        data: CSV data as a string
        search_params: Dictionary or list of dictionaries with search parameters

    Returns:
        A tuple containing the CSV reader and set of available fields

    Raises:
        ValueError: If headers are missing or search keys don't match available fields
    """
    reader = csv.DictReader(io.StringIO(data))
    fieldnames = reader.fieldnames

    if not fieldnames:
        raise ValueError("No header found in data.")

    available_fields = set(fieldnames) - {"value"}

    # Validate search parameters
    if isinstance(search_params, dict):
        _validate_search_keys(search_params, available_fields)
    elif isinstance(search_params, list):
        for search_dict in search_params:
            _validate_search_keys(search_dict, available_fields)

    return reader, available_fields


def task1(search: dict, data: str) -> str:
    """Find first match in CSV data based on search criteria.

    Args:
        search: Dictionary with search criteria
        data: CSV data as a string

    Returns:
        The value from the first matching row or "-1" if no match is found

    Raises:
        ValueError: If headers are missing or search keys don't match available fields
    """
    reader, _ = validate_headers(data, search)

    return next(
        (row["value"] for row in reader
         if all(row.get(key) == value for key, value in search.items())),
        "-1"
    )


def task2(search_list: list[dict], data: str) -> str:
    """Calculate weighted average for values matching any search criteria.

    Args:
        search_list: List of dictionaries with search criteria
        data: CSV data as a string

    Returns:
        Weighted average rounded to one decimal place as string, or "-1" if no matches

    Raises:
        ValueError: If headers are missing or search keys don't match available fields
    """
    reader, _ = validate_headers(data, search_list)

    rows = list(reader)

    weighted_sum = 0
    total_weight = 0

    for row in rows:
        # Check if row matches any search criteria
        matches = any(
            all(row.get(key) == value for key, value in search_dict.items())
            for search_dict in search_list
        )

        if matches:
            val = int(row["value"])
            weight = 10 if val % 2 else 20  # Simplified odd/even check
            weighted_sum += val * weight
            total_weight += weight

    return str(round(weighted_sum / total_weight, 1)) if total_weight > 0 else "-1"
