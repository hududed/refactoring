from dataclasses import dataclass, field
from enum import Enum, auto
from typing import Protocol


class FuelType(Enum):
    PETROL = auto()
    DIESEL = auto()
    ELECTRIC = auto()


class TruckCabStyle(Enum):
    REGULAR = auto()
    EXTENDED = auto()
    CREW = auto()

@dataclass
class Price(Protocol):

    def compute_price(self) -> int:
        ...

@dataclass
class PricePerKm(Price):
    price_per_km: int
    km_driven: int

    def compute_price(self) -> int:
        return (self.price_per_km * self.km_driven)

@dataclass
class PricePerDay(Price):
    price_per_day: int
    days_rented: int

    def compute_price(self) -> int:
        return (self.price_per_day * self.days_rented)

@dataclass
class PricePerMonth(Price):
    price_per_month: int
    months_rented: int

    def compute_price(self) -> int:
        return (self.price_per_month * self.months_rented)
    
@dataclass
class Vehicle:
    brand: str
    model: str
    color: str
    fuel_type: FuelType
    license_plate: str
    reserved: bool
    price: list[Price] = field(default_factory=list)


@dataclass
class Car(Vehicle):
    number_of_seats: int = 5
    storage_capacity_litres: int = 100

@dataclass
class Truck(Vehicle):
    cab_style: TruckCabStyle = TruckCabStyle.REGULAR


@dataclass
class Trailer:
    brand: str
    model: str
    capacity_m3: int
    reserved: bool
    price: list[Price] = field(default_factory=list)


def main():
    pass
    

if __name__ == "__main__":
    main()
