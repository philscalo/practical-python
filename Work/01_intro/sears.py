# sears.py
bill_thickness = 0.11 * 0.001  # Meters (0.11 mm)
sears_height = 442  # Height (meters)
num_bills = 1
day = 1

while num_bills * bill_thickness < sears_height:
    print(
        f"day: {day}  num_bills: {num_bills} current WAD: {num_bills * bill_thickness}"
    )
    day += 1
    num_bills *= 2

print(f"FINAL: Number of days: {day}")
print(f"FINAL: Number of bills: {num_bills}")
print(f"FINAL: Height: {num_bills * bill_thickness}")
