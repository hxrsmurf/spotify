import pandas as pd

def artists(df):
    group = df.groupby(['year', 'artist_name'])['file'].count().nlargest(n=20, keep='all')
    group.to_excel('artists.xlsx', index=True)
    print(group)

def tracks(df):
    group = df.groupby(['year', 'track_name'])['file'].count().nlargest(n=20, keep='all')
    group.to_excel('tracks.xlsx', index=True)
    print(group)

def table(df):
    table = pd.pivot_table(df,values='file', index=['year', 'artist_name'], aggfunc='count')
    print(table)

df = pd.read_csv(r'output7.csv', sep=';')
df = df[df['year'] == 2022]

artists(df)
tracks(df)