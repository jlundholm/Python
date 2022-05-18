customer_basket_cost = 45
customer_basket_weight = 44
total_basket_cost = 0

if customer_basket_cost > 99:
    print("Total Basket Cost: $" + str(customer_basket_cost))
elif customer_basket_cost < 100:
    total_basket_cost = customer_basket_cost + (customer_basket_weight * 1.20)
    print("Total Basket Cost: $" + str(total_basket_cost))