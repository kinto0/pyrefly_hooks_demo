def format_name(first: str, last: str) -> str:
    return f"{first} {last}"


def format_price(amount: float, currency: str) -> str:
    return f"{currency}{amount:.2f}"


def format_list(items: list[str]) -> str:
    return ", ".join(items)


def main():
    print(format_name("John", "Doe"))
    print(format_price(9.99, "USD"))
    print(format_list(["apple", "banana", "cherry"]))


if __name__ == "__main__":
    main()
