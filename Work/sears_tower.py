# One morning, you go out and place a dollar bill on the sidewalk by the Sears
# Tower in Chicago. Each day thereafter, you go out double the number of
# bills. How long does it take for the stack of bills to exceed the height of
# the tower?

bill_thickness = 0.11 * 0.001  # Meters (0.11 mm)
sears_height = 442  # Height (meters)
num_bills = 1
day = 1

stack_height = (num_bills * bill_thickness)

while stack_height < sears_height:
    num_bills *= 2
    day += 1
    stack_height = (num_bills * bill_thickness)
    print(f"stack of bills has {num_bills} bills on day {day}")
