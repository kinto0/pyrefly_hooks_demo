from dataclasses import dataclass, field


@dataclass
class User:
    name: str
    email: str
    age: int
    is_active: bool = True

    def display_name(self) -> str:
        return f"{self.name} <{self.email}>"

    def can_vote(self) -> bool:
        return self.age >= 18 and self.is_active


@dataclass
class Product:
    name: str
    price: float
    quantity: int
    tags: list[str] = field(default_factory=list)

    def total_value(self) -> float:
        return self.price * self.quantity

    def is_in_stock(self) -> bool:
        return self.quantity > 0

    def apply_discount(self, percentage: float) -> float:
        if percentage < 0 or percentage > 100:
            raise ValueError("Discount must be between 0 and 100")
        discount: float = self.price * (percentage / 100.0)
        return self.price - discount


@dataclass
class Order:
    user: User
    items: list[Product]
    order_id: str

    def total(self) -> float:
        return sum(item.total_value() for item in self.items)

    def item_count(self) -> int:
        return len(self.items)

    def summary(self) -> str:
        return f"Order {self.order_id}: {self.item_count()} items, ${self.total():.2f}"
