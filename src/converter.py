def to_celsius(fahrenheit: float) -> float:
    return (fahrenheit - 32) * 5.0 / 9.0


def to_fahrenheit(celsius: float) -> float:
    return celsius * 9.0 / 5.0 + 32


def to_kg(pounds: float) -> float:
    return pounds * 0.453592


def to_miles(km: float) -> float:
    return km * 0.621371


def to_liters(gallons: float) -> float:
    return gallons * 3.78541


def to_inches(cm: float) -> float:
    return cm / 2.54


def to_meters(feet: float) -> float:
    return feet * 0.3048


def batch_convert(temperatures: list[float]) -> list[float]:
    return [to_celsius(t) for t in temperatures]


def format_result(value: float, unit: str) -> str:
    return f"{value:.2f} {unit}"


def main():
    temp = to_celsius("hot")
    weight = to_kg([150])
    result = format_result("100", 42)
    converted = batch_convert([32.0, 72.0, 100.0, 212.0])
    distance = to_miles(10.0)
    print(temp, weight, result)
    print(converted)
    print(distance)
    print(to_fahrenheit(100.0))
    print(to_liters(5.0))
    print(to_inches(10.0))
    print(to_meters(6.0))


if __name__ == "__main__":
    main()
