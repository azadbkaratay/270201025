book_prices= 24.95
book_prices_for_bookstores=book_prices-(book_prices*40/100)
shipping_cost_for_first= 3
shipping_cost_for_each_oth=0.75
cost = 60*book_prices_for_bookstores+shipping_cost_for_first+shipping_cost_for_each_oth*(60-1)
print(cost)
