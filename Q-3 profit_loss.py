cost_price = int(input())
selling_price = int(input())

if cost_price < selling_price:
    print("profit")
elif cost_price > selling_price:
    print("Loss")
else:
    print("Neither")