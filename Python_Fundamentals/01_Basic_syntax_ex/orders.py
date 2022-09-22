orders = int(input())
total = 0
for ord_num in range(orders):
    capsule_price = float(input())
    if not 0.01 <= capsule_price <= 100.00:
        continue
    days = int(input())
    if not 1 <= days <= 31:
        continue
    capsules_per_day = int(input())
    if not 1 <= capsules_per_day <= 2000:
        continue
    order_price = capsule_price * days * capsules_per_day
    total += order_price
    print(f"The price for the coffee is: ${order_price:.2f}")

print(f"Total: ${total:.2f}")
