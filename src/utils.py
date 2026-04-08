from typing import TypeVar

T = TypeVar("T")


def flatten(nested: list[list[T]]) -> list[T]:
    result: list[T] = []
    for sublist in nested:
        result.extend(sublist)
    return result


def chunk(items: list[T], size: int) -> list[list[T]]:
    if size <= 0:
        raise ValueError("Chunk size must be positive")
    return [items[i : i + size] for i in range(0, len(items), size)]


def unique(items: list[T]) -> list[T]:
    seen: set[T] = set()
    result: list[T] = []
    for item in items:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result


def safe_get(mapping: dict[str, T], key: str, default: T) -> T:
    return mapping.get(key, default)


def pluralize(word: str, count: int) -> str:
    if count == 1:
        return word
    return word + "s"


def truncate(text: str, max_length: int, suffix: str = "...") -> str:
    if max_length < len(suffix):
        raise ValueError("max_length must be >= length of suffix")
    if len(text) <= max_length:
        return text
    return text[: max_length - len(suffix)] + suffix
