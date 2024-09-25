import pandas as pd



def findNthLargestSalary(employee, n):
    employee["rank"]=employee["Salary"].rank(method='dense', ascending=False)
    df=employee[employee["rank"]==n]
    
    return pd.DataFrame(
        {
            f"getNthHighestSalary({n})":[df["Salary"].iloc[0] if len(df)>0 else None]
        }
    )




data = [[1, 100], [2, 200], [3, 300]]
employee = pd.DataFrame(data, columns=['Id', 'Salary']).astype({'Id':'Int64', 'Salary':'Int64'})

print(findNthLargestSalary(employee,2))