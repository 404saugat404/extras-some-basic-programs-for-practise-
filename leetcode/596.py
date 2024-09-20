import pandas as pd

def count_sub(courses:pd.DataFrame) -> pd.DataFrame:
    df=courses.groupby('class').count().reset_index()
    df=df[df["student"]>=5]
    return df["class"]






data = [['A', 'Math'], ['B', 'English'], ['C', 'Math'], ['D', 'Biology'], ['E', 'Math'], ['F', 'Computer'], ['G', 'Math'], ['H', 'Math'], ['I', 'Math']]
courses = pd.DataFrame(data, columns=['student', 'class']).astype({'student':'object', 'class':'object'})


print(count_sub(courses))