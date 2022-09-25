# mortgage.py
#
# Exercise 1.7

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
payment_number = 1
# extra_payment_start_month = 1
extra_payment_start_month = 61
# extra_payment_end_month = 12
extra_payment_end_month = 108
extra_payment = 1000

while principal > 0:
    if payment_number >= extra_payment_start_month and payment_number <= extra_payment_end_month:
        principal = principal * (1+rate/12) - (payment + extra_payment)
        total_paid = total_paid + (payment + 1000)
    else:
        principal = round((principal * (1+rate/12) - payment), 2)
        total_paid = round((total_paid + payment), 2)
    print(f'{total_paid=}  {payment_number=} {principal=}')
    payment_number = payment_number + 1

print(
    f'Total paid:\t{round(total_paid, 2)}\nTotal payments:\t{payment_number}'
)
