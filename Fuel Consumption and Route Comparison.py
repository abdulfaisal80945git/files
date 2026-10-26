
n = int(input("Enter number of vehicles: "))

for i in range(n):
    print("\nVehicle", i + 1)

    name = input("Enter vehicle name: ")
    distance = float(input("Enter journey distance (km): "))
    mileage = float(input("Enter mileage (km/litre): "))
    price = float(input("Enter fuel price per litre: "))

    if distance < 0 or mileage <= 0 or price < 0:
        print("Invalid input!")
        continue

    fuel = distance / mileage
    cost = fuel * price

    print("Vehicle:", name)
    print("Fuel required:", round(fuel, 2), "litres")
    print("Journey cost: Rs.", round(cost, 2))
