import pandas as pd

import pandas as pd

import pandas as pd

def largest_orders(orders: pd.DataFrame) -> pd.DataFrame:
    # Group by customer_number and count the number of orders for each customer
    order_counts = orders.groupby("customer_number")["order_number"].count().reset_index()
    
    # Find the maximum number of orders
    max_orders = order_counts["order_number"].max()
    
    # Filter customers who have the maximum number of orders
    result = order_counts[order_counts["order_number"] == max_orders]
    
    # Return only the customer_number column
    return result[["customer_number"]]



data = [[1, 1], [2, 2], [3, 3], [4, 3]]
orders = pd.DataFrame(data, columns=['order_number', 'customer_number']).astype({'order_number':'Int64', 'customer_number':'Int64'})

print(largest_orders(orders))