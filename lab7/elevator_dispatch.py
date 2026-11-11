
import re


def parse_request(text):
    if not isinstance(text, str):
        return None

    match = re.fullmatch(r"\s*(-?\d+)\s*->\s*(-?\d+)\s*", text)

    if not match:
        return None

    return int(match.group(1)), int(match.group(2))


def total_travel(floors_csv):
    if not isinstance(floors_csv, str) or not floors_csv.strip():
        return None

    try:
        parts = floors_csv.split(",")

        if any(not part.strip() for part in parts):
            return None

        floors = [int(part.strip()) for part in parts]

        if any(floor < 0 for floor in floors):
            return None

        return sum(
            abs(floors[i + 1] - floors[i])
            for i in range(len(floors) - 1)
        )

    except (ValueError, TypeError):
        return None


def load_percent(text):
    if not isinstance(text, str):
        return None

    match = re.fullmatch(
        r"\s*(\d+)\s+of\s+(\d+)\s*",
        text,
        re.IGNORECASE
    )

    if not match:
        return None

    load = int(match.group(1))
    capacity = int(match.group(2))

    if capacity <= 0 or load > capacity:
        return None

    return load * 100 // capacity


def main():
    print("==== Running parse_request ====")
    user_input = input("Enter a request as FROM->TO (e.g. 5->9): ")
    result = parse_request(user_input)
    print("From and To:", result if result is not None else "Invalid request")

    print("\n==== Running total_travel ====")
    user_input = input("Enter floors visited as CSV (e.g. 1,5,3,9): ")
    result = total_travel(user_input)
    print("Floors Travelled:", result if result is not None else "Invalid floors")

    print("\n==== Running load_percent ====")
    user_input = input("Enter load as 'X of Y' (e.g. 450 of 630): ")
    result = load_percent(user_input)
    print("Load Percent:", result if result is not None else "Invalid load")


if __name__ == "__main__":
    main()
