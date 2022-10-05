import pandas as pd
import matplotlib.pyplot as plot

def artists(df):
    group = df.groupby(['artist_name'])['file'].count().nlargest(n=10, keep='all')
    group.to_excel('artists.xlsx', index=True)
    return group

def tracks(df):
    group = df.groupby(['track_name'])['file'].count().nlargest(n=10, keep='all')
    group.to_excel('tracks.xlsx', index=True)
    return group

def table(df):
    table = pd.pivot_table(df,values='file', index=['year', 'artist_name'], aggfunc='count')
    print(table)

def plotty(group, type):
    f = plot.figure()
    f.set_figwidth(20)
    f.set_figheight(10)

    group.plot.bar(x=type, y='file', title=f'Top 2022 {type}', rot=0, width=.5)

    for i in range(10):
        plot.text(x=i - .1, y=group[i] + 2, s=group[i], color='black', fontweight='bold')

    plot.show()

df = pd.read_csv(r'output7.csv', sep=';')
df = df[df['year'] == 2022]

plotty(artists(df), 'artist_name')
plotty(tracks(df), 'track_name')