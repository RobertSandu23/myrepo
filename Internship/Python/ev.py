#total = 62 #kWh
#consum = 15.6/100 #kWh / km 
#baterry = False   # X%


def calculate_range(battery):
    total_capacity = 62
    energy_cons = 15.6

    # transform % in decimal ( 20% -> 20/100 -> 0.2) of total batery 
    # ex -> if battery is 100% will consume 1*62kwh energy, if 50 will consume 0.5*62kwh
    current_energy = battery * total_capacity

    # get in km the available range
    range_value = (current_energy / energy_cons)
    return range_value

while True:
    battery = input("Enter the battery level as percentage(ex: 10, 43, 82): ")
    if battery.isdigit():
        battery = int(battery)
    else:
        print("Insert a number (integer)")
        continue
    if battery == 'q':
        break

    estimated_range = calculate_range(battery)
    print(f"Estimated range avaialbe: {estimated_range:.2f}km")
