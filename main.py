import calculator


if __name__ == '__main__':
    calc = calculator.Calculator(years=1)
    calc.add_car(
        calculator.Car('Toyota', 30000, 7, 1200, 2500)
    )
    calc.add_car(
        calculator.ElectricCar('Tesla', 40000, 5500, 150)
    )
    calc.add_car(
        calculator.Car('Range Rover', 50000, 7, 1200, 2500)
    )

    calc.print_cars()