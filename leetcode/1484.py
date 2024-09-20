import pandas as pd

def categorize_products(activities: pd.DataFrame) -> pd.DataFrame:
    activities=activities.drop_duplicates(subset=['sell_date', 'product'])
    df=activities.groupby('sell_date').agg(
        num_sold=("product", "count"),
        products=("product", lambda x:(",".join(sorted(x))))).reset_index()

    return df




data = [['2020-05-30', 'Headphone'], ['2020-06-01', 'Pencil'], ['2020-06-02', 'Mask'], ['2020-05-30', 'Basketball'], ['2020-06-01', 'Bible'], ['2020-06-02', 'Mask'], ['2020-05-30', 'T-Shirt']]
activities = pd.DataFrame(data, columns=['sell_date', 'product']).astype({'sell_date':'datetime64[ns]', 'product':'object'})

print(categorize_products(activities))