from collections import Counter
from time import sleep


class Car:
    def __init__(self, brand: str, color: str, model: int) -> None:
        self.brand = brand
        self.color = color
        self.model = model

    def drive(self, distance: int, speed: int) -> None:
        print(f'{self.brand} {self.model} [{self.color}] started the journey ...')
        for i in range(1, distance + 1):
            sleep(60 / speed)
            print(f'KM: {i}')

        print(f'{self.brand} {self.model} [{self.color}] completed the journey ...')


def test_car() -> None:
    volvo: Car = Car('Volvo', 'Black', 200)
    volvo.drive(10, 140)

def create_cars(cars: list[Car]) -> None:
    brand: str = input('Enter the brand name: ')
    color: str = input('Enter the color of the car: ')
    try:
        model: int = int(input('Enter the model year: '))
        amount: int = int(input('Enter the amount: '))

        for i in range(amount):
            cars.append(Car(brand, color, model))
        
        print('Cars Created!')

    except ValueError:
        print("Error: Please enter number as digits")


def display_stock(cars: list[Car]) -> None:
    car_tuples: list[tuple[str, str, int]] = [(car.brand, car.color, car.model)for car in cars]
    counter: Counter[tuple[str, str, int]] = Counter(car_tuples)

    for (brand, color, model), count in counter.items():
        print(f'{brand} {model} [{color}]: {count} in stock')

# def sell_car(cars: list[Car]) -> None:




def main() -> None:
    cars: list[Car] = [ Car('Volvo', 'Red', 200),
                        Car('Volvo', 'Red', 200),
                        Car('Toyota', 'Green', 321) ]

    print('Type: "create" to create cars and "display" to display the current stock')
    while True:
        user_input: str = input('You: ').lower().strip()
        if user_input == "create":
            create_cars(cars)
        elif user_input == "display":
            display_stock(cars)
        else:
            print(f'Unknow Command: {user_input}')



if __name__ == '__main__':
    main()
