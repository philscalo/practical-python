# A rubber ball is dropped from a height of 100 meters and each time it hits
# the ground, it bounces back up to 3/5 the height it fell. Write a program
# bounce.py that prints a table showing the height of the first 10 bounces.

height = 100
bounce_loss = (3/5)
num_bounces = 1
for bounce in range(10):
    height *= bounce_loss
    num_bounces += 1
    print(f"Bounce {num_bounces} reached {round(height, 4)}")
