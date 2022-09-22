budget = float(input())
flour_price = float(input())
eggs_pack_price = flour_price * 0.75
milk_price_bread = flour_price * 1.25 /4
bread_price = flour_price + eggs_pack_price + milk_price_bread
colored_eggs = 0
breads_counter = 0
while budget >= bread_price:
    breads_counter += 1
    colored_eggs += 3
    if breads_counter % 3 == 0:
        colored_eggs -= (breads_counter - 2)
    budget -= bread_price

print(f'You made {breads_counter} loaves of Easter bread! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.')

