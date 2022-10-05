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

    if type == 'artist_name':
        title_label = 'Artists'
    elif type == 'track_name':
        title_label = 'Tracks'
    else:
        title_label = 'Something'

    horizontal = False

    if horizontal:
        group.plot.barh(x=type, y='file', title=f'Top 10 {title_label} of 2022 (Updated)', rot=0, width=.5)

        plot.ylabel(title_label)
        plot.xlabel('Play Count')

        for i in range(10):
            plot.text(x=group[i] + .5, y=i, s=group[i], color='black', fontweight='bold')
    else:
        group.plot.bar(x=type, y='file', title=f'Top 10 {title_label} of 2022 (Updated)', rot=0, width=.5)

        plot.xlabel(title_label)
        plot.ylabel('Play Count')

        for i in range(10):
            plot.text(x=i - .1, y=group[i] + 2, s=group[i], color='black', fontweight='bold')

    plot.show()
    f.savefig(f'{type}.png')

df = pd.read_csv(r'output7.csv', sep=';')
df = df[df['year'] == 2022]

plotty(artists(df), 'artist_name')
plotty(tracks(df), 'track_name')