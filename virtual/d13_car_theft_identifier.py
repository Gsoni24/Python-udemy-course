class Car:
    def __init__(self, license_plate: str) -> None:
        if len(license_plate) != 6:
            raise ValueError('Invalid license plate.')

        self.license_plate = license_plate.upper()


class StolenCarRegistry:
    def __init__(self) -> None:
        self.stolen_plates: set[str] = set()
    
    def add_stolen_plates(self, plates: list[str]) -> None:
        for plate in plates:
            self.stolen_plates.add(plate.upper())

    def is_stolen(self, plate: str) -> bool:
        return plate.upper() in self.stolen_plates

    def remove_stolen_plate(self, plate:str) -> None:
        if plate in self.stolen_plates:
            self.stolen_plates.remove(plate)
    
    def count_stolen_plate(self) -> int:
        count = 0
        for plate in self.stolen_plates:
            count += 1
        return count



def main() -> None:
    registry: StolenCarRegistry = StolenCarRegistry()
    registry.add_stolen_plates(['ABC123', 'XYZ456', 'BOB789', 'TST111'])
    # registry.remove_stolen_plate('TST111')

    print('Welcome to car theft identifier!')
    print(f'Total number of car that is sotlen: {registry.count_stolen_plate()}')
    while True:
        plate: str= input("Enter a license plate number: ").strip()
        car: Car = Car(plate)
        
        if registry.is_stolen(car.license_plate):
            print(f'❌ Car with {car.license_plate} is: REPORTED STOLEN')
        else:
            print(f'✅ Car with {car.license_plate} is: OK')



if __name__ == '__main__':
    main()

