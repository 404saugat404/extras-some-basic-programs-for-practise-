import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    df=views[views["author_id"]==views["viewer_id"]]
    df.drop_duplicates(subset="author_id",inplace=True)
    df=df.rename(columns={"author_id":"id"})
    df.sort_values(by="id",inplace=True)
    return df[["id"]]


data = [[1, 3, 5, '2019-08-01'], [1, 3, 6, '2019-08-02'], [2, 7, 7, '2019-08-01'], [2, 7, 6, '2019-08-02'], [4, 7, 1, '2019-07-22'], [3, 4, 4, '2019-07-21'], [3, 4, 4, '2019-07-21']]
views = pd.DataFrame(data, columns=['article_id', 'author_id', 'viewer_id', 'view_date']).astype({'article_id':'Int64', 'author_id':'Int64', 'viewer_id':'Int64', 'view_date':'datetime64[ns]'})


print(views)


print(article_views(views))
