transactions = [
    {'item': 'widget', 'trans_type': 'sale', 'quantity': 10},
    {'item': 'widget', 'trans_type': 'sale', 'quantity': 5},
    {'item': 'widget', 'trans_type': 'refund', 'quantity': 2},
    {'item': 'license', 'trans_type': 'sale', 'quantity': 1},
    {'item': 'license', 'trans_type': 'sale', 'quantity': 1},
    {'item': 'license', 'trans_type': 'refund', 'quantity': 1},
]

total_sold = {}
for transaction in transactions:
    item = transaction["item"]
    is_sale = True if transaction["trans_type"] == "sale" else False
    quantity = transaction["quantity"]

    if is_sale:
        if item in total_sold:
            total_sold[item] = total_sold[item] + quantity  # or can be written like this total_sold[item] += quantity
        else:
            total_sold[item] = quantity
print(total_sold)
