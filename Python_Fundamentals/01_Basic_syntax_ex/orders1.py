number_of_orders = int(input())
total_price = 0

for orders in range(number_of_orders):
    price_per_capsule = float(input())
    days = int(input())
    capsule_per_day = int(input())
    price = capsule_per_day * days * price_per_capsule
    if not(0.01 <= price_per_capsule <= 100.00 and 1 <= days <= 31 and 1 <= capsule_per_day <= 2000):
        continue
    total_price += price
    print(f"The price for the coffee is: ${price:.2f}")
print(f"Total: ${total_price:.2f}")
