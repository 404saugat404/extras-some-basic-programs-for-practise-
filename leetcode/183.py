#customer who never order
import pandas as pd
def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    df=customers[~customers["id"].isin(orders["customerId"])]
    df.rename(columns={"name":"Customers"},inplace=True)
    return df[["Customers"]]


data = [[1, 'Joe'], [2, 'Henry'], [3, 'Sam'], [4, 'Max']]
customers = pd.DataFrame(data, columns=['id', 'name']).astype({'id':'Int64', 'name':'object'})
data = [[1, 3], [2, 1]]
orders = pd.DataFrame(data, columns=['id', 'customerId']).astype({'id':'Int64', 'customerId':'Int64'})

print(customers)
print("\n")
print(orders)
print("\n")
print(find_customers(customers,orders))
