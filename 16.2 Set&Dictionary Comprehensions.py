widget_sales = [
    {"name": "widget 1", "sales": 10},
    {"name": "widget 2", "sales": 5},
    {"name": "widget 3", "sales": 0},
]

# first method
sales_by_widget = {}
for d in widget_sales:
    widget_name = d["name"]
    sales = d["sales"]
    sales_by_widget[widget_name] = sales
print(sales_by_widget)

# second method
sales_by_widget = {}
for d in widget_sales:
    sales_by_widget[d["name"]] = d["sales"]
print(sales_by_widget)

# third method
sales_by_widget = {d["name"]: d["sales"] for d in widget_sales}
print(sales_by_widget)
