def format_report(data: dict[str, int]) -> str:
    lines = []
    for key, value in data.items():
        lines.append(f"{key}: {value}")
    return "\n".join(lines)


def get_top_items(items: list[str], count: int) -> list[str]:
    return items[:count]


def calculate_percentage(part: int, total: int) -> float:
    if total == 0:
        return 0.0
    return (part / total) * 100


def main():
    report = format_report({"sales": 100, "returns": 5})
    top = get_top_items(["alpha", "beta", "gamma"], 2)
    pct = calculate_percentage(10, 20)
    print(report, top, pct)


if __name__ == "__main__":
    main()
