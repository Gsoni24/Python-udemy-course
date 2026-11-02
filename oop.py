class Lamp:
    def __init__(self, brand:str) -> None:
        self.brand = brand
        self.state = 'OFF'

    def turn_on(self) -> None:
        self.state = 'ON'
        print(f'{self.brand}: ON')


    def turn_off(self) -> None:
        self.state = 'OFF'
        print(f'{self.brand}: OFF')


smeg: Lamp = Lamp('Smeg')
samsung: Lamp = Lamp('Samsung')

smeg.turn_on()
samsung.turn_on()
samsung.turn_off()

print('Smeg', smeg.state)
print('Samsung', samsung.state)
