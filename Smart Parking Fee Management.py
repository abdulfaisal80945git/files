
from datetime import datetime
from math import ceil

# Parking rates per hour
rates = {
    "bike": 10,
    "car": 30,
    "bus": 50
}

daily_limits = {
    "bike": 100,
    "car": 300,
    "bus": 500
}

overnight_charge = 50
penalty = 200

try:
    entry = input("Enter entry time (DD-MM-YYYY HH:MM): ")
    exit_time = input("Enter exit time (DD-MM-YYYY HH:MM): ")

    entry = datetime.strptime(entry, "%d-%m-%Y %H:%M")
    exit_time = datetime.strptime(exit_time, "%d-%m-%Y %H:%M")

    if exit_time <= entry:
        print("Invalid input: Exit must be after entry.")

    else:
        vehicle = input("Enter vehicle type (bike/car/bus): ").lower()

        if vehicle not in rates:
            print("Invalid vehicle category.")

        else:
            duration = (exit_time - entry).total_seconds() / 3600
            hours = ceil(duration)

            # Calculate daily limit
            days = ceil(duration / 24)
            basic_charge = hours * rates[vehicle]
            maximum_charge = days * daily_limits[vehicle]

            charge = min(basic_charge, maximum_charge)

            # Count overnight stays
            nights = (exit_time.date() - entry.date()).days
            night_charge = nights * overnight_charge

            # Penalty for parking over 24 hours
            extra_penalty = penalty if duration > 24 else 0

            total = charge + night_charge + extra_penalty

            print("\n----- PARKING BILL -----")
            print("Vehicle:", vehicle)
            print("Parking duration:", round(duration, 2), "hours")
            print("Hourly charge: Rs.", charge)
            print("Overnight charge: Rs.", night_charge)
            print("Penalty: Rs.", extra_penalty)
            print("Total amount: Rs.", total)

except ValueError:
    print("Invalid date or time format.")
    print("Please use DD-MM-YYYY HH:MM.")
