def process_items(items: list[str]) -> list[int]:
    return [int(item) for item in items]


def find_user(users: list, user_id: int) -> str | None:
    for user in users:
        if user["id"] == user_id:
            return user["name"]
    return None


def merge_data(data1: dict[str, int], data2: dict[str, int]) -> dict[str, int]:
    result = {**data1, **data2}
    return result


def main():
    numbers = process_items(["1", "2", "3"])

    users = [{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bob"}]
    name = find_user(users, 2)

    merged = merge_data({"a": 1}, {"b": 2})

    print(numbers, name, merged)
