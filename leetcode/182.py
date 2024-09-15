import pandas as pd
def duplicate_mail(person: pd.DataFrame) -> pd.DataFrame:
    df=person.groupby("email")["id"].count().reset_index().rename(columns={"id":"count"})
    return df[df["count"]>1][["email"]]


data = [[1, 'a@b.com'], [2, 'c@d.com'], [3, 'a@b.com']]
person = pd.DataFrame(data, columns=['id', 'email']).astype({'id':'Int64', 'email':'object'})

print(duplicate_mail(person))