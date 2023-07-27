import uuid
import os


def clear() -> None:
    os.system('clear')


def new_car():
    car = {}
    car['id'] = str(uuid.uuid4())
    car['brand'] = input('Enter the brand of the car: ')
    car['model'] = input('Enter the model of the car: ')
    car['position'] = input('Enter the position of the car: ')
    car['color'] = input('Enter the color of the car: ')
    car['year'] = input('Enter the year of the car: ')
    print('Choose the fuel type of the car:')
    print('1. Gasoline')
    print('2. Diesel')
    print('3. Electro')
    fuel_type = input('Enter your choice (1, 2 or 3): ')
    if fuel_type == '1':
        car['fuel_type'] = 'Gasoline'
    elif fuel_type == '2':
        car['fuel_type'] = 'Diesel'
    elif fuel_type == '3':
        car['fuel_type'] = 'Electro'
    else:
        print('Invalid choice, please try again.')
        return
    car['mileage'] = input('Enter the mileage of the car: ')
    car['transmission'] = input('Enter the transmission of the car: ')

    if not os.path.exists('cars'):
        os.makedirs('cars')

    with open(f'cars/{car["id"]}.txt', 'w') as file:
        file.write(f'ID: {car["id"]}\n')
        file.write(f'Brand: {car["brand"]}\n')
        file.write(f'Model: {car["model"]}\n')
        file.write(f'Position: {car["position"]}\n')
        file.write(f'Color: {car["color"]}\n')
        file.write(f'Year: {car["year"]}\n')
        file.write(f'Fuel Type: {car["fuel_type"]}\n')
        file.write(f'Mileage: {car["mileage"]}\n')
        file.write(f'Transmission: {car["transmission"]}\n\n')


def change_car():
    id = input('Enter the ID of the car you want to change: ')

    if not os.path.exists(f'cars/{id}.txt'):
        print("Car not found")
        return

    with open(f'cars/{id}.txt', 'r') as file:
        lines = file.readlines()
        car = {}
        for line in lines:
            if line.startswith('ID'):
                car['id'] = line.split(': ')[1].strip()
            elif line.startswith('Brand'):
                car['brand'] = line.split(': ')[1].strip()
            elif line.startswith('Model'):
                car['model'] = line.split(': ')[1].strip()
            elif line.startswith('Position'):
                car['position'] = line.split(': ')[1].strip()
            elif line.startswith('Color'):
                car['color'] = line.split(': ')[1].strip()
            elif line.startswith('Year'):
                car['year'] = line.split(': ')[1].strip()
            elif line.startswith('Fuel Type'):
                car['fuel_type'] = line.split(': ')[1].strip()
            elif line.startswith('Mileage'):
                car['mileage'] = line.split(': ')[1].strip()
            elif line.startswith('Transmission'):
                car['transmission'] = line.split(': ')[1].strip()

    print('Enter new values for the car (leave blank to keep current value):')
    brand = input('Brand: ')
    if brand:
        car['brand'] = brand
    model = input('Model: ')
    if model:
        car['model'] = model
    position = input('Position: ')
    if position:
        car['position'] = position
    color = input('Color: ')
    if color:
        car['color'] = color
    year = input('Year: ')
    if year:
        car['year'] = year
    fuel_type = input('Fuel Type: ')
    if fuel_type:
        car['fuel_type'] = fuel_type
    mileage = input('Mileage: ')
    if mileage:
        car['mileage'] = mileage
    transmission = input('Transmission: ')
    if transmission:
        car['transmission'] = transmission

    with open(f'cars/{id}.txt', 'w') as file:
        file.write(f'ID: {car["id"]}\n')
        file.write(f'Brand: {car["brand"]}\n')
        file.write(f'Model: {car["model"]}\n')
        file.write(f'Position: {car["position"]}\n')
        file.write(f'Color: {car["color"]}\n')
        file.write(f'Year: {car["year"]}\n')
        file.write(f'Fuel Type: {car["fuel_type"]}\n')
        file.write(f'Mileage: {car["mileage"]}\n')
        file.write(f'Transmission: {car["transmission"]}\n\n')


def search() -> None:
    pass


if __name__ == '__main__':
    history = []
    while True:
        command = input('\nEnter a command (/new, /change, /search, /quit): ')
        history.append(command)
        if command == '/new':
            new_car()
            input('.....')
            clear()
        elif command == '/change':
            change_car()
            input('.....')
            clear()
        elif command == '/search':
            pass
        elif command == '/quit':
            with open('history.txt', 'a') as file:
                for command in history:
                    file.write(command + '\n')
            break
