import pandas as pd

def fix_names(users: pd.DataFrame) -> pd.DataFrame:
    users["name"]=users["name"].str.capitalize()
    return users



data = [[1, 'aLice'], [2, 'bOB']]
users = pd.DataFrame(data, columns=['user_id', 'name']).astype({'user_id':'Int64', 'name':'object'})

print(fix_names(users))