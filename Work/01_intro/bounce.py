# bounce.py

bounce = 1
drop_height = 100
bounce_height = drop_height
rate = 3 / 5.0

while bounce <= 10:
    bounce_height *= rate
    drop_height = bounce_height
    print(f"bounce: {bounce:02d}    bounce height: {bounce_height:.2f}")
    bounce += 1
