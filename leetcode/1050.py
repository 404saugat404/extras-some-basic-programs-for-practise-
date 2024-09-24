import pandas as pd


def actor_director_relation(actor_director:pd.DataFrame) -> pd.DataFrame:
    df=actor_director.groupby(['actor_id', 'director_id']).count().reset_index()
    final=df[df["timestamp"]>=3]
    return final[["actor_id", "director_id"]]

data = [[1, 1, 0], [1, 1, 1], [1, 1, 2], [1, 2, 3], [1, 2, 4], [2, 1, 5], [2, 1, 6]]
actor_director = pd.DataFrame(data, columns=['actor_id', 'director_id', 'timestamp']).astype({'actor_id':'int64', 'director_id':'int64', 'timestamp':'int64'})

print(actor_director_relation(actor_director))