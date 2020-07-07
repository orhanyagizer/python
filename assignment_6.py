sales = {
    "cost_value": 31.87,
    "sell_value": 45.00,
    "inventory": 1000
}

profit = (sales["sell_value"] - sales["cost_value"]) * sales["inventory"]
print(round(profit))
print()
amount = """Orhan : 3 dollars = $%.2f 
Yağızer : 29.99 dollars = $%.2f 
Ömer : 4.1 dollars = $%.2f 
Burhan : 35.5 dollars = $%.2f""" % (3, 29.99, 4.1, 35.5)

print(amount)