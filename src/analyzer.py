def analyze_scores(scores: list[int]) -> float:
    total = sum(scores)
    return total / len(scores)


def categorize(value: float) -> str | None:
    if value >= 90:
        return "excellent"
    elif value >= 70:
        return "good"
    elif value >= 50:
        return "average"
    return None


def summarize(data: dict[str, int]) -> str:
    parts = []
    for key, val in data.items():
        parts.append(f"{key}: {val}")
    return ", ".join(parts)


def main():
    result = analyze_scores([90, 85, 72])

    category = categorize(result)

    summary = summarize({"math": 90, "english": 85, "science": 72})

    print(result, category, summary)


if __name__ == "__main__":
    main()
